// Variables globales para los gráficos
let chartHoras, chartDistancias, chartPickup, chartDropoff;
let filtrosActuales = {};

$(document).ready(function() {
    console.log("🚀 Dashboard NYC Taxi - Inicializando...");

    // Cargar metadatos y configurar
    inicializarDashboard();

    // Configurar eventos
    $('#aplicar_filtros').click(aplicarFiltros);
    $('#limpiar_filtros').click(limpiarFiltros);

    // Agregar eventos de cambio a los filtros
    $('#fecha_inicio, #fecha_fin, #vendor_id, #payment_type').change(function() {
        console.log("Filtro cambiado:", $(this).attr('id'), $(this).val());
    });
});

function inicializarDashboard() {
    console.log("🔄 Inicializando dashboard...");
    $('#status').text('Inicializando...').css('color', 'orange');

    // Cargar metadatos primero
    cargarMetadata()
        .then(() => {
            console.log("✅ Metadata cargada");
            // Cargar dashboard con filtros por defecto
            return cargarDashboardCompleto();
        })
        .then(() => {
            console.log("✅ Dashboard cargado completamente");
            $('#status').text('Listo').css('color', 'green');
        })
        .catch(error => {
            console.error("❌ Error inicializando:", error);
            $('#status').text('Error inicializando').css('color', 'red');
        });
}

function cargarMetadata() {
    return new Promise((resolve, reject) => {
        $.ajax({
            url: '/api/metadata',
            method: 'GET',
            success: function(data) {
                console.log("📋 Metadata recibida:", data);

                // Llenar Vendor IDs
                const vendorSelect = $('#vendor_id');
                vendorSelect.empty();
                vendorSelect.append('<option value="all">Todos los Vendors</option>');

                if (data.vendor_ids && data.vendor_ids.length > 0) {
                    data.vendor_ids.forEach(vendor => {
                        vendorSelect.append(`<option value="${vendor}">Vendor ${vendor}</option>`);
                    });
                }

                // Llenar Payment Types
                const paymentSelect = $('#payment_type');
                paymentSelect.empty();
                paymentSelect.append('<option value="all">Todos los Tipos</option>');

                if (data.payment_types && data.payment_types.length > 0) {
                    data.payment_types.forEach(payment => {
                        let paymentText = '';
                        switch(parseInt(payment)) {
                            case 1: paymentText = 'Crédito'; break;
                            case 2: paymentText = 'Efectivo'; break;
                            case 3: paymentText = 'Sin cargo'; break;
                            case 4: paymentText = 'Disputa'; break;
                            case 5: paymentText = 'Desconocido'; break;
                            case 6: paymentText = 'Anulado'; break;
                            default: paymentText = `Tipo ${payment}`;
                        }
                        paymentSelect.append(`<option value="${payment}">${paymentText}</option>`);
                    });
                }

                // Establecer fechas por defecto
                if (data.date_range) {
                    $('#fecha_inicio').val(data.date_range.min);
                    $('#fecha_fin').val(data.date_range.max);
                    console.log(`📅 Rango de fechas: ${data.date_range.min} a ${data.date_range.max}`);
                }

                console.log(`📊 Total registros: ${data.total_registros || 'N/A'}`);
                resolve(data);
            },
            error: function(xhr, status, error) {
                console.error("❌ Error cargando metadata:", error);
                reject(error);
            }
        });
    });
}

function aplicarFiltros() {
    console.log("🔄 Aplicando filtros...");

    // Mostrar los filtros que se van a aplicar
    const filtros = obtenerFiltros();
    console.log("🎯 Filtros a aplicar:", filtros);

    // Actualizar estado
    $('#status').text('Aplicando filtros...').css('color', 'orange');

    // Guardar filtros actuales
    filtrosActuales = filtros;

    // Cargar dashboard con nuevos filtros
    cargarDashboardCompleto()
        .then(() => {
            console.log("✅ Filtros aplicados correctamente");
            $('#status').text('Filtros aplicados').css('color', 'green');

            // Mostrar mensaje con conteo
            setTimeout(() => {
                const totalViajes = $('#total_viajes').text();
                $('#status').text(`${totalViajes} viajes con filtros actuales`);
            }, 500);
        })
        .catch(error => {
            console.error("❌ Error aplicando filtros:", error);
            $('#status').text('Error aplicando filtros').css('color', 'red');
        });
}

function obtenerFiltros() {
    const filtros = {
        fecha_inicio: $('#fecha_inicio').val(),
        fecha_fin: $('#fecha_fin').val(),
        vendor_id: $('#vendor_id').val(),
        payment_type: $('#payment_type').val()
    };

    console.log("📋 Filtros obtenidos:", filtros);
    return filtros;
}

function cargarDashboardCompleto() {
    const filtros = obtenerFiltros();

    console.log("🔄 Cargando dashboard completo con filtros:", filtros);

    // Cargar todo en paralelo
    return Promise.all([
        cargarEstadisticas(filtros),
        cargarGraficoHoras(filtros),
        cargarGraficoDistancias(filtros),
        cargarGraficoLocations(filtros),
        cargarTablaDatos(filtros)
    ]);
}

function cargarEstadisticas(filtros) {
    return new Promise((resolve, reject) => {
        console.log("📊 Cargando estadísticas...");

        // Agregar timestamp para evitar cache
        const timestamp = new Date().getTime();
        const filtrosConCache = {...filtros, _: timestamp};

        $.ajax({
            url: '/api/estadisticas',
            data: filtrosConCache,
            method: 'GET',
            success: function(data) {
                console.log("📈 Estadísticas recibidas:", data);
                actualizarEstadisticas(data);
                resolve(data);
            },
            error: function(xhr, status, error) {
                console.error("❌ Error cargando estadísticas:", error);
                mostrarErrorEstadisticas();
                reject(error);
            }
        });
    });
}

function actualizarEstadisticas(data) {
    console.log("🔄 Actualizando estadísticas con:", data);

    $('#total_viajes').text(data.total_viajes.toLocaleString());
    $('#ingreso_total').text('$' + data.ingreso_total.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2}));
    $('#distancia_promedio').text(data.distancia_promedio.toFixed(2));
    $('#duracion_promedio').text(data.duracion_promedio.toFixed(2));
    $('#pasajeros_promedio').text(data.pasajeros_promedio.toFixed(2));
    $('#propina_promedio').text('$' + data.propina_promedio.toFixed(2));

    // Agregar tooltip con info adicional
    $('#total_viajes').attr('title', `${data.registros_filtrados || data.total_viajes} registros filtrados`);

    console.log("✅ Estadísticas actualizadas");
}

function mostrarErrorEstadisticas() {
    $('#total_viajes').text('0');
    $('#ingreso_total').text('$0.00');
    $('#distancia_promedio').text('0.00');
    $('#duracion_promedio').text('0.00');
    $('#pasajeros_promedio').text('0.00');
    $('#propina_promedio').text('$0.00');
}

function cargarGraficoHoras(filtros) {
    return new Promise((resolve, reject) => {
        console.log("🕒 Cargando gráfico de horas...");

        const timestamp = new Date().getTime();
        const filtrosConCache = {...filtros, _: timestamp};

        $.ajax({
            url: '/api/distribucion_tiempo',
            data: filtrosConCache,
            method: 'GET',
            success: function(data) {
                console.log("📈 Datos horas recibidos:", data);
                crearGraficoHoras(data);
                resolve(data);
            },
            error: function(xhr, status, error) {
                console.error("❌ Error cargando gráfico de horas:", error);
                reject(error);
            }
        });
    });
}

function crearGraficoHoras(data) {
    const ctx = document.getElementById('graficoHoras');
    if (!ctx) {
        console.error("Canvas 'graficoHoras' no encontrado");
        return;
    }

    // Destruir gráfico anterior si existe
    if (chartHoras) {
        chartHoras.destroy();
    }

    const labels = data.horas.map(h => `${h}:00`);

    chartHoras = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: `Viajes por Hora (Total: ${data.total_registros || data.cantidad.reduce((a, b) => a + b, 0)})`,
                data: data.cantidad,
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 2,
                tension: 0.4,
                fill: true
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: true,
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const hora = context.label;
                            const viajes = context.raw;
                            const porcentaje = data.total_registros > 0 ? (viajes / data.total_registros * 100).toFixed(1) : 0;
                            return `${hora}: ${viajes} viajes (${porcentaje}%)`;
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Número de Viajes'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Hora del Día'
                    }
                }
            }
        }
    });

    console.log("✅ Gráfico de horas creado");
}

function cargarGraficoDistancias(filtros) {
    return new Promise((resolve, reject) => {
        console.log("📏 Cargando gráfico de distancias...");

        const timestamp = new Date().getTime();
        const filtrosConCache = {...filtros, _: timestamp};

        $.ajax({
            url: '/api/distribucion_distancia',
            data: filtrosConCache,
            method: 'GET',
            success: function(data) {
                console.log("📈 Datos distancias recibidos:", data);
                crearGraficoDistancias(data);
                resolve(data);
            },
            error: function(xhr, status, error) {
                console.error("❌ Error cargando gráfico de distancias:", error);
                reject(error);
            }
        });
    });
}

function crearGraficoDistancias(data) {
    const ctx = document.getElementById('graficoDistancias');
    if (!ctx) {
        console.error("Canvas 'graficoDistancias' no encontrado");
        return;
    }

    if (chartDistancias) {
        chartDistancias.destroy();
    }

    chartDistancias = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.categorias,
            datasets: [{
                label: `Viajes por Distancia (mi) (Total: ${data.total_registros || data.cantidad.reduce((a, b) => a + b, 0)})`,
                data: data.cantidad,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.7)',
                    'rgba(54, 162, 235, 0.7)',
                    'rgba(255, 206, 86, 0.7)',
                    'rgba(75, 192, 192, 0.7)',
                    'rgba(153, 102, 255, 0.7)',
                    'rgba(255, 159, 64, 0.7)',
                    'rgba(199, 199, 199, 0.7)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(199, 199, 199, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: true,
                    position: 'top',
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Número de Viajes'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Rango de Distancia (millas)'
                    }
                }
            }
        }
    });

    console.log("✅ Gráfico de distancias creado");
}

function cargarGraficoLocations(filtros) {
    return new Promise((resolve, reject) => {
        console.log("📍 Cargando gráfico de ubicaciones...");

        const timestamp = new Date().getTime();
        const filtrosConCache = {...filtros, _: timestamp};

        $.ajax({
            url: '/api/top_locations',
            data: filtrosConCache,
            method: 'GET',
            success: function(data) {
                console.log("📈 Datos ubicaciones recibidos:", data);
                crearGraficosLocations(data);
                resolve(data);
            },
            error: function(xhr, status, error) {
                console.error("❌ Error cargando gráfico de ubicaciones:", error);
                reject(error);
            }
        });
    });
}

function crearGraficosLocations(data) {
    // Gráfico Pickup
    const ctxPickup = document.getElementById('graficoPickup');
    if (ctxPickup) {
        if (chartPickup) chartPickup.destroy();

        const totalPickups = data.pickup.counts.reduce((a, b) => a + b, 0);

        chartPickup = new Chart(ctxPickup, {
            type: 'doughnut',
            data: {
                labels: data.pickup.locations.map((loc, i) => `Loc ${loc} (${data.pickup.counts[i]})`),
                datasets: [{
                    label: 'Recogidas',
                    data: data.pickup.counts,
                    backgroundColor: [
                        '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF',
                        '#FF9F40', '#8AC926', '#1982C4', '#6A4C93', '#F15BB5'
                    ]
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'right',
                    },
                    title: {
                        display: true,
                        text: `Total: ${totalPickups} recogidas`
                    }
                }
            }
        });
    }

    // Gráfico Dropoff
    const ctxDropoff = document.getElementById('graficoDropoff');
    if (ctxDropoff) {
        if (chartDropoff) chartDropoff.destroy();

        const totalDropoffs = data.dropoff.counts.reduce((a, b) => a + b, 0);

        chartDropoff = new Chart(ctxDropoff, {
            type: 'doughnut',
            data: {
                labels: data.dropoff.locations.map((loc, i) => `Loc ${loc} (${data.dropoff.counts[i]})`),
                datasets: [{
                    label: 'Destinos',
                    data: data.dropoff.counts,
                    backgroundColor: [
                        '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF',
                        '#FF9F40', '#8AC926', '#1982C4', '#6A4C93', '#F15BB5'
                    ]
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'right',
                    },
                    title: {
                        display: true,
                        text: `Total: ${totalDropoffs} destinos`
                    }
                }
            }
        });
    }

    console.log("✅ Gráficos de ubicaciones creados");
}

function cargarTablaDatos(filtros) {
    return new Promise((resolve, reject) => {
        console.log("📋 Cargando tabla de datos...");

        const timestamp = new Date().getTime();
        const filtrosConCache = {...filtros, _: timestamp};

        $.ajax({
            url: '/api/datos',
            data: filtrosConCache,
            method: 'GET',
            success: function(data) {
                console.log("📊 Datos tabla recibidos:", data.length, "registros");
                actualizarTablaDatos(data);
                resolve(data);
            },
            error: function(xhr, status, error) {
                console.error("❌ Error cargando tabla de datos:", error);
                mostrarErrorTabla();
                reject(error);
            }
        });
    });
}

function actualizarTablaDatos(data) {
    const tbody = $('#tablaDatos tbody');
    tbody.empty();

    if (data.length === 0) {
        tbody.append(`
            <tr>
                <td colspan="6" class="text-center text-muted">
                    <i class="bi bi-exclamation-circle"></i> No hay datos para mostrar con los filtros actuales
                </td>
            </tr>
        `);
        return;
    }

    // Mostrar máximo 15 registros en la tabla
    const maxRegistros = Math.min(data.length, 15);

    for (let i = 0; i < maxRegistros; i++) {
        const viaje = data[i];
        const fecha = new Date(viaje.tpep_pickup_datetime);
        const row = `
            <tr>
                <td>${fecha.toLocaleString()}</td>
                <td>${parseFloat(viaje.trip_distance).toFixed(2)}</td>
                <td>${parseFloat(viaje.duracion_minutos).toFixed(2)}</td>
                <td>${viaje.passenger_count}</td>
                <td>$${parseFloat(viaje.total_amount).toFixed(2)}</td>
                <td>$${parseFloat(viaje.tip_amount).toFixed(2)}</td>
            </tr>
        `;
        tbody.append(row);
    }

    if (data.length > maxRegistros) {
        tbody.append(`
            <tr class="text-muted">
                <td colspan="6" class="text-center">
                    <small>Mostrando ${maxRegistros} de ${data.length} registros</small>
                </td>
            </tr>
        `);
    }

    console.log(`✅ Tabla actualizada con ${maxRegistros} registros`);
}

function mostrarErrorTabla() {
    const tbody = $('#tablaDatos tbody');
    tbody.html(`
        <tr>
            <td colspan="6" class="text-center text-danger">
                <i class="bi bi-x-circle"></i> Error cargando datos
            </td>
        </tr>
    `);
}

function limpiarFiltros() {
    console.log("🧹 Limpiando filtros...");

    // Restaurar valores por defecto desde metadata
    cargarMetadata()
        .then(() => {
            console.log("✅ Filtros limpiados");
            $('#status').text('Filtros limpiados').css('color', 'green');

            // Aplicar filtros limpios
            aplicarFiltros();
        })
        .catch(error => {
            console.error("❌ Error limpiando filtros:", error);
            $('#status').text('Error limpiando filtros').css('color', 'red');
        });
}

// Debug: función para verificar filtros
function debugFiltros() {
    console.log("🔍 DEBUG - Filtros actuales:", filtrosActuales);
    console.log("🔍 DEBUG - Valores en formulario:", obtenerFiltros());

    // Probar endpoint de debug
    $.ajax({
        url: '/api/debug_filtros',
        data: filtrosActuales,
        method: 'GET',
        success: function(data) {
            console.log("🔍 DEBUG - Respuesta del servidor:", data);
            alert(`Filtros funcionando:\nOriginal: ${data.datos_originales.total_registros}\nFiltrado: ${data.datos_filtrados.total_registros}`);
        }
    });
}

// Agregar botón de debug (opcional)
$(document).ready(function() {
    // Agregar botón de debug si no existe
    if ($('#debug_btn').length === 0) {
        $('.container').prepend(`
            <button id="debug_btn" class="btn btn-warning btn-sm" style="position: fixed; top: 10px; right: 10px; z-index: 1000;">
                🐛 Debug
            </button>
        `);
        $('#debug_btn').click(debugFiltros);
    }
});

// Actualizar automáticamente cada 2 minutos
setInterval(() => {
    if (Object.keys(filtrosActuales).length > 0) {
        console.log("🔄 Actualización automática...");
        cargarDashboardCompleto()
            .then(() => {
                console.log("✅ Actualización automática completada");
                $('#status').text('Actualizado automáticamente').css('color', 'blue');
                setTimeout(() => {
                    const totalViajes = $('#total_viajes').text();
                    $('#status').text(`${totalViajes} viajes con filtros actuales`);
                }, 2000);
            });
    }
}, 120000); // 2 minutos