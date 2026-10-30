# Bitácora · Exploración de fuentes para la Fase 1 (Dataset)

**Proyecto:** Clasificador de textos en esperanto (Segunda Guerra Mundial, Guerra Civil Española, Guerras Napoleónicas) · Minería de Textos, CUNEF 2026/2027
**Equipo:** Castro Freibott, Pelayo · Hernández-Echevarría López-Baissón, Pedro · Narváez Fontcuberta, José María
**Fecha de la consulta:** 30/10/2026 · **Fuente:** API de MediaWiki de `eo.wikipedia.org`

> Versión 2. La versión 1 (27/10/2026) exploró las clases iniciales WWI, WWII y Guerra Fría; sigue en el historial de Git (commit `4eeb92c`). Consulta preparada con ayuda de IA y revisada por el equipo.

---

## 1. Por qué cambiamos de clases
Con WWI, WWII y Guerra Fría, el estudio de profundidad (versión 1) encontró **32 artículos compartidos entre clases a profundidad 1** (WWII ∩ Guerra Fría = 21, WWI ∩ WWII = 12, WWI ∩ Guerra Fría = 1), sobre todo en la frontera 1943–1949 (Yalta, Potsdam, Telón de Acero) y en el periodo de entreguerras. Eso mete ruido en las etiquetas y limita la precisión del clasificador, que el profesor señaló como importante.

Exploramos alternativas en Vikipedio (29–30/10). Varias se descartaron por falta de datos:

| Candidata | Categoría en Vikipedio | Párrafos (≥10 palabras) a prof. 1 | Resultado |
|---|---|---:|---|
| Guerra de Vietnam | `Kategorio:Vjetnama milito` | 385 (≈ 260 sin biografías ajenas al tema) | Insuficiente |
| Guerra de Afganistán | sin categoría propia | 85 (mezcla cuatro guerras) | No viable |
| Guerra de Aceh | sin categoría ni artículo | ≈ 0 | No viable |
| Guerra civil china | `Kategorio:Ĉina enlanda milito` | 73 | No viable |
| Guerra de Corea | `Kategorio:Korea milito` | 69 | No viable |
| Guerra Civil Rusa | `Kategorio:Rusia enlanda milito` | 676 | Viable (alternativa) |
| **Guerra Civil Española** | `Kategorio:Hispana Enlanda Milito` | 1.702 | **Elegida** |
| **Guerras Napoleónicas** | `Kategorio:Napoleonaj militoj` | 735 | **Elegida** |

**Clases elegidas:** Segunda Guerra Mundial, Guerra Civil Española y Guerras Napoleónicas.
- Son del mismo tema (guerras), como exige el enunciado. El propio enunciado da como ejemplo válido clases de épocas distintas ("Edad Media, Renacimiento, Edad Contemporánea").
- Dos clases son cercanas: la Guerra Civil Española y la Segunda Guerra Mundial (1936–1945, fascismo, intervención alemana e italiana). Así el problema no es trivial.
- La tercera es de otra época, lo que da margen de precisión.

## 2. Qué se comprobó
Que las tres categorías existen y con qué nombre exacto, cuántas páginas y subcategorías tienen, cuánto miden sus artículos y cuántos aparecen en más de una clase.

## 3. Cómo
- Consultas de solo lectura a la API: `categoryinfo` (tamaño de cada categoría), `categorymembers` (páginas y subcategorías) y `extracts` con `explaintext` (texto plano, un artículo por petición).
- **Recuento completo, no muestra:** se descargaron todas las páginas directas de las tres raíces (132 + 54 + 41).
- Métricas: palabras por artículo (mín/mediana/máx), artículos vacíos y párrafos por artículo (líneas de 10 palabras o más, sin títulos `== … ==`).

## 4. Qué se vio (páginas directas, profundidad 0)

| | Segunda Guerra Mundial | Guerra Civil Española | Guerras Napoleónicas |
|---|---|---|---|
| Categoría | `Kategorio:Dua Mondmilito` | `Kategorio:Hispana Enlanda Milito` | `Kategorio:Napoleonaj militoj` |
| Páginas directas (categoryinfo) | 134 | 54 | 41 |
| Artículos (espacio de nombres 0) | 132 | 54 | 41 |
| Subcategorías | 27 | 4 | 8 |
| Palabras mín / mediana / máx | 12 / 284 / 12.238 | 58 / 386 / 5.050 | 76 / 279 / 1.780 |
| Artículos vacíos | 0 | 0 | 0 |
| Párrafos (≥10 palabras) por artículo | 25,1 | 14,9 | 7,3 |
| Párrafos totales en páginas directas | 3.312 | 802 | 298 |

**Solapes entre páginas directas:** ninguno en los tres pares.

**Estructura:** las Guerras Napoleónicas tienen la mitad de su contenido en subcategorías (Homoj de la Napoleonaj militoj, Milito de Hispana Sendependiĝo…). La Guerra Civil Española incluye subcategorías de posguerra ("Frankismo") y obras ("Verkoj pri…"). La Segunda Guerra Mundial mantiene la subcategoría de posguerra "Sekvoj de la Dua Mondmilito".

## 5. Evaluación
- **Viabilidad: positiva.** Las tres categorías existen y tienen material. Con solo páginas directas, las Guerras Napoleónicas no llegan a 300 párrafos (298), así que hace falta bajar a las subcategorías (ver `docs/estudio_profundidad_fase1.md`).
- **Desequilibrio:** 3.312 / 802 / 298 párrafos en páginas directas. Habrá que equilibrar.
- **Ruido:** sin solapes en páginas directas; los cruces aparecen al bajar a subcategorías y son pocos (Hugo Sperrle, militar alemán en la Guerra Civil Española y en la Segunda Guerra Mundial).
- **Riesgo nuevo:** las fechas (1805, 1812 frente a 1936, 1944) pueden decidir la clase casi solas. Se medirá en la Fase 3 entrenando con y sin números.
- **Limitaciones:** los datos cambian con el tiempo (válidos a fecha de consulta). La lista "Listo de svedoj kiuj mortis en la Hispana Enlanda Milito" es una página directa de la Guerra Civil Española con 126 líneas de nombres, que no son párrafos útiles.

## 6. Incidencias conocidas (de la versión 1, siguen aplicando)
1. Los títulos de categoría distinguen mayúsculas (`Dua Mondmilito`, `Hispana Enlanda Milito`, `Napoleonaj militoj`).
2. La API de extractos solo devuelve un texto completo por petición.
3. Wikimedia limita las peticiones (error 429): reintentos con espera, pausa entre peticiones y User-Agent identificativo.

## 7. Siguientes pasos
1. Estudio de profundidad de subcategorías con las clases nuevas (hecho: `docs/estudio_profundidad_fase1.md`).
2. Generador del dataset en el cuaderno con las nuevas categorías y exclusiones.
3. Medir el ruido con una muestra manual de párrafos.
4. Citar en el README la procedencia (Wikipedia en esperanto) y su licencia (CC BY-SA).

---

## Anexo · Versión corta para la celda de texto del cuaderno
Está en la celda "Exploración de fuentes" de `clasificador_milito.ipynb`.
