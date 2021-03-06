from fsbc.desktop import open_url_in_browser
from fs_uae_launcher.ui.download import DownloadGameWindow
from fs_uae_workspace.shell import shell_open
from fsbc.util import unused
from fsgs.context import fsgs
import fsui as fsui
from fsgs.amiga.Amiga import Amiga
from ..I18N import gettext
from ..Settings import Settings
from ..Config import Config
from ..Signal import Signal
from .SetupDialog import SetupDialog
from .Skin import Skin
from .TabPanel import TabPanel

# if Skin.use_unified_toolbar():
#     base_class = fsui.Control
# else:
#    base_class = fsui.Panel


class InfoPanel(fsui.Panel):

    def __init__(
            self, parent, toolbar_mode=False, padding_top=0, padding_bottom=0):
        fsui.Panel.__init__(self, parent, paintable=True)
        Skin.set_background_color(self)
        self.update_web_url = ""
        self.update_version = ""
        self.toolbar_mode = toolbar_mode
        self.padding_top = padding_top
        self.padding_bottom = padding_bottom

        self.chip_memory_warning = ["", ""]
        self.kickstarts_missing = ["", ""]
        self.update_available = ["", ""]
        self.config_error = ["", ""]
        self.missing_files = ["", ""]
        self.download_page = ["", ""]
        self.download_file = ["", ""]
        # self.downloadable = ["", ""]

        self.update_available_icon = fsui.Image(
            "fs_uae_launcher:res/update_available_32.png")
        self.warning_icon = fsui.Image(
            "fs_uae_launcher:res/warning_32.png")
        self.download_icon = fsui.Image(
            "fs_uae_launcher:res/download_32.png")
        self.kickstarts_missing_icon = self.warning_icon

        self.check_kickstarts()
        # Config.add_listener(self)
        # Settings.add_listener(self)
        Signal.add_listener("update_available", self)
        Signal.add_listener("scan_done", self)
        # Signal.add_listener("locker-updated", self)

        Config.add_listener(self)
        Settings.add_listener(self)
        
        for key in ["x_missing_files", "download_page", "download_file"]:
            self.on_config(key, Config.get(key))

    def on_destroy(self):
        # Config.remove_listener(self)
        # Settings.remove_listener(self)
        Settings.remove_listener(self)
        Config.remove_listener(self)
        Signal.remove_listener("scan_done", self)
        Signal.remove_listener("update_available", self)

#    def on_config(self, key, value):
#        pass
#
#    def on_setting(self, key, value):
#        pass

    def on_setting(self, key, value):
        unused(value)
        if key in ["database_auth", "database_username", "database_email"]:
            self.refresh()

    def on_config(self, key, value):
        print("InfoPanel.on_config", key, value)
        if key in ["amiga_model", "chip_memory"]:
            amiga_model = Config.get("amiga_model")
            try:
                chip_memory = int(Config.get("chip_memory"))
            except:
                chip_memory = ""
            print(chip_memory, amiga_model)
            if chip_memory and chip_memory < 2048 and \
                    amiga_model in ["A1200", "A1200/020", "A4000/040"]:
                new_chip_memory_warning = [
                    gettext("Configuration Warning"),
                    gettext("{amiga_model} with < 2 MB chip memory"
                            "").format(amiga_model=amiga_model)]
            else:
                new_chip_memory_warning = None
            if new_chip_memory_warning != self.chip_memory_warning:
                self.chip_memory_warning = new_chip_memory_warning
                self.refresh()
        elif key == "__error":
            if value:
                self.config_error = value.split("\n", 1)
                if len(self.config_error) == 1:
                    self.config_error.append("")
            else:
                self.config_error = ["", ""]
            self.refresh()
        elif key == "x_missing_files":
            self.missing_files = value
            self.refresh()
        elif key == "download_page":
            self.download_page = value
            self.refresh()
        elif key == "download_file":
            self.download_file = value
            self.refresh()

    def on_scan_done_signal(self):
        print("InfoPanel.on_scan_done_signal")
        self.check_kickstarts()

    def check_kickstarts(self):
        # FIXME: instead of this check, check if x_kickstart_sha1 is set
        # properly when amiga_model / x_kickstart_sha1 changes, so you''
        # only get a warning for the Amiga model in question.
        ok = True

        amiga = Amiga.get_model_config("A500")
        for sha1 in amiga["kickstarts"]:
            if fsgs.file.find_by_sha1(sha1):
                ok = False
                break
        self.kickstarts_missing = ok
        # self.kickstarts_missing = True
        self.refresh()

    def on_update_available_signal(self, version, web_url):
        self.update_available = True
        self.update_version = version
        self.update_web_url = web_url
        self.refresh()

    def on_left_up(self):
        if self.missing_files:
            if self.download_page and not self.download_file:
                # open_url_in_browser(self.download_page)
                # self.window = DownloadGameWindow(self.get_window(),
                #                                  fsgs)
                # self.window.show()
                DownloadGameWindow(self.get_window(), fsgs).show()
        elif self.kickstarts_missing:
            SetupDialog(self.get_window()).show()
        elif self.update_available:
            open_url_in_browser(self.update_web_url)
        else:
            auth = Settings.get("database_auth")
            if not auth:
                shell_open("Workspace:Prefs/User/Login",
                           parent=self.get_window())

    def on_paint(self):
        dc = self.create_dc()
        if not self.toolbar_mode:
            TabPanel.draw_background(self, dc)

        # print(self.missing_files, "file", self.download_file,
        #       "page", self.download_page)
        if is_warning(self.missing_files) and not self.download_file:
            if self.download_page:
                self.draw_notification(
                    dc, self.download_icon,
                    gettext("This game must be downloaded"),
                    gettext("Click here to download"))
            else:
                self.draw_notification(
                    dc, self.warning_icon,
                    gettext("Some required files are missing"),
                    gettext("The game may not start properly"))
        elif is_warning(self.config_error):
            self.draw_notification(
                dc, self.warning_icon, *self.config_error)
        elif is_warning(self.chip_memory_warning):
            self.draw_notification(
                dc, self.warning_icon, *self.chip_memory_warning)
        elif is_warning(self.kickstarts_missing):
            self.draw_kickstarts_missing_notification(dc)
        elif is_warning(self.update_available):
            self.draw_update_available_notification(dc)
        else:
            self.draw_user_notification(dc)

    def draw_user_notification(self, dc):
        username = Settings.get("database_username")
        # email = Settings.get("database_email")
        auth = Settings.get("database_auth")
        if auth:
            self.draw_notification(dc, None, gettext("Logged In"), username)
        else:
            self.draw_notification(dc, None, gettext("Not logged in"),
                                   gettext("Log in to enable online game DB"))

    def draw_update_available_notification(self, dc):
        self.draw_notification(
            dc, self.update_available_icon,
            gettext("Update available ({version})").format(
                version=self.update_version),
            gettext("Click here to download"))

    def draw_kickstarts_missing_notification(self, dc):
        self.draw_notification(
            dc, self.kickstarts_missing_icon,
            gettext("Kickstart ROMs are missing"),
            gettext("Click here to import kickstarts"))

    def draw_notification(self, dc, icon, text1, text2):
        available_height = self.size[1]
        available_height -= self.padding_top + self.padding_bottom

        if icon is not None:
            y = self.padding_top + (available_height - icon.size[1]) // 2
        else:
            y = 0

        # if Skin.use_unified_toolbar():
        #     rtl = False
        # else:
        #     rtl = True
        rtl = False

        if rtl:
            right_x = self.size[0]
            if icon is not None:
                icon_x = right_x - icon.size[0] - 10
                dc.draw_image(icon, icon_x, y)
                right_x = icon_x - 20
            font = dc.get_font()
            font.set_bold(True)
            dc.set_font(font)
            tw, th = dc.measure_text(text1)
            lines_height = th * 2
            y = self.padding_top + (available_height - lines_height) // 2
            dc.draw_text(text1, right_x - tw, y)
            y += th
            font.set_bold(False)
            dc.set_font(font)
            tw, th = dc.measure_text(text2)
            dc.draw_text(text2, right_x - tw, y)
        else:
            if icon is not None:
                dc.draw_image(icon, 0, y)
                x = 50
            else:
                x = 0
            font = dc.get_font()
            font.set_bold(True)
            dc.set_font(font)
            tw, th = dc.measure_text(text1)
            lines_height = th * 2
            y = self.padding_top + (available_height - lines_height) // 2
            # dc.draw_text(text1, right_x - tw, y)
            dc.draw_text(text1, x, y)
            y += th
            font.set_bold(False)
            dc.set_font(font)
            # tw, th = dc.measure_text(text2)
            # dc.draw_text(text, right_x - tw, y)
            dc.draw_text(text2, x, y)


def is_warning(w):
    if w is None:
        return False
    if isinstance(w, str):
        return bool(w)
    if isinstance(w, bool):
        return w
    return w[0] or w[1]
