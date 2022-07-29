from kivymd.app import MDApp  #0.104.2
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.button import MDRectangleFlatButton,MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.menu import MDDropdownMenu
from kivy.lang import Builder
from helpers import *
from kivy.metrics import dp
from client_socket import *
import webbrowser

from kivy.core.window import Window # << 모바일은 화면비율 자동으로 바뀌나?



class JukeApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ## cafe_list_dropdownMenu
        self.cafe_list = Builder.load_string(cafe_list_dropdown_helper)
        Registered_WiFi = {'ediya': '172.30.1.11', 'home': '172.30.1.5'}  ## << 카페,와이파이 추가되면 여기만 변경
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": i,
                "height": dp(56),
                "on_release": lambda x= i : self.set_item(x),
            } for i in Registered_WiFi.keys()
        ]
        self.menu = MDDropdownMenu(
            caller=self.cafe_list.ids.drop_item,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )
        self.menu.bind()
        
        ## WiFi 상태에 따른 메뉴창 선택됨
        for key,value in Registered_WiFi.items():
            if socket.gethostbyname(socket.gethostname()) == value:
                print("now u r in " + key)
                self.set_item(key)



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
        self.theme_cls.primary_hue = "600"
        #self.theme_cls.theme_style = "Dark"  # 옵션가서 설정가능하게하면좋을듯 / Light or Dark

        ##### Builders
        self.input_url = Builder.load_string(input_url_helper)
        send_flat_btn = Builder.load_string(send_flat_btn_helper)
        youtube_icon_btn = Builder.load_string(youtube_icon_btn_helper)
        contact_label = Builder.load_string((contact_label_helper))
        connect_label = Builder.load_string((connect_label_helper))

        ##### add_widget
        self.screen = Screen()
        self.screen.add_widget(contact_label)
        self.screen.add_widget(youtube_icon_btn)
        self.screen.add_widget(send_flat_btn)
        self.screen.add_widget(self.input_url)
        self.screen.add_widget(self.cafe_list)
        self.screen.add_widget((connect_label))
        return self.screen





if __name__ == '__main__':
    JukeApp().run()




