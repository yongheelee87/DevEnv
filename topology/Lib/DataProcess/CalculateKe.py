from sympy import *
from sympy.matrices import Matrix
import numpy as np


class KE:
    def __init__(self):
        self.eq_KE = self.generate_equation_KE()

    def generate_equation_KE(self):
        s, t, T = symbols('s t T')

        Ex = 44.8e+03  # longitudinal Elastic modulus [MPa]
        Ey = 4.2e+03  # transversal Elastic modulus [MPa]
        Glt = 1.9e+03  # Shear Modulus [MPa]
        nuxy = 0.33  # Poisson ratio
        nuyx = nuxy * Ey / Ex

        h = 1
        x1 = -1
        y1 = -1
        x2 = 1
        y2 = -1
        x3 = 1
        y3 = 1
        x4 = -1
        y4 = 1

        a = (y1 * (s - 1) + y2 * (-1 - s) + y3 * (1 + s) + y4 * (1 - s)) / 4
        b = (y1 * (t - 1) + y2 * (1 - t) + y3 * (1 + t) + y4 * (-1 - t)) / 4
        c = (x1 * (t - 1) + x2 * (1 - t) + x3 * (1 + t) + x4 * (-1 - t)) / 4
        d = (x1 * (s - 1) + x2 * (-1 - s) + x3 * (1 + s) + x4 * (1 - s)) / 4

        B1 = Matrix([[a * (t - 1) / 4 - b * (s - 1) / 4, 0], [0, c * (s - 1) / 4 - d * (t - 1) / 4],
                     [c * (s - 1) / 4 - d * (t - 1) / 4, a * (t - 1) / 4 - b * (s - 1) / 4]])
        B2 = Matrix([[a * (1 - t) / 4 - b * (-1 - s) / 4, 0], [0, c * (-1 - s) / 4 - d * (1 - t) / 4],
                     [c * (-1 - s) / 4 - d * (1 - t) / 4, a * (1 - t) / 4 - b * (-1 - s) / 4]])
        B3 = Matrix([[a * (t + 1) / 4 - b * (s + 1) / 4, 0], [0, c * (s + 1) / 4 - d * (t + 1) / 4],
                     [c * (s + 1) / 4 - d * (t + 1) / 4, a * (t + 1) / 4 - b * (s + 1) / 4]])
        B4 = Matrix([[a * (-1 - t) / 4 - b * (1 - s) / 4, 0], [0, c * (1 - s) / 4 - d * (-1 - t) / 4],
                     [c * (1 - s) / 4 - d * (-1 - t) / 4, a * (-1 - t) / 4 - b * (1 - s) / 4]])
        Bfirst = Matrix.hstack(B1, B2, B3, B4)

        Jfirst = Matrix(
            [[0, 1 - t, t - s, s - 1], [t - 1, 0, s + 1, -s - t], [s - t, -s - 1, 0, t + 1], [1 - s, s + t, -t - 1, 0]])
        J = np.array(Matrix([[x1, x2, x3, x4]]) * Jfirst * Matrix([y1, y2, y3, y4]) / 8)[0][0]
        B = Bfirst / J

        R = Matrix([[cos(T), -sin(T), 0], [sin(T), cos(T), 0], [0, 0, 1]])
        D = Matrix([[Ex / (1 - (nuxy * nuyx)), (nuyx * Ex) / (1 - (nuxy * nuyx)), 0],
                    [(nuyx * Ex) / (1 - (nuxy * nuyx)), Ey / (1 - (nuxy * nuyx)), 0], [0, 0, Glt]])

        BD = J * Transpose(B) * R * D * Transpose(R) * B
        BD_s = integrate(BD, (t, -1, 1))  # t 적분 후 제거
        r = integrate(BD_s, (s, -1, 1))  # s 적분 후 제거

        z = h * r
        return z

    def get_KE(self, theta):
        T = symbols('T')
        return np.array(self.eq_KE.subs(T, theta), dtype=np.float64)




