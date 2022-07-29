input_url_helper="""
MDTextField:
     pos_hint: {'center_x':0.5,'center_y':0.5}   
     size_hint_x:None 
     width:150
     theme_text_color:'Custom'
     text_color: (41/255.0, 41/255.0, 41/255.0, 1)
     
"""
youtube_icon_btn_helper="""
MDIconButton:
    icon:'youtube'
    pos_hint:{'center_x':0.15 , 'center_y':0.5}
    user_font_size:"32sp"
    theme_text_color:'Custom'
    text_color:(196/255.0, 48/255.0, 43/255.0, 1)
    on_release: app.open_youtube()
"""
send_flat_btn_helper = """
MDRectangleFlatButton:
    text:'Send'
    pos_hint:{'center_x' : 0.5,'center_y':0.3}
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
    text:'temp' 
    pos_hint:{'center_x':0.75,'center_y':.725}
    theme_text_color:'Custom'
    text_color:(125/255.0, 125/255.0, 125/255.0, 1)
    font_style:'Caption'
"""

cafe_list_dropdown_helper = '''
<IconListItem>

    IconLeftWidget:
        icon: root.icon
MDScreen

    MDDropDownItem:
        id: drop_item
        pos_hint: {'center_x': .5, 'center_y': .8}
        text: 'Connect to Wi-Fi in the cafe'
        on_release: app.menu.open()
'''