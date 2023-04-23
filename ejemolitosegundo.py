import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication

class Cronometro:
    def __init__(self):
        self.tiempo = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_tiempo)

    def iniciar(self):
        self.timer.start(1000)

    def detener(self):
        self.timer.stop()

    def actualizar_tiempo(self):
        self.tiempo += 1
        print(self.tiempo)


app = QApplication([])
cronometro = Cronometro()
cronometro.iniciar()
app.exec()