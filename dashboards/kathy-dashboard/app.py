"""
Dashboard Flask - EDA NYC Taxi (versión alumno)
"""

from flask import Flask, render_template, jsonify
import pandas as pd
import os
import numpy as np

app = Flask(__name__)

# Ruta al CSV: ruta absoluta 2 niveles arriba del archivo en app.py C:\Users\tecHK\PycharmProjects\ejercicios-bigdata\dashboards\kathy-dashboard
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_PATH = os.path.join(BASE_DIR, "datos", "nyc_taxi.csv")
#Función devuelve los datos y un dataframe de pandas
#Try y catch para capturar excepción
#Un data Frame es una Tabla de datos en memoria
def cargar_datos():
    try:
        df = pd.read_csv(DATA_PATH)
        return df
    except Exception as e:
        print(f"[ERROR] No se pudo cargar el CSV: {e}")
        return None

#Función.-Diccionario con variable con datos estadísticos
def calcular_estadisticas(df):
    if df is None:
        return None

    stats = {}

    # 1) Total de viajes
    stats["total_viajes"] = int(len(df))

    # 2) Número de columnas
    stats["num_columnas"] = int(len(df.columns))

    # 3) Distancia media
    if "trip_distance" in df.columns:
        stats["distancia_media"] = float(df["trip_distance"].mean())
        stats["distancia_mediana"] = float(df["trip_distance"].median())
    else:
        stats["distancia_media"] = None
        stats["distancia_mediana"] = None

    # 4) Tarifa media (fare_amount)
    if "fare_amount" in df.columns:
        stats["tarifa_media"] = float(df["fare_amount"].mean())
        stats["tarifa_mediana"] = float(df["fare_amount"].median())
    else:
        stats["tarifa_media"] = None
        stats["tarifa_mediana"] = None

    # 5) Pasajeros más frecuentes
    if "passenger_count" in df.columns:
        vc = df["passenger_count"].value_counts()
        stats["pasajeros_mas_frecuentes"] = int(vc.idxmax())
        stats["pasajeros_mas_frecuentes_cuenta"] = int(vc.max())
    else:
        stats["pasajeros_mas_frecuentes"] = None
        stats["pasajeros_mas_frecuentes_cuenta"] = None

    # Info para la tabla (valores nulos, tipos…)
    stats["columnas"] = df.columns.tolist()
    stats["valores_nulos"] = df.isnull().sum().to_dict()
    stats["tipos_datos"] = df.dtypes.astype(str).to_dict()

    return stats

#Función.-Devuelve diccionario con datos para los gráficos
def preparar_datos_graficos(df):

    if df is None:
        return None

    graficos = {}

    # -------- 1) Distribución de distancias --------
    if "trip_distance" in df.columns:
        #Quitar valores extremos
        dist = df["trip_distance"].clip(lower=0, upper=df["trip_distance"].quantile(0.99))
        # Intervalos de 20
        dist_bins = pd.cut(dist, bins=20)
        dist_counts = dist_bins.value_counts().sort_index()
        #Etiquetas y valores
        graficos["distancia"] = {
            "labels": [str(interval) for interval in dist_counts.index],
            "values": dist_counts.values.tolist(),
        }

    # -------- 2) Distribución de tarifas --------
    if "fare_amount" in df.columns:
        fares = df["fare_amount"].clip(lower=0, upper=df["fare_amount"].quantile(0.99))
        fare_bins = pd.cut(fares, bins=20)
        fare_counts = fare_bins.value_counts().sort_index()
        graficos["tarifa"] = {
            "labels": [str(interval) for interval in fare_counts.index],
            "values": fare_counts.values.tolist(),
        }

    # -------- 3) Pasajeros por viaje --------
    if "passenger_count" in df.columns:
        pax_counts = df["passenger_count"].value_counts().sort_index()
        graficos["pasajeros"] = {
            "labels": pax_counts.index.tolist(),
            "values": pax_counts.values.tolist(),
        }

    return graficos



# ===================== RUTAS FLASK =====================

@app.route("/")
def index():
    """
    Página principal. Solo renderiza HTML y pasa estadísticas.
    Los gráficos se cargan por JavaScript desde /api/graficos.
    """
    df = cargar_datos()
    if df is None:
        return "No se pudo cargar el dataset", 500
    #templates es la ruta por defecto de flask
    stats = calcular_estadisticas(df)
    return render_template("index.html", stats=stats)

#json values para charts
@app.route("/api/graficos")
def api_graficos():
    """Devuelve los datos para los gráficos en formato JSON."""
    df = cargar_datos()
    if df is None:
        return jsonify({"error": "No se pudo cargar el dataset"}), 500

    graficos = preparar_datos_graficos(df)
    return jsonify(graficos)
#Gráfico de dispersión
@app.route("/api/scatter_distancia_propina")
def api_scatter_distancia_propina():
    df = cargar_datos()
    if df is None:
        return jsonify({"error": "No se pudo cargar el dataset"}), 500

    # Comprobamos que existan las columnas
    if not {"trip_distance", "tip_amount"}.issubset(df.columns):
        return jsonify({"error": "Faltan columnas 'trip_distance' o 'tip_amount'"}), 400

    # Nos quedamos solo con las columnas relevantes y limpiamos
    datos = df[["trip_distance", "tip_amount"]].replace([np.inf, -np.inf], np.nan).dropna()

    # Filtros para evitar valores locos
    datos = datos[
        (datos["trip_distance"] > 0) &
        (datos["trip_distance"] < 50) &    # no viajes absurdamente largos
        (datos["tip_amount"] >= 0) &
        (datos["tip_amount"] < 100)        # no propinas absurdas
    ]

    # MUESTREO: máximo 10000 puntos para que no sea pesado
    if len(datos) > 10000:
        datos = datos.sample(10000, random_state=42)

    # Formato que Chart.js entiende para scatter: [{x:..., y:...}, ...]
    puntos = [
        {"x": float(row["trip_distance"]), "y": float(row["tip_amount"])}
        for _, row in datos.iterrows()
    ]

    return jsonify({
        "title": "Relación entre distancia del viaje y propina",
        "x_label": "Distancia del viaje",
        "y_label": "Propina ($)",
        "points": puntos
    })

#ejecuta servidor Flask
if __name__ == "__main__":
    # Ejecutar con: python app.py
    app.run(debug=True, host="0.0.0.0", port=5000)
