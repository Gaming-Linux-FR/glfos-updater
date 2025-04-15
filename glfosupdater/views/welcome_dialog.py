from glfosupdater.constants import rootdir, pkgdatadir
from gi.repository import Gtk, Adw

@Gtk.Template(resource_path = rootdir + '/welcome_dialog_welcome.ui')
class WelcomeDialogWelcome(Gtk.Box):
    __gtype_name__ = "WelcomeDialogWelcome"

    logo_image = Gtk.Template.Child('logo')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.logo_image.set_filename(pkgdatadir + '/logo.png')

@Gtk.Template(resource_path = rootdir + '/welcome_dialog_stable.ui')
class WelcomeDialogStable(Gtk.Box):
    __gtype_name__ = "WelcomeDialogStable"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

@Gtk.Template(resource_path = rootdir + '/welcome_dialog_rolling.ui')
class WelcomeDialogRolling(Gtk.Box):
    __gtype_name__ = "WelcomeDialogRolling"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

@Gtk.Template(resource_path = rootdir + '/welcome_dialog_start.ui')
class WelcomeDialogStart(Gtk.Box):
    __gtype_name__ = "WelcomeDialogStart"

    def __init__(self, dialog, **kwargs):
        super().__init__(**kwargs)
        self.dialog = dialog

    @Gtk.Template.Callback()
    def start(self, target):
        self.dialog.close()

    
@Gtk.Template(resource_path = rootdir +'/welcome_dialog.ui')
class WelcomeDialog(Adw.Dialog):
    __gtype_name__ = "WelcomeDialog"

    carousel = Gtk.Template.Child('content')
    index = 0

    prev_btn = Gtk.Template.Child('prev-btn')
    next_btn = Gtk.Template.Child('next-btn')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.carousel_pages = [WelcomeDialogWelcome(), WelcomeDialogStable(), WelcomeDialogRolling(), WelcomeDialogStart(self)]

        for page in self.carousel_pages:
            self.carousel.append(page)

    @Gtk.Template.Callback()
    def prev_page(self, target):
        self.carousel.scroll_to(self.carousel_pages[self.index - 1], True)

    @Gtk.Template.Callback()
    def next_page(self, target):
        self.carousel.scroll_to(self.carousel_pages[self.index + 1], True)

    @Gtk.Template.Callback()
    def page_changed(self, carousel, index):
        self.index = index

        if self.index == len(self.carousel_pages) - 1:
            self.next_btn.set_sensitive(False)
        else:
            self.next_btn.set_sensitive(True)

        if self.index == 0:
            self.prev_btn.set_sensitive(False)
        else:
            self.prev_btn.set_sensitive(True)
