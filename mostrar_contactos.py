from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDList
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.toolbar import MDTopAppBar
from kivy.metrics import dp
from contactos_manager import eliminar_contactos, cargar_contactos


class ListaContactosScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.dialog = None  
        self.create_ui()

    #Actualizar la lista de contactos al entrar a la pantalla.
    def on_pre_enter(self):
        self.actualizar_lista()

    #Interfaz de usuario de la pantalla, mostrar contactos.
    def create_ui(self):
        layout = MDBoxLayout(orientation="vertical", padding=dp(20), spacing=dp(10))
        
        toolbar = MDTopAppBar(title="Lista de Contactos")
        layout.add_widget(toolbar)
        
        self.container = MDBoxLayout(orientation="vertical", size_hint_y=None)
        self.container.bind(minimum_height=self.container.setter("height"))
        
        scroll = MDScrollView()
        scroll.add_widget(self.container)
        layout.add_widget(scroll)
        
        btn_volver = MDRaisedButton(
            text="Volver", pos_hint={"center_x": 0.5}, on_release=self.volver_menu
        )
        layout.add_widget(btn_volver)
        
        self.add_widget(layout)
        self.actualizar_lista()

    #Actualizar la lista de contactos en la base de datos.
    def actualizar_lista(self):
        self.container.clear_widgets()
        contactos = cargar_contactos()
        if not contactos:
            mensaje = MDLabel(text="No hay contactos registrados", halign="center", theme_text_color="Secondary")
            self.container.add_widget(mensaje)
        else:
            for contacto in contactos:
                self.container.add_widget(self.crear_tarjeta_contacto(contacto))

    #Forma en que se muestran los contactos registrados.
    def crear_tarjeta_contacto(self, contacto):
        tarjeta = MDCard(orientation="vertical", padding=dp(10), size_hint_x=0.95, pos_hint={"center_x": 0.5}, size_hint_y=None, height=dp(120))
    
        layout = MDBoxLayout(orientation="vertical", spacing=dp(5))
        layout.add_widget(MDLabel(text=f"Nombre: {contacto['nombre']}", theme_text_color="Primary"))
        layout.add_widget(MDLabel(text=f"Teléfono: {contacto['telefono']}", theme_text_color="Secondary"))
        layout.add_widget(MDLabel(text=f"Correo: {contacto['correo']}", theme_text_color="Secondary"))
    
        botones = MDBoxLayout(orientation="horizontal", size_hint_y=None, height=dp(40), spacing=dp(10))
    
        btn_eliminar = MDIconButton(icon="delete", on_release=lambda x: self.confirmar_eliminar(contacto['nombre']))
        btn_modificar = MDIconButton(
            icon="pencil",
            on_release=lambda x: self.modificar_contacto(contacto)
        )
    
        botones.add_widget(btn_eliminar)
        botones.add_widget(btn_modificar)
    
        layout.add_widget(botones)
        tarjeta.add_widget(layout)
    
        return tarjeta  

    #Confirmacion de eliminacion.
    def confirmar_eliminar(self, nombre_contacto):
        self.dialog = MDDialog(
            title="Eliminar Contacto",
            text=f"¿Estás seguro de que quieres eliminar a {nombre_contacto}?",
            buttons=[
                MDRaisedButton(text="Cancelar", on_release=lambda x: self.dialog.dismiss()),
                MDRaisedButton(text="Eliminar", on_release=lambda x: self.eliminar_contacto(nombre_contacto))
            ],
        )
        self.dialog.open()

    #Eliminar el contacto de la base de datos.
    def eliminar_contacto(self, nombre_contacto):
        eliminar_contactos(nombre_contacto)
        self.dialog.dismiss()
        self.actualizar_lista()

    #Accion de modificar contactos, redirige a la pantalla modificar contacto.
    def modificar_contacto(self, contacto):
        self.manager.get_screen("modificar_contacto").cargar_datos(contacto)
        self.manager.current = "modificar_contacto"

    def volver_menu(self, instance):
        self.manager.current = "menu"
