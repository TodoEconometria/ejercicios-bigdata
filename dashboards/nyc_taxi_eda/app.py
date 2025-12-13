"""
Dashboard Flask - EDA NYC Taxi Dataset
Ejemplo de referencia para alumnos
"""

from flask import Flask, render_template, jsonify
import pandas as pd
import json
import os

app = Flask(__name__)

# Ruta al archivo de datos

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_PATH = os.path.join(BASE_DIR, "datos", "nyc_taxi.csv")
def cargar_datos():
    """Carga y prepara los datos para análisis"""
    try:
        df = pd.read_csv(DATA_PATH)
        return df
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return None

def calcular_estadisticas(df):
    """Calcula estadísticas descriptivas del dataset"""
    if df is None:
        return None

    stats = {
        'total_registros': len(df),
        'total_columnas': len(df.columns),
        'columnas': df.columns.tolist(),
        'valores_nulos': df.isnull().sum().to_dict(),
        'tipos_datos': df.dtypes.astype(str).to_dict(),
    }

    # Estadísticas numéricas
    if 'trip_distance' in df.columns:
        stats['trip_distance'] = {
            'mean': float(df['trip_distance'].mean()),
            'median': float(df['trip_distance'].median()),
            'min': float(df['trip_distance'].min()),
            'max': float(df['trip_distance'].max()),
            'std': float(df['trip_distance'].std())
        }

    if 'fare_amount' in df.columns:
        stats['fare_amount'] = {
            'mean': float(df['fare_amount'].mean()),
            'median': float(df['fare_amount'].median()),
            'min': float(df['fare_amount'].min()),
            'max': float(df['fare_amount'].max()),
            'std': float(df['fare_amount'].std())
        }

    if 'passenger_count' in df.columns:
        stats['passenger_distribution'] = df['passenger_count'].value_counts().to_dict()

    return stats

def preparar_datos_graficos(df):
    """Prepara datos para los gráficos interactivos"""
    if df is None:
        return None

    graficos = {}

    # Distribución de distancias
    if 'trip_distance' in df.columns:
        dist_bins = pd.cut(df['trip_distance'], bins=20)
        dist_counts = dist_bins.value_counts().sort_index()
        graficos['distancia'] = {
            'labels': [str(x) for x in dist_counts.index],
            'values': dist_counts.values.tolist()
        }

    # Distribución de tarifas
    if 'fare_amount' in df.columns:
        # Filtrar valores extremos para mejor visualización
        fare_filtered = df[df['fare_amount'] < df['fare_amount'].quantile(0.95)]
        fare_bins = pd.cut(fare_filtered['fare_amount'], bins=20)
        fare_counts = fare_bins.value_counts().sort_index()
        graficos['tarifa'] = {
            'labels': [str(x) for x in fare_counts.index],
            'values': fare_counts.values.tolist()
        }

    # Pasajeros por viaje
    if 'passenger_count' in df.columns:
        passenger_counts = df['passenger_count'].value_counts().sort_index()
        graficos['pasajeros'] = {
            'labels': passenger_counts.index.tolist(),
            'values': passenger_counts.values.tolist()
        }

    return graficos

@app.route('/')
def index():
    """Página principal del dashboard"""
    df = cargar_datos()

    if df is None:
        return "Error: No se pudo cargar el dataset", 500

    stats = calcular_estadisticas(df)

    return render_template('index.html', stats=stats)

@app.route('/api/graficos')
def api_graficos():
    """API endpoint para datos de gráficos"""
    df = cargar_datos()

    if df is None:
        return jsonify({'error': 'No se pudo cargar el dataset'}), 500

    graficos = preparar_datos_graficos(df)
    return jsonify(graficos)

@app.route('/api/estadisticas')
def api_estadisticas():
    """API endpoint para estadísticas"""
    df = cargar_datos()

    if df is None:
        return jsonify({'error': 'No se pudo cargar el dataset'}), 500

    stats = calcular_estadisticas(df)
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
