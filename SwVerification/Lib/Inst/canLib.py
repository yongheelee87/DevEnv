import os
from cantools import database
from can import interface, Notifier, BufferedReader, Message, CanError
from threading import Thread
from Lib.Common import Configure

CAN_ERR = 0
CAN_DEV = 1
CAN_IN_USE = 2

CAN_EXTENDED = 0xFF


def _get_message(msg):
    return msg


class CANDev:
    """
    main test class for bus and message
    """

    def __init__(self, name: str, config_can):
        self.config = config_can  # CAN Config 파일 Class

        self.bus = None  # CAN bus 선언
        self.buffer = BufferedReader()  # CAN buffer type 선언
        self.notifier = None  # CAN message 전송을 위한 notifier 선언
        self.status = CAN_ERR
        self.db_path = self._get_dbc(name=name)
        self.db = database.load_file(self.db_path)  # path of .dbc file; CAN DBC 불러오기
        self.sig_val = self._get_decode_val()  # dictionary to decode value
        self.connect_dev()  # CAN device 연결

        self.rx = CANRxThread(self.buffer)  # CAN RX 시그널 THREAD 설정
        self.rx.start()  # CAN RX 시그널 THREAD 동작

        self.tx_data = {}  # CAN tx period data 선언; 메모리 보관
        self.tx_period = {}  # CAN tx period data 선언; 메모리 보관
        self.event_time = 0  # CAN event Time 저장

    def connect_dev(self):
        if not self.bus:
            try:
                self.bus = interface.Bus(bustype=self.config['bus_type'], channel=self.config['channel'], bitrate=int(self.config['bit_rate']),
                                         app_name=self.config['app_type'], data_bitrate=int(self.config['data_rate']), fd=True)
                self.notifier = Notifier(self.bus, [_get_message, self.buffer])
                self.status = CAN_DEV
            except CanError:
                self.status = CAN_ERR
        else:
            try:
                can_message = Message(arbitration_id=0, data=[0x00], is_extended_id=False, is_fd=True)  # 의미 없는 데이터 전송
                self.bus.send(can_message, timeout=0.2)  # 일정타임이상의 Timeout설정으로 전달이 안정적임
                self.status = CAN_IN_USE
            except AttributeError:
                self.status = CAN_ERR
                self.bus = None

    def msg_init(self):
        self.rx.msg_dict = {}  # 메세지 초기화

    def msg_read_id(self, can_id: int, decode_on: bool = True) -> dict:
        """
        :param can_id: can id (ex.0x14A)
        :param decode_on: True = decoded return value False = raw value
        :return: dict rx data consisting of signals and values
        """
        rx_data = {}
        if can_id in self.rx.msg_dict:
            rx_raw_data = self.rx.msg_dict[can_id].data  # 데이터 변이 방지
            rx_data = self.db.decode_message(can_id, rx_raw_data, decode_choices=decode_on)
        return rx_data

    def msg_read_name(self, frame_name: str, decode_on: bool = True) -> dict:
        """
        :param frame_name: Frame name based on CAN DB. you can find it in Messages names as well
        :param decode_on: True = decoded return value False = raw value
        :return: dict rx data consisting of signals and values
        """
        rx_data = {}
        can_id = self.get_msg_id(frame_name)
        if can_id in self.rx.msg_dict:
            rx_raw_data = self.rx.msg_dict[can_id].data  # 데이터 변이 방지
            rx_data = self.db.decode_message(can_id, rx_raw_data, decode_choices=decode_on)
        return rx_data

    def msg_read_event(self, frame_name: str, decode_on: bool = True) -> dict:
        """
        :param frame_name: Frame name based on CAN DB. you can find it in Messages names as well
        :param decode_on: True = decoded return value False = raw value
        :return: dict rx data consisting of signals and values
        """
        rx_data = {}
        can_id = self.get_msg_id(frame_name)
        if can_id in self.rx.msg_dict:
            message = self.rx.msg_dict[can_id]  # 데이터 변이 방지
            if self.event_time != message.timestamp:
                rx_data = self.db.decode_message(can_id, message.data, decode_choices=decode_on)
                self.event_time = message.timestamp  # CAN event Time 저장
        return rx_data

    def msg_write(self, frame_name: str, sig_name: str, value: int or float = 0, time_out: float = 0.2, is_extended: bool = False):
        """
        :param frame_name: Frame name based on CAN DB. you can find it in Messages names as well
        :param sig_name: Signal name based on CAN DB. you can find it in Signals names as well
        :param value: Input Value
        :param time_out: duration
        :param is_extended: message id extended
        """
        if value:
            try:
                msg_tx = self.db.get_message_by_name(frame_name)  # 해당 CAN message frame 정보 가져오기
                msg_raw_data = dict(zip(msg_tx.signal_tree, [0 for _ in range(len(msg_tx.signal_tree))]))  # 해당 하위 signal dict 만들기
                msg_raw_data[sig_name] = value  # 해당 signal 값 입력
                msg_data = msg_tx.encode(msg_raw_data)  # CAN message에 맞게 Encoding
                can_message = Message(arbitration_id=msg_tx.frame_id, data=msg_data, is_extended_id=is_extended, is_fd=True)
                self.bus.send(can_message, timeout=time_out)  # 일정타임이상의 Timeout설정으로 전달이 안정적임
            except:
                print(f"Error: WRITE CAN MESSAGE {frame_name}\n")

    def msg_write_by_frame(self, frame_name: str, sig_name: list, value: list, time_out: float = 0.02, is_extended: bool = False):
        """
        :param frame_name: Frame name based on CAN DB. you can find it in Messages names as well
        :param sig_name: Signal name based on CAN DB. you can find it in Signals names as well
        :param value: Input Value
        :param time_out: message duration
        :param is_extended: message id extended
        """
        if value != ([None] * len(value)):
            try:
                msg_tx = self.db.get_message_by_name(frame_name)  # 해당 CAN message frame 정보 가져오기
                msg_raw_data = dict(zip(msg_tx.signal_tree, [0 for _ in range(len(msg_tx.signal_tree))]))  # 해당 하위 signal dict 만들기
                for sig, val in zip(sig_name, value):
                    if val:
                        msg_raw_data[sig] = val  # 해당 signal 값 입력
                msg_data = msg_tx.encode(msg_raw_data)  # CAN message에 맞게 Encoding
                can_message = Message(arbitration_id=msg_tx.frame_id, data=msg_data, is_extended_id=is_extended, is_fd=True)
                self.bus.send(can_message, timeout=time_out)  # 일정타임이상의 Timeout설정으로 전달이 안정적임
            except:
                print(f"Error: WRITE CAN MESSAGE {frame_name}\n")

    def msg_period_write(self, frame_name: str, sig_name: str, value: int or float = 0, period: float = 0.02, is_extended: bool = False):
        """
        :param frame_name: Frame name based on CAN DB. you can find it in Messages names as well
        :param sig_name: Signal name based on CAN DB. you can find it in Signals names as well
        :param value: Input Value
        :param period: message period
        :param is_extended: message id extended
        """
        if value:
            try:
                if frame_name in self.tx_data:  # Frame 값이 있는지 확인
                    if sig_name in self.tx_data[frame_name]:  # 같은 신호 TX 요청이 있을시 신호 값 변경
                        if value == self.tx_data[frame_name][sig_name]:  # 같은 시그널 값 요청시 동작 불필요
                            return  # 함수 종료
                    self.tx_data[frame_name][sig_name] = value  # Frame내 signal value 변경
                else:  # 저장된 Frame 값이 없다면 새로 만들기
                    self.tx_data[frame_name] = {sig_name: value}  # Frame 및 Signal 생성

                msg_tx = self.db.get_message_by_name(frame_name)  # 해당 CAN message frame 정보 가져오기
                msg_raw_data = dict(zip(msg_tx.signal_tree, [0 for _ in range(len(msg_tx.signal_tree))]))  # 해당 하위 signal dict 만들기
                for sig, val in self.tx_data[frame_name].items():
                    msg_raw_data[sig] = val  # 해당 signal 값 입력
                msg_data = msg_tx.encode(msg_raw_data)  # CAN message에 맞게 Encoding
                can_message = Message(arbitration_id=msg_tx.frame_id, data=msg_data, is_extended_id=is_extended, is_fd=True)
                self._stop_overlap_msg(frame_name)
                self.tx_period[frame_name] = self.bus.send_periodic(can_message, period)
            except:
                print(f"Error: WRITE CAN MESSAGE {frame_name}\n")

    def msg_period_write_by_frame(self, frame_name: str, sig_name: list, value: list, period: float = 0.02, is_extended: bool = False):
        """
        :param frame_name: Frame name based on CAN DB. you can find it in Messages names as well
        :param sig_name: Signal name based on CAN DB. you can find it in Signals names as well
        :param value: Input Value
        :param period: message period
        :param is_extended: message id extended
        """
        if value != ([None] * len(value)):
            try:
                if frame_name in self.tx_data:  # Frame 값이 있는지 확인
                    if value == self.tx_data[frame_name]:  # 같은 시그널 값 요청시 동작 불필요
                        return  # 함수 종료

                self.tx_data[frame_name] = value  # Frame내 signal value 변경
                msg_tx = self.db.get_message_by_name(frame_name)  # 해당 CAN message frame 정보 가져오기
                msg_raw_data = dict(zip(msg_tx.signal_tree, [0 for _ in range(len(msg_tx.signal_tree))]))  # 해당 하위 signal dict 만들기
                for sig, val in zip(sig_name, value):
                    if val:
                        msg_raw_data[sig] = val  # 해당 signal 값 입력
                msg_data = msg_tx.encode(msg_raw_data)  # CAN message에 맞게 Encoding
                can_message = Message(arbitration_id=msg_tx.frame_id, data=msg_data, is_extended_id=is_extended, is_fd=True)
                self._stop_overlap_msg(frame_name)
                self.tx_period[frame_name] = self.bus.send_periodic(can_message, period)
            except:
                print(f"Error: WRITE CAN MESSAGE {frame_name}\n")

    def msg_raw_write(self, frame_id: int, msg_data: list, time_out: float = 0.02, is_extended: bool = False):
        """
        :param frame_id:
        :param msg_data:
        :param time_out:
        :param is_extended:
        """
        try:
            can_message = Message(arbitration_id=frame_id, data=msg_data, is_extended_id=is_extended, is_fd=True)
            self.bus.send(can_message, timeout=time_out)  # 일정타임이상의 Timeout설정으로 전달이 안정적임
        except:
            print(f"Error: WRITE CAN MESSAGE {frame_id}\n")

    def msg_stop_period_write(self):
        """
        Stop all currently active periodic messages
        """
        try:
            self.bus.stop_all_periodic_tasks()
            self.tx_period = {}
            self.tx_data = {}
        except CanError:
            print("Error: STOP WRITE CAN MESSAGE\n")

    def get_msg_name(self, id: int) -> str:
        return self.db.get_message_by_frame_id(id).name  # 해당 CAN message frame name 정보 가져오기

    def get_msg_id(self, frame_name: str) -> int:
        return self.db.get_message_by_name(frame_name).frame_id  # 해당 CAN message frame id 정보 가져오기

    def _stop_overlap_msg(self, frame_name: str):
        if frame_name in self.tx_period:
            self.tx_period[frame_name].stop()

    def _get_dbc(self, name: str) -> str:
        db_path = self.config['DBC_file_path']
        if db_path == 'git':
            ref_path = os.path.join(Configure.set['system']['git_path'], 'References', 'DB')
            for file in os.listdir(ref_path):
                if '.dbc' in file and name in file:
                    return os.path.join(ref_path, file)
        return db_path

    def _get_decode_val(self) -> dict:
        dict_decode_val = {}
        with open(self.db_path, "r", encoding="utf8", errors='ignore') as f:
            raw_lines = f.readlines()
            for x in raw_lines:
                if 'VAL_' in x[:4]:
                    val_info = [i.strip() for i in x[5:].split('"')]
                    val_head = val_info[0::2][0].split() + val_info[0::2][1:]
                    dict_decode_val[val_head[1]] = {int(val): decode if '~' not in decode else int(val) for val, decode in zip(val_head[2:], val_info[1::2])}
        return dict_decode_val


# CAN RX Msg Thread로 받기
class CANRxThread(Thread):
    """ CANRxThread(parent: Thread) """

    def __init__(self, buffer):
        super().__init__()
        self.rx_buffer = buffer
        self.msg_normal = None
        self.msg_dict = {}

    def run(self):
        while True:
            self.msg_normal = self.rx_buffer.get_message()
            if self.msg_normal:
                msg_id = self.msg_normal.arbitration_id
                self.msg_dict[msg_id] = self.msg_normal
            else:
                # 데이터 송수신 에러시 dict 클리어
                self.msg_dict.clear()


class CANBus:
    def __init__(self, config_sys):
        self.config = config_sys  # Config 파일 Set
        self.devs = {}

        self.lst_dev = self._find_can()
        for dev in self.lst_dev:
            self.devs[dev] = CANDev(name=dev, config_can=self.config[dev])  # CAN BUS 연결; 전역 변수로 사용

    def check_status(self) -> list:
        lst_fail_dev = []
        lst_connect_dev = []
        for dev in self.lst_dev:
            if self.devs[dev].status == CAN_ERR:
                lst_fail_dev.append(dev)
            else:
                lst_connect_dev.append(dev)

        if lst_connect_dev:
            print(f"CAN STATUS: CONNECT CAN DEVICE w/ {lst_connect_dev}\n")

        if lst_fail_dev:
            print(f'CAN STATUS: NOT CONNECT CAN DEVICE w/ {lst_fail_dev}\nIF YOU WANT TO USE CAN, CHECK IF THERE IS CAN DEVICE IN HARDWARE MANAGER\n')

        return lst_fail_dev

    def stop_all_period_msg(self):
        for dev in self.lst_dev:
            self.devs[dev].msg_stop_period_write()
            self.devs[dev].msg_init()

    def get_all_period_msg(self):
        all_msg = {}
        for dev in self.lst_dev:
            all_msg.update(self.devs[dev].tx_data)
        return all_msg

    def _find_can(self):
        return [i for i in list(self.config.keys())[1:] if 'can' in self.config[i]['type']]
# This is a new line that ends the file
