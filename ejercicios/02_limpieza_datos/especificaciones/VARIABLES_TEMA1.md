# Variables Sugeridas - Tema 1: Evolución Institucional Post-Autoritaria

> **IMPORTANTE:** Estas son **SUGERENCIAS** basadas en literatura académica.
> Debes investigar el codebook QoG completo y seleccionar las variables más apropiadas para tu análisis.

---

## 🎯 Pregunta de Investigación (Genérica)

**¿Cómo evoluciona la calidad institucional en países que transitan desde regímenes autoritarios?**

**Subpreguntas:**
1. ¿La democratización mejora la calidad de gobierno?
2. ¿El crecimiento económico acompaña la transición democrática?
3. ¿Qué factores explican trayectorias divergentes?

---

## 📋 Variables Sugeridas

### Identificadores (OBLIGATORIAS)

| Variable QoG | Descripción | Tipo |
|--------------|-------------|------|
| `cname` | Nombre del país | String |
| `ccodealp` | Código ISO3 (ej: ESP, USA, KAZ) | String |
| `ccode` | Código numérico país | Integer |
| `year` | Año de observación | Integer |

---

### Variables Dependientes: Calidad Democrática

| Variable QoG | Descripción | Rango | Interpretación | Fuente |
|--------------|-------------|-------|----------------|--------|
| `vdem_polyarchy` | Índice de poliarquía | 0-1 | Mayor = más democrático | V-Dem |
| `polity2` | Polity IV Score | -10 a +10 | Mayor = más democrático | Polity IV |
| `fh_pr` | Political Rights | 1-7 | **Menor** = más libertad | Freedom House |
| `fh_cl` | Civil Liberties | 1-7 | **Menor** = más libertad | Freedom House |
| `fh_status` | Status | Free/Partly/Not Free | Categórica | Freedom House |

**⚠️ Nota:** Freedom House está invertido (valores bajos = más libertad).

---

### Variables Independientes: Calidad Institucional

| Variable QoG | Descripción | Rango | Interpretación | Fuente |
|--------------|-------------|-------|----------------|--------|
| `ti_cpi` | Índice percepción corrupción | 0-100 | Mayor = **menos** corrupto | Transparency Int. |
| `icrg_qog` | Quality of Government | 0-1 | Mayor = mejor calidad | ICRG |
| `wbgi_cce` | Control de corrupción | -2.5 a +2.5 | Mayor = menos corrupción | World Bank |
| `wbgi_rle` | Rule of Law | -2.5 a +2.5 | Mayor = mejor estado derecho | World Bank |
| `wbgi_rqe` | Calidad regulatoria | -2.5 a +2.5 | Mayor = mejor regulación | World Bank |
| `wbgi_pve` | Estabilidad política | -2.5 a +2.5 | Mayor = más estable | World Bank |

---

### Variables de Control: Desarrollo Económico

| Variable QoG | Descripción | Unidad | Fuente |
|--------------|-------------|--------|--------|
| `wdi_gdppc` | PIB per cápita | USD constantes | World Bank WDI |
| `wdi_gdpgr` | Crecimiento PIB | % anual | World Bank WDI |
| `wdi_gini` | Índice Gini | 0-100 | World Bank WDI |
| `undp_hdi` | Desarrollo humano | 0-1 | UNDP |
| `mad_gdpch` | PIB histórico (Maddison) | USD 1990 | Maddison Project |

---

### Variables de Control: Socioeconómicas

| Variable QoG | Descripción | Unidad | Fuente |
|--------------|-------------|--------|--------|
| `wdi_pop` | Población total | Habitantes | World Bank WDI |
| `wdi_lifexp` | Esperanza de vida | Años | World Bank WDI |
| `wdi_liter` | Alfabetización adultos | % | World Bank WDI |
| `wdi_educ` | Años promedio educación | Años | World Bank WDI |
| `wdi_urban` | Urbanización | % | World Bank WDI |

---

### Variables Contextuales: Régimen y Duración

| Variable QoG | Descripción | Unidad | Fuente |
|--------------|-------------|--------|--------|
| `lied_regdur` | Duración del régimen actual | Años | LIED |
| `vdem_libdem` | Índice democracia liberal | 0-1 | V-Dem |
| `vdem_delibdem` | Democracia deliberativa | 0-1 | V-Dem |
| `gwf_regimetype` | Tipo de régimen | Categórica | GWF |

---

## 🔬 Variables Derivadas a Crear

Además de las variables originales, debes crear:

### 1. Clasificación de Régimen
```python
# Basado en polity2
regime_type = CASE
    WHEN polity2 >= 6 THEN 'Democracia'
    WHEN polity2 >= -5 AND polity2 < 6 THEN 'Híbrido'
    WHEN polity2 < -5 THEN 'Autocracia'
END
```

### 2. Deciles de Desarrollo
```python
# Deciles de PIB per cápita por año
gdp_decile = NTILE(10) OVER (PARTITION BY year ORDER BY wdi_gdppc)
```

### 3. Nivel de Corrupción
```python
# Basado en ti_cpi
corruption_level = CASE
    WHEN ti_cpi >= 70 THEN 'Bajo'
    WHEN ti_cpi >= 40 THEN 'Medio'
    ELSE 'Alto'
END
```

### 4. Cambio Institucional
```python
# Variación de calidad institucional (lag)
institutional_change = icrg_qog(t) - icrg_qog(t-1)
```

---

## 🚀 Cómo Investigar Variables Adicionales

### Opción 1: Codebook QoG (Recomendado)

**Prompt para Claude/ChatGPT:**
```
Estoy trabajando con el dataset Quality of Government (QoG).
Necesito variables sobre calidad democrática e institucional para
analizar transiciones de regímenes autoritarios a democracias.

Según el codebook QoG Standard Time-Series (última versión),
¿qué variables me recomiendas para:

1. Medir calidad democrática (dependiente)
2. Medir calidad institucional (independiente)
3. Variables de control económicas
4. Variables de control socioeconómicas

Por favor, proporciona:
- Nombre exacto de la variable en QoG
- Descripción
- Fuente original
- Rango de valores
- Interpretación (mayor/menor = mejor/peor)

Enfócate en variables con buena cobertura temporal (1990-2023)
y geográfica (>100 países).
```

---

### Opción 2: Búsqueda por Fuente

**Prompts específicos:**

#### Para V-Dem (Varieties of Democracy):
```
Del proyecto V-Dem incluido en QoG, ¿cuáles son las mejores
variables para medir:
- Democracia electoral (polyarchy)
- Democracia liberal
- Instituciones formales vs prácticas
- Corrupción en diferentes niveles de gobierno

Dame nombres exactos de variables V-Dem en QoG (prefijo "vdem_").
```

#### Para World Bank Governance Indicators:
```
De los World Bank Governance Indicators (WGI) en QoG,
¿cuáles son las 6 dimensiones principales y sus nombres
de variables exactos (prefijo "wbgi_")?

Necesito entender:
- Qué mide cada dimensión
- Cómo se interpretan los valores
- Limitaciones conocidas
```

#### Para Transparency International:
```
¿Qué variables de Transparency International están en QoG
(prefijo "ti_") y cuál es la diferencia entre:
- ti_cpi (Corruption Perceptions Index)
- Otras variables TI disponibles

¿Desde qué año hay datos confiables?
```

---

### Opción 3: Búsqueda por Tema

**Prompt temático:**
```
En el dataset QoG, quiero estudiar países de Asia Central
post-soviéticos (Kazajistán, Uzbekistán, Turkmenistán,
Kirguistán, Tayikistán) desde 1991 hasta 2023.

¿Qué variables QoG tienen buena cobertura para esta región
y período, relacionadas con:
1. Transición democrática
2. Calidad institucional
3. Desarrollo económico
4. Recursos naturales (petróleo, gas)

Dame nombres exactos de variables y sus características.
```

---

## 📚 Recursos para Investigación

### Codebooks Oficiales
- **QoG Codebook:** https://www.qogdata.pol.gu.se/data/codebook_std_jan23.pdf
- **V-Dem Codebook:** https://www.v-dem.net/documents/24/codebook_v13.pdf
- **WDI Metadata:** https://databank.worldbank.org/source/world-development-indicators

### Papers de Referencia
- Teorell et al. (2023). "The Quality of Government Standard Dataset"
- Coppedge et al. (2023). "V-Dem Dataset"
- Kaufmann et al. (2010). "The Worldwide Governance Indicators"

### Herramientas Online
- **QoG Explorer:** https://www.qogdata.pol.gu.se/data/qog_std_ts_jan23.csv
- **V-Dem Online:** https://v-dem.net/graphing/graphing-tools/
- **World Bank DataBank:** https://databank.worldbank.org/

---

## ⚠️ Advertencias Importantes

### 1. Cobertura Temporal Variable
No todas las variables tienen datos para todos los años.

**Verifica siempre:**
```python
# ¿Desde qué año hay datos?
df.groupby('year')['ti_cpi'].count().sort_index()

# ¿Qué % de países tienen datos por año?
coverage = df.groupby('year')['ti_cpi'].count() / df.groupby('year')['cname'].count()
```

### 2. Valores Faltantes Estructurales
Algunos países NUNCA tendrán ciertas variables (ej: países sin costa no tienen datos marítimos).

### 3. Cambios Metodológicos
Algunas variables cambian metodología entre años.

**Ejemplo:** ti_cpi cambió de escala 0-10 a 0-100 en 2012.

### 4. Interpretación Inversa
**Cuidado con Freedom House:** valores BAJOS = MÁS libertad.

---

## 🎯 Variables Mínimas Requeridas

Para que tu análisis sea válido, **como mínimo** debes tener:

1. **1 variable dependiente** (calidad democrática)
2. **2-3 variables independientes** (institucionales)
3. **2-3 variables de control** (económicas/socioeconómicas)
4. **Identificadores** (país, año)

---

## 📊 Ejemplo de Panel Data Final

```
| country_code | year | democracy_index | corruption_index | gdp_per_capita | regime_type | gdp_decile |
|--------------|------|-----------------|------------------|----------------|-------------|------------|
| ESP          | 2000 | 0.85            | 70               | 24000          | Democracia  | 8          |
| ESP          | 2001 | 0.86            | 70               | 24500          | Democracia  | 8          |
| KAZ          | 2000 | 0.25            | 30               | 5000           | Autocracia  | 4          |
| KAZ          | 2001 | 0.24            | 28               | 5200           | Autocracia  | 4          |
```

**Esto es PERFECTO para regresiones panel:**
- Fixed Effects (controlar heterogeneidad no observada por país)
- Random Effects (si asumes no hay correlación con regresores)
- Difference-in-Differences (si tienes una "intervención")

---

**¿Dudas?** Consulta el codebook QoG o pregunta en el foro del curso.

**Última actualización:** 2025-12-17
