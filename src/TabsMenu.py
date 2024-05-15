import flet as ft
from flet import (
	Tabs,
	TextField,
	InputBorder,
	Page,
	ControlEvent,
	app
	)

class TabsMenu(Tabs):
	def __init__(self):
		super().__init__()
		self.selected_index=1
		self.animation_duration=300
		# self.expand=1
		self.scrollable = True
		self.tabs=[]