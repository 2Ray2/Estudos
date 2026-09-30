import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from components import Line, Button, Image

app = QApplication(sys.argv)

main_window = QWidget() # janela principal
main_window.setWindowTitle("Tela de login") # Nome da janela

main_window.setMinimumSize(500, 500) # Definir tamanho mínimo para a janela

main_window.setStyleSheet("background-color: white;") # Altera a cor do background

main_layout = QVBoxLayout() # Layout principal
main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter) # Centraliza o layout

container = QWidget() # Caixa para o widgets
container.setFixedSize(350, 400) # Tamanho fixo da caixa
container.setStyleSheet("""
    border-radius: 10px;
""")

layout = QVBoxLayout(container) # Layout da caixa de widgets
layout.setSpacing(25) # Define o espaço entre os widgets
layout.setContentsMargins(20, 20, 20, 20)

image = Image()

# Adicionando os componentes
layout.addWidget(image, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(Line("Nome"))
layout.addWidget(Line("Senha", password=True))
layout.addWidget(Button("Login"), alignment=Qt.AlignmentFlag.AlignCenter)
layout.addStretch() # Ajuste de posicionamento 

main_layout.addWidget(container) # Adicionando a caixa com os Widgets ao Layout principal
main_window.setLayout(main_layout) # Adicionando o Layout principal na janela

main_window.show()

if __name__ == "__main__":
    sys.exit(app.exec())