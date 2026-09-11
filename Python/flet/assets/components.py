from flet import *

def focus_effect(e, color):
    control = e.control

    control.scale = 1.05
    control.opacity = 0.95
    control.border_color = color
    control.update()

def blur_effect(e, color):
    control = e.control

    control.scale = 1  
    control.opacity = 1
    control.border_color = color
    control.update()

def hover_effect(e):
    control = e.control

    if e.data == "true":
        control.scale = 1.02
        control.opacity = 0.95
        control.shadow = BoxShadow(
            blur_radius=2,
            color=Colors.BLACK
        )

    else:  
        control.scale = 1
        control.opacity = 1

    control.update()

def save(e, fields):
        for field in fields:
        if not (field.value or "").strip():
            field.error_text = "Preencha este campo"
            
            field.update()

class CustomTextfield (TextField):
    def __init__(self, label=None, width=270, 
                 max_length=None, inputfilter=None, 
                 keyboardtype=KeyboardType.TEXT):
        super().__init__()

        self.label = label
        self.width = width
        self.max_length = max_length
        self.color = Colors.BLACK
        self.border_color = Colors.BLUE_100
        self.border_radius = 7
        self.border_width = 2
        self.cursor_height = 13
        self.scale = 1
        self.opacity = 1
        self.autocorrect = True
        self.enable_suggestions = True
        self.label_style = TextStyle(font_family='Power Calm')
        self.text_style = TextStyle(color=Colors.BLUE, font_family='Power Calm')  
        self.keyboard_type = keyboardtype
        self.input_filter = inputfilter
        self.error_style = TextStyle(
            font_family='Power Calm'
        )
        self.animate_scale = Animation(500, AnimationCurve.DECELERATE)
        self.animate_opacity = Animation(500, AnimationCurve.DECELERATE)

        self.on_focus = lambda e: focus_effect(e, color=Colors.BLUE_400)
        self.on_blur = lambda e: blur_effect(e, color=Colors.BLUE_100)

class CustomContainer(Container):
    def __init__(self):
        super().__init__()

        self.fields = [
            CustomTextfield(label="Nota 1", keyboardtype=KeyboardType.NUMBER,),
            CustomTextfield(label="Nota 2", keyboardtype=KeyboardType.NUMBER,),
            CustomTextfield(label="Nota 3", keyboardtype=KeyboardType.NUMBER,),
            CustomTextfield(label="Nota 4", keyboardtype=KeyboardType.NUMBER,)
        ]
        self.bgcolor = "White"
        #self.border_radius = 10
        self.width = 360
        self.height = 550
        self.border_radius = 10
        self.content = Column(
            [
                appbar := AppBar(
                    title=Text("Média", color="Black", font_family='Power Calm', size=20),
                    center_title=True,
                    bgcolor="White"
                ),

                Container(
                    content=Column(
                        self.fields + [CustomButton(on_click=lambda e: save(e, self.fields))],
                        horizontal_alignment="center", # type: ignore
                        width=360,
                        height=550,
                        spacing=30
                    )
                )
            ]
        )

class CustomButton (ElevatedButton):
    def __init__(self, on_click):
        super().__init__()

        self.content = Text('Salvar')
        self.width = 200
        self.scale = 1
        self.height = 40
        self.style = ButtonStyle(
            text_style=TextStyle(color=Colors.WHITE, font_family='Power Calm', size=20),
            bgcolor=Colors.BLUE_100
        )

        self.on_hover = hover_effect

    