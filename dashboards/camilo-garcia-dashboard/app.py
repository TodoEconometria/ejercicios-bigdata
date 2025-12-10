import os
import pandas as pd
from flask import Flask, render_template, jsonify, request
import json
import numpy as np
from datetime import datetime, timedelta

app = Flask(__name__)

# Configurar la ruta del archivo de datos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, '..', '..', 'datos', 'taxi_limpio.csv')


def load_data():
    """Cargar los datos del archivo CSV"""
    print(f"Intentando cargar datos desde: {DATA_PATH}")

    try:
        # Verificar si el archivo existe
        if not os.path.exists(DATA_PATH):
            print(f"Archivo no encontrado: {DATA_PATH}")
            print("Creando datos de ejemplo...")
            return create_sample_data()

        # Intentar cargar los datos
        print("Cargando datos del archivo...")
        df = pd.read_csv(DATA_PATH, nrows=50000)  # Limitar a 50,000 filas para mejor rendimiento

        print(f"Datos cargados: {len(df)} filas, {len(df.columns)} columnas")

        # Convertir columnas de fecha/hora si existen
        if 'tpep_pickup_datetime' in df.columns:
            df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'], errors='coerce')
        if 'tpep_dropoff_datetime' in df.columns:
            df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'], errors='coerce')

        return df
    except Exception as e:
        print(f"Error cargando datos: {e}")
        print("Creando datos de ejemplo debido al error...")
        return create_sample_data()


def create_sample_data():
    """Crear datos de ejemplo si el archivo no existe"""
    print("Creando datos de ejemplo...")
    np.random.seed(42)
    n_samples = 5000

    # Crear fechas base
    base_date = datetime(2021, 1, 1)

    # Crear arrays
    passenger_counts = np.random.choice([0, 1, 2, 3, 4, 5, 6], n_samples, p=[0.01, 0.5, 0.2, 0.15, 0.08, 0.04, 0.02])
    trip_distances = np.random.exponential(3, n_samples).round(2)
    fare_amounts = np.random.uniform(2.5, 100, n_samples).round(2)

    data = {
        'tpep_pickup_datetime': [base_date + timedelta(hours=i % 24) for i in range(n_samples)],
        'passenger_count': passenger_counts,
        'trip_distance': trip_distances,
        'fare_amount': fare_amounts,
        'total_amount': fare_amounts + np.random.uniform(0, 10, n_samples).round(2),
        'tip_amount': np.random.exponential(2, n_samples).round(2)
    }

    # Crear DataFrame
    df = pd.DataFrame(data)

    print(f"Datos de ejemplo creados: {len(df)} filas")
    return df


def calculate_statistics(df):
    """Calcular las estadísticas requeridas"""
    stats = {}

    # 1. Total de viajes
    stats['total_viajes'] = len(df)

    # 2. Distancia promedio
    stats['distancia_promedio'] = float(df['trip_distance'].mean())
    stats['distancia_maxima'] = float(df['trip_distance'].max())

    # 3. Tarifa promedio
    stats['tarifa_promedio'] = float(df['fare_amount'].mean())
    stats['tarifa_maxima'] = float(df['fare_amount'].max())

    # 4. Más/menos pasajeros frecuentes
    passenger_counts = df['passenger_count'].value_counts().sort_index()
    stats['pasajeros_mas_frecuentes'] = int(passenger_counts.idxmax())
    stats['pasajeros_menos_frecuentes'] = int(passenger_counts.idxmin())

    # 5. Valores nulos
    null_counts = df.isnull().sum()
    stats['valores_nulos'] = int(null_counts.sum())
    stats['columnas_con_nulos'] = null_counts[null_counts > 0].to_dict()

    # Estadísticas adicionales
    stats['ingreso_total'] = float(df['total_amount'].sum().round(2))
    stats['propina_promedio'] = float(df['tip_amount'].mean().round(2))

    # Duración promedio (estimada)
    if 'trip_distance' in df.columns:
        # Estimación: 2 minutos por milla + 5 minutos base
        stats['duracion_promedio'] = float((df['trip_distance'] * 2 + 5).mean().round(1))
    else:
        stats['duracion_promedio'] = 0

    return stats


def create_chart_data(df):
    """Crear datos para los gráficos en formato simple"""
    charts = {}

    try:
        # Gráfico 1: Distribución de distancias (histograma)
        distances = df['trip_distance'].dropna()
        hist_dist, bin_edges = np.histogram(distances, bins=30)
        charts['distancia'] = {
            'type': 'histogram',
            'x': distances.tolist(),
            'nbinsx': 30,
            'title': 'Distribución de Distancias de Viaje',
            'xaxis_title': 'Distancia (millas)',
            'yaxis_title': 'Frecuencia',
            'color': '#1f77b4'
        }

        # Gráfico 2: Distribución de tarifas (box plot)
        fares = df['fare_amount'].dropna()
        charts['tarifa'] = {
            'type': 'box',
            'y': fares.tolist(),
            'title': 'Distribución de Tarifas',
            'yaxis_title': 'Tarifa ($)',
            'color': '#ff7f0e'
        }

        # Gráfico 3: Pasajeros por viaje (bar chart)
        passenger_counts = df['passenger_count'].value_counts().sort_index()
        charts['pasajeros'] = {
            'type': 'bar',
            'x': [str(i) for i in passenger_counts.index],
            'y': passenger_counts.values.tolist(),
            'title': 'Distribución de Pasajeros por Viaje',
            'xaxis_title': 'Número de Pasajeros',
            'yaxis_title': 'Número de Viajes',
            'color': '#2ca02c'
        }

        # Gráfico 4: Viajes por hora del día
        if 'tpep_pickup_datetime' in df.columns:
            df['pickup_hour'] = df['tpep_pickup_datetime'].dt.hour
            trips_by_hour = df['pickup_hour'].value_counts().sort_index()
            charts['horas'] = {
                'type': 'line',
                'x': trips_by_hour.index.tolist(),
                'y': trips_by_hour.values.tolist(),
                'title': 'Viajes por Hora del Día',
                'xaxis_title': 'Hora del Día',
                'yaxis_title': 'Número de Viajes',
                'color': '#d62728'
            }

        # Gráfico 5: Relación distancia vs tarifa (scatter)
        mask = df['trip_distance'].notna() & df['fare_amount'].notna()
        sample_size = min(500, mask.sum())
        if sample_size > 0:
            sample_df = df[mask].sample(sample_size)
            charts['distancia_vs_tarifa'] = {
                'type': 'scatter',
                'x': sample_df['trip_distance'].tolist(),
                'y': sample_df['fare_amount'].tolist(),
                'title': 'Relación: Distancia vs Tarifa',
                'xaxis_title': 'Distancia (millas)',
                'yaxis_title': 'Tarifa ($)',
                'color': '#9467bd'
            }

    except Exception as e:
        print(f"Error creando datos de gráficos: {e}")
        # Crear datos de ejemplo para gráficos
        charts = create_sample_chart_data()

    return charts


def create_sample_chart_data():
    """Crear datos de ejemplo para gráficos si hay error"""
    # Datos de ejemplo simples
    np.random.seed(42)

    return {
        'distancia': {
            'type': 'histogram',
            'x': np.random.exponential(3, 1000).tolist(),
            'nbinsx': 30,
            'title': 'Distribución de Distancias de Viaje',
            'xaxis_title': 'Distancia (millas)',
            'yaxis_title': 'Frecuencia',
            'color': '#1f77b4'
        },
        'tarifa': {
            'type': 'box',
            'y': np.random.uniform(2.5, 100, 1000).tolist(),
            'title': 'Distribución de Tarifas',
            'yaxis_title': 'Tarifa ($)',
            'color': '#ff7f0e'
        },
        'pasajeros': {
            'type': 'bar',
            'x': ['0', '1', '2', '3', '4', '5', '6'],
            'y': [10, 500, 200, 150, 80, 40, 20],
            'title': 'Distribución de Pasajeros por Viaje',
            'xaxis_title': 'Número de Pasajeros',
            'yaxis_title': 'Número de Viajes',
            'color': '#2ca02c'
        },
        'horas': {
            'type': 'line',
            'x': list(range(24)),
            'y': [50, 30, 20, 15, 10, 20, 100, 300, 400, 350, 300, 320,
                  350, 300, 280, 300, 350, 400, 450, 420, 380, 300, 200, 100],
            'title': 'Viajes por Hora del Día',
            'xaxis_title': 'Hora del Día',
            'yaxis_title': 'Número de Viajes',
            'color': '#d62728'
        },
        'distancia_vs_tarifa': {
            'type': 'scatter',
            'x': np.random.exponential(3, 200).tolist(),
            'y': (np.random.exponential(3, 200) * 10 + 5).tolist(),
            'title': 'Relación: Distancia vs Tarifa',
            'xaxis_title': 'Distancia (millas)',
            'yaxis_title': 'Tarifa ($)',
            'color': '#9467bd'
        }
    }


@app.route('/')
def index():
    """Página principal del dashboard"""
    try:
        df = load_data()
        stats = calculate_statistics(df)
        charts = create_chart_data(df)

        # Preparar vista previa de datos
        data_preview = df.head(10).to_dict('records')
        columns = list(df.columns)

        return render_template('index_simple.html',
                               stats=stats,
                               charts=charts,
                               columns=columns,
                               data_preview=data_preview)
    except Exception as e:
        print(f"Error en página principal: {e}")
        return f"<h1>Error</h1><p>{str(e)}</p>", 500


@app.route('/api/stats')
def get_stats():
    """API para obtener estadísticas"""
    try:
        df = load_data()
        stats = calculate_statistics(df)
        return jsonify(stats)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/filter', methods=['POST'])
def filter_data():
    """API para filtrar datos"""
    try:
        df = load_data()

        # Obtener parámetros del filtro
        data = request.get_json()
        min_distance = float(data.get('min_distance', 0))
        max_distance = float(data.get('max_distance', 100))
        min_passengers = int(data.get('min_passengers', 0))
        max_passengers = int(data.get('max_passengers', 6))

        # Aplicar filtros
        mask = (df['trip_distance'] >= min_distance) & (df['trip_distance'] <= max_distance)
        mask = mask & (df['passenger_count'] >= min_passengers) & (df['passenger_count'] <= max_passengers)

        filtered_df = df[mask].copy()

        # Calcular estadísticas con los datos filtrados
        stats = calculate_statistics(filtered_df)

        # Crear datos de gráficos con datos filtrados
        charts = create_chart_data(filtered_df)

        return jsonify({
            'stats': stats,
            'charts': charts,
            'filtered_count': len(filtered_df),
            'original_count': len(df)
        })
    except Exception as e:
        print(f"Error filtrando datos: {e}")
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    print("=" * 50)
    print("Iniciando Dashboard de Análisis de Taxis NYC")
    print("=" * 50)

    app.run(debug=True, port=5000)
