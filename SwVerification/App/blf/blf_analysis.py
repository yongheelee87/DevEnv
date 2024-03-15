import matplotlib.pyplot as plt
from can import BLFReader
from Lib.Inst import *

LOG_COL = ['Time', 'Channel', 'CAN / CAN FD', 'Frame Type', 'CAN ID(HEX)', 'Frame Name', 'DLC', 'Data(HEX)', 'Data(Decode)']


class BlfAnalysis:
    """
    blf analysis class
    """
    def __init__(self):
        self.df_log = None
        self.dict_blf = {}
        self.maxT = 0

    def get_ch_dev(self) -> dict:
        return {i: dev for i, dev in enumerate(canBus.lst_dev)}

    def read_blf(self, blf_path: str, dic_channel: dict, sigs: list):
        log = list(BLFReader(blf_path))
        log_output = []
        for msg in log:
            time_secs = msg.timestamp - log[0].timestamp
            if msg.channel in dic_channel.keys():
                device_ch = dic_channel[msg.channel]
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
        '''
        with open("output.csv", "w", newline='') as f:
            writer = csv.writer(f, dialect='excel')
            writer.writerows(log_output)
        '''
        self.df_log = pd.DataFrame(log_output, columns=LOG_COL)
        self.dict_blf, self.maxT = self.convert_dict_blf(sigs)

    def display_graph(self):
        plt.rcParams['axes.xmargin'] = 0
        fig = plt.figure(figsize=(26, 26))
        axs = fig.add_gridspec(len(self.dict_blf), hspace=0.1).subplots(sharex=True, sharey=False)

        for i, (k, data) in enumerate(self.dict_blf.items()):
            color_idx = i % 20
            dev_name = k[0]
            sig_name = k[-1]
            x_data = data['Time'].values
            y_data = data['Value'].values

            axs[i].step(x_data, y_data, 'o-', markersize=2, label=sig_name, c=plt.cm.tab20(color_idx), where='post', linewidth=1.0)
            if y_data.size == 0:
                yticks_val = range(0, 2)
            else:
                yticks_val = range(0, max(y_data) + 2)
            axs[i].set_yticks(yticks_val)
            yticks_labels = []
            for y_val in yticks_val:
                if y_val in canBus.devs[dev_name].sig_val[sig_name].keys():
                    yticks_labels.append(canBus.devs[dev_name].sig_val[sig_name][y_val])
                else:
                    yticks_labels.append(f'{y_val}(RAW)')
            axs[i].set_yticklabels(yticks_labels)
            axs[i].set_xlim(left=0, right=self.maxT + 1)

            if i == len(self.dict_blf) - 1:
                axs[i].set_xlabel('Time[sec]')

            # Hide x labels and tick labels for all but bottom plot
            for ax in axs:
                ax.legend(loc='upper right')
                ax.label_outer()

            plt.show()
            # plt.savefig(f'{filepath}/{filename}.png')
            # plt.cla()  # clear the current axes
            # plt.clf()  # clear the current figure
            # plt.close()  # closes the current figure

    def convert_dict_blf(self, can_sigs: list):
        dict_sig = {}
        maxTime = 0
        for sig in can_sigs:
            df_sig = self._get_signal_value(ch=sig[0], msg_name=sig[1], signal_name=sig[2])
            dict_sig[sig[0], sig[1], sig[2]] = df_sig
            if maxTime < df_sig['Time'].max():
                maxTime = df_sig['Time'].max()
        return dict_sig, maxTime

    def _get_signal_value(self, ch, msg_name, signal_name) -> pd.DataFrame:
        df_temp = self.df_log[(self.df_log['Channel'] == ch) & (self.df_log['Frame Name'] == msg_name)]
        time_log = df_temp['Time'].values
        sig_value = df_temp['Data(Decode)'].apply(lambda x: x[signal_name]).values
        return pd.DataFrame({'Time': time_log, 'Value': sig_value})
