import flet as ft
from flet import (
	UserControl,
	TextField,
	InputBorder,
	Page,
	ControlEvent,
	app
	)

class WiseText(UserControl):
    def __init__(self):
        super().__init__()
        self.textfield = TextField(multiline=True,
        	                       autofocus=True,
        	                       border=ft.InputBorder.NONE,
        	                       min_lines=49,
        	                       on_change=self.save_text,
        	                       content_padding=30,
        	                       cursor_color='yellow')

    def save_text(self, e: ControlEvent) -> None:
        with open('save.txt', 'w') as f:
            f.write(self.textfield.value)

    def read_text(self) -> str | None:
        try:
            with open('save.txt', 'r') as f:
                return f.read()
        except FileNotFoundError:
            self.textfield.hint_text = 'Hello, World!'

    def build(self) -> TextField:
        self.textfield.value=self.read_text()
        return self.textfield