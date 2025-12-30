# Comandos Utiles de Git

Cheatsheet de comandos Git para el dia a dia en el curso.

---

## Comandos Basicos

### Configuracion Inicial

```bash
# Configurar nombre
git config --global user.name "Tu Nombre"

# Configurar email
git config --global user.email "tu@email.com"

# Ver configuracion
git config --list

# Ver configuracion especifica
git config user.name
```

### Clonar y Actualizar

```bash
# Clonar tu fork
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git

# Entrar a la carpeta
cd ejercicios-bigdata

# Agregar upstream (repo del profesor)
git remote add upstream https://github.com/TodoEconometria/ejercicios-bigdata.git

# Ver remotes configurados
git remote -v
```

---

## Trabajo Diario

### Estado y Cambios

```bash
# Ver estado actual
git status

# Ver cambios no guardados
git diff

# Ver cambios en un archivo especifico
git diff archivo.py

# Ver historial de commits
git log

# Ver historial resumido
git log --oneline

# Ver cambios de un commit especifico
git show abc123d
```

### Guardar Cambios

```bash
# Agregar archivo especifico
git add archivo.py

# Agregar todos los archivos modificados
git add .

# Agregar solo archivos Python
git add *.py

# Hacer commit
git commit -m "Mensaje descriptivo"

# Hacer commit de archivos ya trackeados (skip add)
git commit -am "Mensaje descriptivo"

# Modificar ultimo commit (antes de push)
git commit --amend -m "Nuevo mensaje"
```

---

## Ramas (Branches)

### Crear y Cambiar

```bash
# Ver ramas locales
git branch

# Ver todas las ramas (incluyendo remotas)
git branch -a

# Crear nueva rama
git branch garcia-ejercicio-01

# Cambiar a una rama
git checkout garcia-ejercicio-01

# Crear y cambiar en un solo comando
git checkout -b garcia-ejercicio-01

# Cambiar a main
git checkout main
```

### Fusionar y Borrar

```bash
# Fusionar una rama en la actual
git merge nombre-rama

# Borrar rama local
git branch -d garcia-ejercicio-01

# Forzar borrado (si tiene cambios sin fusionar)
git branch -D garcia-ejercicio-01

# Borrar rama remota
git push origin --delete garcia-ejercicio-01
```

---

## Sincronizacion

### Descargar Cambios

```bash
# Descargar cambios del profesor (upstream)
git fetch upstream

# Descargar y fusionar de tu fork (origin)
git pull origin main

# Ver diferencias con upstream
git log HEAD..upstream/main

# Ver commits que tu no tienes
git log HEAD..upstream/main --oneline
```

### Sincronizar Fork Completo

```bash
# Workflow completo para sincronizar
git checkout main
git fetch upstream
git merge upstream/main
git push origin main

# O en una sola linea
git checkout main && git fetch upstream && git merge upstream/main && git push origin main
```

### Subir Cambios

```bash
# Subir rama actual a origin
git push origin nombre-rama

# Subir main
git push origin main

# Subir y establecer upstream (primera vez)
git push -u origin nombre-rama

# Despues solo necesitas
git push
```

---

## Resolver Problemas

### Deshacer Cambios

```bash
# Descartar cambios en un archivo (antes de add)
git checkout -- archivo.py

# Descartar todos los cambios no guardados
git checkout -- .

# Quitar archivo del staging (despues de add, antes de commit)
git reset HEAD archivo.py

# Deshacer ultimo commit (mantiene cambios)
git reset --soft HEAD~1

# Deshacer ultimo commit (descarta cambios)
git reset --hard HEAD~1

# Volver a un commit especifico
git reset --hard abc123d
```

!!! danger "Cuidado con --hard"
    `git reset --hard` elimina cambios permanentemente. Usalo solo si estas seguro.

### Stash (Guardar Temporalmente)

```bash
# Guardar cambios temporalmente
git stash

# Guardar con mensaje
git stash save "WIP: trabajando en ejercicio 03"

# Ver lista de stashes
git stash list

# Aplicar ultimo stash
git stash apply

# Aplicar y eliminar ultimo stash
git stash pop

# Aplicar stash especifico
git stash apply stash@{1}

# Eliminar stash
git stash drop stash@{0}

# Eliminar todos los stashes
git stash clear
```

### Conflictos

```bash
# Ver archivos con conflictos
git status

# Despues de resolver manualmente
git add archivo-resuelto.py
git commit -m "Resolver conflicto en archivo"

# Abortar merge con conflictos
git merge --abort

# Ver herramienta de merge
git mergetool
```

---

## Informacion y Busqueda

### Inspeccionar Historial

```bash
# Ver historial detallado
git log --graph --decorate --all

# Ver quien modifico cada linea de un archivo
git blame archivo.py

# Buscar en el historial
git log --grep="palabra clave"

# Ver archivos modificados en cada commit
git log --stat

# Ver cambios de un autor especifico
git log --author="Tu Nombre"
```

### Buscar Codigo

```bash
# Buscar en archivos trackeados
git grep "palabra clave"

# Buscar en archivos Python
git grep "palabra clave" -- "*.py"

# Buscar mostrando numero de linea
git grep -n "palabra clave"
```

---

## Atajos y Aliases

### Configurar Aliases

```bash
# Crear alias para status
git config --global alias.st status

# Crear alias para checkout
git config --global alias.co checkout

# Crear alias para commit
git config --global alias.ci commit

# Crear alias para branch
git config --global alias.br branch

# Alias para log bonito
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

### Usar Aliases

```bash
# En lugar de: git status
git st

# En lugar de: git checkout main
git co main

# En lugar de: git commit -m "mensaje"
git ci -m "mensaje"

# Ver log bonito
git lg
```

---

## Workflow del Curso

### Empezar Nuevo Ejercicio

```bash
# 1. Actualizar main
git checkout main
git pull origin main
git fetch upstream
git merge upstream/main

# 2. Crear rama para ejercicio
git checkout -b garcia-ejercicio-01

# 3. Trabajar...
# ... editar archivos ...

# 4. Guardar trabajo
git add .
git commit -m "Implementar carga de datos SQLite"

# 5. Subir a GitHub
git push -u origin garcia-ejercicio-01
```

### Actualizar Rama de Ejercicio

```bash
# Si el profesor agrego cambios mientras trabajabas
git checkout main
git fetch upstream
git merge upstream/main
git checkout garcia-ejercicio-01
git merge main
git push origin garcia-ejercicio-01
```

### Aplicar Feedback del Profesor

```bash
# 1. Asegurate de estar en tu rama
git checkout garcia-ejercicio-01

# 2. Hacer correcciones
# ... editar archivos ...

# 3. Guardar y subir
git add .
git commit -m "Aplicar feedback: optimizar queries"
git push origin garcia-ejercicio-01

# El PR se actualiza automaticamente
```

---

## Comandos Avanzados

### Cherry Pick

```bash
# Aplicar un commit especifico a la rama actual
git cherry-pick abc123d

# Aplicar sin hacer commit automatico
git cherry-pick -n abc123d
```

### Rebase

```bash
# Rebase rama actual con main
git rebase main

# Rebase interactivo (ultimos 3 commits)
git rebase -i HEAD~3

# Continuar rebase despues de resolver conflictos
git rebase --continue

# Abortar rebase
git rebase --abort
```

!!! warning "Cuidado con Rebase"
    No hagas rebase de commits que ya subiste a GitHub (despues de push).

### Reflog

```bash
# Ver historial de todas las acciones
git reflog

# Recuperar commit "perdido"
git reflog
git checkout abc123d
git checkout -b rama-recuperada
```

---

## Trucos y Tips

### Configuracion Util

```bash
# Colorear output
git config --global color.ui auto

# Editor por defecto (VSCode)
git config --global core.editor "code --wait"

# Guardar credenciales temporalmente
git config --global credential.helper cache

# Guardar credenciales permanentemente (Windows)
git config --global credential.helper wincred

# Ignorar cambios en permisos de archivos
git config core.fileMode false
```

### .gitignore

Crear archivo `.gitignore` en la raiz del proyecto:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv/

# PyCharm
.idea/

# VSCode
.vscode/

# Jupyter
.ipynb_checkpoints/

# Datos grandes
*.csv
*.db
*.parquet
datos/grandes/

# Sistema
.DS_Store
Thumbs.db
```

---

## Errores Comunes y Soluciones

### "fatal: not a git repository"

```bash
# Solucion: Navega a la carpeta del proyecto
cd path/to/ejercicios-bigdata

# Verifica que estas en la carpeta correcta
git status
```

### "Your branch is behind 'origin/main'"

```bash
# Solucion: Actualiza tu rama local
git pull origin main
```

### "CONFLICT (content): Merge conflict"

```bash
# Solucion:
# 1. Abre el archivo con conflicto
# 2. Busca las marcas <<<<<<< ======= >>>>>>>
# 3. Edita manualmente, elige que codigo mantener
# 4. Elimina las marcas
# 5. Guarda y haz commit
git add archivo-resuelto.py
git commit -m "Resolver conflicto"
```

### "Permission denied (publickey)"

```bash
# Solucion: Usa HTTPS en lugar de SSH
git remote set-url origin https://github.com/TU_USUARIO/ejercicios-bigdata.git
```

### "error: failed to push some refs"

```bash
# Causa: Tu rama local esta detras de la remota
# Solucion: Pull primero
git pull origin tu-rama
# Luego push
git push origin tu-rama
```

---

## Comandos de Emergencia

### Recuperar Trabajo Perdido

```bash
# Ver todos los cambios
git reflog

# Volver a un estado anterior
git reset --hard abc123d

# Recuperar archivo borrado
git checkout HEAD -- archivo.py
```

### Limpiar Repositorio

```bash
# Eliminar archivos no trackeados (dry run)
git clean -n

# Eliminar archivos no trackeados (ejecutar)
git clean -f

# Eliminar archivos y carpetas no trackeadas
git clean -fd

# Incluir archivos ignorados en .gitignore
git clean -fdx
```

---

## Recursos Adicionales

### Ayuda Integrada

```bash
# Ayuda general
git help

# Ayuda de un comando especifico
git help commit
git commit --help

# Version corta de ayuda
git commit -h
```

### Links Utiles

- [Git Cheat Sheet (GitHub)](https://education.github.com/git-cheat-sheet-education.pdf)
- [Visualizar Git](https://git-school.github.io/visualizing-git/)
- [Learn Git Branching](https://learngitbranching.js.org/)
- [Oh Shit, Git!?!](https://ohshitgit.com/)

---

## Proximos Pasos

Ahora que conoces los comandos esenciales:

- [Fork y Clone](fork-clone.md) - Setup inicial del proyecto
- [Sincronizar Fork](sincronizar-fork.md) - Mantener tu fork actualizado
- [Crear Pull Requests](pull-requests.md) - Entregar ejercicios
