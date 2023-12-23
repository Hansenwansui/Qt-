from PySide6.QtWidgets import QApplication, QWidget
from Ui_计算器 import Ui_Form
import sys


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.result = ""

        self.bind()

    def bind(self):
        self.PushButton_n0.clicked.connect(lambda: self.addNumber("0"))
        self.PushButton_n1.clicked.connect(lambda: self.addNumber("1"))
        self.PushButton_n2.clicked.connect(lambda: self.addNumber("2"))
        self.PushButton_n3.clicked.connect(lambda: self.addNumber("3"))
        self.PushButton_n4.clicked.connect(lambda: self.addNumber("4"))
        self.PushButton_n5.clicked.connect(lambda: self.addNumber("5"))
        self.PushButton_n6.clicked.connect(lambda: self.addNumber("6"))
        self.PushButton_n7.clicked.connect(lambda: self.addNumber("7"))
        self.PushButton_n8.clicked.connect(lambda: self.addNumber("8"))
        self.PushButton_n9.clicked.connect(lambda: self.addNumber("9"))
        self.PushButton_add.clicked.connect(lambda: self.addNumber("+"))
        self.PushButton_sub.clicked.connect(lambda: self.addNumber("-"))
        self.PushButton_mul.clicked.connect(lambda: self.addNumber("*"))
        self.PushButton_div.clicked.connect(lambda: self.addNumber("/"))
        self.PushButton_point.clicked.connect(lambda: self.addNumber("."))
        self.PushButton_equal.clicked.connect(lambda: self.equal())
        self.PushButton_clean.clicked.connect(lambda: self.clear())
        self.PushButton_back.clicked.connect(lambda: self.back())
        self.PushButton_quit.clicked.connect(QApplication.instance().quit)

    def addNumber(self, number: str):
        self.LineEdit.clear()
        self.result += str(number)
        self.LineEdit.setText(self.result)

    def equal(self):
        self.result = eval(self.result)
        self.LineEdit.setText(str(self.result))

    def clear(self):
        self.result = ""
        self.LineEdit.clear()

    def back(self):
        self.result = self.result[:-1]
        self.LineEdit.setText(self.result)


def main():
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
