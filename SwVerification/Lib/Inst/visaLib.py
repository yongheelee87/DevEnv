from pyvisa import ResourceManager, VisaIOError
from Lib.Common import Configure


class VisaDev:
    def __init__(self, config_sys):
        super().__init__()
        self.config = config_sys  # Config 파일 Set

        self.resource = {}  # Class 넣을 dictionary 선언
        self.status = {}  # Status 넣을 dictionary 선언

        self.lst_dev = self._find_device()
        if len(self.lst_dev) != 0:
            self.connect_all()

    def connect_all(self):
        for dev in self.lst_dev:
            self.connect_dev(dev)

    def connect_dev(self, dev: str):
        """
        :param dev: device name or ID. In general, ID can be used
        """
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
                            print(f"Success: find device {dev_name}\n")
                            break
                    except Exception as e:
                        print(f'Error: connect {rm_list[i]} with {e}\n')
                if self.status[dev] is False:
                    print(f"Error: find device {dev}\n")
            else:
                print(f"Error: there is no connected device {dev}\n")
        except VisaIOError as e:
            print(f"Error: connect {dev} device with {e}\n")

    def write(self, dev, cmd):
        """
        :param dev: device name defined in the dict
        :param cmd: command via VISA. refer to specification of the device
        """
        self.resource[dev].write(cmd)

    def read(self, dev, cmd) -> str:
        """
        :param dev: device name defined in the dict
        :param cmd: command via VISA. refer to specification of the device
        :return: return response to the command
        """
        return self.resource[dev].query(cmd)

    def get_set_volt_curr(self, dev) -> (str, str):
        """
        :param dev: device name defined in the dict
        :return: source voltage, source current
        """
        return self.resource[dev].query(":SOUR:VOLT?"), self.resource[dev].query(":SOUR:CURR?")

    def set_volt_curr(self, dev, volt, curr):
        """
        :param dev: device name defined in the dict
        :param volt: Input voltage
        :param curr: Input current
        """
        try:
            self.resource[dev].write(f":SOUR:VOLT {str(volt)}")
            self.resource[dev].write(f":SOUR:CURR {str(curr)}")
            print(f'Success: SET VOLTAGE {str(volt)}V AND CURRENT {str(curr)}A\n')
        except VisaIOError:
            print(f'Error: SET VOLTAGE {str(volt)}V AND CURRENT {str(curr)}A\n')

    def output(self, dev, mode):
        """
        :param dev: device name defined in the dict
        :param mode: device output mode
        """
        try:
            self.resource[dev].write(f"OUTPut {str(mode)}")
            print(f'Success: SET OUTPUT {str(mode)}\n')
        except VisaIOError:
            print(f'Error: SET OUTPUT {str(mode)}\n')

    def meas_volt_curr(self, dev) -> (str, str):
        """
        :param dev: device name defined in the dict
        :return: measured voltage, measured current
        """
        return self.resource[dev].query(":MEAS:VOLT?"), self.resource[dev].query(":MEAS:CURR?")

    def fetch_volt_curr(self, dev) -> (str, str):
        """
        :param dev: device name defined in the dict
        :return: fetched voltage, fetched current
        """
        return self.resource[dev].query(":FETC:VOLT?"), self.resource[dev].query(":FETC:CURR?")

    # Reset Device via Command
    def _init_operation(self, dev):
        """
        :param dev: device name defined in the dict
        """
        self.resource[dev].write("*CLS")
        opc = self.resource[dev].query("*OPC?")
        if '1' in opc:
            self.resource[dev].write("*RST")
            print('Success: COMMAND RESET\n')
        else:
            print('Error: COMMAND RESET\n')

    def _find_device(self) -> list:
        return [i for i in self.config.keys()[1:] if 'visa' in self.config[i]['type']]


# This is a new line that ends the file
