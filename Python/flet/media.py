from flet import * 
from assets.components import CustomContainer

def app(page: Page):
    page.title = "Media"
    page.width = 360
    page.height = 567
    page.vertical_alignment = "center"  # type: ignore
    page.horizontal_alignment = "center"   # type: ignore
    #page.window.maximizable = False
    #page.window.resizable = False 
    page.bgcolor = "Blue"
    page.fonts = {
        'Power Calm' : 'fonts/Power Calm.otf'
                 }
    
    page.theme_mode = ThemeMode.LIGHT
    page.add(
        CustomContainer()
    )

if __name__ == "__main__":
    run(app)