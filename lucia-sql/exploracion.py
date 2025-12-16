import os
import pandas as pd

# Carpeta donde están tus CSVs
carpeta_csv = r"C:\Users\Tarde\PycharmProjects\ejercicios-bigdata\lucia-sql\csv_tienda_informatica"

# Archivos donde se guardará la info
archivo_columnas = "columnas_tipos.csv"
archivo_info = "info_csvs.txt"

# Preparar lista para columnas y tipos
columnas_tipos = []

# Limpiar archivo de info si existe
with open(archivo_info, "w", encoding="utf-8") as f:
    f.write("")

# Recorrer todos los CSV
for nombre_csv in os.listdir(carpeta_csv):
    if nombre_csv.endswith(".csv"):
        ruta_csv = os.path.join(carpeta_csv, nombre_csv)
        df = pd.read_csv(ruta_csv)

        # Guardar columnas y tipos
        for col in df.columns:
            columnas_tipos.append({
                "archivo": nombre_csv,
                "columna": col,
                "tipo": str(df[col].dtype)
            })

        # Guardar .info() en archivo de texto
        with open(archivo_info, "a", encoding="utf-8") as f:
            f.write(f"\n--- {nombre_csv} ---\n")
            df.info(buf=f)

# Guardar columnas y tipos en CSV
df_columnas = pd.DataFrame(columnas_tipos)
df_columnas.to_csv(archivo_columnas, index=False, encoding="utf-8")

print("¡Listo! Columnas y tipos guardados en", archivo_columnas)
print("Información de .info() guardada en", archivo_info)
