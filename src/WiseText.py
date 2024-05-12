import flet as ft
from flet import (
	UserControl,
	TextField,
	InputBorder,
	Page,
	ControlEvent,
	app
	)
import src.MenuFiles

class WiseText(UserControl):
	def __init__(self, page):
		super().__init__()
		self.page = page

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
#Colors green
#37b026
#00b952
#Color pink
#
		t = ft.Tabs(selected_index=1,
				animation_duration=300,
				tabs=[
						ft.Tab(
							text="Tab 1",
							content=ft.Container(
							content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
							),
						),
					],
				expand=1,
			)

		self.textfield = TextField(multiline=True,
								   autofocus=True,
								   border=ft.InputBorder.NONE,
								   min_lines=49,
								   # on_change=self.save_text,
								   content_padding=2,
								   )
		
		t.tabs.append(ft.Tab(
				text="Tab 2",
				content=self.textfield
			))

		self.page.padding=ft.padding.all(0)

		return self.page.overlay.append(
			ft.Column([src.MenuFiles(self.page), t], expand=True, spacing=0)
		)