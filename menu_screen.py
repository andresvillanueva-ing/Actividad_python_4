from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

#Archivo KV, estilo de la pantalla, se muestran cada uno de los botones de accion. 
KV = '''
MDScreen:
    MDLabel:
        text: "Gestión de Contactos"
        halign: "center"
        pos_hint: {"center_y": 0.8}

    MDRaisedButton:
        text: "Mostrar Contactos"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        on_press: app.root.current = "mostrar_contactos"

    MDRaisedButton:
        text: "Agregar Contacto"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_press: app.root.current = "Agregar_contacto"

    MDRaisedButton:
        text: "Modificar Contacto"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        on_press: app.root.current = "modificar_contacto"

    MDRaisedButton:
        text: "Eliminar Contacto"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        on_press: app.root.current = "eliminar_contacto"
'''

class MenuScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Builder.load_string(KV))