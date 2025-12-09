import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from flask import Flask, render_template

# --- CONFIGURACIÓN ---
app = Flask(__name__)
DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'datos', 'taxi_limpio.csv'))

# --- CARGA Y LIMPIEZA DE DATOS ---
def cargar_y_preparar_datos():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"No se encontró el archivo de datos en: {DATA_PATH}")
    
    df = pd.read_csv(DATA_PATH, low_memory=False, parse_dates=['tpep_pickup_datetime', 'tpep_dropoff_datetime'])
    
    df = df.dropna(subset=['trip_distance', 'fare_amount', 'passenger_count', 'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'tip_amount', 'total_amount'])
    
    df['duracion_minutos'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60
    df['dia_semana'] = df['tpep_pickup_datetime'].dt.day_name()
    
    df = df[(df['trip_distance'] > 0) & (df['trip_distance'] < 50)]
    df = df[(df['fare_amount'] > 0) & (df['fare_amount'] < 200)]
    df = df[(df['duracion_minutos'] > 0) & (df['duracion_minutos'] < 120)]
    df = df[(df['passenger_count'] > 0) & (df['passenger_count'] < 7)]
    df = df[(df['tip_amount'] >= 0) & (df['tip_amount'] < 50)]
    df = df[(df['total_amount'] > 0) & (df['total_amount'] < 250)]
    
    return df

df_global = cargar_y_preparar_datos()

def obtener_muestra(df, n_muestras=5000):
    if len(df) > n_muestras:
        return df.sample(n=n_muestras, random_state=42)
    return df

# --- FUNCIONES PARA CREAR GRÁFICOS ---
# (Las funciones de los gráficos no cambian)
def crear_grafico_distribucion_distancia(df_sample):
    fig = px.histogram(df_sample, x="trip_distance", nbins=50, title="1. Distribución de Distancias")
    return fig.to_html(full_html=False, include_plotlyjs='cdn')

def crear_grafico_distribucion_tarifa(df_sample):
    fig = px.histogram(df_sample, x="fare_amount", nbins=50, title="2. Distribución de Tarifas")
    return fig.to_html(full_html=False, include_plotlyjs=False)

def crear_grafico_pasajeros_por_viaje(df_sample):
    pasajeros_counts = df_sample['passenger_count'].value_counts().sort_index()
    fig = px.bar(pasajeros_counts, x=pasajeros_counts.index, y=pasajeros_counts.values, title="3. Pasajeros por Viaje")
    fig.update_xaxes(title_text='Cantidad de Pasajeros')
    fig.update_yaxes(title_text='Número de Viajes')
    return fig.to_html(full_html=False, include_plotlyjs=False)

def crear_grafico_duracion_por_dia(df_sample):
    dias_ordenados = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    df_sample['dia_semana'] = pd.Categorical(df_sample['dia_semana'], categories=dias_ordenados, ordered=True)
    fig = px.box(df_sample.sort_values('dia_semana'), x="dia_semana", y="duracion_minutos", title="4. Duración del Viaje por Día de la Semana")
    fig.update_xaxes(title_text='Día de la Semana')
    fig.update_yaxes(title_text='Duración (minutos)')
    return fig.to_html(full_html=False, include_plotlyjs=False)

def crear_grafico_distancia_vs_tarifa(df_sample):
    fig = px.scatter(df_sample, x="trip_distance", y="fare_amount", opacity=0.5, title="5. Relación Distancia vs. Tarifa")
    fig.update_xaxes(title_text='Distancia (millas)')
    fig.update_yaxes(title_text='Tarifa ($)')
    return fig.to_html(full_html=False, include_plotlyjs=False)

def crear_grafico_correlacion(df_sample):
    columnas_numericas = ['trip_distance', 'fare_amount', 'passenger_count', 'duracion_minutos', 'tip_amount', 'total_amount']
    df_corr = df_sample[columnas_numericas].corr()
    fig = go.Figure(data=go.Heatmap(z=df_corr.values, x=df_corr.columns, y=df_corr.index, colorscale='Viridis', colorbar_title='Correlación'))
    fig.update_layout(title='6. Matriz de Correlación entre Variables Numéricas', xaxis_showgrid=False, yaxis_showgrid=False, xaxis_nticks=len(columnas_numericas), yaxis_nticks=len(columnas_numericas))
    return fig.to_html(full_html=False, include_plotlyjs=False)

# --- RUTA PRINCIPAL DEL DASHBOARD ---
@app.route("/")
def dashboard():
    df = df_global
    
    # --- 1. CÁLCULO DE ESTADÍSTICAS DETALLADAS ---
    desc_stats = df[['trip_distance', 'fare_amount', 'duracion_minutos']].describe()
    
    estadisticas = {
        'total_viajes': f"{len(df):,}",
        'resumen_distancia': {
            'mean': f"{desc_stats.loc['mean', 'trip_distance']:.2f}",
            'median': f"{df['trip_distance'].median():.2f}",
            'min': f"{desc_stats.loc['min', 'trip_distance']:.2f}",
            'max': f"{desc_stats.loc['max', 'trip_distance']:.2f}",
            'std': f"{desc_stats.loc['std', 'trip_distance']:.2f}"
        },
        'resumen_tarifa': {
            'mean': f"{desc_stats.loc['mean', 'fare_amount']:.2f}",
            'median': f"{df['fare_amount'].median():.2f}",
            'min': f"{desc_stats.loc['min', 'fare_amount']:.2f}",
            'max': f"{desc_stats.loc['max', 'fare_amount']:.2f}",
            'std': f"{desc_stats.loc['std', 'fare_amount']:.2f}"
        },
        'resumen_duracion': {
            'mean': f"{desc_stats.loc['mean', 'duracion_minutos']:.2f}",
            'median': f"{df['duracion_minutos'].median():.2f}",
            'min': f"{desc_stats.loc['min', 'duracion_minutos']:.2f}",
            'max': f"{desc_stats.loc['max', 'duracion_minutos']:.2f}",
            'std': f"{desc_stats.loc['std', 'duracion_minutos']:.2f}"
        }
    }

    # --- 2. GRÁFICOS ---
    df_muestra = obtener_muestra(df)
    
    grafico1 = crear_grafico_distribucion_distancia(df_muestra)
    grafico2 = crear_grafico_distribucion_tarifa(df_muestra)
    grafico3 = crear_grafico_pasajeros_por_viaje(df_muestra)
    grafico4 = crear_grafico_duracion_por_dia(df_muestra)
    grafico5 = crear_grafico_distancia_vs_tarifa(df_muestra)
    grafico6 = crear_grafico_correlacion(df_muestra)

    # --- 3. ENVIAR DATOS A LA PLANTILLA ---
    return render_template("index.html",
                           estadisticas=estadisticas,
                           grafico1=grafico1,
                           grafico2=grafico2,
                           grafico3=grafico3,
                           grafico4=grafico4,
                           grafico5=grafico5,
                           grafico6=grafico6)

if __name__ == "__main__":
    app.run(debug=True)
