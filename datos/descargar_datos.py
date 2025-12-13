import os
import requests
import gzip
import shutil
# CARLOS MALPICA
# URL del dataset (Enero 2021) - Usamos una fuente alternativa confiable (DataTalksClub)
# El archivo viene comprimido en GZIP (.gz)
DATA_URL = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "ejercicios-bigdata", "datos")

def asegurar_directorio(ruta):
    os.makedirs(ruta, exist_ok=True)

def descargar():
    asegurar_directorio(DATA_DIR)
    ruta_csv_final = os.path.join(DATA_DIR, "nyc_taxi.csv")
    ruta_gz = os.path.join(DATA_DIR, "nyc_taxi.csv.gz")
    
    if os.path.exists(ruta_csv_final):
        print(f"✅ El archivo ya existe en: {ruta_csv_final}")
        return

    print(f"⬇️ Descargando datos comprimidos desde: {DATA_URL}")
    print("Esto puede tardar un poco (aprox. 25 MB)...")
    
    try:
        respuesta = requests.get(DATA_URL, stream=True)
        respuesta.raise_for_status()

        with open(ruta_gz, "wb") as f:
            for trozo in respuesta.iter_content(chunk_size=8192):
                f.write(trozo)
        print("✅ Descarga completada.")
        
        print("📦 Descomprimiendo archivo GZIP...")
        with gzip.open(ruta_gz, 'rb') as f_in:
            with open(ruta_csv_final, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        print(f"✅ Archivo descomprimido listo: {ruta_csv_final}")
        
        # Limpieza: borramos el archivo .gz para ahorrar espacio
        os.remove(ruta_gz)
        print("🧹 Archivo temporal .gz eliminado.")

    except Exception as e:
        print(f"❌ Error durante la descarga o descompresión: {e}")
        # Si falla, intentamos limpiar
        if os.path.exists(ruta_gz):
            os.remove(ruta_gz)

if __name__ == "__main__":
    descargar()
