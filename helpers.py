input_url_helper="""
MDTextField:
     pos_hint: {'center_x':0.55,'center_y':0.4}   
     size_hint_x:None 
     width:dp(190)
     theme_text_color:'Custom'
     text_color: (41/255.0, 41/255.0, 41/255.0, 1)
     #icon_left: 'youtube'
     
"""
youtube_icon_btn_helper="""
MDIconButton:
    icon:'youtube'
    pos_hint:{'center_x':0.15 , 'center_y':0.4}
    user_font_size:dp(28)
    theme_text_color:'Custom'
    text_color:(196/255.0, 48/255.0, 43/255.0, 1)
    on_release: app.open_youtube()
"""
soundcloud_icon_btn_helper="""
MDIconButton:
    icon:'soundcloud'
    pos_hint:{'center_x':0.15 , 'center_y':0.3}
    user_font_size:dp(28)
    theme_text_color:'Custom'
    text_color:(240/255.0, 89/255.0, 34/255.0, 1)
    on_release: app.open_youtube()
"""

send_flat_btn_helper = """
MDRectangleFlatButton:
    text:'Send'
    pos_hint:{'center_x' : 0.5,'center_y':0.2}
    font_size:"14sp"
    #increment_width: "16dp"
    on_release: app.send_url()
"""
contact_label_helper = """
MDLabel:
    text:'Contact: sngmng@naver.com' 
    pos_hint:{'center_x':0.9,'center_y':.015}
    theme_text_color:'Custom'
    text_color:(125/255.0, 125/255.0, 125/255.0, 1)
    font_style:'Caption'
"""
connect_label_helper = """
MDLabel:
    text:'Now playing...' 
    pos_hint:{'center_x':0.55,'center_y':.78}
    theme_text_color:'Custom'
    text_color:(125/255.0, 125/255.0, 125/255.0, 1)
    font_style:'Caption'
"""

cafe_list_dropdown_helper = '''

MDScreen:
        
    MDDropDownItem:
        id: drop_item
        pos_hint: {'center_x': .5, 'center_y': .9}
        text: 'Connect to Wi-Fi'
        on_release: app.menu.open()
'''

Fab_helper = """
MDScreen:
    MDFloatingActionButtonSpeedDial:
        callback:app.callback
        data: app.data
        root_button_anim: True
        hint_animation : False
"""
Thumbnail_helper = '''
MDScreen:

    MDSmartTile:
        radius: 24
        box_radius: [0, 0, 24, 24]
        box_color: 1, 1, 1, 0
        overlap:False
        source: "test.jpg"
        pos_hint: {"center_x": .5, "center_y": .6}
        size_hint: None, None
        size: "240dp", "180dp"


        MDIconButton:
            icon: "heart-outline"
            theme_icon_color: "Custom"
            icon_color: 1, 0, 0, 1
            pos_hint: {"center_y": .5}
            on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

        MDLabel:
            text: "test and heart"
            bold: True
            color: 0,0,0,1
'''
