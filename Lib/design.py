

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_port(object):
    def setupUi(self, port):
        if not port.objectName():
            port.setObjectName(u"port")
        port.resize(800, 600)
        self.widget = QWidget(port)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(80, 50, 343, 222))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.textBrowser = QTextBrowser(self.widget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_2.addWidget(self.textBrowser)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)


        self.retranslateUi(port)

        QMetaObject.connectSlotsByName(port)
    # setupUi

    def retranslateUi(self, port):
        port.setWindowTitle(QCoreApplication.translate("port", u"port", None))
        self.pushButton.setText(QCoreApplication.translate("port", u"Send", None))
        self.pushButton_2.setText(QCoreApplication.translate("port", u"Connection", None))
        self.pushButton_3.setText(QCoreApplication.translate("port", u"clean", None))
    # retranslateUi

