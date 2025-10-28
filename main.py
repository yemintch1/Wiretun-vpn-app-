from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
import threading
import time

class WireTunVPN(App):
    def __init__(self):
        super().__init__()
        self.is_connected = False
        self.data_used = 0
        
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        title = Label(text="WireTun VPN", font_size='24sp', size_hint_y=0.15)
        main_layout.add_widget(title)
        
        self.status = Label(text="🔴 DISCONNECTED", font_size='18sp', size_hint_y=0.15)
        main_layout.add_widget(self.status)
        
        self.progress = ProgressBar(max=100, size_hint_y=0.1)
        main_layout.add_widget(self.progress)
        
        self.connect_btn = Button(text="CONNECT VPN", background_color=(0.2, 0.7, 0.3, 1), 
                                 size_hint_y=0.2, font_size='18sp')
        self.connect_btn.bind(on_press=self.toggle_connection)
        main_layout.add_widget(self.connect_btn)
        
        self.stats_label = Label(text="Data: 0 MB\nSpeed: 0 Mbps", 
                               size_hint_y=0.2, font_size='14sp')
        main_layout.add_widget(self.stats_label)
        
        sites_label = Label(text="Free VPN for Social Media\n• Facebook\n• WhatsApp\n• Twitter\n• Instagram", 
                          size_hint_y=0.2, font_size='14sp')
        main_layout.add_widget(sites_label)
        
        return main_layout
    
    def toggle_connection(self, instance):
        if not self.is_connected:
            self.connect_vpn()
        else:
            self.disconnect_vpn()
    
    def connect_vpn(self):
        self.is_connected = True
        self.connect_btn.text = "DISCONNECT VPN"
        self.connect_btn.background_color = (0.9, 0.2, 0.2, 1)
        self.status.text = "
