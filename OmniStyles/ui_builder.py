import omni.ui as ui
from omni.isaac.ui.element_wrappers import UIWidgetWrapper


class UIBuilder:
    def __init__(self):
        self.wrapped_ui_elements: list[UIWidgetWrapper] = []

    def cleanup(self):
        for ui_elem in self.wrapped_ui_elements:
            ui_elem.cleanup()

    def build_ui(self):
        with ui.VStack(spacing=20):
            ui.Label(
                "Omni Styles with Figma",
                alignment=ui.Alignment.CENTER,
                name="h1",
            )

            ui.Label(
                "Buttons",
                alignment=ui.Alignment.CENTER,
                name="h2",
            )

            with ui.HStack():
                ui.Spacer()

                with ui.VStack(
                    spacing=10,
                    width=200,
                ):
                    button_default = ui.Button(
                        "Isaac Default",
                        name="default",
                    )
                    button_primary = ui.Button(
                        "Primary",
                        name="primary",
                    )
                    button_danger = ui.Button(
                        "Danger",
                        name="danger",
                    )
                    button_secondary = ui.Button(
                        "Secondary",
                        name="secondary",
                    )

                ui.Spacer()

            ui.Label(
                "Dropdowns",
                alignment=ui.Alignment.CENTER,
                name="h2",
            )

            with ui.HStack():
                ui.Spacer()

                with ui.VStack(
                    spacing=10,
                    width=200,
                ):
                    combo_box = ui.ComboBox()
                    for value in ["Default 1", "Default 2", "Default 3"]:
                        combo_box.model.append_child_item(None, ui.SimpleStringModel(value))

                    combo_box_primary = ui.ComboBox(name="primary")
                    for value in ["Primary 1", "Primary 2", "Primary 3"]:
                        combo_box_primary.model.append_child_item(None, ui.SimpleStringModel(value))

                    combo_box_secondary = ui.ComboBox(name="secondary")
                    for value in ["Secondary 1", "Secondary 2", "Secondary 3"]:
                        combo_box_secondary.model.append_child_item(None, ui.SimpleStringModel(value))

                ui.Spacer()

            with ui.HStack():
                ui.Spacer()

                with ui.VStack(
                    spacing=10,
                    width=200,
                ):
                    with ui.HStack(spacing=0):
                        ui.Label("Disable")
                        is_disabled_checkbox = ui.CheckBox()

                        def on_checkbox_change(checked_model: ui.SimpleBoolModel):
                            button_default.enabled = not checked_model.as_bool
                            button_primary.enabled = not checked_model.as_bool
                            button_danger.enabled = not checked_model.as_bool
                            button_secondary.enabled = not checked_model.as_bool
                            # Does not work?
                            combo_box.enabled = not checked_model.as_bool
                            combo_box_primary.enabled = not checked_model.as_bool
                            combo_box_secondary.enabled = not checked_model.as_bool

                        is_disabled_checkbox.model.add_value_changed_fn(on_checkbox_change)
                        is_disabled_checkbox.model.set_value(False)

                ui.Spacer()
