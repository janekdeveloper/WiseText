import flet as ft
import src

def main(page):
	page.title = "WiseText"
	page.theme_mode = "dark"
	page.dark_theme = ft.theme.Theme(color_scheme_seed=ft.colors.GREEN)

	page.add(src.WiseText(page))
	page.update()

ft.app(main)