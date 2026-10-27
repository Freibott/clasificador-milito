# Bitácora · Exploración de fuentes para la Fase 1 (Dataset)

**Proyecto:** Clasificador de textos en esperanto (WWI, WWII, Guerra Fría) · Minería de Textos, CUNEF 2026/2027
**Equipo:** Castro Freibott, Pelayo · Hernández-Echevarría López-Baissón, Pedro · Narváez Fontcuberta, José María
**Fecha de la consulta:** 27/10/2026 · **Ejecutado por:** Pelayo Castro Freibott · **Entorno:** Google Colab y terminal del Codespace

---

## 1. Qué se comprobó
Si Vikipedio (la Wikipedia en esperanto) ofrece texto suficiente, y de calidad razonable, para las tres categorías del trabajo: WWI, WWII y Guerra Fría. En concreto: que las categorías existen y con qué nombre exacto, cuántas páginas y subcategorías tienen, cuánto miden los artículos y cuántos aparecen en más de una categoría.

## 2. Por qué
- El enunciado recomienda explorar la viabilidad de las fuentes antes de elegir temáticas, y exige un dataset con más de 300 párrafos por clase (recomendado).
- El enunciado pide categorías semánticamente cercanas (para que el problema no sea trivial) y que se reconozca y mida el ruido de heredar la etiqueta del artículo. Los solapes y el tipo de contenido son una primera medida de ese riesgo.
- Lo que se descubra decide cómo se monta el generador del dataset (qué categorías, si se incluyen subcategorías, qué filtros).

## 3. Cómo
- Script de solo lectura `explorar_categorias.py`, que consulta la API de MediaWiki de `eo.wikipedia.org`: `categoryinfo` (tamaño de cada categoría), `categorymembers` (páginas y subcategorías directas) y `extracts` con `explaintext` (texto plano de una muestra de artículos).
- Muestra: WWI, las 16 páginas directas (todas); WWII, 20 de 134; Guerra Fría, 20 de 57. La muestra de WWII y Guerra Fría son los primeros artículos en el orden de la categoría, **no una muestra aleatoria**.
- Métricas: palabras por artículo (mín/mediana/máx), artículos vacíos y "párrafos" medios por artículo (líneas con 10 palabras o más, una medida aproximada).
- Solapes: páginas directas que pertenecen a más de una categoría. No incluye las subcategorías.
- No se descargó ni guardó ningún dataset.

## 4. Qué se vio

| | WWI | WWII | Guerra Fría |
|---|---|---|---|
| Categoría | `Kategorio:Unua Mondmilito` | `Kategorio:Dua Mondmilito` | `Kategorio:Malvarma milito` |
| Páginas directas | 16 | 134 | 57 |
| Subcategorías | 13 | 27 | 17 |
| Muestra analizada | 16 | 20 | 20 |
| Palabras mín / mediana / máx | 33 / 305 / 7851 | 0 / 212 / 1557 | 61 / 280 / 6294 |
| Artículos vacíos | 0 | 1 | 0 |
| Párrafos (≥10 palabras) por artículo | ≈ 19,6 | ≈ 5,3 | ≈ 13,6 |
| Orden de magnitud de párrafos en páginas directas* | ≈ 310 | ≈ 710 | ≈ 775 |

\* Cálculo grosero: páginas directas × media de la muestra. Con muestras no aleatorias y unos pocos artículos muy largos que inflan la media, es solo una referencia.

**Solapes entre páginas directas:** WWI ∩ WWII = 5 (el 31 % de las 16 páginas de WWI); WWI ∩ Guerra Fría = 0; WWII ∩ Guerra Fría = 2.

**Estructura:** en las tres categorías, buena parte del contenido está en subcategorías (por batallas, personas, lugares, políticas, consecuencias, obras…). "Sekvoj de la Dua Mondmilito" (consecuencias de la Segunda Guerra Mundial) es subcategoría tanto de WWII como de Guerra Fría. También hay subcategorías de relación dudosa con el tema, como "Zairo" en Guerra Fría, y otras muy específicas (campos de concentración nazis, animales en la guerra…).

### Incidencias durante la exploración
1. **Nombres de categoría.** Los primeros nombres probados (`Unua mondmilito`, `Dua mondmilito`) no existían. Los títulos de categoría distinguen mayúsculas, y la forma correcta lleva "Mondmilito" con M mayúscula.
2. **Textos vacíos.** En la primera versión las longitudes salían a cero. La API de extractos solo devuelve varios textos completos en una misma petición si se pide únicamente la introducción; si no, solo el primero trae texto. Al pedir cada página por separado, los vacíos pasaron a 1 de 56. Las cifras de la primera versión se descartaron.
3. **Error 429 (demasiadas peticiones).** Wikimedia limitó las peticiones. Se añadieron reintentos con espera, una pausa de 1 s entre peticiones y un User-Agent identificativo.

## 5. Evaluación y valoración
- **Viabilidad: positiva.** Las tres categorías existen y tienen material. Es un tema que cumple el requisito de cercanía semántica: tres bloques históricos que comparten vocabulario (guerra, frentes, tratados, ejércitos, personas).
- **Desequilibrio:** 16 / 134 / 57 páginas directas. WWI es el cuello de botella: sus páginas directas apenas rondan los 300 párrafos, en el límite de lo recomendado. WWII y Guerra Fría lo superan con holgura.
- **Riesgo de ruido y etiquetas ambiguas:** el solape WWI ∩ WWII es notable (31 % en páginas directas) y hay subcategorías compartidas o fronterizas. Muchos párrafos serán genéricos y no distinguirán la categoría.
- **Limitaciones de la medición:** muestras no aleatorias; las cifras de párrafos son aproximadas; no se midieron las subcategorías ni la profundidad; el artículo vacío de WWII no se ha inspeccionado; los datos cambian con el tiempo (válidos a fecha de consulta).

## 6. Siguientes pasos
1. Medir cuántas páginas y párrafos **únicos** se obtienen al incluir subcategorías a profundidad 1 y 2, por clase.
2. Decidir las reglas del dataset (propuestas): incluir subcategorías hasta la profundidad que equilibre las clases, descartar páginas presentes en más de una clase, descartar esbozos y párrafos muy cortos, excluir los que contengan `;` o restos de HTML/enlaces/referencias, y limitar cada clase al tamaño de la menor para equilibrar.
3. Escribir en el cuaderno (Fase 1) el generador del dataset, con un parámetro para activarlo o no, y exportar el CSV `text;class` (UTF-8, separador `;`, un párrafo por fila).
4. Medir y comentar el ruido: p. ej., revisar una muestra manual de párrafos y estimar qué fracción es genérica.
5. Indicar en el README la procedencia (Wikipedia en esperanto, con URL de cada artículo) y su licencia (el texto de Wikipedia se publica bajo CC BY-SA; conviene verificarlo antes de publicar el dataset).

---

## Anexo A · Salida íntegra de la ejecución (27/10/2026)

```
probando Kategorio:Unua Mondmilito: existe

=== WWI (Kategorio:Unua Mondmilito) ===
  páginas directas: 16 | subcategorías: 13 | (categoryinfo: 16 págs, 13 subcats)
  subcategorías: Unua Mondmilito laŭ landoj, Bataloj de la Unua Mondmilito, Frontoj de la Unua Mondmilito, Homoj de la Unua Mondmilito, Kaŭzoj de la Unua Mondmilito, Ĉeĥoslovakaj legioj, Lokoj ligitaj al la Unua Mondmilito, Milita ekipaĵo de la Unua Mondmilito, Militkaptitoj de la Unua Mondmilito, Politiko de la Unua Mondmilito, Ribeloj dum la Unua Mondmilito, Sekvoj de la Unua Mondmilito, Verkoj pri la Unua Mondmilito
  muestra de 16: palabras mín/mediana/máx = 33/305/7851 | artículos vacíos: 0 | párrafos (≥10 palabras) por artículo ≈ 19.6
  probando Kategorio:Dua Mondmilito: existe

=== WWII (Kategorio:Dua Mondmilito) ===
  páginas directas: 134 | subcategorías: 27 | (categoryinfo: 134 págs, 27 subcats)
  subcategorías: Dua Mondmilito laŭ landoj, Kronologio de la Dua Mondmilito, Dua Mondmilito laŭ kontinentoj, Bataloj kaj operacoj de la Dua Mondmilito, Bestoj en la Dua Mondmilito, Detencentroj de la Dua Mondmilito, Historiografio de la Dua Mondmilito, Koncentrejo, Naziaj koncentrejoj, Kultura historio de la Dua Mondmilito, Kunlaborado kun nazioj, Lokoj ligitaj al la Dua Mondmilito, Masakroj en la Dua Mondmilito, Memoro de la Dua Mondmilito, Milita ekipaĵo de la Dua Mondmilito, Militaj premioj de la Dua Mondmilito, Militkrimoj dum la Dua Mondmilito, Monumentoj de la Dua Mondmilito, Movadoj de Rezistado en la Dua Mondmilito, Okupitaj teritorioj de la Dua Mondmilito, Personoj de la Dua Mondmilito, Politiko de la Dua Mondmilito, Ribeloj dum la Dua Mondmilito, Sekvoj de la Dua Mondmilito, Trupoj kaj formacioj en la Dua Mondmilito, Urboj-herooj, Verkoj pri la Dua Mondmilito
  muestra de 20: palabras mín/mediana/máx = 0/212/1557 | artículos vacíos: 1 | párrafos (≥10 palabras) por artículo ≈ 5.3
  probando Kategorio:Malvarma milito: existe

=== Guerra Fría (Kategorio:Malvarma milito) ===
  páginas directas: 57 | subcategorías: 17 | (categoryinfo: 57 págs, 17 subcats)
  subcategorías: Anatemitaj Soldatoj, Hungara revolucio de 1956, Konfliktoj de la Malvarma milito, Makartiismo, Malvarma milito en Germanio, Okcidenta Berlino, Organizaĵoj de la Malvarma milito, Orienta Bloko, Personoj de la Malvarma milito, Malvarma milito en populara kulturo, Protestoj sur placo Tian An Men, Sekvoj de la Dua Mondmilito, Solidareco (Pollando), Terminologio de la Malvarma milito, Traktatoj de la Malvarma milito, Verkoj pri la Malvarma milito, Zairo
  muestra de 20: palabras mín/mediana/máx = 61/280/6294 | artículos vacíos: 0 | párrafos (≥10 palabras) por artículo ≈ 13.6

=== Solapes entre categorías (páginas directas) ===
  WWI ∩ WWII: 5
  WWI ∩ Guerra Fría: 0
  WWII ∩ Guerra Fría: 2
```

---

## Anexo B · Versión corta para la celda de texto del cuaderno (Fase 1)

### Exploración de fuentes
**Objetivo.** Antes de construir el dataset, comprobamos (27/10/2026) si Vikipedio (Wikipedia en esperanto) tiene texto suficiente para WWI, WWII y Guerra Fría, consultando su API de MediaWiki con un script de solo lectura.

**Resultados.** Las tres categorías existen (`Kategorio:Unua Mondmilito`, `Kategorio:Dua Mondmilito`, `Kategorio:Malvarma milito`) con 16, 134 y 57 páginas directas y 13, 27 y 17 subcategorías. Los artículos tienen una mediana de entre 212 y 305 palabras. Hay solapes entre clases (5 páginas WWI ∩ WWII, 2 WWII ∩ Guerra Fría) y subcategorías compartidas, como "Sekvoj de la Dua Mondmilito".

**Valoración.** Es viable y las categorías son semánticamente cercanas, como pide el enunciado. WWI es la clase más pequeña (≈ 300 párrafos solo con páginas directas), por lo que se estudia incluir subcategorías y equilibrar las clases. El solape implica ruido en las etiquetas: descartaremos páginas presentes en más de una clase y mediremos el ruido residual.

**Incidencias resueltas.** Los nombres de categoría distinguen mayúsculas; la API de extractos solo devuelve un texto completo por petición; y hubo que gestionar el error 429 con reintentos y pausas.
