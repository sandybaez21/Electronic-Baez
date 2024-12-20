import os

def mostrar_enlace():
    # Nombre del archivo HTML
    archivo_html = 'tienda_online.html'  # Asegúrate de que esté en el mismo directorio

    # Obtener la ruta completa del archivo
    ruta_archivo = os.path.abspath(archivo_html)

    # Crear el enlace
    enlace = f"file://{ruta_archivo}"

    # Imprimir el enlace en la terminal
    print(f"Tu tienda online está lista. Accede a ella con este enlace:")
    print(enlace)

if __name__ == "__main__":
    mostrar_enlace()
