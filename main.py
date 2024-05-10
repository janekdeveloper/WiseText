import flet as ft
import src

def main(page):
	page.title = "WiseText 2"
	page.theme_mode = "dark"
	page.scroll = True
	page.add(
		ft.Row(
			[
				src.MenuFiles()
			],
			alignment=ft.MainAxisAlignment.SPACE_BETWEEN
		)
	)
	page.add(src.WiseText())

ft.app(main)