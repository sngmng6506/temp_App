from kivymd.app import MDApp  #0.104.2
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.button import MDRectangleFlatButton,MDIconButton,MDFloatingActionButtonSpeedDial
from kivymd.uix.textfield import MDTextField
from kivymd.uix.menu import MDDropdownMenu
from kivy.lang import Builder
from helpers import *
from kivy.metrics import dp
from client_socket import *
import webbrowser
from kivy.properties import OptionProperty,NumericProperty
from kivy.core.window import Window # << 모바일은 화면비율 자동으로 바뀌나?
from kivymd.uix.templates import ScaleWidget
from kivymd.toast import toast
import time
import threading
from queue import Queue
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog



class JukeApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ## cafe_list_dropdownMenu
        self.cafe_list = Builder.load_string(cafe_list_dropdown_helper)
        self.Registered_WiFi = {'ediya': '172.30.1.34', 'home': '172.30.1.25'}
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": i,
                "height": dp(56),
                "on_release": lambda x= i : self.set_item(x),
            } for i in self.Registered_WiFi.keys()
        ]
        self.menu = MDDropdownMenu(
            caller=self.cafe_list.ids.drop_item,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )
        self.menu.bind()

        #FAB
        self.data = {
            "a": 'heart',
            'b': 'help',
        }
        ## WiFi 상태에 따른 메뉴창 선택됨
        init_IP = socket.gethostbyname(socket.gethostname())
        for key,value in self.Registered_WiFi.items():
            if init_IP == value:
                print("now u r in " + key)
                self.set_item(key)

        ## help - dialog
        self.dialog = None

    def set_item(self, text_item):
        self.cafe_list.ids.drop_item.set_item(text_item)
        self.menu.dismiss()

    def send_url(self):
        print(self.input_url.text)
        self.input_url.text=""

    def open_youtube(self):
        webbrowser.open("https://www.youtube.com/")

    def build(self):
        Window.size = [720/2.5, 1600/2.5]
        self.theme_cls.primary_palette="DeepPurple"
        self.theme_cls.primary_hue = "300"
        #self.theme_cls.theme_style = "Dark"  # 옵션가서 설정가능하게하면좋을듯 / Light or Dark

        ##### Builders
        self.input_url = Builder.load_string(input_url_helper)
        send_flat_btn = Builder.load_string(send_flat_btn_helper)
        youtube_icon_btn = Builder.load_string(youtube_icon_btn_helper)
        #contact_label = Builder.load_string((contact_label_helper))
        connect_label = Builder.load_string((connect_label_helper))
        fab = Builder.load_string(Fab_helper)
        thumbnail = Builder.load_string(Thumbnail_helper)
        #soundcloud_icon_btn=Builder.load_string(soundcloud_icon_btn_helper)
        #Builder.load_file('main.kv')

        ##### add_widget
        self.screen = Screen()
        #self.screen.add_widget(contact_label)
        self.screen.add_widget(youtube_icon_btn)
        self.screen.add_widget(send_flat_btn)
        self.screen.add_widget(self.input_url)
        self.screen.add_widget(self.cafe_list)
        self.screen.add_widget(connect_label)
        self.screen.add_widget(fab)
        self.screen.add_widget(thumbnail)
        #self.screen.add_widget(soundcloud_icon_btn)

        #thread
        self.temp = False

        thread = self.go(self.func)
        thread.start()

        return self.screen

    def callback(self,instance):
        if instance.icon == 'help':
            self.show_alert_dialog()
        if instance.icon == 'heart':
            pass

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
        text="1.매장 와이파이 연결 \n"
             "2.유튜브 URL 입력 \n"
             "3.SEND \n"
             "\n"
             "contact) sngmng@naver.com",
        radius=[20, 7, 20, 7],
        )
        self.dialog.open()

    def go(self,target):
        thread = threading.Thread(target=target)
        return thread

    def func(self): ##네트워크변경감지를위한 스레딩
        #Registered_WiFi = {'ediya': '172.30.1.34', 'home': '172.30.1.25'}  ## << 카페,와이파이 추가되면 여기 변경
        init_IP = socket.gethostbyname(socket.gethostname())

        #네트워크변경계속감지 : IP변경안되면 pass 변경되면 다시목록탐색 -> 반복
        while self.run:

            time.sleep(1)
            print("네트워크변경감지중")
            current_IP = socket.gethostbyname(socket.gethostname())
            if init_IP == current_IP:


                print("네트워크동일")
                pass
            else:
                print("네트워크변경!")
                init_IP = current_IP
                for key, value in self.Registered_WiFi.items():
                    if init_IP == value:
                        print("u r in " + key)
                        self.set_item(key)

                    else: #toast : you got the wrong WiFi
                        #self.temp = not self.temp
                        pass





def Appstart():
    JukeApp().run()

if __name__ == '__main__':
    Appstart()



