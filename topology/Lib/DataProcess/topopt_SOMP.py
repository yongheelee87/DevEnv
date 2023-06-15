# A 200 LINE TOPOLOGY OPTIMIZATION CODE BY NIELS AAGE AND VILLADS EGEDE JOHANSEN, JANUARY 2013
# Updated by Niels Aage February 2016

from __future__ import division
import numpy as np
import datetime

from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve
from matplotlib import colors
import matplotlib.pyplot as plt
import cvxopt
import cvxopt.cholmod
from Lib.DataProcess.CalculateKe import *
from Lib.Common.basicFunction import *


params = {'font.family': 'Times New Roman',
          'axes.titlesize': 16,
          'figure.titlesize': 16,
          'figure.figsize': (14, 7)
          }

MAX_LOOP = 2000

class SOMP(KE):
    def __init__(self):
        super().__init__()
        self.time = datetime.datetime.now()  # 시간 변수 선언
        self.log_lst = []  # 로그 변수 선언
        self.angle = 0.05  # 각도

        # Plot variables
        self.res_density = None
        self.cmap = None
        self.plt_pause = 0.01  # plt delay 시간

        # Default input parameters
        self.nelx = 100
        self.nely = 30
        self.volfrac = 0.4
        self.penal = 1.5
        self.rmin = 3.0
        self.ft = 1  # ft == 0 -> sens, ft == 1 -> dens
        self.KE = self.get_KE(theta=self.angle)

        # boundary parameters
        self.bc_change = 0.01

        # result folder
        isdir_and_make('./data/result')

    def start(self):
        self.log_lst = []  # 로그 변수 초기화

        # Max and min stiffness
        Emin = 1e-9
        Emax = 1.0

        # dofs:
        ndof = 2 * (self.nelx + 1) * (self.nely + 1)

        # Allocate design variables (as array), initialize and allocate sens.
        x = self.volfrac * np.ones(self.nely * self.nelx, dtype=float)
        xold = x.copy()
        xPhys = x.copy()

        g = 0  # must be initialized to use the NGuyen/Paulino OC approach
        volume = 0

        edofMat = np.zeros((self.nelx * self.nely, 8), dtype=int)
        for elx in range(self.nelx):
            for ely in range(self.nely):
                el = ely + elx * self.nely
                n1 = (self.nely + 1) * elx + ely
                n2 = (self.nely + 1) * (elx + 1) + ely
                edofMat[el, :] = np.array(
                    [2 * n1 + 2, 2 * n1 + 3, 2 * n2 + 2, 2 * n2 + 3, 2 * n2, 2 * n2 + 1, 2 * n1, 2 * n1 + 1])
        # Construct the index pointers for the coo format
        iK = np.kron(edofMat, np.ones((8, 1))).flatten()
        jK = np.kron(edofMat, np.ones((1, 8))).flatten()

        # Filter: Build (and assemble) the index+data vectors for the coo matrix format
        nfilter = int(self.nelx * self.nely * ((2 * (np.ceil(self.rmin) - 1) + 1) ** 2))
        iH = np.ones(nfilter)
        jH = np.ones(nfilter)
        sH = np.zeros(nfilter)
        cc = 0
        for i in range(self.nelx):
            for j in range(self.nely):
                row = i * self.nely + j
                kk1 = int(np.maximum(i - (np.ceil(self.rmin) - 1), 0))
                kk2 = int(np.minimum(i + np.ceil(self.rmin), self.nelx))
                ll1 = int(np.maximum(j - (np.ceil(self.rmin) - 1), 0))
                ll2 = int(np.minimum(j + np.ceil(self.rmin), self.nely))
                for k in range(kk1, kk2):
                    for l in range(ll1, ll2):
                        col = k * self.nely + l
                        fac = self.rmin - np.sqrt(((i - k) * (i - k) + (j - l) * (j - l)))
                        iH[cc] = row
                        jH[cc] = col
                        sH[cc] = np.maximum(0.0, fac)
                        cc = cc + 1
        # Finalize assembly and convert to csc format
        H = coo_matrix((sH, (iH, jH)), shape=(self.nelx * self.nely, self.nelx * self.nely)).tocsc()
        Hs = H.sum(1)

        # BC's and support
        dofs = np.arange(2 * (self.nelx + 1) * (self.nely + 1))
        fixed = np.union1d(dofs[0:2 * (self.nely + 1):2], np.array([2 * (self.nelx + 1) * (self.nely + 1) - 1]))
        free = np.setdiff1d(dofs, fixed)

        # Solution and RHS vectors
        # Set load
        '''
        From matlab, F = sparse(2, 1, -1, 2 * (nely + 1) * (nelx + 1), 1);
        '''
        F = np.zeros((ndof, 1))
        F[1, 0] = -100
        U = np.zeros((ndof, 1))

        loop = 0
        change = 1
        obj = 0
        dv = np.ones(self.nely * self.nelx)
        dc = np.ones(self.nely * self.nelx)
        ce = np.ones(self.nely * self.nelx)

        # Initialize plot and plot the initial design
        self._initialize_plot(x_data=xPhys)
        self._activate_plot('Figure 1')

        start_time = datetime.datetime.now()  # Loop 시작 전 측정 시작 시간 저장
        while change > self.bc_change and loop < MAX_LOOP:
            loop = loop + 1
            # Setup and solve FE problem
            sK = ((self.KE.flatten()[np.newaxis]).T * (Emin + (xPhys) ** self.penal * (Emax - Emin))).flatten(order='F')
            K = coo_matrix((sK, (iK, jK)), shape=(ndof, ndof)).tocsc()
            # Remove constrained dofs from matrix and convert to coo
            K = self._delete_row_col(K, fixed, fixed).tocoo()

            # Solve system
            K = cvxopt.spmatrix(K.data, K.row.astype(int), K.col.astype(int))
            B = cvxopt.matrix(F[free, 0])
            cvxopt.cholmod.linsolve(K, B)
            U[free, 0] = np.array(B)[:, 0]

            # Objective and sensitivity
            ce[:] = (np.dot(U[edofMat].reshape(self.nelx * self.nely, 8), self.KE) * U[edofMat].reshape(self.nelx * self.nely, 8)).sum(1)
            obj = ((Emin + xPhys ** self.penal * (Emax - Emin)) * ce).sum()
            dc[:] = (-self.penal * xPhys ** (self.penal - 1) * (Emax - Emin)) * ce
            dv[:] = np.ones(self.nely * self.nelx)

            # Sensitivity filtering:
            if self.ft == 0:
                dc[:] = np.asarray((H * (x * dc))[np.newaxis].T / Hs)[:, 0] / np.maximum(0.001, x)
            elif self.ft == 1:
                dc[:] = np.asarray(H * (dc[np.newaxis].T / Hs))[:, 0]
                dv[:] = np.asarray(H * (dv[np.newaxis].T / Hs))[:, 0]

            # Optimality criteria
            xold[:] = x
            x[:], g = self._optimal_criteria(x, dc, dv, g)

            # Filter design variables
            if self.ft == 0:
                xPhys[:] = x
            elif self.ft == 1:
                xPhys[:] = np.asarray(H * x[np.newaxis].T / Hs)[:, 0]

            # Compute the change by the inf. norm
            change = np.linalg.norm(x.reshape(self.nelx * self.nely, 1) - xold.reshape(self.nelx * self.nely, 1), np.inf)

            # Plot to screen
            self._update_plot(x_data=xPhys)

            # Write iteration history to screen
            self.time = datetime.datetime.now()
            elapse_time = (self.time - start_time).total_seconds()
            volume = (g + self.volfrac * self.nelx * self.nely) / (self.nelx * self.nely)
            self.log_lst.append([self.time.strftime('%Y-%m-%d %H:%M:%S'), round(elapse_time, 3), loop, obj, volume, change])
            print("iteration: {0}, Obj: {1:.3f}, Vol: {2:.3f}, change: {3:.3f}"
                  .format(loop, obj, volume, change))

        # Make sure the plot stays and that the shell remains
        logging_print("\n[Final Result] Obj: {0:.3f}, Vol: {1:.3f}, change: {2:.3f}\n"
                      .format(obj, volume, change))
        self.stop()  # 최적화 완료

    def stop(self):
        self._save_data()  # 데이터 저장
        print(self.res_density)
        plt.show(block=True)  # 그림 창 고정

    def update_params(self, str_params):
        if len(str_params) != 0:
            self.nelx = int(str_params[0].strip())
            self.nely = int(str_params[1].strip())
            self.volfrac = float(str_params[2].strip())
            self.penal = float(str_params[3].strip())
            self.rmin = float(str_params[4].strip())
            self.ft = int(str_params[5].strip())

        logging_print("Topology optimization for minimum compliance problems with parameters\n" +
                      "ndes: {} x {}\nvolfrac: {}, rmin: {}, penal: {}\nFilter method: {}\n"
                      .format(self.nelx, self.nely, self.volfrac, self.rmin, self.penal, ["Sensitivity based", "Density based"][self.ft]))

    def _optimal_criteria(self, x, dc, dv, g):
        l1 = 0
        l2 = 1e9
        gt = 0
        move = 0.2
        # reshape to perform vector operations
        xnew = np.zeros(self.nelx * self.nely)

        while (l2 - l1) / (l1 + l2) > 1e-3:
            lmid = 0.5 * (l2 + l1)
            xnew[:] = np.maximum(0.0, np.maximum(x - move, np.minimum(1.0, np.minimum(x + move, x * np.sqrt(-dc / dv / lmid)))))
            gt = g + np.sum((dv * (xnew - x)))
            if gt > 0:
                l1 = lmid
            else:
                l2 = lmid
        return xnew, gt

    # noinspection PyMethodMayBeStatic
    def _delete_row_col(self, A, row, col):
        # Assumes that matrix is in symmetric csc form !
        m = A.shape[0]
        keep = np.delete(np.arange(0, m), row)
        A = A[keep, :]
        keep = np.delete(np.arange(0, m), col)
        A = A[:, keep]
        return A
    
    def _save_data(self):
        data_col = ['Time', 'Elapsed Time', 'Iteration', 'Object', 'Volume', 'Change']
        df_log = pd.DataFrame(self.log_lst, columns=data_col)
        file_date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        export_csv_dataframe(df_log, './data/result', 'result_{}'.format(file_date))
        np.savetxt("./data/result/density_{}.csv".format(file_date), self.res_density, delimiter=",")
        plt.savefig('./data/result/result_{}.png'.format(file_date))
        logging_print("Success: Save Result Data\n")

    def _initialize_plot(self, x_data):
        '''
        Initialize plot and plot the initial design
        '''
        plt.rcParams.update(params)
        fig = plt.figure()

        plt.title('TOPOLOGY OPTIMIZATION\nx: {}, y: {}, volfrac: {}, penal: {}, rmin: {}, angle: {}\n'
                  .format(self.nelx, self.nely, self.volfrac, self.penal, self.rmin, self.angle))
        self.cmap = plt.imshow(-x_data.reshape((self.nelx, self.nely)).T, cmap='gray', interpolation='none',
                       norm=colors.Normalize(vmin=-1, vmax=0))
        plt.colorbar(self.cmap)
        plt.pause(self.plt_pause)
        plt.show(block=False)

    def _update_plot(self, x_data):
        '''
        Update plot based on the new data
        '''
        self.res_density = -x_data.reshape((self.nelx, self.nely)).T
        self.cmap.set_array(self.res_density)
        plt.pause(self.plt_pause)
        plt.show(block=False)

    # noinspection PyMethodMayBeStatic
    def _activate_plot(self, name):
        fig_win = gw.getWindowsWithTitle(name)[0]
        fig_win.minimize()
        fig_win.restore()
