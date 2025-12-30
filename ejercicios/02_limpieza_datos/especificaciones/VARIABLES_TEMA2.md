# Variables Sugeridas - Tema 2: Recursos Naturales y Desarrollo Regional

> **IMPORTANTE:** Estas son **SUGERENCIAS** basadas en literatura académica.
> Debes investigar el codebook QoG completo y seleccionar las variables más apropiadas para tu análisis.

---

## 🎯 Pregunta de Investigación (Genérica)

**¿La dependencia de recursos naturales afecta el desarrollo económico e institucional?**

**Subpreguntas:**
1. ¿"Maldición de los recursos" (resource curse) es real?
2. ¿Países con más petróleo/gas tienen peor calidad institucional?
3. ¿El acceso a agua y servicios básicos está relacionado con desarrollo?

---

## 📋 Variables Sugeridas

### Identificadores (OBLIGATORIAS)

| Variable QoG | Descripción | Tipo |
|--------------|-------------|------|
| `cname` | Nombre del país | String |
| `ccodealp` | Código ISO3 (ej: SAU, NOR, IRQ) | String |
| `ccode` | Código numérico país | Integer |
| `year` | Año de observación | Integer |

---

### Variables Independientes: Recursos Naturales

#### Hidrocarburos (Petróleo y Gas)

| Variable QoG | Descripción | Unidad | Fuente |
|--------------|-------------|--------|--------|
| `ross_oil_value_2014` | Valor producción petróleo pc | USD 2014 pc | Ross Oil & Gas |
| `ross_gas_value_2014` | Valor producción gas pc | USD 2014 pc | Ross Oil & Gas |
| `ross_oil_production` | Producción petróleo | Barriles/día | Ross |
| `ross_gas_production` | Producción gas | Metros cúbicos | Ross |

#### Rentas de Recursos (World Bank)

| Variable QoG | Descripción | Unidad | Fuente |
|--------------|-------------|--------|--------|
| `wdi_nrrent` | Rentas recursos naturales | % PIB | World Bank WDI |
| `wdi_ores` | Exportaciones minerales | % mercancías | World Bank WDI |
| `wdi_fuel` | Exportaciones combustibles | % mercancías | World Bank WDI |
| `wdi_coal` | Rentas carbón | % PIB | World Bank WDI |
| `wdi_mineral` | Rentas minerales | % PIB | World Bank WDI |

---

### Variables Dependientes: Desarrollo

#### Económico

| Variable QoG | Descripción | Unidad | Fuente |
|--------------|-------------|--------|--------|
| `wdi_gdppc` | PIB per cápita | USD constantes | World Bank WDI |
| `wdi_gdpgr` | Crecimiento PIB | % anual | World Bank WDI |
| `undp_hdi` | Desarrollo humano | 0-1 | UNDP |
| `wdi_gini` | Desigualdad (Gini) | 0-100 | World Bank WDI |

#### Pobreza

| Variable QoG | Descripción | Unidad | Fuente |
|--------------|-------------|--------|--------|
| `wdi_povgap` | Brecha de pobreza | % | World Bank WDI |
| `wdi_poverty` | Tasa de pobreza | % < $1.90/día | World Bank WDI |

---

### Variables de Agua y Agricultura

#### Sector Agrícola

| Variable QoG | Descripción | Unidad | Fuente |
|--------------|-------------|--------|--------|
| `wdi_agrvad` | Valor agregado agricultura | % PIB | World Bank WDI |
| `wdi_agrland` | Tierra agrícola | % superficie | World Bank WDI |
| `wdi_arable` | Tierra cultivable | % superficie | World Bank WDI |
| `wdi_cereal` | Producción cereales | kg/hectárea | World Bank WDI |

#### Acceso a Servicios Básicos

| Variable QoG | Descripción | Unidad | Fuente |
|--------------|-------------|--------|--------|
| `wdi_water` | Acceso agua potable mejorada | % población | World Bank WDI |
| `wdi_sanit` | Acceso saneamiento mejorado | % población | World Bank WDI |
| `wdi_elec` | Acceso electricidad | % población | World Bank WDI |

**⚠️ Nota:** "Mejorada" = fuente protegida de contaminación según OMS.

---

### Variables Mediadoras: Calidad Institucional

| Variable QoG | Descripción | Rango | Interpretación | Fuente |
|--------------|-------------|-------|----------------|--------|
| `ti_cpi` | Percepción corrupción | 0-100 | Mayor = menos corrupto | Transparency Int. |
| `icrg_qog` | Calidad de gobierno | 0-1 | Mayor = mejor | ICRG |
| `wbgi_rqe` | Calidad regulatoria | -2.5 a +2.5 | Mayor = mejor | World Bank |
| `wbgi_cce` | Control corrupción | -2.5 a +2.5 | Mayor = menos corrupción | World Bank |

**Hipótesis:** Recursos → Corrupción → Peor desarrollo.

---

### Variables de Control

#### Demográficas

| Variable QoG | Descripción | Unidad | Fuente |
|--------------|-------------|--------|--------|
| `wdi_pop` | Población total | Habitantes | World Bank WDI |
| `wdi_popgr` | Crecimiento poblacional | % anual | World Bank WDI |
| `wdi_urban` | Urbanización | % | World Bank WDI |
| `wdi_density` | Densidad poblacional | hab/km² | World Bank WDI |

#### Sociales

| Variable QoG | Descripción | Unidad | Fuente |
|--------------|-------------|--------|--------|
| `wdi_lifexp` | Esperanza de vida | Años | World Bank WDI |
| `wdi_liter` | Alfabetización | % adultos | World Bank WDI |
| `wdi_educ` | Años educación | Años promedio | World Bank WDI |

---

## 🔬 Variables Derivadas a Crear

### 1. Dependencia de Recursos
```python
resource_dependence = CASE
    WHEN wdi_nrrent > 20 THEN 'Alta'
    WHEN wdi_nrrent > 10 THEN 'Media'
    WHEN wdi_nrrent > 0 THEN 'Baja'
    ELSE 'Sin datos'
END
```

### 2. Índice de Servicios Básicos
```python
# Promedio de acceso a agua y saneamiento
basic_services_index = (wdi_water + wdi_sanit) / 2.0
```

### 3. Total Hidrocarburos
```python
# Suma de petróleo y gas
oil_gas_total = ross_oil_value_2014 + ross_gas_value_2014
```

### 4. Clasificación de Países Productores
```python
oil_producer = CASE
    WHEN ross_oil_value_2014 > 5000 THEN 'Productor mayor'
    WHEN ross_oil_value_2014 > 1000 THEN 'Productor medio'
    WHEN ross_oil_value_2014 > 0 THEN 'Productor menor'
    ELSE 'No productor'
END
```

### 5. Dependencia Agrícola
```python
agriculture_dependent = CASE
    WHEN wdi_agrvad > 30 THEN True
    ELSE False
END
```

---

## 🚀 Cómo Investigar Variables Adicionales

### Opción 1: Búsqueda por Tema Resource Curse

**Prompt para Claude/ChatGPT:**
```
Estoy investigando la "maldición de los recursos naturales"
(resource curse) usando el dataset Quality of Government (QoG).

Necesito variables para testar:
1. Países ricos en petróleo/gas tienen peor desarrollo institucional
2. Relación entre recursos naturales y desigualdad
3. Impacto de recursos en calidad democrática

¿Qué variables QoG me recomiendas de estas fuentes?
- Ross Oil and Gas Dataset (prefijo "ross_")
- World Bank WDI recursos naturales (prefijo "wdi_")
- Variables de corrupción e instituciones

Dame nombres exactos de variables, rangos, e interpretación.
Enfócate en datos desde 1990 con buena cobertura geográfica.
```

---

### Opción 2: Seguridad Hídrica

**Prompt específico:**
```
Quiero analizar seguridad hídrica y desarrollo usando QoG.

¿Qué variables hay sobre:
1. Acceso a agua potable
2. Saneamiento
3. Estrés hídrico / escasez de agua
4. Agricultura dependiente de agua
5. Conflictos por recursos hídricos

Dame variables QoG exactas (prefijos "wdi_", "fao_", etc.)
y explica cómo se miden.

Contexto: Me interesa Asia Central (Mar de Aral) y región
MENA (Middle East North Africa).
```

---

### Opción 3: Países Específicos

**Prompt geográfico:**
```
Usando QoG, quiero comparar:
- Países petroleros del Golfo (Arabia Saudí, Emiratos, Kuwait)
- Noruega (petróleo pero alto desarrollo)
- Venezuela (petróleo pero crisis)
- Países sin petróleo vecinos (Jordania, España)

¿Qué variables QoG tienen buena cobertura para estos países
desde 1990, relacionadas con:
- Producción hidrocarburos
- Rentas de recursos
- Calidad institucional
- Desarrollo humano

Dame nombres exactos de variables.
```

---

## 📚 Recursos para Investigación

### Datasets de Recursos Naturales

**Ross Oil and Gas Dataset:**
- Incluido en QoG con prefijo `ross_`
- Variables: producción, valor, descubrimientos
- Paper: Ross, M. (2012). "The Oil Curse"

**World Bank Commodity Prices:**
- NO está en QoG directamente
- Pero puedes cruzar con variables WDI
- Fuente: https://www.worldbank.org/commodities

### Literatura Académica

**Resource Curse:**
- Sachs & Warner (1995, 1997): Papers fundacionales
- Ross (2001, 2012): Teoría completa
- Haber & Menaldo (2011): Crítica a la teoría

**Agua y Desarrollo:**
- UN Water Development Report
- FAO AQUASTAT (algunos datos en QoG vía FAO)

### Codebooks
- **QoG Codebook:** Sección "Natural Resources" (página ~450)
- **Ross Codebook:** https://www.rossoilgas.com/

---

## ⚠️ Advertencias Importantes

### 1. Datos Ross: Solo hasta 2014
Variables `ross_*` tienen datos hasta 2014 máximo.

**Para años recientes, usa:**
- `wdi_nrrent` (actualizado anualmente)
- `wdi_fuel` / `wdi_ores` (exportaciones)

### 2. Definiciones Variables
**"Rentas" vs "Producción" vs "Exportaciones":**

- **Rentas (`wdi_nrrent`):** Ganancias después de costos de extracción
- **Producción (`ross_oil_production`):** Cantidad física extraída
- **Exportaciones (`wdi_fuel`):** % de exportaciones de mercancías

### 3. Valores per Cápita
Variables Ross están en **USD per cápita**.

**Ejemplo:** Arabia Saudí tiene alto valor pc porque población pequeña.

### 4. Conversión de Unidades
Petróleo: barriles/día
Gas: metros cúbicos o pies cúbicos

**Verifica unidades en codebook antes de comparar.**

### 5. Cobertura Geográfica Desigual
Países sin recursos naturales tendrán muchos `NULL` en variables Ross.

**Es normal.** NO los elimines del análisis (son tu grupo de control).

---

## 🎯 Variables Mínimas Requeridas

Para análisis válido de resource curse:

1. **1-2 variables de recursos** (ej: `wdi_nrrent`, `ross_oil_value`)
2. **1 variable de desarrollo** (ej: `wdi_gdppc` o `undp_hdi`)
3. **1 variable institucional** (ej: `ti_cpi` o `icrg_qog`)
4. **2-3 controles** (población, educación, región)

---

## 📊 Ejemplo de Panel Data Final

```
| country_code | year | oil_value_pc | nrrent_pct_gdp | gdp_pc | corruption_index | water_access | resource_dep |
|--------------|------|--------------|----------------|--------|------------------|--------------|--------------|
| NOR          | 2010 | 15000        | 12.5           | 85000  | 85               | 100          | Media        |
| NOR          | 2011 | 16000        | 13.0           | 86000  | 86               | 100          | Media        |
| SAU          | 2010 | 8000         | 45.0           | 22000  | 45               | 97           | Alta         |
| SAU          | 2011 | 9000         | 48.0           | 23000  | 44               | 97           | Alta         |
| ESP          | 2010 | 0            | 0.1            | 30000  | 65               | 100          | Baja         |
| ESP          | 2011 | 0            | 0.1            | 29000  | 64               | 100          | Baja         |
```

**Perfecto para:**
- Comparar Noruega (maneja bien recursos) vs Arabia Saudí (resource curse)
- España como control (sin recursos)
- Fixed Effects: controlar características fijas por país
- Interacciones: recursos × instituciones

---

## 🧪 Hipótesis a Testar (Ejemplos)

### H1: Resource Curse Clásico
**H1:** Mayor dependencia de recursos → Menor crecimiento económico

**Variables:**
- DV: `wdi_gdpgr` (crecimiento)
- IV: `wdi_nrrent` (rentas recursos)
- Controls: `wdi_pop`, `wdi_liter`, región

### H2: Instituciones como Mediadora
**H2:** Recursos → Corrupción → Menor desarrollo

**Mediación:**
1. Recursos → Corrupción: `wdi_nrrent` → `ti_cpi`
2. Corrupción → Desarrollo: `ti_cpi` → `wdi_gdppc`

### H3: Servicios Básicos
**H3:** Países agrícolas con bajo acceso a agua tienen peor desarrollo humano

**Variables:**
- DV: `undp_hdi`
- IV: `wdi_water`, `wdi_agrvad`
- Interacción: `wdi_water` × `wdi_agrvad`

---

## 🌍 Regiones de Interés

### Golfo Pérsico (Alta dependencia petróleo)
SAU, ARE, KWT, QAT, BHR, OMN

### América Latina (Minería y petróleo)
VEN, BOL, CHL (cobre), PER, ECU

### Asia Central (Gas y petróleo post-soviético)
KAZ, TKM, UZB

### MENA (Recursos hídricos escasos)
Todos los países Middle East & North Africa

### Control (Sin recursos)
ESP, PRT, ITA (Europa sin recursos)
JPN, KOR (Asia sin recursos)

---

**¿Dudas?** Revisa codebook QoG sección "Natural Resources" o pregunta en el foro.

**Última actualización:** 2025-12-17
