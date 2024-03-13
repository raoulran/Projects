import sys
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from AI import start

class AnimatedButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.animation = QtCore.QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(300)  # Animation duration in milliseconds

    def enterEvent(self, event):
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(QtCore.QRect(self.geometry().x(), self.geometry().y() - 10, self.geometry().width(), self.geometry().height()))
        self.animation.start()

    def leaveEvent(self, event):
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(QtCore.QRect(self.geometry().x(), self.geometry().y() + 10, self.geometry().width(), self.geometry().height()))
        self.animation.start()

class Ui_WiseGUI(object):
    def setupUi(self, WiseGUI):
        WiseGUI.setObjectName("WiseGUI")
        WiseGUI.resize(561, 336)
        self.centralwidget = QtWidgets.QWidget(WiseGUI)
        self.centralwidget.setObjectName("centralwidget")

        # Background Animation
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 561, 336))
        self.movie = QtGui.QMovie("C:/Users/kamin_t7sflus/Desktop/New folder/Project W.I.S.E/WISE/images/inter2.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        # START Button
        self.pushButton = AnimatedButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 260, 91, 31))  # Adjusted button size
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 0);\n"
                                       "border-color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")

        # EXIT Button
        self.pushButton_2 = AnimatedButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 260, 61, 31))  # Adjusted button size
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")

        WiseGUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(WiseGUI)
        QtCore.QMetaObject.connectSlotsByName(WiseGUI)

    def retranslateUi(self, WiseGUI):
        _translate = QtCore.QCoreApplication.translate
        WiseGUI.setWindowTitle(_translate("WiseGUI", "Dialog"))
        self.pushButton.setText(_translate("WiseGUI", "START"))
        self.pushButton_2.setText(_translate("WiseGUI", "EXIT"))

class WiseGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WiseGUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start_assistant)
        self.ui.pushButton_2.clicked.connect(self.exit_application)
        self.assistant_thread = None

    def start_assistant(self):
        print("Start button clicked")
        self.ui.pushButton.setVisible(False)
        self.assistant_thread = threading.Thread(target=start)
        self.assistant_thread.start()

    def exit_application(self):
        print("Exit button clicked")
        if self.assistant_thread and self.assistant_thread.is_alive():
            self.assistant_thread.join()  # Wait for the assistant thread to finish
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = WiseGUI()
    main_window.show()

    sys.exit(app.exec_())
