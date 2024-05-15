import os
import time
import numpy as np
import pandas as pd
from can import Message
from Lib.Common import to_hex_little_lst


class XcpVar:
    status: bool = False  # True: Done on request, False: Idle


class XcpProtocol:
    def __init__(self, bus, map_file: str, rx_id: int):
        """
        :param bus: can bus
        :param map_file: map file path
        :param rx_id: XCP or CCP id based on CAN DB
        """
        super().__init__()
        self.can = bus
        if os.path.isfile(map_file):
            self.df_symbol = self._get_df_symbol(map_file)
        else:
            self.df_symbol = None
        self.xcp_rx_id = rx_id

    # noinspection PyMethodMayBeStatic
    def _get_df_symbol(self, map_file: str) -> pd.DataFrame:
        """
        :param map_file: map file path
        :return: Dataframe with symbols corresponding to hex address
        """
        lst_symbol = []
        with open(map_file, 'r') as f:
            lines = "".join(f.readlines())
            symbol_lines = lines[lines.find('* Symbols (sorted on name)'):lines.find(
                '* Symbols (sorted on address)')].splitlines()[7:-2]
            for symbol_line in symbol_lines:
                lst_symbol.append(symbol_line.replace(' ', '')[1:].split('|')[:2])
        return pd.DataFrame(np.array(lst_symbol, dtype=object), columns=['Name', 'Address']).set_index(keys='Name', drop=True)

    def _get_addr_hex_from_df(self, sym: str):
        """
        :param sym: symbol
        :return: hex address
        """
        addr = sym
        # if sym is not hex address, it would find the address
        if sym[:2] != '0x':
            if sym in self.df_symbol.index.to_numpy():
                addr = self.df_symbol.loc[sym].to_numpy()[0]
            else:
                addr = '0x00000000'
                print(f"Error: Get address of symbol [{sym}]\nThere is no symbol information in map\n")
        return addr

    def connect(self, bus):
        if self.can is None:
            self.can = bus
        # 0xFF: start XCP Protocol
        can_message = Message(arbitration_id=self.xcp_rx_id, data=[0xFF, 0x00, ], is_extended_id=False, is_fd=True)
        self.can.send(can_message, timeout=None)
        XcpVar.status = False

    def send_msg_write(self, time_delay: int or float, addr_hex: str, data):
        """
        :param time_delay: Time after Message Transfer Request
        :param addr_hex: Symbol or Address Hex 입력; 메모리에 없는 address입력시 MCU 리셋
        :param data: Input Data
        """
        if self.df_symbol:
            addr = self._get_addr_hex_from_df(addr_hex)

            # 0xF6: set Message Transfer Agent(MTA) with Address
            can_message = Message(arbitration_id=self.xcp_rx_id,
                                  data=[0xF6, 0x00, 0x00, 0xFF] + to_hex_little_lst(addr), is_extended_id=False,
                                  is_fd=True)
            self.can.send(can_message, timeout=None)
            XcpVar.status = False

            time.sleep(time_delay)  # Need a Time for Message Transfer Request

            # 0xF0: Download Data
            lst_data = to_hex_little_lst(data)
            can_message = Message(arbitration_id=self.xcp_rx_id, data=[0xF0, len(lst_data)] + lst_data,
                                  is_extended_id=False, is_fd=True)
            self.can.send(can_message, timeout=None)
            XcpVar.status = False
        else:
            print("Error: XCP MAP FILE IS NOT FOUND AND PLEASE RE-CHECK CONFIGURE AND FILE\n")

    def send_msg_read(self, addr_hex: str):
        """
        :param addr_hex: Symbol or Address Hex 입력; 메모리에 없는 address입력시 MCU 리셋
        """
        if self.df_symbol:
            addr = self._get_addr_hex_from_df(addr_hex)

            # 0xF4: Upload Data with Address
            can_message = Message(arbitration_id=self.xcp_rx_id,
                                  data=[0xF4, 0x04, 0x00, 0xFF] + to_hex_little_lst(addr), is_extended_id=False,
                                  is_fd=True)
            self.can.send(can_message, timeout=None)
            XcpVar.status = False
        else:
            print("Error: XCP MAP FILE IS NOT FOUND AND PLEASE RE-CHECK CONFIGURE AND FILE\n")
