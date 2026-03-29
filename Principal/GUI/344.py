from PySide6.QtWidgets import QApplication,QPushButton
import sys

app = QApplication(sys.argv)

button = QPushButton('Texto do botão')
button.setStyleSheet('font-size: 40px; color: red')
button.show() # Adicionar o widget na hierarquia e exibe a janela

button2 = QPushButton('Texto do botão 2')
button2.show()

app.exec() # Executa o loop da aplicação