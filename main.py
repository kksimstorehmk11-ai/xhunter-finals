from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import subprocess
import threading

class XHunterUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.add_widget(Label(text="[X-HUNTER MYANMAR]", font_size='22sp', color=(0, 1, 0, 1), size_hint_y=0.1))
        self.console = TextInput(text="[+] SYSTEM READY...\n", readonly=True, background_color=(0,0,0,1), foreground_color=(0,1,0,1), size_hint_y=0.7)
        self.add_widget(self.console)
        btn_grid = BoxLayout(size_hint_y=0.2, spacing=10)
        scan_btn = Button(text="WIFI SCAN", background_color=(0, 0.4, 0, 1))
        scan_btn.bind(on_release=self.wifi_scan)
        btn_grid.add_widget(scan_btn)
        self.add_widget(btn_grid)

    def wifi_scan(self, instance):
        self.console.text += "[!] SCANNING...\n"
        threading.Thread(target=self.run_cmd, args=("cat /proc/net/arp",)).start()

    def run_cmd(self, cmd):
        res = subprocess.getoutput(cmd)
        Clock.schedule_once(lambda dt: self.set_text(res))

    def set_text(self, res):
        self.console.text += res + "\n"

class MainApp(App):
    def build(self): return XHunterUI()

if __name__ == "__main__":
    MainApp().run()
