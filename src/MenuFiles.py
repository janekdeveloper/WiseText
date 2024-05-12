import flet as ft
from flet import (
	UserControl,
	MenuBar,
	Page,
	ControlEvent,
	app
	)

class MenuFiles(UserControl):
	def __init__(self, page):
		super().__init__()
		self.page = page
		self.page.on_keyboard_event = self.on_keyboard

	def new_clicked(self, e):
		print(1)

	def open_clicked(self, e):
		pass

	def save_clicked(self, e):
		pass

	def save_as_clicked(self, e):
		pass

	def on_keyboard(self, e: ft.KeyboardEvent):
		if e.ctrl and e.key == 'N':
			self.new_clicked(e)

		if e.ctrl and e.key == 'O':
			self.open_clicked(e)
		
		if e.ctrl and e.shift and e.key == 'S':
			self.save_as_clicked(e)

		if e.ctrl and e.key == 'S':
			self.save_clicked(e)
		
		self.page.update()

	def build(self) -> MenuBar:
		self.menubar = MenuBar( expand=True,
								style=ft.MenuStyle(
									alignment=ft.alignment.top_left,
									bgcolor=ft.colors.BLACK,
									mouse_cursor={ft.MaterialState.HOVERED: ft.MouseCursor.WAIT, ft.MaterialState.DEFAULT: ft.MouseCursor.ZOOM_OUT},
									),
								controls=[
									ft.SubmenuButton(
										expand=True,
										content=ft.Text("File", color=ft.colors.WHITE),
										controls=[
											ft.MenuItemButton(
												content=ft.Text("About")
											),
											ft.MenuItemButton(
												content=ft.Text("New"),
												on_click=self.new_clicked
											),
											ft.MenuItemButton(
												content=ft.Text("Open"),
												on_click=self.open_clicked
											),
											ft.MenuItemButton(
												content=ft.Text("Save"),
												on_click=self.save_clicked
											),
											ft.MenuItemButton(
												content=ft.Text("Save As"),
												on_click=self.save_as_clicked
											),
										]
									),
									ft.SubmenuButton(
										expand=True,
										content=ft.Text("Edit", color=ft.colors.WHITE),
										controls=[
											ft.MenuItemButton(
												content=ft.Text("Paste"),
											),
											ft.MenuItemButton(
												content=ft.Text("Copy")
											),
											ft.MenuItemButton(
												content=ft.Text("Cut")
											),
										]
									),
									ft.SubmenuButton(
										expand=True,
										content=ft.Text("Selection", color=ft.colors.WHITE),
										controls=[
											ft.MenuItemButton(
												content=ft.Text("Select All")
											)
										]
									),
								]
							  )
		
		return ft.Row(
			[
				self.menubar,
			]
		)