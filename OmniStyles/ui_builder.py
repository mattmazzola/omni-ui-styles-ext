import omni.ui as ui
from omni.isaac.ui.element_wrappers import UIWidgetWrapper


class UIBuilder:
    def __init__(self):
        self.wrapped_ui_elements: list[UIWidgetWrapper] = []

    def cleanup(self):
        for ui_elem in self.wrapped_ui_elements:
            ui_elem.cleanup()

    def build_ui(self):
        with ui.VStack(
            spacing=20,
        ):
            ui.Label(
                "Omni Styles with Figma",
                alignment=ui.Alignment.CENTER,
                name="header",
            )

            ui.Button(
                "Button 1",
            )
