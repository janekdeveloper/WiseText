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

	def build(self):

		self.page.padding=ft.padding.all(0)

		return self.page.overlay.append(
			ft.Column([src.MenuFiles(self.page, self.tabs_menu), self.tabs_menu], expand=True, spacing=0)
		)