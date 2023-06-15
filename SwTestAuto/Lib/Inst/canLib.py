from cantools import database
from can import interface, Notifier, BufferedReader, Message, CanError
from threading import Thread
from Lib.Inst.xcpLib import *
from Lib.Common.basicFunction import *

CAN_IN_USE = 0
CAN_DEV = 1
CAN_ERR = 2


def _get_message(msg):
    return msg


class CANCommunication:
    """
    main test class for bus and message
    """

    def __init__(self, config_sys):
        self.config = config_sys  # Config 파일 Set

        self.can_bus = None  # CAN bus 선언
        self.can_buffer = BufferedReader()  # CAN buffer type 선언
        self.can_notifier = None  # CAN message 전송을 위한 notifier 선언
        self.status = CAN_ERR
        self.db = None

        if 'CAN' in self.config.sections():
            self.db = database.load_file(self.config['CAN']['DBC_file_path'])  # path of .dbc file; CAN DBC 불러오기
            self.connect_dev(bus_type=self.config['CAN']['bus_type'],
                             ch=self.config['CAN']['channel'],
                             app_type=self.config['CAN']['app_type'],
                             bit_rate=int(self.config['CAN']['bit_rate']),
                             data_rate=int(self.config['CAN']['data_rate']))  # CAN device 연결

        if 'XCP' in self.config.sections():
            self.xcp = XcpProtocol(self.can_bus, self.config['XCP']['map_file_path'],
                                   self._get_msg_id(self.config['XCP']['xcp_rx_name']))  # CAN XCP 선언
            self.can_rx = CANRxTread(self.can_buffer,
                                     self._get_msg_id(self.config['XCP']['xcp_tx_name']))  # CAN RX 시그널 THREAD 설정
        else:
            self.xcp = None
            self.can_rx = CANRxTread(self.can_buffer, 0xFFFF)  # CAN RX 시그널 THREAD 설정

        self.can_rx.start()  # CAN RX 시그널 THREAD 동작

        self.rx_data = dict()  # CAN rx data 선언
        self.tx_data = dict()  # CAN tx period data 선언; 메모리 보관
        self.tx_period = dict()  # CAN tx period data 선언; 메모리 보관

    def check_status(self):
        if self.status == CAN_IN_USE:
            logging_print("CAN STATUS: IN USE OF CAN DEVICE\n{}\n".format(self.can_bus))
        elif self.status == CAN_DEV:
            logging_print("CAN STATUS: CONNECT CAN DEVICE\n{}\n".format(self.can_bus))
        else:
            logging_print(
                '[INFO] CAN is NOT CONNECTED with HOST\nIF YOU WANT TO USE CAN, CHECK IF THERE IS CAN DEVICE IN HARDWARE MANAGER\n')

        if self.status != CAN_ERR and self.xcp is not None and os.path.isfile(self.config['XCP']['map_file_path']):
            logging_print("XCP STATUS: THE FUNCTIONS ARE GOOD TO OPERATE\n")
        else:
            logging_print("XCP STATUS: MAP FILE IS NOT FOUND AND PLEASE RE-CHECK CONFIGURE AND FILE\n")

    def connect_dev(self, bus_type, ch, bit_rate, data_rate, app_type):
        try:
            can_message = Message(arbitration_id=0, data=[0x00], is_extended_id=False, is_fd=True)  # 의미 없는 데이터 전송
            self.can_bus.send(can_message, timeout=0.2)  # 일정타임이상의 Timeout설정으로 전달이 안정적임
            logging_print("Success: IN USE OF CAN DEVICE\n{}\n".format(self.can_bus))
            self.status = CAN_IN_USE
        except:
            try:
                self.can_bus = interface.Bus(bustype=bus_type, channel=ch, bitrate=bit_rate, app_name=app_type,
                                             data_bitrate=data_rate, fd=True)
                self.can_notifier = Notifier(self.can_bus, [_get_message, self.can_buffer])
                logging_print("Success: CONNECT CAN DEVICE\n{}\n".format(self.can_bus))
                self.status = CAN_DEV
            except CanError:
                logging_print("Error: CONNECT CAN DEVICE\n{}\n".format(self.can_bus))
                self.status = CAN_ERR

    def msg_read_id(self, can_id: int, decode_on: bool = True):
        '''
        :param can_id: can id (ex.0x14A)
        :param decode_on: True = decoded return value False = raw value
        :return: dict rx data consisting of signals and values
        '''
        if int(can_id) in self.can_rx.msg_dict.keys():
            self.rx_data = self.db.decode_message(self.can_rx.msg_dict[can_id].arbitration_id, self.can_rx.msg_dict[can_id].data, decode_choices=decode_on)
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
        if can_id in self.can_rx.msg_dict.keys():
            self.rx_data = self.db.decode_message(self.can_rx.msg_dict[can_id].arbitration_id, self.can_rx.msg_dict[can_id].data, decode_choices=decode_on)
        else:
            self.rx_data = dict()
        return self.rx_data

    def msg_write(self, frame_name: str, sig_name: str, value: int or float = 0, time_out: float = 0.2):
        '''
        :param frame_name: Frame name based on CAN DB. you can find it in Messages names as well
        :param sig_name: Signal name based on CAN DB. you can find it in Signals names as well
        :param value: Input Value
        :param time_out: duration
        '''
        try:
            msg_tx = self.db.get_message_by_name(frame_name)  # 해당 CAN message frame 정보 가져오기
            msg_raw_data = dict(
                zip(msg_tx.signal_tree, [0 for _ in range(len(msg_tx.signal_tree))]))  # 해당 하위 signal dict 만들기
            msg_raw_data[sig_name] = value  # 해당 signal 값 입력
            msg_data = msg_tx.encode(msg_raw_data)  # CAN message에 맞게 Encoding
            can_message = Message(arbitration_id=msg_tx.frame_id, data=msg_data, is_extended_id=False, is_fd=True)
            self.can_bus.send(can_message, timeout=time_out)  # 일정타임이상의 Timeout설정으로 전달이 안정적임
        except:
            print("Error: WRITE CAN MESSAGE {}\n".format(frame_name))

    def msg_write_by_frame(self, frame_name: str, frame_msg: dict, time_out: float = 0.2):
        '''
        :param frame_name: Frame name based on CAN DB. you can find it in Messages names as well
        :param frame_msg: Frame dict including signals based on CAN DB. you can find it in Messages names as well
        :param time_out: duration
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
            can_message = Message(arbitration_id=msg_tx.frame_id, data=msg_data, is_extended_id=False, is_fd=True)
            self.can_bus.send(can_message, timeout=time_out)  # 일정타임이상의 Timeout설정으로 전달이 안정적임
        except:
            print("Error: WRITE CAN MESSAGE {}\n".format(frame_name))

    def msg_period_write(self, frame_name: str, sig_name: str, value: int or float = 0, period: float = 0.02):
        '''
        :param frame_name: Frame name based on CAN DB. you can find it in Messages names as well
        :param sig_name: Signal name based on CAN DB. you can find it in Signals names as well
        :param value: Input Value
        :param period: message period
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
            can_message = Message(arbitration_id=msg_tx.frame_id, data=msg_data, is_extended_id=False, is_fd=True)
            self._stop_overlap_msg(frame_name)
            self.tx_period[frame_name] = self.can_bus.send_periodic(can_message, period)
        except:
            print("Error: WRITE CAN MESSAGE {}\n".format(frame_name))

    def msg_stop_period_write(self):
        '''
        Stop all currently active periodic messages
        '''
        try:
            self.can_bus.stop_all_periodic_tasks()

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

    def xcp_read_symbol(self, symbol: str):
        '''
        :param symbol: Symbol or Address Hex 입력
        :return ret_value is str or None
        '''
        ret_value = None
        self.xcp.send_msg_read(addr_hex=symbol)
        time.sleep(0.005)
        if XcpVar.status is True:
            ret_value = bytearray_to_hex(self.can_rx.msg_xcp[1:5][::-1])
        return ret_value


# CAN RX Msg Thread로 받기
class CANRxTread(Thread):
    """ CANRxTread(parent: Thread) """

    def __init__(self, buffer, xcp_id):
        super().__init__()
        self.rx_buffer = buffer
        self.msg_normal = None
        self.msg_xcp = None
        self.xcp_id = xcp_id
        self.msg_dict = dict()

    def run(self):
        while True:
            self.msg_normal = self.rx_buffer.get_message()
            if self.msg_normal is not None:
                # XCP 데이터 다른 메모리에 저장하며 따로 관리 (별도의 프로토콜)
                if self.msg_normal.arbitration_id == self.xcp_id:
                    self.msg_xcp = list(self.msg_normal.data)
                    XcpVar.status = True
                else:
                    self.msg_dict[self.msg_normal.arbitration_id] = self.msg_normal
            else:
                # 데이터 송수신 에러시 dict 클리어
                self.msg_dict.clear()


canBus = CANCommunication(config_sys=Configure.set)  # CAN BUS 연결; 전역 변수로 사용
# This is a new line that ends the file
