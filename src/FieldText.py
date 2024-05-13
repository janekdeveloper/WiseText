import flet as ft
from flet import (
	TextField,
	InputBorder,
	Page,
	ControlEvent,
	app
	)
import src


md1 = f'''```py
{ft.TextField(multiline = True, border=ft.InputBorder.NONE)}
'''
class FieldText(TextField):
	def __init__(self):
		super().__init__()
		self.multiline = True
		self.autofocus=True
		self.border=ft.InputBorder.NONE
		self.min_lines=49
		self.content_padding=2
		self.value=''