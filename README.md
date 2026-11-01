# Clasificador de textos en esperanto: Segunda Guerra Mundial, Guerra Civil Española y Guerras Napoleónicas

Práctica de Minería de Textos (CUNEF, 2026/2027).

<a href="https://colab.research.google.com/github/Freibott/clasificador-milito/blob/main/clasificador_milito.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## Equipo
- Castro Freibott, Pelayo
- Hernández-Echevarría López-Baissón, Pedro
- Narváez Fontcuberta, José María

## Tema
Guerras. Clases y categoría raíz en Vikipedio (Wikipedia en esperanto):

| Clase | Categoría raíz |
|---|---|
| Segunda Guerra Mundial | `Kategorio:Dua Mondmilito` |
| Guerra Civil Española | `Kategorio:Hispana Enlanda Milito` |
| Guerras Napoleónicas | `Kategorio:Napoleonaj militoj` |

El 30/10/2026 sustituyeron a las clases iniciales (WWI, WWII y Guerra Fría), que compartían demasiados artículos entre sí. El motivo se explica en `docs/bitacora_exploracion_fase1.md`. Los estudios con las clases iniciales siguen en el historial de Git (commit `4eeb92c`).

## Estructura
```
clasificador_milito.ipynb   # cuaderno de la práctica
requirements.txt            # librerías
docs/                       # bitácora de exploración y estudio de profundidad (Fase 1)
data/raw/                   # datos descargados sin tocar
data/                       # dataset final
```

## Descripción
Sistema que clasifica textos en esperanto en una de las tres clases anteriores. Se construye en tres fases dentro de un único cuaderno:

1. **Dataset.** Descarga artículos de Vikipedio con su API (categoría raíz + subcategorías a profundidad 1), los parte en párrafos, los limpia y genera `data/dataset.csv` (UTF-8, separador `;`, columnas `text;class`), equilibrado entre clases.
2. **NLP.** Modelo propio de NLP para esperanto, basado en reglas y con una API parecida a la de spaCy (`Doc` / `Token`): tokenizador, lematizador, etiquetado gramatical y stop-words.
3. **Clasificación.** Vectoriza el dataset con el modelo de la Fase 2, entrena un clasificador, lo evalúa (accuracy, F1 macro y matriz de confusión) y clasifica páginas web reales en esperanto.

Las decisiones de diseño de la Fase 1 están justificadas en `docs/`.

## Cómo ejecutarlo
1. Abrir el cuaderno en Google Colab con la insignia "Open in Colab".
2. Elegir el modo en la celda de parámetros:
   - `GENERAR_DATASET = False`: carga el CSV ya generado desde este repositorio (rápido).
   - `GENERAR_DATASET = True`: reconstruye el dataset desde la API de Vikipedio (varios minutos por las pausas entre peticiones).
3. Ejecutar todo (*Entorno de ejecución → Ejecutar todas*). No necesita ficheros locales, GPU ni interacción.

Las librerías están en `requirements.txt` y vienen preinstaladas en Colab. Para ejecutarlo en local: `pip install -r requirements.txt`.

## Fuente y licencia de los datos
Los textos proceden de la Wikipedia en esperanto (eo.wikipedia.org), publicada bajo licencia CC BY-SA.
