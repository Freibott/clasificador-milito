# Estudio de profundidad de subcategorías · Fase 1 (Dataset)

**Proyecto:** Clasificador de textos en esperanto (WWI, WWII, Guerra Fría) · Minería de Textos, CUNEF 2026/2027
**Fecha de la consulta:** 28/10/2026 · **Fuente:** API de MediaWiki de `eo.wikipedia.org`
**Relación con la bitácora anterior:** completa los "Siguientes pasos 1" de `docs/bitacora_exploracion_fase1.md` (medir el volumen con subcategorías a profundidad 1 y 2).

> Tabla de subcategorías preparada con ayuda de IA y **revisada por el equipo**. Las cifras se volverán a obtener con el generador del cuaderno (Fase 1); si difieren, mandan las del cuaderno.

---

## 1. Método

- **Recorrido en anchura** (nivel a nivel) desde cada categoría raíz con `list=categorymembers` (`cmtype=page|subcat`, `cmlimit=500`, siguiendo `continue` hasta agotar resultados).
- **Profundidad 0** = páginas directas de la raíz; **1** = además, páginas de sus subcategorías; **2** = además, las de las sub-subcategorías.
- Se lleva un conjunto de **categorías visitadas** (evita ciclos) y cada artículo se cuenta **una sola vez por clase**, en la menor profundidad a la que aparece.
- Texto: `prop=extracts&explaintext=1`, **un artículo por petición** (la API solo devuelve un texto completo por petición).
- **Párrafo** = línea del texto plano, sin títulos de sección (`== … ==`), con **10 palabras o más**. Misma medida que en la bitácora anterior.
- **Únicos** = artículos que no están en ninguna otra clase a esa misma profundidad.
- Se descargaron los 1.366 artículos distintos hasta profundidad 2, sin errores. **No es una estimación por muestra: es el recuento completo.**

---

## 2. Artículos y párrafos por clase y profundidad

| Prof. | Clase | Artículos | Párrafos (≥10 pal.) | Artículos únicos | **Párrafos únicos** | Párrafos únicos (≥20 pal.) |
|---|---|---:|---:|---:|---:|---:|
| 0 | WWI | 16 | 313 | 11 | **269** | 155 |
| 0 | WWII | 132 | 3.312 | 125 | **3.231** | 1.293 |
| 0 | Guerra Fría | 57 | 647 | 55 | **610** | 454 |
| 1 | WWI | 72 | 991 | 60 | **875** | 648 |
| 1 | WWII | 343 | 5.384 | 311 | **5.103** | 2.630 |
| 1 | Guerra Fría | 202 | 1.929 | 181 | **1.740** | 1.248 |
| 2 | WWI | 112 | 1.461 | 97 | **1.246** | 944 |
| 2 | WWII | 1.022 | 11.974 | 958 | **11.316** | 7.056 |
| 2 | Guerra Fría | 297 | 2.879 | 247 | **2.412** | 1.707 |

Categorías alcanzadas (hasta prof. 2, incluidas las de nivel 3 que no se recorren): WWI 64 · WWII 454 · Guerra Fría 76.

**Lectura:**
- **A profundidad 0, WWI no llega a 300** párrafos una vez quitados los artículos compartidos (269). La estimación anterior (≈ 310) era correcta en el total, pero no tenía en cuenta los duplicados.
- **WWII estaba muy subestimada** (≈ 710 estimados frente a 3.312 reales): la muestra no aleatoria tenía muchos esbozos.
- **Profundidad 1:** las tres clases superan con holgura los 300 párrafos únicos (875 / 5.103 / 1.740).
- **Profundidad 2:** WWII se multiplica por 2,2 y su solape con Guerra Fría pasa de 21 a 50 artículos. El desequilibrio y la deriva temática crecen más que el beneficio para WWI.

---

## 3. Solape entre clases (artículos en ambos árboles)

| Prof. | WWI ∩ WWII | WWI ∩ Guerra Fría | WWII ∩ Guerra Fría |
|---|---:|---:|---:|
| 0 | 5 | 0 | 2 |
| 1 | 12 | 1 | 21 |
| 2 | 15 | 1 | 50 |

**Ejemplos a profundidad 1:**
- **WWII ∩ Guerra Fría** (frontera 1943–1949): Jalta konferenco, Pocdama Interkonsento, Teherana Konferenco, Okupacio de Germanio, Okupacio de Japanio, Fera Kurteno, Greka Enlanda Milito, Tago de Venko en Eŭropo, Ratlinioj, Du-plus-kvar-traktato… La mayoría entra por la subcategoría **"Sekvoj de la Dua Mondmilito"**, que cuelga de ambas raíces.
- **WWI ∩ WWII:** Intermilita periodo, U-boato, Hugo Sperrle, Aleksandros Papagos, Volksbund Deutsche Kriegsgräberfürsorge… (periodo de entreguerras, armas y militares que sirvieron en las dos guerras).
- **WWI ∩ Guerra Fría:** solo Militnovedzino, que está en las tres clases.

Esto confirma con datos que el par más confundible es **WWII ↔ Guerra Fría**, seguido de **WWI ↔ WWII**, y que **WWI ↔ Guerra Fría** apenas se toca.

---

## 4. Revisión de subcategorías de nivel 1

Columnas: páginas directas de la subcategoría · nº de subcategorías propias · artículos nuevos que aporta hasta prof. 2 · valoración.
Valoración: **Sí** = tema propio de la clase; **Dudoso** = mezcla contenido de otra época o temas generales (personas, lugares, obras, armas); **No** = proponemos excluirla.

### WWI · `Kategorio:Unua Mondmilito`

| Subcategoría | Págs. | Subcats | Nuevos (≤2) | ¿Propia? | Motivo |
|---|---:|---:|---:|---|---|
| Unua Mondmilito laŭ landoj | 0 | 13 | 12 | Sí | Solo aporta a prof. 2 |
| Bataloj de la Unua Mondmilito | 24 | 0 | 24 | Sí | Núcleo bélico |
| Frontoj de la Unua Mondmilito | 0 | 1 | 0 | Sí | Vacía en la práctica |
| Homoj de la Unua Mondmilito | 6 | 2 | 7 | Dudoso | Biografías que cubren toda una vida |
| Kaŭzoj de la Unua Mondmilito | 2 | 0 | 2 | Sí | |
| Ĉeĥoslovakaj legioj | 2 | 1 | 9 | Sí | |
| Lokoj ligitaj al la Unua Mondmilito | 0 | 1 | 1 | Dudoso | Lugares |
| Milita ekipaĵo de la Unua Mondmilito | 6 | 1 | 7 | Dudoso | Armas usadas también en WWII (U-boato) |
| Militkaptitoj de la Unua Mondmilito | 10 | 0 | 10 | Dudoso | Biografías de prisioneros |
| Politiko de la Unua Mondmilito | 1 | 2 | 3 | Sí | |
| Ribeloj dum la Unua Mondmilito | 2 | 0 | 2 | Sí | |
| Sekvoj de la Unua Mondmilito | 5 | 6 | 19 | Dudoso | Entreguerras: frontera con WWII |
| Verkoj pri la Unua Mondmilito | 0 | 2 | 0 | Dudoso | Obras (cine, libros) |

### WWII · `Kategorio:Dua Mondmilito`

| Subcategoría | Págs. | Subcats | Nuevos (≤2) | ¿Propia? | Motivo |
|---|---:|---:|---:|---|---|
| Dua Mondmilito laŭ landoj | 1 | 59 | 181 | Sí | Muy grande a prof. 2 |
| Kronologio de la Dua Mondmilito | 11 | 0 | 2 | Sí | |
| Dua Mondmilito laŭ kontinentoj | 0 | 5 | 0 | Sí | |
| Bataloj kaj operacoj de la Dua Mondmilito | 38 | 16 | 76 | Sí | Núcleo bélico |
| Bestoj en la Dua Mondmilito | 2 | 0 | 2 | Dudoso | Tema lateral |
| Detencentroj de la Dua Mondmilito | 0 | 1 | 2 | Sí | |
| Historiografio de la Dua Mondmilito | 1 | 1 | 4 | Sí | |
| Koncentrejo | 7 | 3 | 6 | Dudoso | Concepto general, no solo nazi |
| Naziaj koncentrejoj | 18 | 7 | 85 | Sí | |
| Kultura historio de la Dua Mondmilito | 2 | 2 | 5 | Dudoso | |
| Kunlaborado kun nazioj | 7 | 5 | 24 | Sí | |
| Lokoj ligitaj al la Dua Mondmilito | 6 | 10 | 27 | Dudoso | Lugares |
| Masakroj en la Dua Mondmilito | 23 | 5 | 54 | Sí | |
| Memoro de la Dua Mondmilito | 1 | 2 | 11 | Dudoso | Memoria de posguerra |
| Milita ekipaĵo de la Dua Mondmilito | 0 | 1 | 0 | Dudoso | Armas |
| Militaj premioj de la Dua Mondmilito | 1 | 0 | 1 | Sí | |
| Militkrimoj dum la Dua Mondmilito | 23 | 7 | 70 | Sí | |
| Monumentoj de la Dua Mondmilito | 15 | 3 | 21 | Dudoso | Describen monumentos de posguerra |
| Movadoj de Rezistado en la Dua Mondmilito | 16 | 13 | 58 | Sí | |
| Okupitaj teritorioj de la Dua Mondmilito | 2 | 2 | 15 | Sí | |
| Personoj de la Dua Mondmilito | 25 | 16 | 105 | Dudoso | Biografías completas |
| Politiko de la Dua Mondmilito | 14 | 8 | 17 | Sí | |
| Ribeloj dum la Dua Mondmilito | 4 | 1 | 15 | Sí | |
| Sekvoj de la Dua Mondmilito | 19 | 11 | 32 | **No** | Compartida con Guerra Fría |
| Trupoj kaj formacioj en la Dua Mondmilito | 1 | 1 | 1 | Sí | |
| Urboj-herooj | 3 | 1 | 14 | Dudoso | Historia general de ciudades |
| Verkoj pri la Dua Mondmilito | 3 | 10 | 62 | Dudoso | Obras (cine, libros) |

### Guerra Fría · `Kategorio:Malvarma milito`

| Subcategoría | Págs. | Subcats | Nuevos (≤2) | ¿Propia? | Motivo |
|---|---:|---:|---:|---|---|
| Anatemitaj Soldatoj | 14 | 0 | 14 | Sí | Resistencia anticomunista polaca |
| Hungara revolucio de 1956 | 38 | 0 | 38 | Sí | |
| Konfliktoj de la Malvarma milito | 6 | 10 | 29 | Sí | |
| Makartiismo | 8 | 0 | 7 | Sí | |
| Malvarma milito en Germanio | 8 | 0 | 7 | Sí | |
| Okcidenta Berlino | 6 | 0 | 4 | Sí | |
| Organizaĵoj de la Malvarma milito | 1 | 2 | 6 | Sí | |
| Orienta Bloko | 9 | 0 | 7 | Sí | |
| Personoj de la Malvarma milito | 9 | 2 | 20 | Dudoso | Biografías |
| Malvarma milito en populara kulturo | 3 | 2 | 4 | Dudoso | Cultura popular |
| Protestoj sur placo Tian An Men | 5 | 0 | 5 | Dudoso | Política interna china (1989) |
| Sekvoj de la Dua Mondmilito | 19 | 11 | 41 | **No** | Pertenece a WWII |
| Solidareco (Pollando) | 14 | 1 | 37 | Dudoso | Sindicalismo polaco |
| Terminologio de la Malvarma milito | 7 | 0 | 4 | Sí | |
| Traktatoj de la Malvarma milito | 11 | 0 | 11 | Sí | |
| Verkoj pri la Malvarma milito | 1 | 2 | 3 | Dudoso | Obras |
| Zairo | 2 | 1 | 3 | **No** | País; relación indirecta |

---

## 5. Decisiones propuestas

1. **Profundidad 1** en las tres clases. Es la mínima que da margen claro a WWI (875 párrafos únicos frente a 300) sin disparar el desequilibrio ni el solape de la profundidad 2.
2. **Excluir** las subcategorías marcadas "No": "Sekvoj de la Dua Mondmilito" (en ambas clases) y "Zairo". Las "Dudoso" se mantienen y su ruido se mide en la Fase 1.
3. **Descartar los artículos presentes en más de una clase** (32 artículos distintos a profundidad 1). Es más limpio y defendible que asignarlos a una sola.
4. **Equilibrar** limitando cada clase al tamaño de la menor tras la limpieza (muestreo aleatorio con semilla fija), y comparar en la Fase 3 con el dataset sin equilibrar.
5. **Números y fechas:** se conservan en esta fase (decisión pendiente para la Fase 2, por su peso como pista: 1914–18, 1939–45, 1947–91).
