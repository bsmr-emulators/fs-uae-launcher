from fsui import Image
from ...Config import Config
from ...I18N import gettext
from .StatusElement import StatusElement


class ProtectionElement(StatusElement):

    def __init__(self, parent):
        StatusElement.__init__(self, parent)
        # self.set_min_width(140)
        # self.layout = HorizontalLayout()
        self.protection_icon = Image("fs_uae_launcher:res/16/lock.png")
        # self.unknown_icon = self.icon.grey_scale()
        self.disabled_icon = Image(
            "fs_uae_launcher:res/16/lock_open_green.png")
        # self.disabled_icon = self.disabled_icon.grey_scale()
        self.icon = self.protection_icon

        self.protection = ""
        self.active = False

        Config.add_listener(self)
        self.on_config("protection", Config.get("protection"))

    def on_destroy(self):
        Config.remove_listener(self)

    def on_config(self, key, value):
        if key == "protection":
            print(" -- protection --", value)
            if value != self.protection:
                self.protection = value
                if not value:
                    self.icon = self.protection_icon
                    self.active = False
                    self.text = ""
                elif value.lower() == "none":
                    self.icon = self.disabled_icon
                    self.active = True
                    self.text = gettext("No Protection")
                elif value.lower() in ["dongle"]:
                    self.icon = self.disabled_icon
                    self.active = True
                    self.text = gettext("Dongle")
                else:
                    self.icon = self.protection_icon
                    self.active = True
                    self.text = value
                self.refresh()
