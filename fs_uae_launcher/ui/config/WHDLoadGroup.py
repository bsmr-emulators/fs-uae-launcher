import fsui as fsui
from ...Config import Config
from ...I18N import gettext
from ..HelpButton import HelpButton


class WHDLoadGroup(fsui.Group):

    def __init__(self, parent):
        fsui.Group.__init__(self, parent)
        self.layout = fsui.VerticalLayout()

        heading_label = fsui.HeadingLabel(self, gettext("WHDLoad Arguments"))
        self.layout.add(heading_label, margin=10)
        self.layout.add_spacer(0)

        self.text_field = fsui.TextField(self, "")
        hori_layout = fsui.HorizontalLayout()
        self.layout.add(hori_layout, fill=True, margin=10)
        hori_layout.add(self.text_field, expand=True)

        self.help_button = HelpButton(
            self, "http://fs-uae.net/whdload-support")
        hori_layout.add(self.help_button, margin_left=10)

        self.initialize_from_config()
        self.set_config_handlers()

    def initialize_from_config(self):
        self.on_config("x_whdload_args", Config.get("x_whdload_args"))

    def set_config_handlers(self):
        self.text_field.on_change = self.on_text_change
        Config.add_listener(self)

    def on_destroy(self):
        print("on_destroy")
        Config.remove_listener(self)

    def on_config(self, key, value):
        if key == "x_whdload_args":
            if value != self.text_field.get_text():
                self.text_field.set_text(value)

    def on_text_change(self):
        Config.set("x_whdload_args", self.text_field.get_text())
