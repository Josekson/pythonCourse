import sys
import time
from PySide6.QtWidgets import (QApplication, QMainWindow, QPlainTextEdit, 
                             QVBoxLayout, QWidget, QPushButton, QLabel)
from PySide6.QtCore import QThread, Signal, Slot, Qt

class AutomationWorker(QThread):
    log_signal = Signal(str)
    finished_signal = Signal()

    def run(self):
        # Simulação de passos de verificação
        passos = [
            "Checando sensores...",
            "Validando firmware...",
            "Leitura de QR Code: OK",
            "PASS"  # Esta é a palavra-chave que mudará a cor
        ]

        for p in passos:
            time.sleep(1.2)
            self.log_signal.emit(p)
        
        self.finished_signal.emit()

class SmartConsole(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Monitor de Teste")
        self.resize(500, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.console = QPlainTextEdit()
        self.console.setReadOnly(True)
        
        # Estilo inicial padrão (cinza/escuro)
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
        """Define o visual do console baseado no status"""
        if mode == "success":
            # Fundo Verde quando der PASS
            self.console.setStyleSheet("""
                background-color: #28a745; 
                color: white; 
                font-family: 'Consolas'; 
                font-weight: bold;
                font-size: 14px;
            """)
        else:
            # Fundo padrão (Escuro/Neutro) para quando estiver processando
            self.console.setStyleSheet("""
                background-color: #2b2b2b; 
                color: #cfcfcf; 
                font-family: 'Consolas';
                font-size: 13px;
            """)

    @Slot(str)
    def process_log(self, text):
        self.console.appendPlainText(f"> {text}")
        
        # Lógica: Se a mensagem for exatamente "PASS", muda para verde
        if text == "PASS":
            self.set_console_style("success")
        
        # Scroll automático
        self.console.verticalScrollBar().setValue(
            self.console.verticalScrollBar().maximum()
        )

    def start_test(self):
        self.console.clear()
        self.set_console_style("default") # Reseta a cor ao iniciar novo teste
        self.btn_start.setEnabled(False)
        self.worker.start()

    @Slot()
    def on_finished(self):
        self.btn_start.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SmartConsole()
    window.show()
    sys.exit(app.exec())