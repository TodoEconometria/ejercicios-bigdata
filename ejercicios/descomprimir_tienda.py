
import os
import zipfile
import shutil

# --- CONFIGURACIÓN ---

# Construimos las rutas
ruta_base = os.path.dirname(__file__)
directorio_datos = os.path.join(ruta_base, '..', 'datos')
nombre_archivo = "csv_tienda_informatica.zip"
ruta_zip = os.path.join(directorio_datos, nombre_archivo)

# Nombre de la carpeta donde se descomprimirá
nombre_carpeta = nombre_archivo.replace('.zip', '')
ruta_carpeta_destino = os.path.join(directorio_datos, nombre_carpeta)

# --- LÓGICA ---

if __name__ == "__main__":
    # Verificar que el archivo ZIP existe
    if not os.path.exists(ruta_zip):
        print(f"[ERROR] No se encontro el archivo: {ruta_zip}")
        print(f"\n        Por favor:")
        print(f"        1. Descarga el archivo desde Google Drive/Classroom")
        print(f"        2. Guardalo como: {ruta_zip}")
        print(f"        3. Ejecuta este script nuevamente")
        exit(1)

    print(f"[OK] Archivo encontrado: {ruta_zip}")

    # --- DESCOMPRIMIR ---
    print(f"\n[>] Descomprimiendo el archivo en '{ruta_carpeta_destino}'...")

    # Si la carpeta ya existe, la eliminamos primero
    if os.path.exists(ruta_carpeta_destino):
        print(f"    La carpeta '{nombre_carpeta}' ya existe. Sera reemplazada.")
        shutil.rmtree(ruta_carpeta_destino)

    # Crear la carpeta de destino
    os.makedirs(ruta_carpeta_destino, exist_ok=True)

    # Descomprimir
    try:
        with zipfile.ZipFile(ruta_zip, 'r') as zip_ref:
            zip_ref.extractall(ruta_carpeta_destino)

        print(f"[OK] Descompresion completada.")

        # --- ELIMINAR EL ARCHIVO ZIP ---
        print(f"\n[>] Eliminando el archivo ZIP '{nombre_archivo}'...")
        os.remove(ruta_zip)
        print(f"[OK] Archivo ZIP eliminado.")

        print(f"\n[OK] Proceso completado exitosamente.")
        print(f"     Los archivos estan en: {ruta_carpeta_destino}")

        # Mostrar contenido
        print(f"\nContenido de la carpeta:")
        for item in os.listdir(ruta_carpeta_destino):
            ruta_item = os.path.join(ruta_carpeta_destino, item)
            if os.path.isdir(ruta_item):
                print(f"  [DIR]  {item}")
            else:
                tamano = os.path.getsize(ruta_item)
                print(f"  [FILE] {item} ({tamano:,} bytes)")

    except zipfile.BadZipFile:
        print(f"[ERROR] El archivo no es un ZIP valido o esta corrupto.")
        print(f"        Intenta descargarlo nuevamente.")
    except Exception as e:
        print(f"[ERROR] Ocurrio un error: {e}")
