import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from serial_working import ComSerialCommunication

from design import Ui_port



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_port()
        self.Serial=ComSerialCommunication()
        self.ui.setupUi(self)


    def list_port(self):
        print(str(self.Serial.PORT))
        self.ui.comboBox.addItems(self.Serial.PORT)
        self.ui.pushButton_2.clicked.connect(self.change_name)
        self.ui.pushButton.clicked.connect(self.send_data)


    def change_name(self):
        self.ui.pushButton_2.setText("disconnect")

    def send_data(self):
        self.Serial.port_write(self.ui.comboBox.currentText(),self.ui.lineEdit.text())








if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.list_port()
    window.show()
    sys.exit(app.exec())