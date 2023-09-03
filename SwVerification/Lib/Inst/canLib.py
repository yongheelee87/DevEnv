from cantools import database
from can import interface, Notifier, BufferedReader, Message, CanError
from threading import Thread
from Lib.Common.basicFunction import *

CAN_IN_USE = 0
CAN_DEV = 1
CAN_ERR = 2


def _get_message(msg):
    return msg


class CANDev:
    """
    main test class for bus and message
    """

    def __init__(self, config_can):
        self.config = config_can  # CAN Config 파일 Class

        self.bus = None  # CAN bus 선언
        self.buffer = BufferedReader()  # CAN buffer type 선언
        self.notifier = None  # CAN message 전송을 위한 notifier 선언
        self.status = CAN_ERR
        self.db_path = self.config['DBC_file_path']

        self.db = database.load_file(self.db_path)  # path of .dbc file; CAN DBC 불러오기
        self.connect_dev(bus_type=self.config['bus_type'],
                         ch=self.config['channel'],
                         app_type=self.config['app_type'],
                         bit_rate=int(self.config['bit_rate']),
                         data_rate=int(self.config['data_rate']))  # CAN device 연결

        self.rx = CANRxThread(self.buffer)  # CAN RX 시그널 THREAD 설정
        self.rx.start()  # CAN RX 시그널 THREAD 동작

        self.rx_data = dict()  # CAN rx data 선언
        self.tx_data = dict()  # CAN tx period data 선언; 메모리 보관
        self.tx_period = dict()  # CAN tx period data 선언; 메모리 보관

    def connect_dev(self, bus_type, ch, bit_rate, data_rate, app_type):
        try:
            can_message = Message(arbitration_id=0, data=[0x00], is_extended_id=False, is_fd=True)  # 의미 없는 데이터 전송
            self.bus.send(can_message, timeout=0.2)  # 일정타임이상의 Timeout설정으로 전달이 안정적임
            self.status = CAN_IN_USE
        except:
            try:
                self.bus = interface.Bus(bustype=bus_type, channel=ch, bitrate=bit_rate, app_name=app_type,
                                         data_bitrate=data_rate, fd=True)
                self.notifier = Notifier(self.bus, [_get_message, self.buffer])
                self.status = CAN_DEV
            except CanError:
                self.status = CAN_ERR

    def msg_read_id(self, can_id: int, decode_on: bool = True):
        '''
        :param can_id: can id (ex.0x14A)
        :param decode_on: True = decoded return value False = raw value
        :return: dict rx data consisting of signals and values
        '''
        if int(can_id) in self.rx.msg_dict.keys():
            self.rx_data = self.db.decode_message(self.rx.msg_dict[can_id].arbitration_id, self.rx.msg_dict[can_id].data, decode_choices=decode_on)
        else:
            self.rx_data = dict()
        return self.rx_data

    def msg_read_name(self, frame_name: str, decode_on: bool = True):
        '''
        :param frame_name: Frame name based on CAN DB. you can find it in Messages names as well
        :param decode_on: True = decoded return value False = raw value
        :return: dict rx data consisting of signals and values
        '''
        can_id = self._get_msg_id(frame_name)
        if can_id in self.rx.msg_dict.keys():
            self.rx_data = self.db.decode_message(self.rx.msg_dict[can_id].arbitration_id, self.rx.msg_dict[can_id].data, decode_choices=decode_on)
        else:
            self.rx_data = dict()
        return self.rx_data

    def msg_write(self, frame_name: str, sig_name: str, value: int or float = 0, time_out: float = 0.2, is_extended: bool = False):
        '''
        :param frame_name: Frame name based on CAN DB. you can find it in Messages names as well
        :param sig_name: Signal name based on CAN DB. you can find it in Signals names as well
        :param value: Input Value
        :param time_out: duration
        :param is_extended: message id extended
        '''
        try:
            msg_tx = self.db.get_message_by_name(frame_name)  # 해당 CAN message frame 정보 가져오기
            msg_raw_data = dict(
                zip(msg_tx.signal_tree, [0 for _ in range(len(msg_tx.signal_tree))]))  # 해당 하위 signal dict 만들기
            msg_raw_data[sig_name] = value  # 해당 signal 값 입력
            msg_data = msg_tx.encode(msg_raw_data)  # CAN message에 맞게 Encoding
            can_message = Message(arbitration_id=msg_tx.frame_id, data=msg_data, is_extended_id=is_extended, is_fd=True)
            self.bus.send(can_message, timeout=time_out)  # 일정타임이상의 Timeout설정으로 전달이 안정적임
        except:
            print("Error: WRITE CAN MESSAGE {}\n".format(frame_name))

    def msg_write_by_frame(self, frame_name: str, frame_msg: dict, time_out: float = 0.2, is_extended: bool = False):
        '''
        :param frame_name: Frame name based on CAN DB. you can find it in Messages names as well
        :param frame_msg: Frame dict including signals based on CAN DB. you can find it in Messages names as well
        :param time_out: duration
        :param is_extended: message id extended
        '''
        try:
            '''
            Here is an Example for frame msg

            frame_msg = dict()
            frame_msg[sig_name] = value1
            frame_msg[sig_name] = value2
            frame_msg[sig_name] = value3

            Write the Frame msg like this and put it in the function
            '''
            msg_tx = self.db.get_message_by_name(frame_name)  # 해당 CAN message frame 정보 가져오기
            msg_data = msg_tx.encode(frame_msg)  # CAN message에 맞게 Encoding
            can_message = Message(arbitration_id=msg_tx.frame_id, data=msg_data, is_extended_id=is_extended, is_fd=True)
            self.bus.send(can_message, timeout=time_out)  # 일정타임이상의 Timeout설정으로 전달이 안정적임
        except:
            print("Error: WRITE CAN MESSAGE {}\n".format(frame_name))

    def msg_period_write(self, frame_name: str, sig_name: str, value: int or float = 0, period: float = 0.02, is_extended: bool = False):
        '''
        :param frame_name: Frame name based on CAN DB. you can find it in Messages names as well
        :param sig_name: Signal name based on CAN DB. you can find it in Signals names as well
        :param value: Input Value
        :param period: message period
        :param is_extended: message id extended
        '''
        try:
            msg_tx = self.db.get_message_by_name(frame_name)  # 해당 CAN message frame 정보 가져오기
            msg_raw_data = dict(
                zip(msg_tx.signal_tree, [0 for _ in range(len(msg_tx.signal_tree))]))  # 해당 하위 signal dict 만들기

            if frame_name in self.tx_data.keys():  # Frame 값이 있는지 확인
                if sig_name in self.tx_data[frame_name]:  # 같은 신호 TX 요청이 있을시 신호 값 변경
                    sig_index = self.tx_data[frame_name].index(sig_name) + 1  # Frame내 signal value 인덱스 찾기
                    self.tx_data[frame_name][sig_index] = value  # Frame내 signal value 변경
                else:  # 다른 신호 TX 요청이 있을시 추가로 넣기
                    self.tx_data[frame_name] += [sig_name, value]

                for i in range(0, len(self.tx_data[frame_name]), 2):
                    msg_raw_data[self.tx_data[frame_name][i]] = self.tx_data[frame_name][i + 1]  # 해당 signal 값 입력

            else:  # 저장된 Frame 값이 없다면 새로 만들기
                self.tx_data[frame_name] = [sig_name, value]
                msg_raw_data[sig_name] = value  # 해당 signal 값 입력

            msg_data = msg_tx.encode(msg_raw_data)  # CAN message에 맞게 Encoding
            can_message = Message(arbitration_id=msg_tx.frame_id, data=msg_data, is_extended_id=is_extended, is_fd=True)
            self._stop_overlap_msg(frame_name)
            self.tx_period[frame_name] = self.bus.send_periodic(can_message, period)
        except:
            print("Error: WRITE CAN MESSAGE {}\n".format(frame_name))

    def msg_stop_period_write(self):
        '''
        Stop all currently active periodic messages
        '''
        try:
            self.bus.stop_all_periodic_tasks()

            if len(self.tx_period) != 0:
                self.tx_period.clear()

            if len(self.tx_data) != 0:
                self.tx_data.clear()
            print("Success: STOP WRITE CAN MESSAGE\n")
        except CanError:
            print("Error: STOP WRITE CAN MESSAGE\n")

    def _stop_overlap_msg(self, frame_name: str):
        if frame_name in self.tx_period.keys():
            self.tx_period[frame_name].stop()

    def _get_msg_id(self, frame_name: str):
        return self.db.get_message_by_name(frame_name).frame_id  # 해당 CAN message frame id 정보 가져오기


# CAN RX Msg Thread로 받기
class CANRxThread(Thread):
    """ CANRxThread(parent: Thread) """

    def __init__(self, buffer):
        super().__init__()
        self.rx_buffer = buffer
        self.msg_normal = None
        self.msg_dict = dict()

    def run(self):
        while True:
            self.msg_normal = self.rx_buffer.get_message()
            if self.msg_normal is not None:
                self.msg_dict[self.msg_normal.arbitration_id] = self.msg_normal
            else:
                # 데이터 송수신 에러시 dict 클리어
                self.msg_dict.clear()


class CANBus:
    def __init__(self, config_sys):
        self.config = config_sys  # Config 파일 Set
        self.devs = dict()

        self.lst_dev = self._find_can()
        for dev in self.lst_dev:
            self.devs[dev] = CANDev(config_can=self.config[dev])  # CAN BUS 연결; 전역 변수로 사용

    def check_status(self):
        lst_fail_dev = []
        lst_connect_dev = []
        for dev in self.lst_dev:
            if self.devs[dev].status == CAN_ERR:
                lst_fail_dev.append(dev)
            else:
                lst_connect_dev.append(dev)

        if lst_connect_dev:
            logging_print("{} CAN STATUS: CONNECT CAN DEVICE\n".format(lst_connect_dev))

        if lst_fail_dev:
            logging_print('{} CAN is NOT CONNECTED with HOST\nIF YOU WANT TO USE CAN, CHECK IF THERE IS CAN DEVICE IN HARDWARE MANAGER\n'.format(lst_fail_dev))

        return lst_fail_dev

    def stop_all_period_msg(self):
        for dev in self.lst_dev:
            self.devs[dev].msg_stop_period_write()

    def get_all_period_msg(self):
        all_msg = dict()
        for dev in self.lst_dev:
            all_msg.update(self.devs[dev].tx_data)
        return all_msg

    def _find_can(self):
        lst_can = []
        for i in self.config.sections()[1:]:
            if 'can' in self.config[i]['type']:
                lst_can.append(i)
        return lst_can


canBus = CANBus(config_sys=Configure.set)  # CAN BUS 연결; 전역 변수로 사용
# This is a new line that ends the file
