import sys

from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QPushButton, QLabel
from PySide6.QtGui import QPixmap

class Line(QLineEdit):
    def __init__(self, text, password=False):
        super().__init__()

        if password:
            self.setEchoMode(QLineEdit.EchoMode.Password)
        self.setPlaceholderText(text)
        self.setFixedHeight(30)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("""
            QLineEdit{
                border: 2px solid #9a9b9c;
                border-radius: 5px
            }
        """)

class Button(QPushButton):
    def __init__(self, text):
        super().__init__()

        self.setText(text)
        self.setFixedSize(60, 30)
        self.setStyleSheet("""
        QPushButton {
            background-color: #00ff7b;
            border-radius: 4px;
            font-size: 14px;
            }
        
        QPushButton:hover {             /* Animacao de passar o mouse em cima */
            background-color: #38a4eb;  
            }

        QPushButton:pressed {           /* Animacao para clicar no botao */
            background-color: #328cc7;  
            font-size: 16px;          
            }
        """)

class Image(QLabel):
    def __init__(self):
        super().__init__()

        self.setScaledContents(True)
        self.setFixedSize(100, 100)

        self.local_image = Path(__file__).parent / "Icone_login.png"
        self.icone_login = QPixmap(str(self.local_image))

        self.setPixmap(self.icone_login)