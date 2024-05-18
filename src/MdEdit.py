import flet as ft
from flet import (
	UserControl,
	Page,
	ControlEvent,
	app
	)
import src


class MdEdit(UserControl):
	def __init__(self, page, value=''):
		super().__init__()
		self.page = page
		self.text_field = src.FieldText(
			on_change=self.update_preview,
		)
		self.text_field.value=value
		self.md = ft.Markdown(
			value=self.text_field.value,
			selectable=True,
			extension_set="gitHubWeb",
		)

	async def update_preview(self, e):
		self.md.value = self.text_field.value
		self.page.update()

	async def final(self):
		return ft.Row(
			controls=[
				self.text_field,
				ft.VerticalDivider(width=9, thickness=3),
				ft.Container(
					ft.Column(
						[self.md],
						scroll="hidden"
					),
					expand=True,
					alignment=ft.alignment.top_left,
				)
			],
			vertical_alignment=ft.CrossAxisAlignment.START,
			expand=True
		)