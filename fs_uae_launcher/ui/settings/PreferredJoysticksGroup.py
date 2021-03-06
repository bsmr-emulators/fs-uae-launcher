import fsui as fsui
from ...DeviceManager import DeviceManager
from ...I18N import gettext
from ...Settings import Settings


joystick_mode_values = ["nothing", "mouse", "joystick"]
joystick_values = ["none", "mouse", "keyboard"]


# def get_joystick_mode_titles():
#     return [gettext("Nothing"), gettext("Mouse"), gettext("Joystick")]


class PreferredJoysticksGroup(fsui.Group):

    def __init__(self, parent):
        fsui.Group.__init__(self, parent)
        self.layout = fsui.HorizontalLayout()
        # self.layout.padding_left = 10
        # self.layout.padding_right = 10

        # image = fsui.Image("fs_uae_launcher:res/joystick.png")
        # self.image_view = fsui.ImageView(self, image)
        # self.layout.add(self.image_view, valign=0.0)

        # self.layout.add_spacer(20)

        self.layout2 = fsui.VerticalLayout()
        self.layout.add(self.layout2, fill=True, expand=True)

        heading = gettext("Preferred Joysticks")
        label = fsui.HeadingLabel(self, heading)
        self.layout2.add(label)

        self.layout2.add_spacer(20)
        label = fsui.Label(self, gettext("The following joystick will be "
                                         "preferred, if present:"))
        self.layout2.add(label)

        self.layout2.add_spacer(6)
        selector = PreferredJoystickSelector(self, 0)
        self.layout2.add(selector, fill=True)

        self.layout2.add_spacer(20)
        label = fsui.Label(
            self, gettext("Preferred device for secondary joystick:"))
        self.layout2.add(label)

        self.layout2.add_spacer(6)
        selector = PreferredJoystickSelector(self, 1)
        self.layout2.add(selector, fill=True)


class PreferredJoystickSelector(fsui.Group):

    def __init__(self, parent, index):
        self.index = index
        if index:
            self.key = "secondary_joystick"
        else:
            self.key = "primary_joystick"

        fsui.Group.__init__(self, parent)
        self.layout = fsui.HorizontalLayout()

        devices = ["", get_keyboard_title()]
        # for i, name in enumerate(DeviceManager.get_joystick_names()):
        #     devices.append(name)
        for device_name in DeviceManager.get_joystick_names():
            if DeviceManager.is_joystick(device_name):
                devices.append(device_name)

        self.device_choice = fsui.ComboBox(self, devices)

        self.layout.add(self.device_choice, expand=True)

        # Config.add_listener(self)

        self.initialize_from_settings()
        self.set_settings_handlers()

    def initialize_from_settings(self):
        self.on_setting(self.key, Settings.get(self.key))

    def set_settings_handlers(self):
        self.device_choice.on_change = self.on_device_change
        Settings.add_listener(self)

    def on_destroy(self):
        Settings.remove_listener(self)

    def on_device_change(self):
        value = self.device_choice.get_text()
        print("on_device_change", value)
        if value == get_keyboard_title():
            value = "keyboard"
        Settings.set(self.key, value)

    def on_setting(self, key, value):
        if key == self.key:
            if value == "keyboard":
                value = get_keyboard_title()
            self.device_choice.set_text(value)


def get_keyboard_title():
    return gettext("Cursor Keys and Right Ctrl/Alt")
