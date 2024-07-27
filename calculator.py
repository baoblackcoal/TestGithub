import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Calculator')

        self.layout = QVBoxLayout()
        self.result = QLineEdit()
        self.layout.addWidget(self.result)

        self.buttons = QGridLayout()
        self.layout.addLayout(self.buttons)

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0), ('CE', 4, 1)
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.on_click)
            self.buttons.addWidget(button, row, col)

        self.setLayout(self.layout)

    def on_click(self):
        sender = self.sender().text()
        current_text = self.result.text()

        if sender == 'C':
            self.result.clear()
        elif sender == 'CE':
            self.result.setText(current_text[:-1])
        elif sender == '=':
            try:
                self.result.setText(str(eval(current_text)))
            except:
                self.result.setText('Error')
        else:
            self.result.setText(current_text + sender)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
