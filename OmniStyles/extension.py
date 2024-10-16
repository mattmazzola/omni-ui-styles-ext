import gc
import weakref

import omni
import omni.kit.app
import omni.kit.commands
import omni.log
import omni.timeline
import omni.ui as ui
import omni.ui.workspace_utils
import omni.usd
from omni.isaac.ui.element_wrappers import ScrollingWindow
from omni.isaac.ui.menu import make_menu_item_description
from omni.kit.menu.utils import add_menu_items, remove_menu_items

from .global_variables import EXTENSION_TITLE, MENU_BAR_BUTTON_NAME
from .theme.styles import styles
from .ui_builder import UIBuilder


class Extension(omni.ext.IExt):

    def on_startup(self, ext_id: str):
        self.ext_id = ext_id
        self.ui_builder = UIBuilder()

        name = EXTENSION_TITLE
        self._window = ScrollingWindow(
            title=EXTENSION_TITLE,
            width=600,
            height=600,
            visible=False,
            dockPreference=ui.DockPreference.LEFT_BOTTOM,
        )
        self._window.set_visibility_changed_fn(self._on_change_window_visibility)
        self._menu_items = [
            make_menu_item_description(
                ext_id=self.ext_id,
                name=name,
                onclick_fun=lambda a=weakref.proxy(self): a._on_click_menu_callback(),
            )
        ]

        add_menu_items(self._menu_items, MENU_BAR_BUTTON_NAME)

        # Make the Window visible by default
        self._window.visible = True
        self._on_change_window_visibility(True)

    def on_shutdown(self):
        remove_menu_items(self._menu_items, MENU_BAR_BUTTON_NAME)

        if self._window:
            self._window = None

        self.ui_builder.cleanup()
        gc.collect()

    def _on_click_menu_callback(self):
        self._window.visible = not self._window.visible

    def _on_change_window_visibility(self, visible: bool):
        omni.log.info(f"{self._on_change_window_visibility.__name__}: {visible}")
        if self._window.visible:
            self._build_ui()
        else:
            self.ui_builder.cleanup()

    def _build_ui(self):
        with self._window.frame:
            with ui.VStack(
                spacing=0,
                height=0,
                style=styles,
            ):
                self.ui_builder.build_ui()
