from glfosupdater.constants import rootdir, pkgdatadir
from gi.repository import Gtk, Adw

from glfosupdater.views import welcome_dialog

import os

@Gtk.Template(resource_path = rootdir +'/window.ui')
class MainWindow(Adw.ApplicationWindow):
    __gtype_name__ = "MainWindow"

    rebuild_banner = Gtk.Template.Child('rebuild-banner')
    rebuild_error_banner = Gtk.Template.Child('rebuild-error-banner')
    rebuild_done_banner = Gtk.Template.Child('rebuild-done-banner')

    logo_image = Gtk.Template.Child('logo')
    update_btn = Gtk.Template.Child('update-btn')
    branches_dropdown = Gtk.Template.Child('branches')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.app = Adw.Application.get_default()
        self.set_icon_name('glfos-updater')

        self.logo_image.set_filename(pkgdatadir + '/logo.png')

        branches = Gtk.StringList()
        self.branches_dropdown.props.model = branches

        branches.append(_("stable (recommended)"))
        branches.append(_("rolling (for the cutting-edge enjoyers)"))

        welcome_dialog.WelcomeDialog().present(self)

    @Gtk.Template.Callback()
    def on_update(self, target):
        self.app.update(self.branches_dropdown.get_selected_item().get_string().split(' ')[0])

    @Gtk.Template.Callback()
    def reboot(self, target):
        os.system('reboot')
