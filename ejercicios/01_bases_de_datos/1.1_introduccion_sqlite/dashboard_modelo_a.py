"""
Dashboard Estilo Trading para el Modelo A (Versión Refinada)

Este dashboard utiliza un diseño oscuro y gráficos financieros simplificados
para visualizar los datos de la tienda.

Ejecutar con:
streamlit run ejercicios/01_bases_de_datos/1.1_introduccion_sqlite/dashboard_modelo_a.py
"""

import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go

# --- CONFIGURACIÓN DE LA PÁGINA (MODO DARK) ---
st.set_page_config(
    page_title="Market Terminal - Modelo A",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    .explanation-box {
        background-color: #1e2130;
        border-left: 5px solid #00ff00;
        padding: 15px;
        border-radius: 5px;
        margin-top: 10px;
        margin-bottom: 20px;
        font-size: 0.9em;
    }
    .conclusion-box {
        background-color: #262730;
        border: 1px solid #4e5d6c;
        padding: 20px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- RUTAS ---
RUTA_BASE = Path(__file__).parent
DB_MODELO_A = RUTA_BASE / "tienda_modelo_a.db"

# --- FUNCIÓN DE CARGA DE DATOS ---
@st.cache_data
def cargar_datos_unificados(db_path):
    if not db_path.exists():
        return None

    with sqlite3.connect(db_path) as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = cursor.fetchall()

        lista_dfs = []

        for tabla in tablas:
            nombre_tabla = tabla[0]
            if nombre_tabla.startswith("sqlite_"):
                continue

            try:
                df = pd.read_sql_query(f"SELECT * FROM '{nombre_tabla}'", conexion)
                df.columns = [c.lower() for c in df.columns]
                df['categoria'] = nombre_tabla.replace('_', ' ').title()

                if 'price' not in df.columns: df['price'] = 0
                df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0)

                if 'name' not in df.columns: df['name'] = f"Item en {nombre_tabla}"

                cols_interes = ['name', 'price', 'categoria']
                lista_dfs.append(df[cols_interes])

            except Exception as e:
                print(f"Error: {e}")

        if lista_dfs:
            return pd.concat(lista_dfs, ignore_index=True)
        else:
            return pd.DataFrame()

# --- INTERFAZ PRINCIPAL ---

st.title("📈 Market Terminal: Componentes PC")
st.markdown("Análisis financiero de componentes de hardware.")

df_total = cargar_datos_unificados(DB_MODELO_A)

if df_total is not None and not df_total.empty:

    # --- KPI ROW ---
    col1, col2, col3, col4 = st.columns(4)
    
    total_prods = len(df_total)
    avg_price = df_total['price'].mean()
    max_price = df_total['price'].max()
    
    col1.metric("MARKET CAP (Items)", f"{total_prods}", delta="Live")
    col2.metric("INDEX PRICE (Promedio)", f"${avg_price:.2f}", delta=f"+{(avg_price*0.05):.2f}")
    col3.metric("ALL TIME HIGH (Máximo)", f"${max_price:.2f}", delta="High Volatility")
    col4.metric("SECTORS (Categorías)", f"{df_total['categoria'].nunique()}")

    st.divider()

    # --- GRÁFICO 1: LIVE TICKER (TOP 5) ---
    st.header("1. 📊 Live Ticker: Top 5 Sectores 'Blue Chip'")
    st.info("👉 Dale al **Play (▶)** para ver la simulación de precios de las categorías más valiosas.")

    # 1. Identificar las Top 5 categorías por precio promedio
    top_5_categorias = df_total.groupby('categoria')['price'].mean().nlargest(5).index.tolist()
    
    # 2. Filtrar el DataFrame
    df_top5 = df_total[df_total['categoria'].isin(top_5_categorias)].copy()
    
    # 3. Preparar datos para animación (ordenar por precio)
    df_top5 = df_top5.sort_values(['categoria', 'price'])
    df_top5['volumen_simulado'] = df_top5.groupby('categoria').cumcount()

    fig_line = px.line(
        df_top5,
        x="volumen_simulado",
        y="price",
        animation_frame="categoria", 
        markers=True,
        title="Tendencia de Precios: Top 5 Categorías Premium",
        labels={'price': 'Precio Cotizado', 'volumen_simulado': 'Transacción'},
        template="plotly_dark"
    )

    fig_line.update_traces(line=dict(color='#00ff00', width=3), marker=dict(size=8, color='white'))
    fig_line.update_layout(
        yaxis=dict(range=[0, df_top5['price'].max() * 1.1]),
        xaxis=dict(showgrid=False, title="Secuencia de Productos"),
        plot_bgcolor='#0e1117',
        paper_bgcolor='#0e1117'
    )
    fig_line.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1500

    st.plotly_chart(fig_line, use_container_width=True)

    st.markdown("""
    <div class="explanation-box">
    <b>💡 Explicación del Gráfico:</b><br>
    Esta animación simula un "ticker" de bolsa mostrando solo las <b>5 categorías más costosas</b> (Blue Chips). 
    La línea verde traza el precio de cada producto individual dentro de esa categoría, permitiéndote ver 
    cómo fluctúa el valor desde los modelos económicos hasta los topes de gama en tiempo real.
    </div>
    """, unsafe_allow_html=True)


    # --- GRÁFICO 2: VOLATILIDAD (BOX PLOT) ---
    st.header("2. 📦 Análisis de Distribución y Volatilidad")
    
    # Usamos Box Plot que es más claro que las velas
    fig_box = px.box(
        df_total, 
        x="categoria", 
        y="price",
        color="categoria",
        title="Rango de Precios por Categoría (Diagrama de Caja)",
        template="plotly_dark",
        points="outliers" # Mostrar puntos atípicos
    )
    
    fig_box.update_layout(showlegend=False, height=500)
    st.plotly_chart(fig_box, use_container_width=True)

    st.markdown("""
    <div class="explanation-box">
    <b>💡 Explicación del Gráfico:</b><br>
    Este gráfico muestra la "salud" de precios de cada sector:
    <ul>
        <li><b>La Caja:</b> Representa el rango de precios "normal" (donde cae el 50% de los productos).</li>
        <li><b>La Línea dentro de la caja:</b> Es la mediana (el precio central).</li>
        <li><b>Los Puntos sueltos:</b> Son "Outliers" (valores atípicos), productos inusualmente caros o baratos que se salen de la norma.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)


    # --- GRÁFICO 3: TOP 10 PRODUCTOS ---
    st.header("3. 🏆 Top 10 Activos Más Valiosos")
    
    top_10 = df_total.nlargest(10, 'price').sort_values('price', ascending=True) # Ascendente para que el mayor quede arriba en barra H
    
    fig_bar = px.bar(
        top_10,
        x='price',
        y='name',
        orientation='h',
        color='price',
        color_continuous_scale='Greens', # Escala de verdes tipo dinero
        text='price',
        title="Ranking de los 10 Productos Más Costosos",
        template="plotly_dark"
    )
    fig_bar.update_traces(texttemplate='$%{text:.2f}', textposition='outside')
    fig_bar.update_layout(xaxis_title="Precio (USD)", yaxis_title="Producto")
    
    st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("""
    <div class="explanation-box">
    <b>💡 Explicación del Gráfico:</b><br>
    Un listado directo de los "activos" con mayor valoración en el inventario. 
    Generalmente dominado por Tarjetas de Video (GPUs) y Procesadores (CPUs) de gama extrema.
    </div>
    """, unsafe_allow_html=True)


    # --- CONCLUSIONES GENERALES ---
    st.header("📑 Conclusiones del Mercado")
    
    # Calcular categoría más cara y más barata
    cat_cara = df_total.groupby('categoria')['price'].mean().idxmax()
    cat_barata = df_total.groupby('categoria')['price'].mean().idxmin()
    
    st.markdown(f"""
    <div class="conclusion-box">
    <h3>Resumen Ejecutivo</h3>
    <ul>
        <li><b>Sector Dominante:</b> La categoría <b>{cat_cara}</b> presenta el precio promedio más alto, indicando que es el componente que requiere mayor inversión por parte del usuario.</li>
        <li><b>Oportunidad de Entrada:</b> El sector <b>{cat_barata}</b> tiene los costos más bajos, actuando como productos de entrada o commodities.</li>
        <li><b>Volatilidad:</b> Observando el gráfico de cajas, categorías como <b>Video Card</b> suelen tener una dispersión enorme (cajas muy largas), lo que significa que hay opciones para todos los bolsillos, pero los modelos premium son extremadamente costosos.</li>
        <li><b>Concentración de Valor:</b> El Top 10 revela que unos pocos componentes específicos pueden costar más que una PC completa de gama media, destacando el nicho de mercado "entusiasta".</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

else:
    st.error("Base de datos no encontrada.")
