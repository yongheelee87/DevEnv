from pyvisa import ResourceManager, VisaIOError
from Lib.Common.basicFunction import *


class VisaDev:
    def __init__(self, config_sys):
        super().__init__()
        self.config = config_sys  # Config 파일 Set

        self.resource = dict()  # Class 넣을 dictionary 선언
        self.status = dict()  # Status 넣을 dictionary 선언

        self.lst_dev = self._find_device()
        if len(self.lst_dev) != 0:
            self.connect_all(self.lst_dev)

    def connect_all(self, lst_dev: list):
        '''
        :param lst_dev: list of device names
        '''
        for dev in lst_dev:
            self.connect_dev(dev)

    def connect_dev(self, dev: str):
        '''
        :param dev: device name or ID. In general, ID can be used
        '''
        self.status[dev] = False
        try:
            rm = ResourceManager()
            rm_list = rm.list_resources()
            len_rm = len(rm_list)
            if len_rm != 0:
                for i in range(len_rm):
                    try:
                        res = rm.open_resource(rm_list[i])
                        # self._init_operation(device_str)  # Reset Device
                        # ID 확인 함수 추가
                        dev_name = res.query("*IDN?").split(",")[1]
                        # Configuration Parser ID
                        if Configure.set[dev]['ID'] in dev_name:
                            self.resource[dev] = res
                            self.status[dev] = True
                            logging_print("Success: find device {}\n".format(dev_name))
                            break
                    except Exception as e:
                        logging_print('Error: connect {} with {}\n'.format(rm_list[i], e))
                if self.status[dev] is False:
                    logging_print("Error: find device {}\n".format(dev))
            else:
                logging_print("Error: there is no connected device {}\n".format(dev))
        except VisaIOError as e:
            logging_print("Error: connect {} device with {}\n".format(dev, e))

    def write(self, dev, cmd):
        '''
        :param dev: device name defined in the dict
        :param cmd: command via VISA. refer to specification of the device
        '''
        self.resource[dev].write(cmd)

    def read(self, dev, cmd):
        '''
        :param dev: device name defined in the dict
        :param cmd: command via VISA. refer to specification of the device
        :return: return response to the command
        '''
        return self.resource[dev].query(cmd)

    def get_set_volt_curr(self, dev):
        '''
        :param dev: device name defined in the dict
        :return: source voltage, source current
        '''
        return self.resource[dev].query(":SOUR:VOLT?"), self.resource[dev].query(":SOUR:CURR?")

    def set_volt_curr(self, dev, volt, curr):
        '''
        :param dev: device name defined in the dict
        :param volt: Input voltage
        :param curr: Input current
        '''
        try:
            self.resource[dev].write(":SOUR:VOLT {}".format(str(volt)))
            self.resource[dev].write(":SOUR:CURR {}".format(str(curr)))
            print('Success: SET VOLTAGE {}V AND CURRENT {}A\n'.format(str(volt), str(curr)))
        except VisaIOError:
            print('Error: SET VOLTAGE {}V AND CURRENT {}A\n'.format(str(volt), str(curr)))

    def output(self, dev, mode):
        '''
        :param dev: device name defined in the dict
        :param mode: device output mode
        '''
        try:
            self.resource[dev].write("OUTPut {}".format(str(mode)))
            print('Success: SET OUTPUT {}\n'.format(str(mode)))
        except VisaIOError:
            print('Error: SET OUTPUT {}\n'.format(str(mode)))

    def meas_volt_curr(self, dev):
        '''
        :param dev: device name defined in the dict
        :return: measured voltage, measured current
        '''
        return self.resource[dev].query(":MEAS:VOLT?"), self.resource[dev].query(":MEAS:CURR?")

    def fetch_volt_curr(self, dev):
        '''
        :param dev: device name defined in the dict
        :return: fetched voltage, fetched current
        '''
        return self.resource[dev].query(":FETC:VOLT?"), self.resource[dev].query(":FETC:CURR?")

    # Reset Device via Command
    def _init_operation(self, dev):
        '''
        :param dev: device name defined in the dict
        '''
        self.resource[dev].write("*CLS")
        opc = self.resource[dev].query("*OPC?")
        if '1' in opc:
            self.resource[dev].write("*RST")
            logging_print('Success: COMMAND RESET\n')
        else:
            logging_print('Error: COMMAND RESET\n')

    def _find_device(self):
        lst_dev = []
        for i in self.config.sections()[1:]:
            if 'visa' in self.config[i]['type']:
                lst_dev.append(i)
        return lst_dev


visa = VisaDev(config_sys=Configure.set)  # ViSA 연결; 전역 변수로 사용
# This is a new line that ends the file
