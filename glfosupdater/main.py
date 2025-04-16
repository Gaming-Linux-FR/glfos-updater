import sys, subprocess, requests
from gi.repository import GLib, Adw, Gio

from concurrent.futures import ThreadPoolExecutor as Pool

from glfosupdater.views.main_window import MainWindow

class App(Adw.Application):
    def __init__(self):
        super().__init__(application_id="org.glfos.updater")
        GLib.set_application_name('GLF-OS Updater')
        GLib.set_prgname('glfos-updater')

        self.nix_rebuild_cmd = 'nixos-rebuild switch'
        self.flake_file = '/etc/nixos/flake.nix'

    def do_activate(self):
        self.window = MainWindow(application=self)
        self.window.present()

    def rebuild_finished(self, future):
        res = future.result()
        self.window.rebuild_banner.set_revealed(False)

        if res == 0:
            self.window.rebuild_done_banner.set_revealed(True)
        else:
            self.window.rebuild_error_banner.set_revealed(True)

    def update(self, branch):
        req = requests.get(f'https://raw.githubusercontent.com/Gaming-Linux-FR/GLF-OS/refs/heads/{branch}/iso-cfg/flake.nix')

        if req.status_code != 200:
            self.window.rebuild_error_banner.set_revealed(True)
            return
        
        with open(self.flake_file, 'wb') as f:
            f.write(req.content)

        self.window.rebuild_banner.set_revealed(True)
        self.window.rebuild_done_banner.set_revealed(False)
        self.window.rebuild_error_banner.set_revealed(False)

        self.window.update_btn.set_sensitive(False)

        pool = Pool(max_workers=1)
        cmd_call = pool.submit(subprocess.call, self.nix_rebuild_cmd, shell = True)
        cmd_call.add_done_callback(self.rebuild_finished)

def main():
    app = App()
    exit_status = app.run(sys.argv)
    return exit_status
