import serial
import serial.tools.list_ports
from time import sleep



class ComSerialCommunication:

    def __init__(self):
        self.PORT = [comport.device for comport in serial.tools.list_ports.comports()]
        self.Serialdata = ""
        self.enterclose = 1
        self.ser_com = serial.Serial()
        self.ser_com.baudrate = 9600
        self.ser_com.bytesize = serial.EIGHTBITS
        self.ser_com.parity = serial.PARITY_NONE
        self.ser_com.stopbits = serial.STOPBITS_ONE
        self.ser_com.timeout = 10
        self.ser_com.write_timeout = 20

    def port_write(self, write_key):
        self.ser_com.dsrdtr = False
        self.ser_com.port = self.PORT[0]
        self.ser_com.open()
        self.ser_com.write(str(write_key).encode("utf-8"))
        self.ser_com.close()

    def port_read(self):
        self.ser_com.port = self.PORT[0]
        self.enterclose = 1
        self.ser_com.open()
        sleep(2)
        self.Serialdata = self.ser_com.readline()
        self.ser_com.close()
        return self.Serialdata.decode("utf-8")



# data=ComSerialCommunication()
# data.port_write("OFF")
# print(data.port_read())