import flet as ft
from flet import (
	UserControl,
	TextField,
	InputBorder,
	Page,
	ControlEvent,
	app
	)
import src

class WiseText(UserControl):
	def __init__(self, page, tabs_menu):
		super().__init__()
		self.page = page
		self.tabs_menu = tabs_menu

	# def save_text(self, e: ControlEvent) -> None:
	#     with open('save.txt', 'w') as f:
	#         f.write(self.textfield.value)

	# def read_text(self) -> str | None:
	#     try:
	#         with open('save.txt', 'r') as f:
	#             return f.read()
	#     except FileNotFoundError:
	#         self.textfield.hint_text = 'Hello, World!'

	def build(self):

		self.page.padding=ft.padding.all(0)

		return self.page.overlay.append(
			ft.Column([src.MenuFiles(self.page, self.tabs_menu), self.tabs_menu], expand=True, spacing=0)
		)