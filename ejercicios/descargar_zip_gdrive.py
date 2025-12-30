# -*- coding: utf-8 -*-
"""
Script para descargar un archivo ZIP desde Google Drive utilizando la librería gdown.

Esta es la solución recomendada y más robusta, ya que gdown está diseñado
específicamente para manejar las complejidades de las descargas desde Google Drive.

El script:
1. Descarga el archivo ZIP desde Google Drive (reemplaza si existe)
2. Descomprime el contenido en una carpeta
3. Elimina el archivo ZIP después de descomprimir
"""

import gdown
import os
import zipfile
import shutil

# --- CONFIGURACIÓN ---

# La URL compartida de Google Drive
# No es necesario extraer el ID manualmente, gdown lo hace por nosotros.
url = "https://drive.google.com/file/d/1lqejgfEC8AlDDbOvZYV_VUPkRr7iQI0W/view?usp=classroom_web&authuser=2"

# Nombre del archivo de salida
nombre_archivo = "csv_tienda_informatica.zip"

# Construimos la ruta de destino en la carpeta 'datos'
# Sube dos niveles desde 'ejercicios' y luego entra a 'datos'
ruta_base = os.path.dirname(__file__)
directorio_destino = os.path.join(ruta_base, '..', 'datos')

# Nos aseguramos de que el directorio de destino exista
os.makedirs(directorio_destino, exist_ok=True)

ruta_completa_destino = os.path.join(directorio_destino, nombre_archivo)

# Nombre de la carpeta donde se descomprimirá (sin extensión .zip)
nombre_carpeta_descomprimida = nombre_archivo.replace('.zip', '')
ruta_carpeta_descomprimida = os.path.join(directorio_destino, nombre_carpeta_descomprimida)


# --- LÓGICA DE DESCARGA ---

if __name__ == "__main__":
    # Si el archivo ya existe, lo eliminamos para reemplazarlo
    if os.path.exists(ruta_completa_destino):
        print(f"[!] El archivo '{nombre_archivo}' ya existe. Sera reemplazado.")
        os.remove(ruta_completa_destino)

    print(f"[>] Iniciando la descarga desde Google Drive a '{ruta_completa_destino}'...")
    print("    Esto puede tardar unos minutos. gdown mostrara el progreso.")

    try:
        # Extraer el ID del archivo de la URL
        file_id = "1lqejgfEC8AlDDbOvZYV_VUPkRr7iQI0W"

        # Intentar con diferentes métodos
        # Método 1: URL directa de descarga
        url_directa = f"https://drive.google.com/uc?id={file_id}&export=download"

        print(f"    Intentando descarga con URL directa...")
        gdown.download(url_directa, ruta_completa_destino, quiet=False, fuzzy=True)

        print(f"\n[OK] Descarga completada con exito.")

        # --- DESCOMPRIMIR EL ARCHIVO ---
        print(f"\n[>] Descomprimiendo el archivo en '{ruta_carpeta_descomprimida}'...")

        # Si la carpeta ya existe, la eliminamos primero
        if os.path.exists(ruta_carpeta_descomprimida):
            print(f"    La carpeta '{nombre_carpeta_descomprimida}' ya existe. Sera reemplazada.")
            shutil.rmtree(ruta_carpeta_descomprimida)

        # Crear la carpeta de destino
        os.makedirs(ruta_carpeta_descomprimida, exist_ok=True)

        # Descomprimir
        with zipfile.ZipFile(ruta_completa_destino, 'r') as zip_ref:
            zip_ref.extractall(ruta_carpeta_descomprimida)

        print(f"[OK] Descompresion completada.")

        # --- ELIMINAR EL ARCHIVO ZIP ---
        print(f"\n[>] Eliminando el archivo ZIP '{nombre_archivo}'...")
        os.remove(ruta_completa_destino)
        print(f"[OK] Archivo ZIP eliminado.")

        print(f"\n[OK] Proceso completado exitosamente.")
        print(f"     Los archivos estan en: {ruta_carpeta_descomprimida}")

    except Exception as e:
        print(f"\n[ERROR] Ocurrio un error: {e}")
        print("        Por favor, verifica la URL y tu conexion a internet.")
        # Si el archivo se creó pero está incompleto, lo borramos
        if os.path.exists(ruta_completa_destino):
            os.remove(ruta_completa_destino)
