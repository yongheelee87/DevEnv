import time
from telnetlib import Telnet


class TelnetClient:
    def __init__(self, config_sys):
        self.config = config_sys  # Config 파일 Set
        '''
        :param host: Host IP address connected by ethernet
        :param port: Host Port
        '''
        super().__init__()
        self.device = None
        self.status = False

        if 'TELNET' in self.config:
            self.connect_dev(self.config['TELNET']['host'], self.config['TELNET']['port'])

        '''
        Telent을 Servo Motor 제어용으로만 사용한다면 아래 변수들 사용
        self.servo_ready
        self.servo_mode
        '''
        self.servo_ready = False
        self.servo_mode = ''

    def connect_dev(self, host: str = '0.0.0.0', port: str = '23'):
        """
        :param host: Host IP address connected by ethernet
        :param port: Host Port
        """

        if host == '' or port == '':
            host = '0.0.0.0'
            port = '23'

        try:
            self.device = Telnet(host, int(port))
            self.status = True
            print(f"Success: CONNECT DEVICE {host}:{port}\n")
        except (OSError, ConnectionRefusedError):
            self.status = False
            print('[INFO] Telnet is NOT CONNECTED with HOST\nIF YOU WANT TO USE telnet, CHECK IF THERE IS PC with Ethernet\n')

    def msg_read(self):
        """
        :return: return read raw data
        """
        raw_data = self.device.read_eager()
        return raw_data

    def msg_write(self, command):
        """
        :param command: command via Telnet. refer to specification of the device
        """
        command = f'{command}\r\n'.encode()
        self.device.write(command)
        time.sleep(0.1)
        print(f"Success: WRITE TELNET MESSAGE {command}\n")

    def query(self, command):
        """
        :param command: command via Telnet. refer to specification of the device
        :return: return read decoded data
        """
        self.msg_write(command)
        time.sleep(0.1)
        response = self.msg_read().decode()
        print(f"Success: READ TELNET MESSAGE {response}\n")
        return response

    '''
    Telnet을 Servo Motor 제어용으로만 사용한다면 아래 함수들 사용
    self.set_servo_mode
    self.enable_servo
    self.set_servo_speed
    self.set_servo_torque
    '''

    def set_servo_mode(self, mode: str = 'RPM'):
        if mode == 'RPM':
            self.msg_write("DRV.OPMODE 1")
        elif mode == 'TORQUE':
            self.msg_write("DRV.OPMODE 0")
        time.sleep(0.5)

        self.msg_write("SM.MODE 0")
        self.msg_write("DRV.CMDSOURCE 0")

        self.servo_mode = mode

    def enable_servo(self, on_off: bool):
        if on_off is True:
            self.msg_write("DRV.EN")
            self.msg_write("DRV.ACTIVE")

            self.msg_write("SM.MODE 0")
            self.msg_write("DRV.CMDSOURCE 0")
        else:
            self.msg_write("DRV.DIS")
            self.msg_write("DRV.ACTIVE")
            self.msg_write("DRV.CMDSOURCE 3")

    def set_servo_speed(self, servo_rpm: int = 0):
        # 단위: RPM
        servo_rpm = min(max(-5000, servo_rpm), 5000)
        self.msg_write(f'VL.CMDU {servo_rpm}')

    def set_servo_torque(self, servo_torque: float = 0.0):
        # 단위: N.m
        servo_torque = min(max(-5.0, servo_torque), 5.0)
        self.msg_write(f'IL.CMDU {servo_torque}')


# This is a new line that ends the file
