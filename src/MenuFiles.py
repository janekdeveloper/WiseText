import flet as ft
from flet import (
	UserControl,
	MenuBar,
	Page,
	ControlEvent,
	app
	)
import src

class MenuFiles(UserControl):
	def __init__(self, page, tabs_menu):
		super().__init__()
		self.page = page
		self.tabs_menu = tabs_menu
		self.page.on_keyboard_event = self.on_keyboard

	def close_tab_clicked(self, e: ControlEvent):
		if len(self.tabs_menu.tabs) > 0:
			del self.tabs_menu.tabs[self.tabs_menu.selected_index]
			self.tabs_menu.update()

			if len(self.tabs_menu.tabs) == 0:
				self.tabs_menu.selected_index = -1
			elif self.tabs_menu.selected_index >= len(self.tabs_menu.tabs):
				self.tabs_menu.selected_index = len(self.tabs_menu.tabs) - 1

			self.tabs_menu.update()

	def new_clicked(self, e: ControlEvent):
		new_tab_content = src.FieldText()
		new_tab_content.value='Hello, World!'
		new_tab = ft.Tab(content=new_tab_content, tab_content = ft.Row([ ft.Text(f"Untitled"), ft.IconButton(icon=ft.icons.CLOSE, tooltip="Close tab", on_click=self.close_tab_clicked) ]))

		self.tabs_menu.tabs.append(new_tab)
		self.tabs_menu.update()

	def open_clicked(self, e: ControlEvent):
		pass

	def save_clicked(self, e: ControlEvent):
		pass

	def save_as_clicked(self, e: ControlEvent):
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

		if e.ctrl and e.key == 'W':
			self.close_tab_clicked(e)
		
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