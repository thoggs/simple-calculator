
import sys
from PyQt5 import QtWidgets

teste = False


# Classe calculadora
class Calculadora(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora Simples')  # Titulo da aplicação
        self.setFixedSize(400, 400)  # Definindo um tamanho fixo
        self.cw = QtWidgets.QWidget()
        self.grid = QtWidgets.QGridLayout(self.cw)

        self.display = QtWidgets.QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background: white; color: #000; font-size: 30px; '
            'font-weight: 700}'
        )
        self.display.setSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                   QtWidgets.QSizePolicy.Expanding)

        self.addbtn(QtWidgets.QPushButton('7'), 1, 0, 1, 1)
        self.addbtn(QtWidgets.QPushButton('8'), 1, 1, 1, 1)
        self.addbtn(QtWidgets.QPushButton('9'), 1, 2, 1, 1)
        self.addbtn(QtWidgets.QPushButton('+'), 1, 3, 1, 1)
        self.addbtn(QtWidgets.QPushButton('C'), 1, 4, 1, 1,
                    lambda: self.display.setText(''),
                    'background: #ff867c; font-weight: 700'
                    )

        self.addbtn(QtWidgets.QPushButton('4'), 2, 0, 1, 1)
        self.addbtn(QtWidgets.QPushButton('5'), 2, 1, 1, 1)
        self.addbtn(QtWidgets.QPushButton('6'), 2, 2, 1, 1)
        self.addbtn(QtWidgets.QPushButton('-'), 2, 3, 1, 1)
        self.addbtn(QtWidgets.QPushButton('<='), 2, 4, 1, 1,
                    lambda: self.display.setText(
                        self.display.text()[:-1]
                    ),
                    'background: #66bb6a; font-weight: 700'
                    )

        self.addbtn(QtWidgets.QPushButton('1'), 3, 0, 1, 1)
        self.addbtn(QtWidgets.QPushButton('2'), 3, 1, 1, 1)
        self.addbtn(QtWidgets.QPushButton('3'), 3, 2, 1, 1)
        self.addbtn(QtWidgets.QPushButton('/'), 3, 3, 1, 1)
        self.addbtn(QtWidgets.QPushButton(''), 3, 4, 1, 1)

        self.addbtn(QtWidgets.QPushButton(','), 4, 0, 1, 1)
        self.addbtn(QtWidgets.QPushButton('0'), 4, 1, 1, 1)
        self.addbtn(QtWidgets.QPushButton('%'), 4, 2, 1, 1)
        self.addbtn(QtWidgets.QPushButton('*'), 4, 3, 1, 1)
        self.addbtn(QtWidgets.QPushButton('='), 4, 4, 1, 1,
                    self.eval_eq,
                    'background: #63a4ff; font-weight: 700'
                    )

        self.setCentralWidget(self.cw)

    def addbtn(self, btn, row, col, rowspan, colspan, funcao=None,
               style=None):  # Botões e parâmetros
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QtWidgets.QSizePolicy.Preferred,
                          QtWidgets.QSizePolicy.Expanding)

    def eval_eq(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception:
            self.display.setText('Conta Inválida!')


if __name__ == '__main__':
    qt = QtWidgets.QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    teste = True
    qt.exec_()
