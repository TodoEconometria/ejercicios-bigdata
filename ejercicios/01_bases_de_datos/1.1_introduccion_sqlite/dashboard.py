"""
Dashboard Interactivo para el Análisis de la Tienda de Componentes

Este script utiliza Streamlit, Pandas y Plotly para crear una visualización
interactiva de los datos de la base de datos normalizada (Modelo B).

Para ejecutarlo:
1. Asegúrate de tener las librerías: pip install streamlit pandas plotly
2. En la terminal, ejecuta: streamlit run dashboard.py
"""

import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path
import plotly.express as px

# --- CONFIGURACIÓN DE LA PÁGINA Y RUTAS ---
st.set_page_config(
    page_title="Dashboard de la Tienda de Componentes",
    page_icon="🖥️",
    layout="wide"
)

RUTA_BASE = Path(__file__).parent
DB_MODELO_B = RUTA_BASE / "tienda_modelo_b.db"


# --- CARGA DE DATOS (CON CACHÉ PARA MEJORAR RENDIMIENTO) ---
@st.cache_data
def cargar_datos_completos(db_path):
    """
    Carga los datos de productos, uniéndolos con categorías y fabricantes.
    """
    if not db_path.exists():
        st.error(f"Error: No se encontró la base de datos en '{db_path}'. Asegúrate de haber ejecutado el script del Modelo B.")
        return None

    with sqlite3.connect(db_path) as conexion:
        query = """
        SELECT
            p.nombre AS producto,
            p.precio,
            c.nombre AS categoria,
            f.nombre AS fabricante
        FROM
            productos AS p
        LEFT JOIN
            categorias AS c ON p.categoria_id = c.id
        LEFT JOIN
            fabricantes AS f ON p.fabricante_id = f.id;
        """
        df = pd.read_sql_query(query, conexion)
    return df

# --- INICIO DEL DASHBOARD ---
st.title("🖥️ Dashboard de Análisis de la Tienda de Componentes")
st.markdown("Análisis visual de los datos extraídos de la base de datos normalizada (`tienda_modelo_b.db`).")

# Cargar los datos
df_completo = cargar_datos_completos(DB_MODELO_B)

if df_completo is not None:
    # --- SECCIÓN 1: ANÁLISIS POR CATEGORÍA ---
    st.header("1. Distribución de Productos por Categoría")

    # Cálculo
    df_categorias = df_completo['categoria'].value_counts().reset_index()
    df_categorias.columns = ['Categoría', 'Número de Productos']

    # Gráfico
    fig_cat = px.bar(
        df_categorias,
        x='Categoría',
        y='Número de Productos',
        title="Número de Productos por Categoría",
        labels={'Número de Productos': 'Cantidad de Productos'},
        color='Número de Productos',
        color_continuous_scale=px.colors.sequential.Viridis
    )
    st.plotly_chart(fig_cat, use_container_width=True)

    # Tabla y Conclusión
    col1, col2 = st.columns([1, 1])
    with col1:
        st.dataframe(df_categorias.style.background_gradient(cmap='viridis'))
    with col2:
        st.subheader("Conclusión")
        st.markdown("""
        *   **Observación:** El gráfico y la tabla muestran la cantidad de productos distintos disponibles para cada categoría.
        *   **Análisis:** Categorías como **'Internal Hard Drive'**, **'Case Fan'** y **'Power Supply'** dominan el catálogo, ofreciendo la mayor variedad de opciones a los consumidores.
        *   **Implicación:** Esto puede reflejar una alta demanda o una mayor competencia de fabricantes en estos segmentos del mercado.
        """)
    st.divider()


    # --- SECCIÓN 2: ANÁLISIS POR FABRICANTE ---
    st.header("2. Top 15 Fabricantes por Cantidad de Productos")

    # Cálculo
    df_fabricantes = df_completo['fabricante'].value_counts().nlargest(15).reset_index()
    df_fabricantes.columns = ['Fabricante', 'Número de Productos']

    # Gráfico
    fig_fab = px.bar(
        df_fabricantes.sort_values('Número de Productos', ascending=True),
        x='Número de Productos',
        y='Fabricante',
        orientation='h',
        title="Top 15 Fabricantes con Más Productos en el Catálogo",
        labels={'Número de Productos': 'Cantidad de Productos'},
        color='Número de Productos',
        color_continuous_scale=px.colors.sequential.Plasma
    )
    st.plotly_chart(fig_fab, use_container_width=True)

    # Tabla y Conclusión
    col1, col2 = st.columns([1, 1])
    with col1:
        st.dataframe(df_fabricantes.style.background_gradient(cmap='plasma'))
    with col2:
        st.subheader("Conclusión")
        st.markdown("""
        *   **Observación:** Se visualizan los 15 fabricantes con mayor presencia en la tienda.
        *   **Análisis:** Marcas como **Corsair**, **Cooler Master** y **Noctua** tienen un portafolio de productos significativamente más amplio que sus competidores.
        *   **Implicación:** Estos fabricantes son clave para la tienda y probablemente representan una parte importante de las ventas en múltiples categorías.
        """)
    st.divider()


    # --- SECCIÓN 3: ANÁLISIS DE PRECIOS ---
    st.header("3. Análisis de Distribución de Precios")

    # Filtro interactivo por categoría
    categoria_seleccionada = st.selectbox(
        "Selecciona una categoría para analizar sus precios:",
        options=sorted(df_completo['categoria'].unique())
    )

    df_filtrado = df_completo[df_completo['categoria'] == categoria_seleccionada].dropna(subset=['precio'])

    if not df_filtrado.empty:
        # Gráfico
        fig_precio = px.histogram(
            df_filtrado,
            x='precio',
            nbins=50,
            title=f"Distribución de Precios para la Categoría: {categoria_seleccionada}",
            labels={'precio': 'Rango de Precios (USD)'},
            marginal="box" # Añade un box plot para ver cuartiles
        )
        st.plotly_chart(fig_precio, use_container_width=True)

        # Métricas y Conclusión
        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric("Precio Promedio", f"${df_filtrado['precio'].mean():.2f}")
            st.metric("Precio Mínimo", f"${df_filtrado['precio'].min():.2f}")
            st.metric("Precio Máximo", f"${df_filtrado['precio'].max():.2f}")
        with col2:
            st.subheader("Conclusión")
            st.markdown(f"""
            *   **Observación:** El histograma muestra cómo se agrupan los precios para la categoría **'{categoria_seleccionada}'**.
            *   **Análisis:** La mayoría de los productos se concentran en el rango de precios más bajo, con una 'cola larga' de productos de gama alta y muy costosos.
            *   **Implicación:** El mercado para esta categoría tiene una fuerte base de entrada y gama media, pero también ofrece opciones premium para entusiastas con mayor poder adquisitivo.
            """)
    else:
        st.warning(f"No hay datos de precios disponibles para la categoría '{categoria_seleccionada}'.")
    st.divider()


    # --- SECCIÓN 4: EXPLORADOR DE DATOS ---
    st.header("4. Explorador de Datos Completo")
    st.markdown("Utiliza los filtros para explorar la tabla de productos completa. Puedes ordenar haciendo clic en los encabezados.")
    st.dataframe(df_completo, use_container_width=True, height=500)

else:
    st.warning("No se pudieron cargar los datos para generar el dashboard.")
