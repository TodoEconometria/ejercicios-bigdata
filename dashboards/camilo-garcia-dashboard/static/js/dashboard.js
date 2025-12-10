// static/js/dashboard.js - Script adicional para el dashboard

// Función para inicializar todos los gráficos
function initializeCharts() {
    console.log("Inicializando gráficos...");

    // Verificar si Plotly está cargado
    if (typeof Plotly === 'undefined') {
        console.error('Plotly no está cargado');
        setTimeout(initializeCharts, 100); // Reintentar
        return;
    }

    // Intentar renderizar cada gráfico
    const chartIds = ['distanciaChart', 'tarifaChart', 'pasajerosChart', 'horaChart', 'distanciaTarifaChart'];

    chartIds.forEach(chartId => {
        const element = document.getElementById(chartId);
        if (element && element.dataset.graph) {
            try {
                const graphData = JSON.parse(element.dataset.graph);
                Plotly.newPlot(chartId, graphData.data, graphData.layout);
                console.log(`Gráfico ${chartId} inicializado`);
            } catch (e) {
                console.error(`Error inicializando gráfico ${chartId}:`, e);
            }
        }
    });
}

// Esperar a que el DOM esté completamente cargado
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeCharts);
} else {
    initializeCharts();
}

// Función para actualizar un gráfico específico
function updateChart(chartId, graphData) {
    try {
        Plotly.react(chartId, graphData.data, graphData.layout);
    } catch (e) {
        console.error(`Error actualizando gráfico ${chartId}:`, e);
    }
}

// Exportar funciones para uso global
window.dashboard = {
    initializeCharts,
    updateChart,
    formatNumber: function(num) {
        if (num === null || num === undefined) return '0';
        return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }
};