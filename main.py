from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from menu_screen import MenuScreen
from mostrar_contactos import ListaContactosScreen
from Agregar_contactos import AgregarContactoScreen
from eliminar_contactos import EliminarContactoScreen
from modificar_contactos import ModificarContactoScreen
from contactos_manager import agregar_contacto
from contactos_manager import buscar_contacto_por_nombre, actualizar_contacto


class ContactosApp(MDApp):
    def build(self):
        sm = MDScreenManager()

        # Añadir las pantallas a la principal.
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(ListaContactosScreen(name="mostrar_contactos"))
        sm.add_widget(AgregarContactoScreen(name="Agregar_contacto"))
        sm.add_widget(EliminarContactoScreen(name="eliminar_contacto"))
        sm.add_widget(ModificarContactoScreen(name="modificar_contacto"))
        return sm

    #Agregar contactos a la base de datos.
    def Agregar_contacto(self, nombre, telefono, correo):
        agregar_contacto(nombre, telefono, correo)
        print("Contacto guardado exitosamente.")
    
    # Buscar contacto por nombre.
    def buscar_contacto(self, nombre):
        return buscar_contacto_por_nombre(nombre)

    #Actualizar contacto.
    def actualizar_contacto(self, nombre_original, nuevo_nombre, telefono, correo):
        return actualizar_contacto(nombre_original, nuevo_nombre, telefono, correo)
            
if __name__ == "__main__":
    ContactosApp().run()


