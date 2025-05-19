import csv
import os

archivo = "contactos.csv"

def cargar_contactos():
    contactos = []
    if os.path.exists(archivo):
        with open(archivo, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            contactos = list(reader)
    return contactos

def guardar_contactos(contactos):
    with open(archivo, mode='w', encoding='utf-8') as file:
        campos = ['nombre', 'telefono', 'correo']
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()
        writer.writerows(contactos)

def agregar_contacto(nombre, telefono, correo):
    contactos = cargar_contactos()
    contactos.append({"nombre": nombre, "telefono": telefono, "correo": correo})
    guardar_contactos(contactos)

def listar_contactos():
    contactos = cargar_contactos()
    if not contactos:
        print("No hay contactos registrados.")
    else:
        for contacto in contactos:
            print(f"Nombre: {contacto['nombre']}, Telefono: {contacto['telefono']}, Correo: {contacto['correo']}")

def editar_contactos(nombre, telefono, correo):
    contactos = cargar_contactos()
    for contacto in contactos:
        if contacto['nombre'].lower() == nombre.lower():
            contacto['telefono'] = telefono
            contacto['correo'] = correo
            guardar_contactos(contactos)
            return
    print("Contacto no encontrado.")

def eliminar_contactos(nombre):
    contactos = cargar_contactos()
    nuevos_contactos = [contacto for contacto in contactos if contacto['nombre'].lower() != nombre.lower()]
    if len(nuevos_contactos) == len(contactos):
        print("Contacto no encontrado.")
    else:
        guardar_contactos(nuevos_contactos)
        print("Contacto eliminado.")


def buscar_contacto_por_nombre(nombre):
    contactos = cargar_contactos()
    for contacto in contactos:
        if contacto["nombre"].lower() == nombre.lower():
            return contacto
    return None

def actualizar_contacto(nombre_original, nuevo_nombre, nuevo_telefono, nuevo_correo):
    contactos = cargar_contactos()
    for contacto in contactos:
        if contacto["nombre"].lower() == nombre_original.lower():
            contacto["nombre"] = nuevo_nombre
            contacto["telefono"] = nuevo_telefono
            contacto["correo"] = nuevo_correo
            guardar_contactos(contactos)
            return True
    return False