import re
import serial
import serial.tools.list_ports


def serial_Initialization(port_word, baud_rate, byte_size, time_out):
    ports = serial.tools.list_ports.comports()
    CP210_COM = []
    for port in ports:
        if port_word in port.description:
            for st in re.finditer("COM", port.description):
                CP210_COM.append(port.description[st.start():st.start() + 4])

    ser = serial.Serial(CP210_COM[0], baudrate=baud_rate, bytesize=byte_size, parity='N', stopbits=1, timeout=time_out)
    print(f'[INFO] {ser}\n')
    if not ser.is_open:
        ser.open()
        print("SUCCESS: Connect HOST PC and POWER SUPPLY\n")
    else:
        print("SUCCESS: Connect HOST PC and POWER SUPPLY\n")
    return ser
