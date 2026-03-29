# QWidget e Qlayout de Pyside6.QtWidgets
# QWidget -> Janela genérica
# QLayout -> Um widget de layout que recebe outros widgets

# PASSO A PASSO DE COMO CRIAR UMA GUI
# O QAPPLICATION É UMA JANELA QUE RODA SEM APARECER NA TELA (UI-CONTROL DO NODE-RED)
# DEPOIS A GENTE CRIA UMA JANELA(QUE TAMBÉM É UM WIDGET)
# DEPOIS CRIA UM LAYOUT QUE É RESPONSÁVEL POR RECEBER OUTROS WIDGETS(BOTÕES,ETC.)
# ADICIONA O LAYOUT NA JANELA
# ADICIONA WIDGETS NESSE LAYOUT

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout
# COM QGridLayout É POSSIVEL DEFINIR PARA ONDE VAI CADA WIDGET
import sys

app = QApplication(sys.argv)

central_widget = QWidget() # janela
layout = QGridLayout() # layout -> QHBoxLayout: adiciona widgets na horizontal. QVBoxLayout: adiciona widgets na vertical

central_widget.setLayout(layout) # adiciona layout na janela

button = QPushButton('Texto do botão') #widget dentro do layout da janela
button.setStyleSheet('font-size: 40px; color: red')

button2 = QPushButton('Texto do botão 2') #widget dentro do layout da janela

button3 = QPushButton('Texto do botão 3') #widget dentro do layout da janela

layout.addWidget(button, # adiciona widgets dentro do layout
                 1, # linha onde o widget ficará
                 1, # coluna onde o widget ficará
                 1, # quantas linhas o widget se expandirá (row_expand)
                 2  # quantas colunas o widget se expandirá (columm_expand)
                 ) 

layout.addWidget(button2,2,1)
layout.addWidget(button3,2,2)

central_widget.show() # MOSTRA A JANELA

app.exec() # Executa o loop da aplicação