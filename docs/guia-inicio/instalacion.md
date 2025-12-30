# Instalacion de Herramientas

Esta guia te llevara paso a paso por la instalacion de todas las herramientas necesarias para el curso.

## Requisitos del Sistema

!!! info "Requisitos Minimos"
    - **RAM:** 8GB
    - **Espacio en disco:** 20GB
    - **Procesador:** i5 o equivalente
    - **Sistema Operativo:** Windows 10+, macOS 10.14+, o Linux (Ubuntu 20.04+)

!!! success "Requisitos Recomendados"
    - **RAM:** 16GB
    - **Espacio en disco:** 50GB SSD
    - **Procesador:** i7 o equivalente
    - **Sistema Operativo:** Ultimo sistema operativo disponible

---

## Paso 1: Instalar Git

Git es el sistema de control de versiones que usaremos para gestionar el codigo.

=== "Windows"

    ### Opcion A: Con winget (Recomendado)

    ```bash
    # Abrir PowerShell o CMD como Administrador
    winget install Git.Git
    ```

    ### Opcion B: Instalador grafico

    1. Descargar desde [git-scm.com](https://git-scm.com/download/win)
    2. Ejecutar el instalador
    3. Usar configuracion por defecto (Next, Next, Next...)

    ### Verificar instalacion

    ```bash
    git --version
    # Debe mostrar: git version 2.x.x
    ```

=== "macOS"

    ### Opcion A: Con Homebrew (Recomendado)

    ```bash
    # Si no tienes Homebrew, instalalo primero:
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    # Instalar Git
    brew install git
    ```

    ### Opcion B: Con Xcode Command Line Tools

    ```bash
    xcode-select --install
    ```

    ### Verificar instalacion

    ```bash
    git --version
    # Debe mostrar: git version 2.x.x
    ```

=== "Linux"

    ### Ubuntu/Debian

    ```bash
    sudo apt-get update
    sudo apt-get install git
    ```

    ### Fedora

    ```bash
    sudo dnf install git
    ```

    ### Arch Linux

    ```bash
    sudo pacman -S git
    ```

    ### Verificar instalacion

    ```bash
    git --version
    # Debe mostrar: git version 2.x.x
    ```

---

## Paso 2: Configurar Git

Una vez instalado Git, debemos configurarlo con tu informacion:

```bash
# Configurar nombre (usa tu nombre real)
git config --global user.name "Tu Nombre Completo"

# Configurar email (usa el mismo email de GitHub)
git config --global user.email "tu@email.com"

# Verificar configuracion
git config --list
```

!!! tip "Consejo"
    El nombre y email que configures aparecera en todos tus commits, asi que usa tu nombre real y el email que usaras en GitHub.

---

## Paso 3: Crear Cuenta en GitHub

GitHub es la plataforma donde alojaremos el codigo.

1. Ve a [github.com](https://github.com)
2. Click en **"Sign Up"**
3. Completa el formulario:
    - Username: Elige un nombre profesional (ej: `juan-garcia`, no `gatito123`)
    - Email: Usa el mismo que configuraste en Git
    - Password: Usa un password seguro
4. Verifica tu email
5. Completa tu perfil (foto, bio opcional)

!!! warning "Importante"
    Usa el **mismo email** que configuraste en Git. Esto vincula tus commits con tu cuenta de GitHub.

---

## Paso 4: Instalar Python

Necesitamos Python 3.11 o superior.

=== "Windows"

    ### Opcion A: Con winget (Recomendado)

    ```bash
    winget install Python.Python.3.11
    ```

    ### Opcion B: Instalador grafico

    1. Descargar desde [python.org](https://www.python.org/downloads/)
    2. **IMPORTANTE:** Marcar "Add Python to PATH"
    3. Ejecutar instalador
    4. Click en "Install Now"

    ### Verificar instalacion

    ```bash
    python --version
    # Debe mostrar: Python 3.11.x

    pip --version
    # Debe mostrar: pip 23.x.x
    ```

=== "macOS"

    ### Con Homebrew (Recomendado)

    ```bash
    brew install python@3.11
    ```

    ### Verificar instalacion

    ```bash
    python3 --version
    # Debe mostrar: Python 3.11.x

    pip3 --version
    # Debe mostrar: pip 23.x.x
    ```

=== "Linux"

    ### Ubuntu/Debian

    ```bash
    sudo apt-get update
    sudo apt-get install python3.11 python3-pip
    ```

    ### Fedora

    ```bash
    sudo dnf install python3.11 python3-pip
    ```

    ### Verificar instalacion

    ```bash
    python3 --version
    # Debe mostrar: Python 3.11.x

    pip3 --version
    # Debe mostrar: pip 23.x.x
    ```

!!! warning "Nota para macOS/Linux"
    En macOS y Linux, usa `python3` y `pip3` en lugar de `python` y `pip`.

---

## Paso 5: Instalar PyCharm (Opcional pero Recomendado)

PyCharm es el IDE que recomendamos para el curso.

### PyCharm Community Edition (Gratis)

=== "Windows"

    1. Descargar desde [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/download/)
    2. Elegir **"Community Edition"** (gratis)
    3. Ejecutar instalador
    4. Seguir pasos del instalador

=== "macOS"

    ```bash
    brew install --cask pycharm-ce
    ```

    O descarga desde [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/download/)

=== "Linux"

    Descarga desde [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/download/)

    O usa Snap:

    ```bash
    sudo snap install pycharm-community --classic
    ```

### Alternativas a PyCharm

Si prefieres otro editor:

- **Visual Studio Code:** Ligero y extensible ([code.visualstudio.com](https://code.visualstudio.com))
- **Jupyter Lab:** Para trabajar con notebooks ([jupyter.org](https://jupyter.org))
- **Sublime Text:** Editor de texto avanzado ([sublimetext.com](https://www.sublimetext.com))

---

## Paso 6: Clonar el Repositorio

Ahora que tienes todo instalado, clona tu fork del repositorio:

!!! warning "Importante"
    Primero debes hacer **Fork** del repositorio en GitHub. Ve a la [guia de Fork y Clone](../git-github/fork-clone.md) para mas detalles.

```bash
# Navega a la carpeta donde quieres guardar el proyecto
cd Documents  # o la carpeta que prefieras

# Clona TU fork (reemplaza TU_USUARIO)
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git

# Entra a la carpeta
cd ejercicios-bigdata

# Conecta con el repositorio original (upstream)
git remote add upstream https://github.com/TodoEconometria/ejercicios-bigdata.git

# Verifica que todo este bien
git remote -v
```

Deberas ver algo asi:

```
origin    https://github.com/TU_USUARIO/ejercicios-bigdata.git (fetch)
origin    https://github.com/TU_USUARIO/ejercicios-bigdata.git (push)
upstream  https://github.com/TodoEconometria/ejercicios-bigdata.git (fetch)
upstream  https://github.com/TodoEconometria/ejercicios-bigdata.git (push)
```

---

## Paso 7: Crear Entorno Virtual

Es una buena practica usar entornos virtuales para cada proyecto:

```bash
# Asegurate de estar en la carpeta del proyecto
cd ejercicios-bigdata

# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# Windows:
.venv\Scripts\activate

# macOS/Linux:
source .venv/bin/activate

# Deberas ver (.venv) al inicio de tu terminal
```

!!! tip "Consejo"
    Siempre activa el entorno virtual antes de trabajar en el proyecto.

---

## Paso 8: Instalar Dependencias

Con el entorno virtual activado, instala las dependencias del proyecto:

```bash
# Actualizar pip
pip install --upgrade pip

# Instalar dependencias del proyecto
pip install -r requirements.txt

# Verificar que todo se instalo correctamente
python -c "import pandas, dask, sqlite3; print('Todo OK!')"
```

Si ves **"Todo OK!"**, estas listo para empezar.

---

## Verificacion Final

Ejecuta estos comandos para verificar que todo esta instalado correctamente:

```bash
# Git
git --version

# Python
python --version

# Pip
pip --version

# Verificar librerias
python -c "import pandas; print(f'Pandas {pandas.__version__}')"
python -c "import dask; print(f'Dask {dask.__version__}')"
```

!!! success "Instalacion Completa"
    Si todos los comandos anteriores funcionaron, estas listo para empezar con [Tu Primer Ejercicio](primer-ejercicio.md)!

---

## Problemas Comunes

??? question "Error: 'python' no se reconoce como comando"

    **Windows:** Python no esta en el PATH.

    Solucion:

    1. Reinstala Python
    2. Marca la opcion **"Add Python to PATH"**
    3. Reinicia la terminal

    **macOS/Linux:** Usa `python3` en lugar de `python`

??? question "Error: Permission denied al instalar con pip"

    **Causa:** Intentando instalar paquetes globalmente sin permisos.

    **Solucion:** Usa un entorno virtual:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # macOS/Linux
    .venv\Scripts\activate      # Windows
    pip install -r requirements.txt
    ```

??? question "Git dice 'fatal: not a git repository'"

    **Causa:** No estas en la carpeta del proyecto.

    **Solucion:**

    ```bash
    # Navega a la carpeta correcta
    cd path/to/ejercicios-bigdata

    # Verifica que estas en la carpeta correcta
    ls -la  # Deberas ver una carpeta .git/
    ```

??? question "PyCharm no detecta el interprete de Python"

    **Solucion:**

    1. Abre PyCharm
    2. File → Settings (Windows/Linux) o PyCharm → Preferences (macOS)
    3. Project → Python Interpreter
    4. Click en el icono de engranaje → Add
    5. Selecciona "Existing environment"
    6. Busca `.venv/Scripts/python.exe` (Windows) o `.venv/bin/python` (macOS/Linux)

---

## Proximos Pasos

Ahora que tienes todo instalado, continua con:

- [Tu Primer Ejercicio](primer-ejercicio.md) - Aprende el flujo de trabajo basico
- [Fork y Clone](../git-github/fork-clone.md) - Entiende como trabajar con Git y GitHub
- [Roadmap del Curso](roadmap.md) - Ve todos los ejercicios disponibles
