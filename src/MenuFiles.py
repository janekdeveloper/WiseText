import flet as ft
from flet import (
	UserControl,
	MenuBar,
	Page,
	ControlEvent,
	app
	)

class MenuFiles(UserControl):
    def __init__(self):
        super().__init__()
        self.menubar = MenuBar( expand=True,
                                style=ft.MenuStyle(
                                    alignment=ft.alignment.top_left,
                                    bgcolor=ft.colors.BLACK,
                                    mouse_cursor={ft.MaterialState.HOVERED: ft.MouseCursor.WAIT, ft.MaterialState.DEFAULT: ft.MouseCursor.ZOOM_OUT},
                                    ),
                                controls=[
                                    ft.SubmenuButton(
                                        content=ft.Text("File", color=ft.colors.WHITE),
                                        controls=[
                                            ft.MenuItemButton(
                                                content=ft.Text("About")
                                            )
                                        ]
                                    )
                                ]
                              )

    def build(self) -> MenuBar:
        return self.menubar