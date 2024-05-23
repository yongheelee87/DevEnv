import os
import time
import numpy as np
import pandas as pd
from can import BLFReader
import matplotlib.pyplot as plt
from mplcursors import cursor
from Lib.Common import isdir_and_make, open_path
from Lib.Inst import canBus
import warnings
warnings.filterwarnings("ignore")


LOG_COL = ['Time', 'Channel', 'CAN / CAN FD', 'Frame Type', 'CAN ID(HEX)', 'Frame Name', 'DLC', 'Data(HEX)', 'Data(Decode)']
CAN_DECODE_MAX = 8


class BlfAnalysis:
    """
    blf analysis class
    """
    def __init__(self):
        self.df_log = None
        self.df_blf = None
        self.maxT = 0
        self.blf_path = ''
        self.dic_channel = {}
        self.can_sigs = []
        self.inter_graph = False
        self.resample_rate = '100ms'
        self.fig = plt.Figure(figsize=(26, 26))
        isdir_and_make('./data/result/blf')

    def get_ch_dev(self) -> dict:
        return {i: dev for i, dev in enumerate(canBus.lst_dev)}

    def run(self):
        print("************************************************************")
        print("*** BLF Analysis Start!\n"
              "*** Please Do not try additional command until it completes")
        print("************************************************************\n")

        start_time = time.localtime(time.time())
        start_time_str = time.strftime("%a, %d-%b-%Y %I:%M:%S", start_time)
        print(f'Starting at: {start_time_str}')

        self.read_blf()
        self.display_graph()
        self.resample_blf()
        self.stop()

    def stop(self):
        end_time_str = time.strftime("%a, %d-%b-%Y %I:%M:%S", time.localtime(time.time()))
        print(f'Ending at: {end_time_str}')
        print("************************************************************")
        print("*** BLF Analysis completed")
        print("************************************************************\n")
        time.sleep(1)

    def update_param(self, blf_path: str, dic_channel: dict, sigs: list, rate: str):
        self.blf_path = blf_path
        self.dic_channel = dic_channel
        self.can_sigs = sigs
        self.resample_rate = rate

    def read_blf(self):
        log = list(BLFReader(self.blf_path))
        log_output = []
        for msg in log:
            time_secs = msg.timestamp - log[0].timestamp
            if msg.channel in self.dic_channel:
                device_ch = self.dic_channel[msg.channel]
            else:
                device_ch = msg.channel

            if msg.is_fd:
                can_fd = 'CAN FD'
            else:
                can_fd = 'CAN'

            if msg.is_error_frame:
                frame_type = 'Error'
            elif msg.is_remote_frame:
                frame_type = 'Remote'
            else:
                frame_type = 'Data'

            if msg.is_extended_id:
                can_id = f'0x{msg.arbitration_id:08X}'
            else:
                can_id = f'0x{msg.arbitration_id:03X}'

            try:
                frame_name = canBus.devs[device_ch].get_msg_name(int(msg.arbitration_id))
            except KeyError:
                frame_name = 'Not Defined'

            data = ''
            for byte in msg.data:
                data = f'{data}{byte:02X} '

            if frame_name != 'Not Defined':
                try:
                    data_decode = canBus.devs[device_ch].db.decode_message(msg.arbitration_id, msg.data, decode_choices=False)
                except:
                    data_decode = 'N/A'
            else:
                data_decode = 'N/A'

            log_output.append([time_secs, device_ch, can_fd, frame_type, can_id, frame_name, msg.dlc, data, data_decode])

        self.df_log = pd.DataFrame(np.array(log_output, dtype=object), columns=LOG_COL)
        self.df_blf.to_csv(os.path.join('./data/result/blf', os.path.basename(self.blf_path).replace('.blf', '_raw.csv')), encodings='utf-8-sig')
        # self.df_blf.to_pickle(os.path.join('./data/result/blf', os.path.basename(self.blf_path).replace('.blf', '_raw.pkl')))
        self.df_blf, self.maxT = self._convert_df_blf()
        self.df_blf.to_csv(os.path.join('./data/result/blf', os.path.basename(self.blf_path).replace('.blf', '.csv')), encodings='utf-8-sig')
        # self.df_blf.to_pickle(os.path.join('./data/result/blf', os.path.basename(self.blf_path).replace('.blf', '.pkl')))

    def display_graph(self):
        self.fig.clf()  # figure clear
        self.fig.set_size_inches(26, 26)  # resize

        plt.rcParams['axes.xmargin'] = 0
        data_col = self.df_blf.columns

        axs = self.fig.add_gridspec(len(data_col), hspace=0.2).subplots(sharex=True, sharey=False)

        for i, signal in enumerate(data_col):
            color_idx = i % 20
            lst_signal = signal.split(', ')
            dev_name = lst_signal[0]
            sig_name = lst_signal[-1]

            df_signal = self.df_blf[[signal]].dropna(axis=0)
            x_data = df_signal.index.to_numpy()  # ['Time'].values
            y_data = df_signal.to_numpy()  # ['Value'].values

            axs[i].step(x_data, y_data, 'o-', markersize=2, label=sig_name, c=plt.cm.tab20(color_idx), where='post', linewidth=1.0)
            if y_data.size == 0:
                yticks_val = range(0, 2)
            else:
                min_y = int(min(y_data))
                max_y = int(max(y_data))
                if max_y == 0:
                    yticks_val = range(min_y, max_y + 2)
                else:
                    if max_y > CAN_DECODE_MAX:
                        yticks_val = list(range(min_y, max_y, int(max_y / (CAN_DECODE_MAX-1))))
                        yticks_val[-1] = max_y
                    else:
                        yticks_val = range(min_y, max_y + 1)
            axs[i].set_yticks(yticks_val)
            yticks_labels = []
            for y_val in yticks_val:
                if (sig_name in canBus.devs[dev_name].sig_val) and (y_val in canBus.devs[dev_name].sig_val[sig_name]):
                    yticks_labels.append(canBus.devs[dev_name].sig_val[sig_name][y_val])
                else:
                    yticks_labels.append(f'{y_val}(RAW)')
            axs[i].set_yticklabels(yticks_labels, fontsize=6)
            axs[i].set_xlim(left=0, right=self.maxT + 1)

            if i == len(data_col) - 1:
                axs[i].set_xlabel('Time[sec]')

            # Hide x labels and tick labels for all but bottom plot
            for ax in axs:
                ax.legend(loc='upper right', fontsize=7)
                # ax.label_outer()
            filepath = os.path.join('./data/result/blf', os.path.basename(self.blf_path).replace('.blf', '.png'))
            plt.savefig(filepath, format='png')
            print(f"[INFO] {filepath} has been created\n")

            # Interative Graph Flag
            if self.inter_graph is True:
                cursor(hover=True, highlight=False)
            else:
                open_path(filepath)  # Open png file

            # plt.savefig(filepath, format='svg')
            # plt.cla()  # clear the current axes
            # plt.clf()  # clear the current figure
            # plt.close()  # closes the current figure

    def resample_blf(self):
        self.df_blf.index = pd.to_timedelta(self.df_blf.index, 's')
        df_resample = self.df_blf.resample(self.resample_rate, label='right', closed='right').last()
        df_resample.index = df_resample.index.total_seconds()
        rate = self.resample_rate.replace('s', '')
        rate = float(rate.replace('m', '')) / 1000 if 'm' in rate else float(rate)
        df_resample.insert(loc=0, column='TimeDiff[sec]', value=rate)
        df_resample.to_csv(os.path.join('./data/result/blf', os.path.basename(self.blf_path).replace('.blf', f'_{self.resample_rate}.csv')), encodings='utf-8-sig')
        # df_resample.to_pickle(os.path.join('./data/result/blf', os.path.basename(self.blf_path).replace('.blf', f'_{self.resample_rate}.pkl')))

    def _convert_df_blf(self) -> (pd.DataFrame, float or int):
        lst_df_sig = []
        maxTime = 0
        for sig in self.can_sigs:
            df_sig = self._get_signal_value(ch=sig[0], msg_name=sig[1], signal_name=sig[2])
            if maxTime < df_sig['Time'].max():
                maxTime = df_sig['Time'].max()
            lst_df_sig.append(df_sig.set_index('Time'))
        return pd.concat(lst_df_sig, axis=1).sort_index(ascending=True), maxTime

    def _get_signal_value(self, ch: str, msg_name: str, signal_name: str) -> pd.DataFrame:
        df_temp = self.df_log[(self.df_log['Channel'] == ch) & (self.df_log['Frame Name'] == msg_name)]
        time_log = df_temp['Time'].to_numpy()
        sig_value = df_temp['Data(Decode)'].apply(lambda x: x[signal_name]).to_numpy()
        col_sig = ', '.join((ch, msg_name, signal_name))
        return pd.DataFrame({'Time': time_log, col_sig: sig_value})
