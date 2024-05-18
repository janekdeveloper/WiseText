import flet as ft
from flet import (
	TextField,
	InputBorder,
	Page,
	ControlEvent,
	app
	)

class FieldText(TextField):
	def __init__(self, on_change):
		super().__init__()
		self.expand=True
		self.multiline = True
		self.autofocus=True
		self.border=ft.InputBorder.NONE
		# self.min_lines=49
		self.content_padding=2
		self.value=''
		self.on_change = on_change