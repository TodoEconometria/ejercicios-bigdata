from flask import Flask, render_template, jsonify, request
import pandas as pd
import numpy as np
from datetime import datetime
import json
import os
import traceback

app = Flask(__name__)

# Ruta al archivo CSV
CSV_PATH = r"C:\Users\LENOVO\PycharmProjects\ejercicios_bigdata\datos\taxi_limpio.csv"

# Variable global para cachear datos
df_cache = None


def cargar_datos():
    global df_cache
    if df_cache is not None:
        return df_cache.copy()

    print(f"Cargando datos desde: {CSV_PATH}")

    if not os.path.exists(CSV_PATH):
        print("Archivo no encontrado. Creando datos de ejemplo...")
        # Crear datos de ejemplo más realistas
        np.random.seed(42)
        n_samples = 10000
        dates = pd.date_range('2021-01-01', periods=n_samples, freq='T')

        df_cache = pd.DataFrame({
            'VendorID': np.random.choice([1, 2], n_samples, p=[0.7, 0.3]),
            'tpep_pickup_datetime': dates,
            'tpep_dropoff_datetime': dates + pd.Timedelta(minutes=np.random.exponential(20, n_samples)),
            'passenger_count': np.random.choice([1, 2, 3, 4, 5, 6], n_samples, p=[0.4, 0.3, 0.15, 0.08, 0.05, 0.02]),
            'trip_distance': np.round(np.random.exponential(2.5, n_samples), 2),
            'PULocationID': np.random.choice(range(1, 264), n_samples),
            'DOLocationID': np.random.choice(range(1, 264), n_samples),
            'payment_type': np.random.choice([1, 2, 3, 4, 5, 6], n_samples, p=[0.6, 0.3, 0.05, 0.03, 0.01, 0.01]),
            'total_amount': np.round(np.random.uniform(3, 100, n_samples), 2),
            'tip_amount': np.round(np.random.exponential(3, n_samples), 2),
            'duracion_minutos': np.round(np.random.uniform(2, 120, n_samples), 2)
        })

        # Hacer que algunos viajes no tengan propina
        df_cache.loc[np.random.random(n_samples) > 0.7, 'tip_amount'] = 0

        print(f"Datos de ejemplo creados: {len(df_cache)} registros")
        return df_cache.copy()

    try:
        df = pd.read_csv(CSV_PATH, low_memory=False)

        # Convertir columnas de fecha
        if 'tpep_pickup_datetime' in df.columns:
            df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'], errors='coerce')
        if 'tpep_dropoff_datetime' in df.columns:
            df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'], errors='coerce')

        # Crear duracion_minutos si no existe
        if 'duracion_minutos' not in df.columns and 'tpep_pickup_datetime' in df.columns and 'tpep_dropoff_datetime' in df.columns:
            df['duracion_minutos'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60

        # Limpiar nulos
        df = df.dropna(subset=['tpep_pickup_datetime'])

        print(f"Datos cargados: {len(df)} registros")
        df_cache = df
        return df.copy()
    except Exception as e:
        print(f"Error al cargar datos: {str(e)}")
        traceback.print_exc()
        return cargar_datos()  # Recursión para usar datos de ejemplo


def aplicar_filtros(df, args):
    """Aplica todos los filtros al DataFrame"""
    df_filtrado = df.copy()

    # Filtro por fechas
    fecha_inicio = args.get('fecha_inicio')
    fecha_fin = args.get('fecha_fin')

    if fecha_inicio and fecha_fin:
        try:
            fecha_inicio_dt = pd.to_datetime(fecha_inicio)
            fecha_fin_dt = pd.to_datetime(fecha_fin) + pd.Timedelta(days=1)  # Incluir todo el día final
            mask = (df_filtrado['tpep_pickup_datetime'] >= fecha_inicio_dt) & (
                        df_filtrado['tpep_pickup_datetime'] < fecha_fin_dt)
            df_filtrado = df_filtrado[mask]
            print(f"Filtro fecha: {len(df_filtrado)} registros después de filtrar")
        except Exception as e:
            print(f"Error en filtro fecha: {e}")

    # Filtro por VendorID
    vendor_id = args.get('vendor_id')
    if vendor_id and vendor_id != 'all' and vendor_id != '':
        try:
            vendor_val = int(vendor_id)
            df_filtrado = df_filtrado[df_filtrado['VendorID'] == vendor_val]
            print(f"Filtro VendorID {vendor_val}: {len(df_filtrado)} registros")
        except Exception as e:
            print(f"Error en filtro VendorID: {e}")

    # Filtro por tipo de pago
    payment_type = args.get('payment_type')
    if payment_type and payment_type != 'all' and payment_type != '':
        try:
            payment_val = int(payment_type)
            df_filtrado = df_filtrado[df_filtrado['payment_type'] == payment_val]
            print(f"Filtro payment_type {payment_val}: {len(df_filtrado)} registros")
        except Exception as e:
            print(f"Error en filtro payment_type: {e}")

    return df_filtrado


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/datos')
def get_datos():
    df = cargar_datos()
    df_filtrado = aplicar_filtros(df, request.args)

    # Limitar a 50 registros para la tabla
    if len(df_filtrado) > 50:
        df_sample = df_filtrado.sample(50)
    else:
        df_sample = df_filtrado

    # Preparar datos para JSON
    result = []
    for _, row in df_sample.iterrows():
        result.append({
            'tpep_pickup_datetime': row['tpep_pickup_datetime'].strftime('%Y-%m-%d %H:%M:%S') if pd.notna(
                row['tpep_pickup_datetime']) else '',
            'trip_distance': float(row['trip_distance']) if 'trip_distance' in row else 0,
            'duracion_minutos': float(row['duracion_minutos']) if 'duracion_minutos' in row else 0,
            'passenger_count': int(row['passenger_count']) if 'passenger_count' in row else 0,
            'total_amount': float(row['total_amount']) if 'total_amount' in row else 0,
            'tip_amount': float(row['tip_amount']) if 'tip_amount' in row else 0
        })

    print(f"Devolviendo {len(result)} registros para tabla")
    return jsonify(result)


@app.route('/api/estadisticas')
def get_estadisticas():
    df = cargar_datos()
    df_filtrado = aplicar_filtros(df, request.args)

    if len(df_filtrado) == 0:
        return jsonify({
            'total_viajes': 0,
            'ingreso_total': 0,
            'distancia_promedio': 0,
            'duracion_promedio': 0,
            'pasajeros_promedio': 0,
            'propina_promedio': 0,
            'registros_filtrados': 0
        })

    estadisticas = {
        'total_viajes': len(df_filtrado),
        'ingreso_total': float(df_filtrado['total_amount'].sum() if 'total_amount' in df_filtrado.columns else 0),
        'distancia_promedio': float(
            df_filtrado['trip_distance'].mean() if 'trip_distance' in df_filtrado.columns else 0),
        'duracion_promedio': float(
            df_filtrado['duracion_minutos'].mean() if 'duracion_minutos' in df_filtrado.columns else 0),
        'pasajeros_promedio': float(
            df_filtrado['passenger_count'].mean() if 'passenger_count' in df_filtrado.columns else 0),
        'propina_promedio': float(df_filtrado['tip_amount'].mean() if 'tip_amount' in df_filtrado.columns else 0),
        'registros_filtrados': len(df_filtrado)
    }

    print(f"Estadísticas calculadas sobre {len(df_filtrado)} registros filtrados")
    return jsonify(estadisticas)


@app.route('/api/distribucion_tiempo')
def get_distribucion_tiempo():
    df = cargar_datos()
    df_filtrado = aplicar_filtros(df, request.args)

    if len(df_filtrado) == 0:
        return jsonify({
            'horas': list(range(24)),
            'cantidad': [0] * 24
        })

    # Extraer hora del día
    df_filtrado['pickup_hour'] = df_filtrado['tpep_pickup_datetime'].dt.hour

    # Contar viajes por hora
    horas = list(range(24))
    conteo_horas = df_filtrado['pickup_hour'].value_counts().reindex(horas, fill_value=0)

    return jsonify({
        'horas': horas,
        'cantidad': conteo_horas.values.tolist(),
        'total_registros': len(df_filtrado)
    })


@app.route('/api/distribucion_distancia')
def get_distribucion_distancia():
    df = cargar_datos()
    df_filtrado = aplicar_filtros(df, request.args)

    if len(df_filtrado) == 0:
        return jsonify({
            'categorias': ['0-1', '1-3', '3-5', '5-10', '10-20', '20-50', '50+'],
            'cantidad': [0, 0, 0, 0, 0, 0, 0]
        })

    # Crear bins de distancia
    bins = [0, 1, 3, 5, 10, 20, 50, float('inf')]
    labels = ['0-1', '1-3', '3-5', '5-10', '10-20', '20-50', '50+']

    if 'trip_distance' in df_filtrado.columns:
        df_filtrado['distancia_categoria'] = pd.cut(df_filtrado['trip_distance'], bins=bins, labels=labels,
                                                    include_lowest=True)
        distribucion = df_filtrado['distancia_categoria'].value_counts().reindex(labels, fill_value=0)
    else:
        distribucion = pd.Series([0] * len(labels), index=labels)

    return jsonify({
        'categorias': labels,
        'cantidad': distribucion.values.tolist(),
        'total_registros': len(df_filtrado)
    })


@app.route('/api/top_locations')
def get_top_locations():
    df = cargar_datos()
    df_filtrado = aplicar_filtros(df, request.args)

    if len(df_filtrado) == 0:
        return jsonify({
            'pickup': {
                'locations': ['Sin datos'] * 10,
                'counts': [0] * 10
            },
            'dropoff': {
                'locations': ['Sin datos'] * 10,
                'counts': [0] * 10
            }
        })

    # Obtener top 10 ubicaciones
    if 'PULocationID' in df_filtrado.columns:
        top_pickup = df_filtrado['PULocationID'].value_counts().head(10)
        pickup_locations = top_pickup.index.astype(str).tolist()
        pickup_counts = top_pickup.values.tolist()
    else:
        pickup_locations = ['N/A'] * 10
        pickup_counts = [0] * 10

    if 'DOLocationID' in df_filtrado.columns:
        top_dropoff = df_filtrado['DOLocationID'].value_counts().head(10)
        dropoff_locations = top_dropoff.index.astype(str).tolist()
        dropoff_counts = top_dropoff.values.tolist()
    else:
        dropoff_locations = ['N/A'] * 10
        dropoff_counts = [0] * 10

    # Completar con ceros si hay menos de 10
    while len(pickup_locations) < 10:
        pickup_locations.append(f"Loc {len(pickup_locations) + 1}")
        pickup_counts.append(0)

    while len(dropoff_locations) < 10:
        dropoff_locations.append(f"Loc {len(dropoff_locations) + 1}")
        dropoff_counts.append(0)

    return jsonify({
        'pickup': {
            'locations': pickup_locations,
            'counts': pickup_counts
        },
        'dropoff': {
            'locations': dropoff_locations,
            'counts': dropoff_counts
        },
        'total_registros': len(df_filtrado)
    })


@app.route('/api/metadata')
def get_metadata():
    df = cargar_datos()

    # Valores únicos para filtros
    vendor_ids = sorted(df['VendorID'].dropna().unique().tolist()) if 'VendorID' in df.columns else [1, 2]
    payment_types = sorted(df['payment_type'].dropna().unique().tolist()) if 'payment_type' in df.columns else [1, 2, 3,
                                                                                                                4]

    # Fechas mínima y máxima
    if 'tpep_pickup_datetime' in df.columns:
        min_date = df['tpep_pickup_datetime'].min().strftime('%Y-%m-%d')
        max_date = df['tpep_pickup_datetime'].max().strftime('%Y-%m-%d')
    else:
        min_date = '2021-01-01'
        max_date = '2021-12-31'

    return jsonify({
        'vendor_ids': vendor_ids,
        'payment_types': payment_types,
        'date_range': {
            'min': min_date,
            'max': max_date
        },
        'total_registros': len(df)
    })


@app.route('/api/debug_filtros')
def debug_filtros():
    """Endpoint para debug de filtros"""
    df = cargar_datos()
    args = request.args

    info = {
        'filtros_recibidos': dict(args),
        'datos_originales': {
            'total_registros': len(df),
            'vendor_ids': sorted(df['VendorID'].unique().tolist()) if 'VendorID' in df.columns else [],
            'payment_types': sorted(df['payment_type'].unique().tolist()) if 'payment_type' in df.columns else []
        },
        'datos_filtrados': {}
    }

    # Aplicar filtros
    df_filtrado = aplicar_filtros(df, args)
    info['datos_filtrados'] = {
        'total_registros': len(df_filtrado),
        'ejemplo_fechas': df_filtrado['tpep_pickup_datetime'].head(3).astype(str).tolist() if len(
            df_filtrado) > 0 else []
    }

    return jsonify(info)


if __name__ == '__main__':
    print("=" * 60)
    print("🚕 DASHBOARD NYC TAXI - FILTROS ACTIVADOS")
    print("=" * 60)
    print(f"Archivo de datos: {CSV_PATH}")
    print(f"¿Archivo existe? {os.path.exists(CSV_PATH)}")

    # Cargar datos iniciales
    df_test = cargar_datos()
    print(f"\n📊 Datos cargados: {len(df_test)} registros")
    print(f"📅 Rango de fechas: {df_test['tpep_pickup_datetime'].min()} a {df_test['tpep_pickup_datetime'].max()}")
    print(f"🔢 Vendor IDs: {sorted(df_test['VendorID'].unique().tolist()) if 'VendorID' in df_test.columns else 'N/A'}")
    print(
        f"💳 Tipos de pago: {sorted(df_test['payment_type'].unique().tolist()) if 'payment_type' in df_test.columns else 'N/A'}")

    print("\n" + "=" * 60)
    print("🌐 Servidor iniciando en http://localhost:5000")
    print("🔧 Debug filtros: http://localhost:5000/api/debug_filtros")
    print("=" * 60)

    app.run(debug=True, port=5000)