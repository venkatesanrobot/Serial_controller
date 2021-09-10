import serial
import serial.tools.list_ports


class ComSerialCommunication:

    def __init__(self):
        self.PORT=[]

    def com_config(self,com_port):
        self.ser_com=serial.Serial()
        self.ser_com.port=com_port
        self.ser_com.baudrate=9600
        self.ser_com.bytesize=serial.EIGHTBITS
        self.ser_com.parity=serial.PARITY_NONE
        self.ser_com.stopbits=serial.STOPBITS_ONE
        return self.ser_com

    def list_port(self):
        for _ in serial.tools.list_ports.comports():
            self.PORT.append(_.device)

    def port_write(self,write_key):
        self.list_port()
        self.port_commuincation=self.com_config(self.PORT[0])
        self.port_commuincation.dsrdtr=False
        self.port_commuincation.open()
        self.port_commuincation.write(str(write_key).encode("utf-8"))
        self.port_commuincation.close()


    def port_read(self):
        pass




data=ComSerialCommunication()
#data.list_port()
data.port_write("OFF")