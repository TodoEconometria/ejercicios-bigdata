#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Sincronización para Repositorio del Profesor
======================================================

Este script facilita la sincronización bidireccional entre:
- Repositorio PRIVADO (desarrollo): ejercicios-bigdata-profesor
- Repositorio PUBLICO (origin): ejercicios-bigdata

Flujo de trabajo:
- Trabajas en rama 'desarrollo' del repo privado
- Publicas cambios a rama 'main' del repo público
- Sincronizas entre ordenadores usando el repo privado

Uso:
    python sync.py pull              # Descargar cambios del repo privado
    python sync.py push              # Subir cambios al repo privado
    python sync.py publicar          # Publicar desarrollo → main público
    python sync.py sync-bidireccional # Sincronización completa (pull + push)
    python sync.py status            # Ver estado de sincronización
"""

import subprocess
import sys
import os
from pathlib import Path

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')


def run_command(cmd, description=""):
    """Ejecuta un comando y muestra el resultado."""
    if description:
        print(f"\n[>] {description}...")

    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        if result.stdout.strip():
            print(result.stdout)
        return True
    else:
        print(f"[ERROR] {result.stderr}")
        return False


def check_remotes():
    """Verifica que los remotos estén configurados."""
    result = subprocess.run(
        "git remote -v",
        shell=True,
        capture_output=True,
        text=True
    )

    has_origin = "origin" in result.stdout
    has_desarrollo = "desarrollo" in result.stdout

    return has_origin, has_desarrollo


def get_current_branch():
    """Obtiene la rama actual."""
    result = subprocess.run(
        "git branch --show-current",
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()


def sync_pull():
    """Descarga cambios del repositorio privado (desarrollo)."""
    print("=" * 60)
    print("[PULL] DESCARGANDO CAMBIOS DEL REPO PRIVADO")
    print("=" * 60)

    current_branch = get_current_branch()
    print(f"\n[INFO] Rama actual: {current_branch}")

    # Asegurarse de estar en rama desarrollo
    if current_branch != "desarrollo":
        print("\n[WARN] No estás en la rama 'desarrollo'")
        respuesta = input("¿Cambiar a rama 'desarrollo'? (s/n): ")
        if respuesta.lower() == 's':
            if not run_command("git checkout desarrollo", "Cambiando a rama desarrollo"):
                return False
        else:
            print("[INFO] Continuando en rama actual...")

    # Verificar estado actual
    run_command("git status", "Verificando estado actual")

    # Fetch de desarrollo
    if not run_command("git fetch desarrollo", "Descargando cambios del remoto 'desarrollo'"):
        return False

    # Pull de desarrollo/desarrollo
    if not run_command("git pull desarrollo desarrollo", "Aplicando cambios"):
        print("\n[WARN] Si hay conflictos, resuélvelos manualmente y luego:")
        print("    git add .")
        print("    git commit -m 'Resolver conflictos'")
        return False

    print("\n[OK] Sincronización completada exitosamente")
    return True


def sync_push():
    """Sube cambios al repositorio privado (desarrollo)."""
    print("=" * 60)
    print("[PUSH] SUBIENDO CAMBIOS AL REPO PRIVADO")
    print("=" * 60)

    current_branch = get_current_branch()
    print(f"\n[INFO] Rama actual: {current_branch}")

    # Asegurarse de estar en rama desarrollo
    if current_branch != "desarrollo":
        print("\n[WARN] No estás en la rama 'desarrollo'")
        respuesta = input("¿Cambiar a rama 'desarrollo'? (s/n): ")
        if respuesta.lower() == 's':
            if not run_command("git checkout desarrollo", "Cambiando a rama desarrollo"):
                return False
        else:
            print("[INFO] Continuando en rama actual...")

    # Verificar si hay cambios
    result = subprocess.run(
        "git status --porcelain",
        shell=True,
        capture_output=True,
        text=True
    )

    if result.stdout.strip():
        print("[WARN] Tienes cambios sin commitear:")
        run_command("git status", "")

        respuesta = input("\n¿Quieres commitear estos cambios ahora? (s/n): ")
        if respuesta.lower() == 's':
            run_command("git add .", "Agregando archivos")
            mensaje = input("Mensaje del commit: ")
            if not run_command(f'git commit -m "{mensaje}"', "Creando commit"):
                return False
        else:
            print("[ERROR] Cancelado. Commitea tus cambios primero.")
            return False

    # Push a desarrollo/desarrollo
    if not run_command("git push desarrollo desarrollo", "Subiendo cambios a desarrollo/desarrollo"):
        return False

    print("\n[OK] Cambios subidos exitosamente")
    return True


def sync_publicar():
    """Publica cambios de rama desarrollo a main público vía Pull Request."""
    print("=" * 60)
    print("[PUBLICAR] DESARROLLO -> MAIN PUBLICO (VIA PR)")
    print("=" * 60)

    print("\n[INFO] La rama main está PROTEGIDA - requiere Pull Request")
    print("[INFO] Este comando te guiará en el proceso...\n")

    current_branch = get_current_branch()

    # Verificar que no hay cambios sin commitear
    result = subprocess.run(
        "git status --porcelain",
        shell=True,
        capture_output=True,
        text=True
    )

    if result.stdout.strip():
        print("[ERROR] Tienes cambios sin commitear. Commitea primero.")
        run_command("git status", "")
        return False

    # Asegurarse de estar en desarrollo
    if current_branch != "desarrollo":
        if not run_command("git checkout desarrollo", "Cambiando a rama desarrollo"):
            return False

    # Push desarrollo al remoto privado
    print("[PASO 1/3] Subiendo desarrollo al repo privado...")
    if not run_command("git push desarrollo desarrollo", ""):
        return False

    # Merge local para actualizar main
    print("\n[PASO 2/3] Actualizando tu main local...")
    if not run_command("git checkout main", ""):
        return False

    if not run_command("git merge desarrollo --no-edit", ""):
        print("[ERROR] Error en merge. Resuelve conflictos y vuelve a intentar.")
        run_command("git checkout desarrollo", "")
        return False

    run_command("git checkout desarrollo", "")

    # Instrucciones para publicar
    print("\n[PASO 3/3] Publicar al repo público:")
    print("=" * 60)
    print("\nLa rama main está protegida. Usa UNO de estos métodos:\n")

    print("OPCIÓN A - GitHub Web (MÁS RÁPIDO):")
    print("1. Ve a: https://github.com/TodoEconometria/ejercicios-bigdata-profesor")
    print("2. Click 'Contribute' → 'Open pull request'")
    print("3. Click 'Create pull request' → 'Merge pull request'")

    print("\nOPCIÓN B - Línea de comandos (gh CLI):")
    print("gh pr create --repo TodoEconometria/ejercicios-bigdata \\")
    print("  --base main --head TodoEconometria:desarrollo \\")
    print("  --title 'SYNC: Publicar cambios' --body 'Sync desde desarrollo'")
    print("\nLuego mergear:")
    print("gh pr merge --repo TodoEconometria/ejercicios-bigdata --merge")

    print("\n" + "=" * 60)
    print("[OK] Desarrollo actualizado en repo privado")
    print("[MANUAL] Completa el PASO 3 para publicar al repo público")

    return True


def sync_bidireccional():
    """Sincronización completa: pull + push."""
    print("=" * 60)
    print("[SYNC] SINCRONIZACION BIDIRECCIONAL")
    print("=" * 60)

    print("\n[PASO 1/2] Descargando cambios del repo privado...")
    if not sync_pull():
        print("\n[ERROR] Fallo en pull. Abortando.")
        return False

    print("\n[PASO 2/2] Subiendo cambios al repo privado...")
    if not sync_push():
        print("\n[ERROR] Fallo en push. Abortando.")
        return False

    print("\n[OK] Sincronización bidireccional completada")
    return True


def sync_status():
    """Muestra el estado de sincronización."""
    print("=" * 60)
    print("[STATUS] ESTADO DE SINCRONIZACION")
    print("=" * 60)

    has_origin, has_desarrollo = check_remotes()
    current_branch = get_current_branch()

    print(f"\n[RAMA ACTUAL] {current_branch}")

    print("\n[REMOTOS CONFIGURADOS]")
    if has_origin:
        print("  [OK] origin (publico)")
    else:
        print("  [ERROR] origin (NO configurado)")

    if has_desarrollo:
        print("  [OK] desarrollo (privado)")
    else:
        print("  [ERROR] desarrollo (NO configurado)")

    print("\n[ESTADO LOCAL]")
    run_command("git status", "")

    if has_desarrollo:
        print("\n[COMPARACION CON REPO PRIVADO]")
        run_command("git fetch desarrollo", "Actualizando información")

        print("\n  Commits locales no subidos a desarrollo/desarrollo:")
        run_command(
            "git log --oneline desarrollo/desarrollo..HEAD",
            ""
        )

        print("\n  Commits en desarrollo/desarrollo no descargados:")
        run_command(
            "git log --oneline HEAD..desarrollo/desarrollo",
            ""
        )

    if has_origin:
        print("\n[COMPARACION CON REPO PUBLICO]")
        run_command("git fetch origin", "Actualizando información")

        print("\n  Commits locales no publicados en origin/main:")
        result = subprocess.run(
            "git log --oneline origin/main..main",
            shell=True,
            capture_output=True,
            text=True
        )
        if result.stdout.strip():
            print(result.stdout)
        else:
            print("  (ninguno)")


def main():
    """Función principal."""
    if len(sys.argv) < 2:
        print("Uso: python sync.py [COMANDO]")
        print()
        print("Comandos disponibles:")
        print("  pull              - Descargar cambios del repo privado")
        print("  push              - Subir cambios al repo privado")
        print("  publicar          - Publicar desarrollo -> main publico")
        print("  sync-bidireccional - Sincronizacion completa (pull + push)")
        print("  status            - Ver estado de sincronizacion")
        print()
        print("Flujo típico:")
        print("  1. python sync.py pull           # Descargar cambios")
        print("  2. [Hacer cambios en rama desarrollo]")
        print("  3. python sync.py push           # Subir al repo privado")
        print("  4. python sync.py publicar       # Publicar a repo público")
        sys.exit(1)

    comando = sys.argv[1].lower()

    # Verificar que estamos en un repositorio git
    if not Path(".git").exists():
        print("[ERROR] No estás en un repositorio git")
        sys.exit(1)

    # Verificar remotos
    has_origin, has_desarrollo = check_remotes()

    if not has_desarrollo and comando != "status":
        print("[ERROR] El remoto 'desarrollo' no está configurado.")
        print("Configúralo con:")
        print("  git remote add desarrollo https://github.com/TodoEconometria/ejercicios-bigdata-profesor.git")
        sys.exit(1)

    # Ejecutar comando
    if comando == "pull":
        sync_pull()
    elif comando == "push":
        sync_push()
    elif comando == "publicar":
        sync_publicar()
    elif comando == "sync-bidireccional":
        sync_bidireccional()
    elif comando == "status":
        sync_status()
    else:
        print(f"[ERROR] Comando desconocido: {comando}")
        print("Usa: python sync.py (sin argumentos) para ver la ayuda")
        sys.exit(1)


if __name__ == "__main__":
    main()
