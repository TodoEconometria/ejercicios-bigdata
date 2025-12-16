"""
Dashboard Flask - EDA NYC Taxi Dataset

"""
from flask import Flask, render_template, jsonify
import numpy as np
import os
import pandas as pd
import plotly.express as px  # pip install plotly
from scipy.stats import pearsonr  # pip install scipy

app = Flask(__name__)

# Ruta al archivo de datos
DATA_PATH = os.path.join('..', '..', 'datos', 'nyc_taxi.csv')

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
        df["trip_distance"] = pd.to_numeric(df["trip_distance"], errors='coerce') * 1.60934
        stats['trip_distance'] = {
            'mean': float(df['trip_distance'].mean()),
            'median': float(df['trip_distance'].median()),
            'min': float(df['trip_distance'].min()),
            'max': float(df['trip_distance'].max()),
            'std': float(df['trip_distance'].std())
        }
    if 'total_amount' in df.columns:
        df["total_amount"] = pd.to_numeric(df["total_amount"], errors='coerce') * 0.92
        stats['fare_amount'] = {
            'mean': float(df['total_amount'].mean()),
            'median': float(df['total_amount'].median()),
            'min': float(df['total_amount'].min()),
            'max': float(df['total_amount'].max()),
            'std': float(df['total_amount'].std())
        }

    if 'passenger_count' in df.columns:
        stats['passenger_distribution'] = df['passenger_count'].value_counts().to_dict()

    return stats

def preparar_datos_graficos(df):
    """Prepara datos para los gráficos interactivos"""
    if df is None:
        return None

    graficos = {}

    # Pasajeros por viaje
    if 'passenger_count' in df.columns:
        passenger_counts = df['passenger_count'].value_counts().sort_index()
        fig_pass = px.bar(
            x=passenger_counts.index,
            y=passenger_counts.values,
            labels={'x': 'Número de Pasajeros', 'y': 'Cantidad de Viajes'},
            title='Distribución de Pasajeros por Viaje',
            color=passenger_counts.index,
            color_continuous_scale='Viridis'
        )
        graficos['pasajeros'] = {
            'labels': passenger_counts.index.tolist(),
            'values': passenger_counts.values.tolist()
        }

    # Histograma de distancia refinado (bins cada 0.5 km)
    if 'trip_distance' in df.columns:
        bins = np.arange(0, 20.5, 0.5)  # bins de 0 a 20 km, paso 0.5
        dist_counts, bin_edges = np.histogram(df['trip_distance'].dropna(), bins=bins)
        labels = [f"{bin_edges[i]:.1f}-{bin_edges[i + 1]:.1f}" for i in range(len(bin_edges) - 1)]

        graficos['distancia'] = {
            'labels': labels,
            'values': dist_counts.tolist()
        }

    # Histograma de tarifas (propina)
    if 'tip_amount' in df.columns:
        bins = np.arange(0, 200, 5)
        fare_counts, bin_edges = np.histogram(df['tip_amount'].dropna(), bins=bins)
        labels = [f"{bin_edges[i]:.0f}-{bin_edges[i + 1]:.0f}" for i in range(len(bin_edges) - 1)]

        graficos['tarifa'] = {
            'labels': labels,
            'values': fare_counts.tolist()
        }

    # Gráfico interactivo: distancia vs precio
    if 'trip_distance' in df.columns and 'total_amount' in df.columns:
        df['trip_distance'] = pd.to_numeric(df['trip_distance'], errors='coerce')
        df['total_amount'] = pd.to_numeric(df['total_amount'], errors='coerce')
        df_corr = df[['trip_distance', 'total_amount']].dropna()
        r, pval = pearsonr(df_corr['trip_distance'], df_corr['total_amount'])

        fig = px.scatter(
            df_corr,
            x='trip_distance',
            y='total_amount',
            trendline='ols',
            labels={'trip_distance': 'Distancia', 'total_amount': 'Precio total'},
            title=f'Distancia vs Precio — Pearson r={r:.3f}',
            height=500, width=700
        )

        # Guardamos el gráfico interactivo en JSON
        graficos['correlaciones'] = fig.to_dict()

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
