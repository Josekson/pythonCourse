import sys
import time
from PySide6.QtWidgets import (QApplication, QMainWindow, QPlainTextEdit, 
                             QVBoxLayout, QWidget, QPushButton, QLabel, 
                             QLineEdit, QDialog, QMessageBox)
from PySide6.QtCore import QThread, Signal, Slot, Qt

# --- TELA DE LOGIN ---
class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Acesso ao Sistema")
        self.setFixedSize(300, 180)
        
        layout = QVBoxLayout()
        
        self.label_user = QLabel("Usuário:")
        self.input_user = QLineEdit()
        self.input_user.setPlaceholderText("Digite o usuário")
        
        self.label_pass = QLabel("Senha:")
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.Password)
        self.input_pass.setPlaceholderText("Digite a senha")
        
        self.btn_login = QPushButton("ENTRAR")
        self.btn_login.setFixedHeight(40)
        self.btn_login.clicked.connect(self.check_login)
        
        layout.addWidget(self.label_user)
        layout.addWidget(self.input_user)
        layout.addWidget(self.label_pass)
        layout.addWidget(self.input_pass)
        layout.addSpacing(10)
        layout.addWidget(self.btn_login)
        
        self.setLayout(layout)

    def check_login(self):
        # Lógica simples de validação (Exemplo: admin / 123)
        if self.input_user.text() == "admin" and self.input_pass.text() == "123":
            self.accept()  # Fecha o diálogo e retorna QDialog.Accepted
        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha inválidos!")

# --- WORKER E CONSOLE (SEU CÓDIGO ORIGINAL) ---
class AutomationWorker(QThread):
    log_signal = Signal(str)
    finished_signal = Signal()

    def run(self):
        passos = ["Checando sensores...", "Validando firmware...", "Leitura de QR Code: OK", "PASS"]
        for p in passos:
            time.sleep(1.2)
            self.log_signal.emit(p)
        self.finished_signal.emit()

class SmartConsole(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Monitor de Teste - Logado")
        self.resize(500, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.console = QPlainTextEdit()
        self.console.setReadOnly(True)
        self.set_console_style("default")
        self.layout.addWidget(self.console)

        self.btn_start = QPushButton("INICIAR TESTE")
        self.btn_start.setFixedHeight(40)
        self.btn_start.clicked.connect(self.start_test)
        self.layout.addWidget(self.btn_start)

        self.worker = AutomationWorker()
        self.worker.log_signal.connect(self.process_log)
        self.worker.finished_signal.connect(self.on_finished)

    def set_console_style(self, mode):
        if mode == "success":
            self.console.setStyleSheet("background-color: #28a745; color: white; font-family: 'Consolas'; font-weight: bold; font-size: 14px;")
        else:
            self.console.setStyleSheet("background-color: #2b2b2b; color: #cfcfcf; font-family: 'Consolas'; font-size: 13px;")

    @Slot(str)
    def process_log(self, text):
        self.console.appendPlainText(f"> {text}")
        if text == "PASS": self.set_console_style("success")
        self.console.ensureCursorVisible()

    def start_test(self):
        self.console.clear()
        self.set_console_style("default")
        self.btn_start.setEnabled(False)
        self.worker.start()

    @Slot()
    def on_finished(self):
        self.btn_start.setEnabled(True)

# --- EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 1. Instancia e mostra a tela de login primeiro
    login = LoginWindow()
    
    # exec() para QDialog trava o código aqui até a janela ser fechada
    if login.exec() == QDialog.Accepted:
        # 2. Se o login foi aceito, abre a janela principal
        main_window = SmartConsole()
        main_window.show()
        sys.exit(app.exec())
    else:
        # Se fechar o login sem sucesso, encerra o app
        sys.exit(0)