#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Sincronización entre Ordenadores
===========================================

Este script facilita la sincronización del repositorio entre
el ordenador principal y el portátil.

Uso:
    python sync.py pull    # Descargar cambios del ordenador principal
    python sync.py push    # Subir cambios al ordenador principal
    python sync.py status  # Ver estado de sincronización
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
        print(f"\n🔄 {description}...")

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
        print(f"❌ Error: {result.stderr}")
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


def sync_pull():
    """Descarga cambios del repositorio privado (desarrollo)."""
    print("=" * 60)
    print("📥 DESCARGANDO CAMBIOS DEL ORDENADOR PRINCIPAL")
    print("=" * 60)

    # Verificar estado actual
    run_command("git status", "Verificando estado actual")

    # Fetch de desarrollo
    if not run_command("git fetch desarrollo", "Descargando cambios"):
        return False

    # Pull de desarrollo
    if not run_command("git pull desarrollo main", "Aplicando cambios"):
        print("\n⚠️  Si hay conflictos, resuélvelos manualmente y luego:")
        print("    git add .")
        print("    git commit -m 'Resolver conflictos'")
        return False

    print("\n✅ Sincronización completada exitosamente")
    return True


def sync_push():
    """Sube cambios al repositorio privado (desarrollo)."""
    print("=" * 60)
    print("📤 SUBIENDO CAMBIOS AL ORDENADOR PRINCIPAL")
    print("=" * 60)

    # Verificar si hay cambios
    result = subprocess.run(
        "git status --porcelain",
        shell=True,
        capture_output=True,
        text=True
    )

    if result.stdout.strip():
        print("⚠️  Tienes cambios sin commitear:")
        run_command("git status", "")

        respuesta = input("\n¿Quieres commitear estos cambios ahora? (s/n): ")
        if respuesta.lower() == 's':
            run_command("git add .", "Agregando archivos")
            mensaje = input("Mensaje del commit: ")
            if not run_command(f'git commit -m "{mensaje}"', "Creando commit"):
                return False
        else:
            print("❌ Cancelado. Commitea tus cambios primero.")
            return False

    # Push a desarrollo
    if not run_command("git push desarrollo main", "Subiendo cambios"):
        return False

    print("\n✅ Cambios subidos exitosamente")
    return True


def sync_status():
    """Muestra el estado de sincronización."""
    print("=" * 60)
    print("📊 ESTADO DE SINCRONIZACIÓN")
    print("=" * 60)

    has_origin, has_desarrollo = check_remotes()

    print("\n📍 Remotos configurados:")
    if has_origin:
        print("  ✅ origin (público)")
    else:
        print("  ❌ origin (NO configurado)")

    if has_desarrollo:
        print("  ✅ desarrollo (privado)")
    else:
        print("  ❌ desarrollo (NO configurado)")

    print("\n📂 Estado local:")
    run_command("git status", "")

    if has_desarrollo:
        print("\n🔄 Comparación con desarrollo:")
        run_command("git fetch desarrollo", "Actualizando información")
        run_command(
            "git log --oneline desarrollo/main..HEAD",
            "Commits locales no subidos"
        )
        run_command(
            "git log --oneline HEAD..desarrollo/main",
            "Commits en desarrollo no descargados"
        )


def main():
    """Función principal."""
    if len(sys.argv) < 2:
        print("Uso: python sync.py [pull|push|status]")
        print()
        print("Comandos:")
        print("  pull   - Descargar cambios del ordenador principal")
        print("  push   - Subir cambios al ordenador principal")
        print("  status - Ver estado de sincronización")
        sys.exit(1)

    comando = sys.argv[1].lower()

    # Verificar que estamos en un repositorio git
    if not Path(".git").exists():
        print("❌ Error: No estás en un repositorio git")
        sys.exit(1)

    # Verificar remotos
    has_origin, has_desarrollo = check_remotes()

    if not has_desarrollo:
        print("⚠️  El remoto 'desarrollo' no está configurado.")
        print("Configúralo con:")
        print("  git remote add desarrollo https://github.com/TodoEconometria/ejercicios-bigdata-profesor.git")
        sys.exit(1)

    # Ejecutar comando
    if comando == "pull":
        sync_pull()
    elif comando == "push":
        sync_push()
    elif comando == "status":
        sync_status()
    else:
        print(f"❌ Comando desconocido: {comando}")
        sys.exit(1)


if __name__ == "__main__":
    main()
