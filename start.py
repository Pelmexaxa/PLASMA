import sys
import os

from gpiozero import LED

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from ui_plasma import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = UI_MainWindow()
        self.ui.setupUi(self)

        self.timer = QTimer(self)

        self.outLED = LED(17)

        self.time_now = {'hour': 0, 'minute': 0, 'second': 0}

        self.mass_control_button = [
            self.ui.l_down_button,
            self.ui.l_up_button,
            self.ui.c_down_nutton,
            self.ui.c_up_button,
            self.ui.r_up_button,
            self.ui.r_down_button]

        self.mass_control_button[0].clicked.connect(lambda: self.change_data_in_digit(0, False))
        self.mass_control_button[1].clicked.connect(lambda: self.change_data_in_digit(0, True))
        self.mass_control_button[2].clicked.connect(lambda: self.change_data_in_digit(1, False))
        self.mass_control_button[3].clicked.connect(lambda: self.change_data_in_digit(1, True))
        self.mass_control_button[4].clicked.connect(lambda: self.change_data_in_digit(2, True))
        self.mass_control_button[5].clicked.connect(lambda: self.change_data_in_digit(2, False))

        self.mass_data_digit = [
            self.ui.digit_1,
            self.ui.digit_2,
            self.ui.digit_3]

        # Набор состояний - NORMAL, NEW_TIMER, START_TIMER, END_TIMER
        # self.state = 'NORMAL'

    def visible_control_button(self, state):
        for elem in self.mass_control_button:
            if state:
                elem.show()
            else:
                elem.hide()

    def change_data_in_digit(self, index, increment):
        old = int(self.mass_data_digit[index].text())
        if increment:
            if old + 1 == 10:
                old = 8
            self.mass_data_digit[index].setText(f"{old + 1}")
        else:
            if old - 1 == -1:
                old = 1
            self.mass_data_digit[index].setText(f"{old - 1}")

    def get_data_on_digit(self):
        self.time_now['hour'] = int(self.mass_data_digit[0].text())
        self.time_now['minute'] = int(self.mass_data_digit[1].text())
        self.time_now['second'] = int(self.mass_data_digit[2].text())

    def set_data_on_digit(self):
        self.mass_data_digit[0].setText(str(self.time_now['hour']))
        self.mass_data_digit[1].setText(str(self.time_now['minute']))
        self.mass_data_digit[2].setText(str(self.time_now['second']))
        print(f"{self.time_now['hour']}-{self.time_now['minute']}-{self.time_now['second']}")
        if self.end_timer():
            print('ВЫКЛ')
            self.timer_on_off()
            self.timer.timeout.disconnect()
            self.ui.pushButton.clicked.disconnect()
            self.state_NORMAL()
        else:
            self.reduce_one_sec()

    def end_timer(self):
        if (self.time_now['hour'] <= 0) and (self.time_now['minute'] <= 0) and (self.time_now['second'] <= 0):
            return True
        else:
            return False

    def reduce_one_sec(self):
        if self.time_now['second'] - 1 < 0 and self.time_now['minute'] <= 0 and self.time_now['hour'] <= 0:
            self.time_now['second'] = 0
        elif self.time_now['second'] - 1 < 0:
            self.reduce_one_minute()
            self.time_now['second'] = 9
        else:
            self.time_now['second'] -= 1

    def reduce_one_minute(self):
        if self.time_now['minute'] - 1 < 0 and self.time_now['hour'] <= 0:
            self.time_now['minute'] = 0
        elif self.time_now['minute'] - 1 < 0:
            self.reduce_one_hour()
            self.time_now['minute'] = 9
        else:
            self.time_now['minute'] -= 1

    def reduce_one_hour(self):
        if self.time_now['hour'] - 1 < 0:
            self.time_now['hour'] = 0
        else:
            self.time_now['hour'] -= 1

    def timer_on_off(self):
        print('kek')
        if self.timer.isActive() == False:
            self.timer.setInterval(100)
            self.outLED.on()
            self.timer.start()
        else:
            self.outLED.off()
            self.timer.stop()

    def state_NORMAL(self):
        self.time_now['hour'] = 0
        self.time_now['minute'] = 0
        self.time_now['second'] = 0
        #self.disconnect(self.button_connect)
        self.ui.pushButton.clicked.connect(self.state_NEW_TIMER)
        self.visible_control_button(False)

    def state_NEW_TIMER(self):
        self.visible_control_button(True)
        self.ui.pushButton.clicked.disconnect()
        self.button_connect = self.ui.pushButton.clicked.connect(self.state_START_TIMER)

    def state_START_TIMER(self):
        self.get_data_on_digit()
        self.visible_control_button(False)
        self.timer.timeout.connect(self.set_data_on_digit)
        self.timer_on_off()
        self.ui.pushButton.clicked.disconnect()
        self.ui.pushButton.clicked.connect(self.timer_on_off)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.state_NORMAL()
    window.show()
    sys.exit(app.exec_())
