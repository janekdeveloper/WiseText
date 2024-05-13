import flet as ft
import src

def main(page):
	page.title = "WiseText"
	page.theme_mode = "dark"
	page.dark_theme = ft.theme.Theme(color_scheme_seed=ft.colors.GREEN)

	tabs_menu = src.TabsMenu()
	page.add(src.WiseText(page, tabs_menu))
	page.update()

ft.app(main)