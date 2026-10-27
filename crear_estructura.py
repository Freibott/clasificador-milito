"""
Crea el esqueleto vacío del repositorio de la práctica de Minería de Textos.

Solo crea estructura: carpetas, un README con los datos del equipo, un .gitignore,
un requirements.txt y un cuaderno con los títulos de las fases. No contiene nada
del trabajo de la práctica (ni código de descarga, ni NLP, ni modelos).

Uso:  python crear_estructura.py            # en la carpeta actual
      python crear_estructura.py mi_carpeta # en otra carpeta
Es seguro repetirlo: no sobrescribe archivos que ya existan.
"""
import json
import sys
from pathlib import Path

RAIZ = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")

README = """# Clasificador de textos en esperanto: WWI, WWII y Guerra Fría

Práctica de Minería de Textos (CUNEF, 2026/2027).

## Equipo
- Castro Freibott, Pelayo
- Hernández-Echevarría López-Baissón, Pedro
- Narváez Fontcuberta, José María

## Tema
Guerras. Categorías: WWI, WWII y Guerra Fría.

## Estructura
```
clasificador_milito.ipynb   # cuaderno de la práctica
requirements.txt            # librerías
data/raw/                   # datos descargados sin tocar
data/                       # dataset final
```

## Descripción
(por completar)

## Cómo ejecutarlo
(por completar)
"""

GITIGNORE = """__pycache__/
*.pyc
.ipynb_checkpoints/
.venv/
venv/
.env
.DS_Store
"""

# Solo los nombres de las librerías que menciona el enunciado.
REQUIREMENTS = """requests
beautifulsoup4
pandas
scikit-learn
matplotlib
"""


def celda_md(texto: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": texto.splitlines(keepends=True)}


CUADERNO = {
    "cells": [
        celda_md(
            "# Clasificador de textos en esperanto: WWI, WWII y Guerra Fría\n"
            "\n"
            "Minería de Textos · CUNEF · 2026/2027"
        ),
        celda_md("## Fase 1 · Dataset"),
        celda_md("## Fase 2 · NLP"),
        celda_md("## Fase 3 · Clasificación"),
    ],
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python"},
    },
    "nbformat": 4,
    "nbformat_minor": 4,
}


def escribir(ruta: Path, contenido: str) -> None:
    if ruta.exists():
        print(f"  ya existe, no se toca: {ruta}")
        return
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(contenido, encoding="utf-8")
    print(f"  creado: {ruta}")


def main() -> None:
    print(f"Creando estructura en: {RAIZ.resolve()}")
    escribir(RAIZ / "README.md", README)
    escribir(RAIZ / ".gitignore", GITIGNORE)
    escribir(RAIZ / "requirements.txt", REQUIREMENTS)
    escribir(
        RAIZ / "clasificador_milito.ipynb",
        json.dumps(CUADERNO, ensure_ascii=False, indent=1) + "\n",
    )
    # Git no guarda carpetas vacías; .gitkeep hace que data/raw/ llegue al repositorio.
    escribir(RAIZ / "data" / "raw" / ".gitkeep", "")
    print("Listo.")


if __name__ == "__main__":
    main()