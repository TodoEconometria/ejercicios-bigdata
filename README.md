# 🚀 Big Data con Python - De Cero a Producción

> **Aprende a procesar millones de registros sin que tu computadora explote**
> Repositorio educativo completo para dominar Big Data con Python, desde conceptos básicos hasta producción.

[![GitHub stars](https://img.shields.io/github/stars/TodoEconometria/ejercicios-bigdata?style=social)](https://github.com/TodoEconometria/ejercicios-bigdata/stargazers)
[![Documentación](https://img.shields.io/badge/📖_Documentación-Leer-blue?style=for-the-badge)](https://todoeconometria.github.io/ejercicios-bigdata/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conectar-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/juangutierrezconsultor/)
[![Web](https://img.shields.io/badge/Web-TodoEconometria-FF6B35)](https://www.todoeconometria.com)

---

## 📖 Documentación Completa

**Esta es la landing page del repositorio.**
Toda la documentación, guías, ejercicios y tutoriales están en:

### **👉 [todoeconometria.github.io/ejercicios-bigdata](https://todoeconometria.github.io/ejercicios-bigdata/)**

---

## 🚀 Inicio Rápido

¿Primera vez aquí? Sigue estos pasos:

1. **[📚 Guía de Instalación](https://todoeconometria.github.io/ejercicios-bigdata/guia-inicio/instalacion/)** - Configura tu entorno
2. **[🔧 Fork y Clone](https://todoeconometria.github.io/ejercicios-bigdata/git-github/fork-clone/)** - Comienza a trabajar
3. **[📝 Ver Ejercicios](https://todoeconometria.github.io/ejercicios-bigdata/ejercicios/)** - Lista completa

---

## ⚠️ IMPORTANTE: Mantén tu Fork Actualizado

> **Si ya hiciste fork del repositorio, lee esto:**
>
> Durante el curso agregaré **nuevos ejercicios constantemente**. Tu fork NO se actualiza automáticamente.
>
> **👉 [Guía completa de sincronización →](https://todoeconometria.github.io/ejercicios-bigdata/git-github/sincronizar-fork/#el-problema)**
>
> **Resumen rápido:**
> ```bash
> git fetch upstream
> git merge upstream/main
> ```
>
> **¿No funciona?** Lee la guía completa arriba - tiene diagramas paso a paso.

---

## 🎯 ¿Qué Aprenderás?

### El Problema Común

```python
# ❌ Antes: Excel y Pandas básico
df = pd.read_csv("ventas_5_años.csv")  # 💥 MemoryError
df.groupby("región").sum()              # 🐌 20 minutos
```

### La Solución

```python
# ✅ Después: Big Data con Python
df = dd.read_csv("ventas_5_años.csv")  # ⚡ Carga lazy
df.groupby("región").sum().compute()    # 🚀 2 segundos
```

**Resultado:** Procesas 100GB de datos en tu laptop como si fueran 10MB.

---

## 📊 Contenido del Curso

| Módulo | Tecnologías | Nivel |
|--------|-------------|-------|
| **01. Bases de Datos** | SQLite, PostgreSQL | 🟢 Principiante |
| **02. Procesamiento Distribuido** | Dask, Spark | 🟡 Intermedio |
| **03. Almacenamiento Eficiente** | Parquet, HDF5 | 🟡 Intermedio |
| **04. Cloud y Producción** | AWS, Docker | 🔴 Avanzado |

Ver [Roadmap Completo →](https://todoeconometria.github.io/ejercicios-bigdata/guia-inicio/roadmap/)

---

## 🎓 Para Estudiantes

Si eres alumno del curso:

1. **[Cómo Hacer Fork](https://todoeconometria.github.io/ejercicios-bigdata/git-github/fork-clone/)** - Crea tu copia del repo
2. **[Sincronizar Fork](https://todoeconometria.github.io/ejercicios-bigdata/git-github/sincronizar-fork/)** - Mantén tu fork actualizado
3. **[Entregar Ejercicios](https://todoeconometria.github.io/ejercicios-bigdata/git-github/pull-requests/)** - Crea un Pull Request
4. **[FAQ](https://todoeconometria.github.io/ejercicios-bigdata/faq/)** - Preguntas frecuentes

---

## 🛠️ Tecnologías Usadas

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Dask-FDA061?style=for-the-badge&logo=dask&logoColor=white" alt="Dask">
  <img src="https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white" alt="Spark">
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
</p>

---

## 📫 Contacto

- **LinkedIn:** [Juan Gutiérrez](https://www.linkedin.com/in/juangutierrezconsultor/)
- **Web:** [TodoEconometria.com](https://www.todoeconometria.com)
- **Email:** Disponible en mi perfil de LinkedIn

---

## 📄 Licencia

Este material educativo está disponible bajo [MIT License](LICENSE).

---

<p align="center">
  <strong>📖 Toda la documentación está en:</strong><br>
  <a href="https://todoeconometria.github.io/ejercicios-bigdata/">
    <img src="https://img.shields.io/badge/📖_Documentación_Completa-Leer_Ahora-4CAF50?style=for-the-badge" alt="Documentación">
  </a>
</p>
