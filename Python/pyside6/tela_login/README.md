# Tela de login

Projeto de aprendizado que cria uma tela de login simples com Python e PySide6.

## Estrutura

- `main.py`: cria a janela, organiza os componentes e inicia a aplicação.
- `components.py`: define os componentes reutilizáveis `Line` (campo de texto), `Button` (botão) e `Image` (ícone).
- `icone_login.png`: imagem exibida na parte superior do formulário.

O ícone é carregado a partir da própria pasta do projeto. Mantenha esse arquivo junto de `components.py`.

## Classes

### `Line`

Campo de texto com placeholder centralizado. O modo ``password`` oculta os caracteres digitados.

```python
class Line(QLineEdit):
    def __init__(self, text, password=False):
        super().__init__()

        if password:
            self.setEchoMode(QLineEdit.EchoMode.Password)
        self.setPlaceholderText(text)
        self.setFixedHeight(30)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("""
            QLineEdit {
                border: 2px solid #9a9b9c;
                border-radius: 5px;
            }
        """)
```

### `Button`

Botão com tamanho fixo e estilos diferentes para os estados normal, hover e pressionado.

```python
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

            QPushButton:hover {
                background-color: #38a4eb;
            }

            QPushButton:pressed {
                background-color: #328cc7;
                font-size: 16px;
            }
        """)
```

### `Image`

Widget que carrega `icone_login.png` da pasta do projeto e exibe a imagem em um espaço de 100 × 100 pixels.

```python
class Image(QLabel):
    def __init__(self):
        super().__init__()

        self.setScaledContents(True)
        self.setFixedSize(100, 100)

        self.local_image = Path(__file__).parent /      "icone_login.png"
        self.icone_login = QPixmap(str(self.local_image))

        self.setPixmap(self.icone_login)
```

## Interface

A janela contém campos para **nome** e **senha**, um **ícone** e um botão **Login**. O campo de senha oculta o texto digitado, e o botão muda de aparência ao passar o mouse ou ser pressionado.

Esta versão implementa apenas a interface: o botão ainda não valida credenciais nem realiza autenticação.
