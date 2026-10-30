# Estudio de profundidad de subcategorías · Fase 1 (Dataset)

**Proyecto:** Clasificador de textos en esperanto (Segunda Guerra Mundial, Guerra Civil Española, Guerras Napoleónicas) · Minería de Textos, CUNEF 2026/2027
**Fecha de la consulta:** 30/10/2026 · **Fuente:** API de MediaWiki de `eo.wikipedia.org`
**Relación con la bitácora:** completa el paso 1 de los "Siguientes pasos" de `docs/bitacora_exploracion_fase1.md`.

> Versión 2, con las clases nuevas. La versión 1 (28/10/2026, WWI / WWII / Guerra Fría) sigue en el historial de Git (commit `4eeb92c`). Tabla de subcategorías preparada con ayuda de IA y **revisada por el equipo**. Las cifras se volverán a obtener con el generador del cuaderno (Fase 1); si difieren, mandan las del cuaderno.

---

## 1. Método
(Igual que en la versión 1.)
- **Recorrido en anchura** (nivel a nivel) desde cada categoría raíz con `list=categorymembers` (`cmtype=page|subcat`, `cmlimit=500`, siguiendo `continue` hasta agotar resultados).
- **Profundidad 0** = páginas directas de la raíz; **1** = además, páginas de sus subcategorías; **2** = además, las de las sub-subcategorías.
- Se lleva un conjunto de **categorías visitadas** (evita ciclos) y cada artículo se cuenta **una sola vez por clase**, en la menor profundidad a la que aparece.
- Texto: `prop=extracts&explaintext=1`, **un artículo por petición**.
- **Párrafo** = línea del texto plano, sin títulos de sección (`== … ==`), con **10 palabras o más**.
- **Únicos** = artículos que no están en ninguna otra clase a esa misma profundidad.
- Se descargaron los **1.306 artículos distintos** hasta profundidad 2, sin errores. Es el recuento completo, no una estimación por muestra.

---

## 2. Artículos y párrafos por clase y profundidad (sin exclusiones)

| Prof. | Clase | Artículos | Párrafos (≥10 pal.) | Artículos únicos | **Párrafos únicos** | Párrafos únicos (≥20 pal.) |
|---|---|---:|---:|---:|---:|---:|
| 0 | Segunda Guerra Mundial | 132 | 3.312 | 132 | **3.312** | 1.342 |
| 0 | Guerra Civil Española | 54 | 802 | 54 | **802** | 493 |
| 0 | Guerras Napoleónicas | 41 | 298 | 41 | **298** | 211 |
| 1 | Segunda Guerra Mundial | 343 | 5.384 | 341 | **5.371** | 2.799 |
| 1 | Guerra Civil Española | 150 | 1.702 | 148 | **1.689** | 1.110 |
| 1 | Guerras Napoleónicas | 97 | 735 | 97 | **735** | 531 |
| 2 | Segunda Guerra Mundial | 1.022 | 11.974 | 1.013 | **11.880** | 7.405 |
| 2 | Guerra Civil Española | 194 | 2.128 | 185 | **2.034** | 1.315 |
| 2 | Guerras Napoleónicas | 99 | 746 | 99 | **746** | 538 |

Categorías alcanzadas (hasta prof. 2, incluidas las de nivel 3 que no se recorren): Segunda Guerra Mundial 454 · Guerra Civil Española 15 · Guerras Napoleónicas 10.

**Lectura:**
- **A profundidad 0, las Guerras Napoleónicas no llegan a 300 párrafos** (298).
- **Profundidad 1:** las tres clases superan con holgura los 300 párrafos (5.371 / 1.689 / 735).
- **Profundidad 2** apenas aporta a las Guerras Napoleónicas (+11 párrafos) y a la Guerra Civil Española (+345), pero multiplica por 2,2 la Segunda Guerra Mundial. Solo aumentaría el desequilibrio.

---

## 3. Solape entre clases (artículos en ambos árboles)

| Prof. | SGM ∩ GCE | SGM ∩ G. Napoleónicas | GCE ∩ G. Napoleónicas |
|---|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 1 | 2 | 0 | 0 |
| 2 | 9 | 0 | 0 |

- **Profundidad 1:** Hugo Sperrle (militar alemán en ambas guerras) e Hispana ekonomia miraklo (milagro económico español, entra por "Sekvoj de la Dua Mondmilito" y por "Frankismo").
- **Profundidad 2:** además Francisco Franco, Ramón Serrano Súñer, Koncentrejo de Gurso, Giorgio Perlasca, Elisabeth Eidenbenz, Rafael Gómez Nieto e Internacia Zono de Tanĝero.

El único par confundible es **Segunda Guerra Mundial ↔ Guerra Civil Española**, como se esperaba. Las Guerras Napoleónicas no comparten ningún artículo. Con las clases anteriores había 32 artículos compartidos a profundidad 1.

---

## 4. Revisión de subcategorías de nivel 1

Columnas: páginas directas de la subcategoría · nº de subcategorías propias · artículos nuevos que aporta hasta prof. 2 · párrafos nuevos que aporta a prof. 1 · valoración.
Valoración: **Sí** = tema propio de la clase; **Dudoso** = mezcla contenido de otra época o temas generales (personas, lugares, obras); **No** = proponemos excluirla.

### Segunda Guerra Mundial · `Kategorio:Dua Mondmilito`

| Subcategoría | Págs. | Subcats | Nuevos (≤2) | Párr. (prof. 1) | ¿Propia? | Motivo |
|---|---:|---:|---:|---:|---|---|
| Dua Mondmilito laŭ landoj | 1 | 59 | 181 | 14 | Sí | Solo aporta a prof. 2 |
| Kronologio de la Dua Mondmilito | 11 | 0 | 2 | 4 | Sí | |
| Dua Mondmilito laŭ kontinentoj | 0 | 5 | 0 | 0 | Sí | Vacía en la práctica |
| Bataloj kaj operacoj de la Dua Mondmilito | 38 | 16 | 76 | 561 | Sí | Núcleo bélico |
| Bestoj en la Dua Mondmilito | 2 | 0 | 2 | 17 | Dudoso | Tema lateral |
| Detencentroj de la Dua Mondmilito | 0 | 1 | 2 | 0 | Sí | |
| Historiografio de la Dua Mondmilito | 1 | 1 | 4 | 10 | Sí | |
| Koncentrejo | 7 | 3 | 6 | 82 | Dudoso | Concepto general, no solo nazi |
| Naziaj koncentrejoj | 18 | 7 | 85 | 103 | Sí | |
| Kultura historio de la Dua Mondmilito | 2 | 2 | 5 | 14 | Dudoso | |
| Kunlaborado kun nazioj | 7 | 5 | 24 | 65 | Sí | |
| Lokoj ligitaj al la Dua Mondmilito | 6 | 10 | 27 | 28 | Dudoso | Lugares |
| Masakroj en la Dua Mondmilito | 23 | 5 | 54 | 263 | Sí | |
| Memoro de la Dua Mondmilito | 1 | 2 | 11 | 2 | Dudoso | Memoria de posguerra |
| Milita ekipaĵo de la Dua Mondmilito | 0 | 1 | 0 | 0 | Dudoso | Armas |
| Militaj premioj de la Dua Mondmilito | 1 | 0 | 1 | 4 | Sí | |
| Militkrimoj dum la Dua Mondmilito | 23 | 7 | 70 | 163 | Sí | |
| Monumentoj de la Dua Mondmilito | 15 | 3 | 21 | 70 | Dudoso | Monumentos de posguerra |
| Movadoj de Rezistado en la Dua Mondmilito | 16 | 13 | 58 | 107 | Sí | |
| Okupitaj teritorioj de la Dua Mondmilito | 2 | 2 | 15 | 6 | Sí | |
| Personoj de la Dua Mondmilito | 25 | 16 | 105 | 177 | Dudoso | Biografías completas |
| Politiko de la Dua Mondmilito | 14 | 8 | 17 | 81 | Sí | |
| Ribeloj dum la Dua Mondmilito | 4 | 1 | 15 | 14 | Sí | |
| Sekvoj de la Dua Mondmilito | 19 | 11 | 32 | 141 | **No** | Posguerra (Guerra Fría); trae un solape con GCE |
| Trupoj kaj formacioj en la Dua Mondmilito | 1 | 1 | 1 | 10 | Sí | |
| Urboj-herooj | 3 | 1 | 14 | 115 | Dudoso | Historia general de ciudades |
| Verkoj pri la Dua Mondmilito | 3 | 10 | 62 | 21 | Dudoso | Obras (cine, libros) |

### Guerra Civil Española · `Kategorio:Hispana Enlanda Milito`

| Subcategoría | Págs. | Subcats | Nuevos (≤2) | Párr. (prof. 1) | ¿Propia? | Motivo |
|---|---:|---:|---:|---:|---|---|
| Bataloj de la Hispana Enlanda Milito | 5 | 0 | 5 | 31 | Sí | Núcleo bélico |
| Frankismo | 22 | 5 | 41 | 118 | **No** | Dictadura de posguerra (1939–1975); trae el solape "Hispana ekonomia miraklo" |
| Homoj de la Hispana Enlanda Milito | 51 | 0 | 49 | 474 | Dudoso | Biografías completas |
| Verkoj pri la Hispana Enlanda Milito | 24 | 2 | 45 | 277 | Dudoso | Obras (novelas, cine) |

Además, la página directa **"Listo de svedoj kiuj mortis en la Hispana Enlanda Milito"** es una lista de nombres (126 líneas): proponemos excluir ese artículo.

### Guerras Napoleónicas · `Kategorio:Napoleonaj militoj`

| Subcategoría | Págs. | Subcats | Nuevos (≤2) | Párr. (prof. 1) | ¿Propia? | Motivo |
|---|---:|---:|---:|---:|---|---|
| Brit-usona milito de 1812 | 2 | 0 | 2 | 16 | **No** | Guerra distinta (EE. UU. contra Reino Unido) |
| Napoleonaj militoj en fikcio | 2 | 1 | 3 | 21 | Dudoso | Ficción |
| Milito de Hispana Sendependiĝo | 21 | 0 | 17 | 104 | Sí | Guerra de la Independencia española. Comparte vocabulario con GCE (Hispanio, Madrido) |
| Homoj de la Napoleonaj militoj | 23 | 0 | 23 | 196 | Dudoso | Biografías |
| Internaciaj traktatoj de la Napoleonaj militoj | 4 | 0 | 4 | 13 | Sí | |
| Militkampanjoj de la Napoleonaj militoj | 4 | 0 | 4 | 20 | Sí | |
| Milito de la Tria Koalicio | 9 | 0 | 3 | 10 | Sí | |
| Franca invado al Rusio | 7 | 0 | 2 | 57 | Sí | |

---

## 5. Decisiones propuestas

1. **Profundidad 1** en las tres clases. Es la mínima con la que las Guerras Napoleónicas superan los 300 párrafos (735). La profundidad 2 casi no les aporta nada y duplica la Segunda Guerra Mundial.
2. **Excluir tres subcategorías y un artículo:**
   - "Sekvoj de la Dua Mondmilito" y "Frankismo": son de posguerra y son la vía de entrada del solape "Hispana ekonomia miraklo".
   - "Brit-usona milito de 1812": es otra guerra.
   - El artículo "Listo de svedoj kiuj mortis en la Hispana Enlanda Milito": es una lista de nombres.

   Las subcategorías "Dudoso" se mantienen y su ruido se mide más adelante.
3. **Descartar los artículos presentes en más de una clase.** Tras las exclusiones solo queda uno (Hugo Sperrle).
4. **Equilibrar** limitando cada clase al tamaño de la menor tras la limpieza (muestreo aleatorio con semilla 42), y comparar en la Fase 3 con el dataset sin equilibrar.
5. **Números y fechas:** se conservan en esta fase. En la Fase 3 se entrena con y sin números, porque los años (1799–1815, 1936–1939, 1939–1945) pueden delatar la clase casi solos.

**Volumen esperado con estas decisiones (profundidad 1):**

| Clase | Artículos | Párrafos (≥10 pal.) | Artículos únicos | Párrafos únicos | Párrafos únicos (≥20 pal.) |
|---|---:|---:|---:|---:|---:|
| Segunda Guerra Mundial | 326 | 5.243 | 325 | 5.234 | 2.700 |
| Guerra Civil Española | 131 | 1.458 | 130 | 1.449 | 978 |
| Guerras Napoleónicas | 95 | 719 | 95 | 719 | 517 |

Cifras aproximadas: cada artículo se atribuyó a la primera subcategoría por la que apareció.
