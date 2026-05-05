# Raport zbiorczy — Właściwości materiałów organicznych dla pojazdów kosmicznych
## *A comparison of selected organic materials for low orbiting spacecraft*

**Data:** 2026-05-05  
**Materiały:** M1–M13 (przydziały: Magda M1–M4 · Filip M5–M8 · Kalina M9–M13)

---

## 1. Wstęp

Niniejszy raport zestawia właściwości mechaniczne i termiczne trzynastu organicznych materiałów rozpatrywanych w kontekście zastosowań na pojazdach kosmicznych operujących w fazie startu oraz na niskiej orbicie okołoziemskiej (LEO, 160–2000 km). W końcowej sekcji dokonano wyboru **pięciu najlepszych materiałów** z uzasadnieniem opartym na wymaganiach środowiskowych LEO i fazy startowej.

### Wymagania środowiskowe

| Faza | Główne zagrożenia | Kluczowe wymagania |
|---|---|---|
| **Start** | Strumień cieplny 1–10 MW/m², drgania, przeciążenia 5–12 g | Ablacja / TPS, wytrzymałość mechaniczna, mała masa |
| **LEO (orbit.)** | Tlenkowanie atomowe (AO), UV, cykle termiczne −150…+150 °C, MMOD | Odporność na AO/UV, stabilność wymiarowa, wysoka K_IC |

Struktura raportu: każdy materiał opisany jest tabelą właściwości i czterema wykresami:

| Wykres | Treść |
|---|---|
| **A** | Krzywa naprężenie–odkształcenie (23 °C) |
| **B** | UTS vs. temperatura |
| **C** | Moduł Younga vs. temperatura |
| **D** | Przewodnictwo cieplne vs. temperatura |

---

## 2. M1 — Kapton (Poliimid HN, DuPont)

### Charakterystyka

Kapton HN (poli(4,4'-oksydifenylen)-piromellitimid) to standardowy film kosmiczny stosowany od lat 60. XX w. na praktycznie każdym statku kosmicznym — od Apollo do ISS. Wyjątkowa stabilność termiczna, zerowe pełzanie w próżni, doskonała odporność na promieniowanie jonizujące. Słaba strona: erozja atomowego tlenu (~3×10⁻²⁴ cm³/atom).

### Właściwości mechaniczne (T = 23 °C)

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Wytrzymałość na rozciąganie (UTS) | **231** | MPa | [DuPont Kapton HN — datasheet (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/EI-10142_Kapton-HN-datasheet.pdf); [Google Doc — dane projektu](https://docs.google.com/document/d/1SUNR-o6LlR9Npx723FPGlJ8TDAnhCzqREIrAE7FIKa0/edit) |
| Moduł Younga (E) | **2,5** | GPa | [DuPont Kapton HN — datasheet (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/EI-10142_Kapton-HN-datasheet.pdf) |
| Granica plastyczności σ_y | **69** | MPa | [Google Doc — dane projektu](https://docs.google.com/document/d/1SUNR-o6LlR9Npx723FPGlJ8TDAnhCzqREIrAE7FIKa0/edit) |
| Wydłużenie przy zerwaniu | **72** | % | [DuPont Kapton HN — datasheet (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/EI-10142_Kapton-HN-datasheet.pdf) |
| Odporność na pękanie K_IC | 1,65–5,4 | MPa·m^0.5 | [Google Doc — dane projektu](https://docs.google.com/document/d/1SUNR-o6LlR9Npx723FPGlJ8TDAnhCzqREIrAE7FIKa0/edit) |
| Gęstość | **1 420** | kg/m³ | [DuPont Kapton HN — datasheet (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/EI-10142_Kapton-HN-datasheet.pdf) |

### Właściwości termiczne

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Przewodnictwo cieplne k | **0,12** | W/m·K | [DuPont Kapton HN — datasheet (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/EI-10142_Kapton-HN-datasheet.pdf); [AZoM ID:921](https://www.azom.com/article.aspx?ArticleID=921) |
| Pojemność cieplna Cp | **1 090** | J/kg·K | [DuPont Kapton HN — datasheet (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/EI-10142_Kapton-HN-datasheet.pdf) |
| Zakres temperatur | **−269 … +400** | °C | [DuPont Kapton HN — datasheet (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/EI-10142_Kapton-HN-datasheet.pdf); [Google Doc — dane projektu](https://docs.google.com/document/d/1SUNR-o6LlR9Npx723FPGlJ8TDAnhCzqREIrAE7FIKa0/edit) |

### Wykresy

![A — krzywa naprężenie–odkształcenie M1](plots/m1_A_stress_strain.png)

*Model semi-ciągliwy: liniowy do granicy plastyczności (69 MPa), następnie utwardzanie potęgowe do zerwania przy 231 MPa / 72%.*

![B — UTS vs. temperatura M1](plots/m1_B_uts_vs_temp.png)

*UTS spada z 270 MPa (−100 °C) do 40 MPa (400 °C); wzrasta przy bardzo niskich T (ciecz. azot). Dane wg Google Doc — dane projektu.*

![C — moduł Younga vs. temperatura M1](plots/m1_C_modulus_vs_temp.png)

*E = 2,5 GPa w RT; monotonicznie spada do ~0,5 GPa przy 400 °C. Źródło: DuPont Kapton HN datasheet.*

![D — przewodnictwo cieplne vs. temperatura M1](plots/m1_D_thermal_cond_vs_temp.png)

*k rośnie nieznacznie z T (0,09→0,19 W/m·K). Źródło: AZoM ID:921, DuPont datasheet.*

---

## 3. M2 — POSS-Poliimid (Nano-PI)

### Charakterystyka

Poliimid modyfikowany nanocząstkami POSS (polyhedral oligomeric silsesquioxane). Nanocząstki SiO₂ wbudowane w łańcuch polimerowy poprawiają odporność na **atomowy tlen** (pasywacja SiO₂) i podwyższają temperaturę ugięcia. Właściwości mechaniczne porównywalne z Kaptonem, nieco gorsze ciągliwości. Materiał nowej generacji dla długoterminowych misji LEO.

### Właściwości mechaniczne (T = 23 °C)

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Wytrzymałość na rozciąganie (UTS) | **210** | MPa | [Brunsvold et al., High Perform. Polym. (2004)](https://doi.org/10.1177/0954008304024680) · [Sci-Hub](https://sci-hub.pl/10.1177/0954008304024680) |
| Moduł Younga (E) | **2,3** | GPa | [Brunsvold et al., High Perform. Polym. (2004)](https://doi.org/10.1177/0954008304024680) · [Sci-Hub](https://sci-hub.pl/10.1177/0954008304024680) |
| Granica plastyczności σ_y | **60** | MPa | [AZoM ID:921 — Poliimid (ogólny)](https://www.azom.com/article.aspx?ArticleID=921) — dane przybliżone |
| Wydłużenie przy zerwaniu | **40** | % | [Brunsvold et al., High Perform. Polym. (2004)](https://doi.org/10.1177/0954008304024680) · [Sci-Hub](https://sci-hub.pl/10.1177/0954008304024680) |
| Odporność na pękanie K_IC | ~2,0 | MPa·m^0.5 | [Gouzman et al., Acta Astronaut. (2010)](https://doi.org/10.1016/j.actaastro.2010.09.010) · [Sci-Hub](https://sci-hub.pl/10.1016/j.actaastro.2010.09.010) — szacunek |
| Gęstość | **1 450** | kg/m³ | [Brunsvold et al., High Perform. Polym. (2004)](https://doi.org/10.1177/0954008304024680) · [Sci-Hub](https://sci-hub.pl/10.1177/0954008304024680) |

### Właściwości termiczne

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Przewodnictwo cieplne k | **0,15** | W/m·K | [Gouzman et al., Acta Astronaut. (2010)](https://doi.org/10.1016/j.actaastro.2010.09.010) · [Sci-Hub](https://sci-hub.pl/10.1016/j.actaastro.2010.09.010) |
| Pojemność cieplna Cp | **1 050** | J/kg·K | dane katalogowe Evonik POSS — szacunek bazowany na Kaptons HN |
| Zakres temperatur | **−269 … +450** | °C | [Gouzman et al., Acta Astronaut. (2010)](https://doi.org/10.1016/j.actaastro.2010.09.010) · [Sci-Hub](https://sci-hub.pl/10.1016/j.actaastro.2010.09.010) |

### Wykresy

![A — krzywa naprężenie–odkształcenie M2](plots/m2_A_stress_strain.png)

![B — UTS vs. temperatura M2](plots/m2_B_uts_vs_temp.png)

![C — moduł Younga vs. temperatura M2](plots/m2_C_modulus_vs_temp.png)

![D — przewodnictwo cieplne vs. temperatura M2](plots/m2_D_thermal_cond_vs_temp.png)

---

## 4. M3 — Żywica fenolowa (Phenolic Resin)

### Charakterystyka

Żywice fenolowo-formaldehydowe (np. SC-1008, Durite) to klasyczne tworzywa ablacyjne. Przy pirolizie (>300 °C) tworzą porowatą warstwę zwęgloną o wysokiej pojemności cieplnej. Stosowane w TPS (AVCOAT NASA, Phoenix lander) i dyszy silników rakietowych.

### Właściwości mechaniczne (T = 23 °C)

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Wytrzymałość na rozciąganie (UTS) | **45** | MPa | [AZoM ID:475 — Żywica fenolowa](https://www.azom.com/article.aspx?ArticleID=475); [MatWeb — Phenolic Resin (Cast)](https://www.matweb.com/search/QuickText.aspx?SearchText=phenolic+cast+resin) |
| Moduł Younga (E) | **3,5** | GPa | [AZoM ID:475](https://www.azom.com/article.aspx?ArticleID=475) |
| Granica plastyczności | — | kruchy materiał | — |
| Wydłużenie przy zerwaniu | **1,0** | % | [AZoM ID:475](https://www.azom.com/article.aspx?ArticleID=475) |
| Odporność na pękanie K_IC | **0,7** | MPa·m^0.5 | [AZoM ID:475](https://www.azom.com/article.aspx?ArticleID=475) |
| Gęstość | **1 250** | kg/m³ | [AZoM ID:475](https://www.azom.com/article.aspx?ArticleID=475) |
| Uzysk węglowy (TGA) | **~55** | % | [Natali et al., Compos. Part A (2012)](https://doi.org/10.1016/j.compositesa.2011.10.009) · [Sci-Hub](https://sci-hub.pl/10.1016/j.compositesa.2011.10.009) |

### Właściwości termiczne

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Przewodnictwo cieplne k | **0,30** | W/m·K | [AZoM ID:475](https://www.azom.com/article.aspx?ArticleID=475) |
| Pojemność cieplna Cp | **1 200** | J/kg·K | [MatWeb — Phenolic Resin](https://www.matweb.com/search/QuickText.aspx?SearchText=phenolic+cast+resin) |
| Zakres temperatur | **−55 … >2000** | °C (ablacyjny) | [Natali et al., Compos. Part A (2012)](https://doi.org/10.1016/j.compositesa.2011.10.009) · [Sci-Hub](https://sci-hub.pl/10.1016/j.compositesa.2011.10.009) |

### Wykresy

![A — krzywa naprężenie–odkształcenie M3](plots/m3_A_stress_strain.png)

*Kruchy termozestaw: liniowy przebieg aż do pęknięcia przy 45 MPa / 1%. Źródło: AZoM ID:475.*

![B — UTS vs. temperatura M3](plots/m3_B_uts_vs_temp.png)

![C — moduł Younga vs. temperatura M3](plots/m3_C_modulus_vs_temp.png)

![D — przewodnictwo cieplne vs. temperatura M3](plots/m3_D_thermal_cond_vs_temp.png)

---

## 5. M4 — Żywica ftalonitrylowa (Phthalonitrile Resin)

### Charakterystyka

Żywice ftalonitrylowe (PT resin) to termozestawy następnej generacji z rekordową temperaturą ciągłej pracy (~370 °C) wśród polimerów organicznych. Utwardzają się bez wydzielania lotnych składników — zerowe porowatości i minimalne odgazowywanie próżniowe. Stosowane w węzłach strukturalnych statków kosmicznych i radome'ach.

### Właściwości mechaniczne (T = 23 °C)

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Wytrzymałość na rozciąganie (UTS) | **65** | MPa | [Hergenrother et al., Polymer (2005)](https://doi.org/10.1016/j.polymer.2005.09.039) · [Sci-Hub](https://sci-hub.pl/10.1016/j.polymer.2005.09.039) |
| Moduł Younga (E) | **4,0** | GPa | [Hergenrother et al., Polymer (2005)](https://doi.org/10.1016/j.polymer.2005.09.039) · [Sci-Hub](https://sci-hub.pl/10.1016/j.polymer.2005.09.039) |
| Granica plastyczności | — | kruchy termostat | — |
| Wydłużenie przy zerwaniu | **1,5** | % | [Laskoski et al., J. Polym. Sci. A (2006)](https://doi.org/10.1002/pola.21358) · [Sci-Hub](https://sci-hub.pl/10.1002/pola.21358) |
| Odporność na pękanie K_IC | **1,0** | MPa·m^0.5 | [Laskoski et al., J. Polym. Sci. A (2006)](https://doi.org/10.1002/pola.21358) · [Sci-Hub](https://sci-hub.pl/10.1002/pola.21358) |
| Gęstość | **1 250** | kg/m³ | [Hergenrother et al., Polymer (2005)](https://doi.org/10.1016/j.polymer.2005.09.039) · [Sci-Hub](https://sci-hub.pl/10.1016/j.polymer.2005.09.039) |
| Uzysk węglowy | **~65** | % | [Laskoski et al., J. Polym. Sci. A (2006)](https://doi.org/10.1002/pola.21358) · [Sci-Hub](https://sci-hub.pl/10.1002/pola.21358) |

### Właściwości termiczne

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Przewodnictwo cieplne k | **0,20** | W/m·K | [Hergenrother et al., Polymer (2005)](https://doi.org/10.1016/j.polymer.2005.09.039) · [Sci-Hub](https://sci-hub.pl/10.1016/j.polymer.2005.09.039) |
| Pojemność cieplna Cp | **1 200** | J/kg·K | szacunek na podstawie danych Hergenrother 2005 — klasa żywic PT |
| Zakres temperatur | **−55 … +375** | °C | [Hergenrother et al., Polymer (2005)](https://doi.org/10.1016/j.polymer.2005.09.039) · [Sci-Hub](https://sci-hub.pl/10.1016/j.polymer.2005.09.039) |

### Wykresy

![A — krzywa naprężenie–odkształcenie M4](plots/m4_A_stress_strain.png)

![B — UTS vs. temperatura M4](plots/m4_B_uts_vs_temp.png)

*Wyjątkowo dobre zachowanie UTS w wysokich T (58 MPa przy 300 °C) — lepsze niż Kapton. Źródło: Hergenrother et al. 2005.*

![C — moduł Younga vs. temperatura M4](plots/m4_C_modulus_vs_temp.png)

![D — przewodnictwo cieplne vs. temperatura M4](plots/m4_D_thermal_cond_vs_temp.png)

---

## 6. M5 — Guma silikonowa / RTV

### Charakterystyka

Elastomery silikonowe (RTV — Room Temperature Vulcanizing, np. RTV566 Momentive) bazują na polidimetylosiloksanie (PDMS). Stosowane jako kleje konstrukcyjne, uszczelnienia i elementy tłumiące drgania w satelitach. Ekstremalnie elastyczne (400%), stabilne od −115 do +300 °C. Zawartość Si zapewnia częściową odporność na AO.

### Właściwości mechaniczne (T = 23 °C)

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Wytrzymałość na rozciąganie (UTS) | **2–10** (typowo 6) | MPa | [AZoM ID:920](https://www.azom.com/properties.aspx?ArticleID=920); [MatWeb RTV566](https://www.matweb.com/search/datasheettext.aspx?matguid=70466aea960a4c84be3bbc5045c219aa) |
| Moduł Younga (E) | **1–5** | MPa | Elastomer — 3–4 rzędy wielkości poniżej metali |
| Granica plastyczności | — | — | **Nie dotyczy** — brak dla elastomerów |
| Wydłużenie przy zerwaniu | 100–800 (typowo **400**) | % | [AZoM ID:920](https://www.azom.com/properties.aspx?ArticleID=920) |
| Odporność na pękanie K_IC | — | — | Opisywana energią rozdarcia, nie K_IC |
| Gęstość | **1 100–1 250** | kg/m³ | [AZoM ID:920](https://www.azom.com/properties.aspx?ArticleID=920); [MatWeb RTV566](https://www.matweb.com/search/datasheettext.aspx?matguid=70466aea960a4c84be3bbc5045c219aa) |

### Właściwości termiczne

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Przewodnictwo cieplne k | **0,25** | W/m·K | [AZoM ID:920](https://www.azom.com/properties.aspx?ArticleID=920) |
| Pojemność cieplna Cp | **1 400** | J/kg·K | [AZoM ID:920](https://www.azom.com/properties.aspx?ArticleID=920) |
| Zakres temperatur | **−115 … +300** | °C | [MatWeb RTV566](https://www.matweb.com/search/datasheettext.aspx?matguid=70466aea960a4c84be3bbc5045c219aa); [Barucci et al., Cryogenics (1998)](https://doi.org/10.1016/S0011-2275(97)00111-3) · [Sci-Hub](https://sci-hub.pl/10.1016/S0011-2275(97)00111-3) |

### Wykresy

![A — krzywa naprężenie–odkształcenie M5](plots/m5_A_stress_strain.png)

*Model Neo-Hookean (G ≈ 0,85 MPa): nieliniowy hipersprężysty, brak granicy plastyczności, zerwanie ~400%.*

![B — UTS vs. temperatura M5](plots/m5_B_uts_vs_temp.png)

![C — moduł Younga vs. temperatura M5](plots/m5_C_modulus_vs_temp.png)

*Skala logarytmiczna — E zmienia się o 3 rzędy wielkości (2000→0,9 MPa). Dane: [Barucci et al., Cryogenics (1998)](https://doi.org/10.1016/S0011-2275(97)00111-3) · [Sci-Hub](https://sci-hub.pl/10.1016/S0011-2275(97)00111-3)*

![D — przewodnictwo cieplne vs. temperatura M5](plots/m5_D_thermal_cond_vs_temp.png)

---

## 7. M6 — Kompozyt polisiloksanowy

### Charakterystyka

Kompozyty na osnowie polisiloksanowej (2.5D SiO₂f/SiO₂ — McDermott et al. 2022; CF/UHTR — Hou et al. Techneglas) łączą odporność na wysokie temperatury z ablacyjnością. Pyroliza daje ceramiczną matrycę SiOC zachowującą integralność do 1400 °C. Uzysk węglowy 86,5%. Odporność na AO dzięki pasywacji SiO₂.

### Właściwości mechaniczne (T = 23 °C)

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Wytrzymałość na rozciąganie (UTS) | **182** ±9,6 | MPa | [McDermott et al., J. Compos. Mater. (2022)](https://doi.org/10.1177/00219983211038622) · [Sci-Hub](https://sci-hub.pl/10.1177/00219983211038622) |
| Moduł Younga (E) | **45,5** ±5 | GPa | [Hou et al. — Techneglas (PDF)](https://www.techneglas.com/wp-content/uploads/2021/12/Yanan-Hou-Performance-of-a-Carbon-FiberPolysiloxane-Composite-Thermal-Ablation-Flammability-and-Mechanical-Characterization.pdf) |
| Granica plastyczności | — | — | Nie dotyczy — pęknięcie kruche |
| Wydłużenie przy zerwaniu | **0,97** | % | [Hou et al. — Techneglas (PDF)](https://www.techneglas.com/wp-content/uploads/2021/12/Yanan-Hou-Performance-of-a-Carbon-FiberPolysiloxane-Composite-Thermal-Ablation-Flammability-and-Mechanical-Characterization.pdf) |
| Odporność na pękanie K_IC | **2,52** ±0,2 | MPa·m^0.5 | [PMC11945185 (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11945185/) — otwarty dostęp |
| Gęstość | **1 320** | kg/m³ | [McDermott et al., J. Compos. Mater. (2022)](https://doi.org/10.1177/00219983211038622) · [Sci-Hub](https://sci-hub.pl/10.1177/00219983211038622) |
| Uzysk węglowy (1000 °C) | **86,5** | % | [Tate et al. — Techneglas (PDF)](https://www.techneglas.com) |

### Właściwości termiczne

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Przewodnictwo cieplne k | **0,21** ±0,03 | W/m·K | [McDermott et al., J. Compos. Mater. (2022)](https://doi.org/10.1177/00219983211038622) · [Sci-Hub](https://sci-hub.pl/10.1177/00219983211038622) |
| Pojemność cieplna Cp | **1 400** | J/kg·K | [McDermott et al., J. Compos. Mater. (2022)](https://doi.org/10.1177/00219983211038622) · [Sci-Hub](https://sci-hub.pl/10.1177/00219983211038622) |
| Zakres temperatur | **−60 … +1400** | °C | [Hou et al. — Techneglas (PDF)](https://www.techneglas.com/wp-content/uploads/2021/12/Yanan-Hou-Performance-of-a-Carbon-FiberPolysiloxane-Composite-Thermal-Ablation-Flammability-and-Mechanical-Characterization.pdf) |

### Wykresy

![A — krzywa naprężenie–odkształcenie M6](plots/m6_A_stress_strain.png)

![B — UTS vs. temperatura M6](plots/m6_B_uts_vs_temp.png)

*Wyjątkowe zachowanie — UTS zachowuje 33% wartości RT nawet w 1400 °C. Źródło: Hou et al. Techneglas.*

![C — moduł Younga vs. temperatura M6](plots/m6_C_modulus_vs_temp.png)

![D — przewodnictwo cieplne vs. temperatura M6](plots/m6_D_thermal_cond_vs_temp.png)

---

## 8. M7 — Kevlar / Włókno aramidowe (Kevlar-29 i Kevlar-49)

### Charakterystyka

Kevlar (DuPont, poli-*p*-fenylenotereftaloamid) to włókno aramidowe o najwyższej wytrzymałości właściwej spośród wszystkich 13 analizowanych materiałów. Dwa stopnie: Kevlar-29 (wyższa ciągliwość) i Kevlar-49 (wyższy moduł). Stosowany w zbiornikach ciśnieniowych, tarczach Whipple'a (MMOD), strukturach nośnych.

### Właściwości mechaniczne (T = 23 °C)

| Właściwość | Kevlar-29 | Kevlar-49 | Jednostka | Źródło |
|---|---|---|---|---|
| Wytrzymałość na rozciąganie (UTS) | **3 600** ±200 | **3 800** ±200 | MPa | [DuPont Kevlar Technical Guide (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/Kevlar_Technical_Guide.pdf); [MatWeb Kevlar 29](https://www.matweb.com/search/datasheettext.aspx?matguid=7f0915e45f3b490db5e5e88c75d2e8b0) |
| Moduł Younga (E) | **70,5** ±2 | **125** ±5 | GPa | [DuPont Kevlar Technical Guide (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/Kevlar_Technical_Guide.pdf) |
| Wydłużenie przy zerwaniu | **3,6** ±0,2 | **2,4** ±0,2 | % | [DuPont Kevlar Technical Guide (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/Kevlar_Technical_Guide.pdf) |
| Odporność na pękanie K_IC | — | — | — | Nie definiowana dla włókna |
| Gęstość | **1 440** | **1 440** | kg/m³ | [DuPont Kevlar Technical Guide (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/Kevlar_Technical_Guide.pdf) |

### Właściwości termiczne

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Przewodnictwo cieplne k (poprzeczne) | **0,04** | W/m·K | [Ventura & Martelli, Cryogenics (2009)](https://doi.org/10.1016/j.cryogenics.2009.04.001) · [Sci-Hub](https://sci-hub.pl/10.1016/j.cryogenics.2009.04.001) |
| Pojemność cieplna Cp | **1 420** | J/kg·K | [PMC12349578 (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12349578/) — otwarty dostęp |
| Zakres temperatur | **−196 … +430** | °C | [DuPont Kevlar Technical Guide (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/Kevlar_Technical_Guide.pdf) |

### Wykresy

![A — krzywa naprężenie–odkształcenie M7](plots/m7_A_stress_strain.png)

*K-29: wyższe wydłużenie (3,6%), K-49: wyższy moduł (125 GPa) przy nieco wyższym UTS. Źródło: DuPont Technical Guide.*

![B — UTS vs. temperatura M7](plots/m7_B_uts_vs_temp.png)

*Wyjątkowa stabilność — UTS zachowuje >75% od −196 do +430 °C. Źródło: DuPont Technical Guide; PMC12349578.*

![C — moduł Younga vs. temperatura M7](plots/m7_C_modulus_vs_temp.png)

![D — przewodnictwo cieplne vs. temperatura M7](plots/m7_D_thermal_cond_vs_temp.png)

*Dane kriogeniczne z [Ventura & Martelli, Cryogenics (2009)](https://doi.org/10.1016/j.cryogenics.2009.04.001) — k → 0,007 W/m·K przy 7 K.*

---

## 9. M8 — Mylar / BoPET (Folia PET)

### Charakterystyka

Mylar (DuPont Teijin Films) to dwuosiowo orientowana folia BoPET. Powszechnie stosowana w wielowarstwowych izolatorach termicznych (MLI), jako substrat folii złotej/aluminowej i jako osłona EMI. Ograniczenie: Tg ~80 °C, topnienie 254–260 °C.

### Właściwości mechaniczne (T = 23 °C)

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Wytrzymałość na rozciąganie (UTS) | **200** ±10 | MPa | [DuPont Teijin Films — Mylar A datasheet (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/DFC-H-81479-Mylar-A-Data-Sheet.pdf) |
| Moduł Younga (E) | **3,95** ±0,15 | GPa | [DuPont Teijin Films — Mylar A datasheet (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/DFC-H-81479-Mylar-A-Data-Sheet.pdf) |
| Granica plastyczności σ_y | **67,5** ±12,5 | MPa | [AZoM ID:2047](https://www.azom.com/article.aspx?ArticleID=2047) |
| Wydłużenie przy zerwaniu | **137,5** ±22,5 | % | [DuPont Teijin Films — Mylar A datasheet (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/DFC-H-81479-Mylar-A-Data-Sheet.pdf) |
| Odporność na pękanie K_IC | ~3,5 ±1,5 | MPa·m^0.5 | [AZoM ID:2047](https://www.azom.com/article.aspx?ArticleID=2047) — szacunek (bulk PET 2–5 MPa·m^0.5) |
| Gęstość | **1 395** | kg/m³ | [DuPont Teijin Films — Mylar A datasheet (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/DFC-H-81479-Mylar-A-Data-Sheet.pdf) |

### Właściwości termiczne

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Przewodnictwo cieplne k | **0,15** | W/m·K | [Thermtest — BoPET/Mylar](https://thermtest.com/polyethylene-terephthalate-pet) |
| Pojemność cieplna Cp | **1 275** | J/kg·K | [DuPont Teijin Films — Mylar A datasheet (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/DFC-H-81479-Mylar-A-Data-Sheet.pdf) |
| Zakres temperatur | **−70 … +150** | °C | [DuPont Teijin Films — Mylar A datasheet (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/DFC-H-81479-Mylar-A-Data-Sheet.pdf) |

### Wykresy

![A — krzywa naprężenie–odkształcenie M8](plots/m8_A_stress_strain.png)

*Model półciągliwy: granica plastyczności przy 67,5 MPa, utwardzanie do 200 MPa przy 137,5%.*

![B — UTS vs. temperatura M8](plots/m8_B_uts_vs_temp.png)

*Silny spadek UTS powyżej 80 °C (Tg PET). Źródło: DuPont Teijin datasheet.*

![C — moduł Younga vs. temperatura M8](plots/m8_C_modulus_vs_temp.png)

![D — przewodnictwo cieplne vs. temperatura M8](plots/m8_D_thermal_cond_vs_temp.png)

---

## 10. M9 — UHMWPE (Polietylen o ultra-wysokiej masie cząsteczkowej)

### Charakterystyka

UHMWPE (Ultra-High Molecular Weight Polyethylene) — masa cząsteczkowa 3,5–7,5 × 10⁶ g/mol. Najlżejszy materiał spośród 13 (940 kg/m³). Przy RT balistyczne parametry ochrony przewyższają Kevlar. **Kluczowe ograniczenie:** T_topnienia ~135 °C — już przy 80 °C traci ~75% wytrzymałości. Podatny na AO (brak grup aromatycznych w łańcuchu).

### Właściwości mechaniczne (T = 23 °C)

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Wytrzymałość na rozciąganie (UTS) | **200** ±50 | MPa | [Kurtz (ed.), UHMWPE Biomaterials Handbook, Elsevier (2009), rozdz. 2](https://doi.org/10.1016/B978-0-12-374721-1.00002-7) · [Sci-Hub](https://sci-hub.pl/10.1016/B978-0-12-374721-1.00002-7) |
| Moduł Younga (E) | **0,9** ±0,1 | GPa | [Sobieraj & Rimnac, J. Mech. Behav. Biomed. Mater. (2009)](https://doi.org/10.1016/j.jmbbm.2008.07.002) · [Sci-Hub](https://sci-hub.pl/10.1016/j.jmbbm.2008.07.002) |
| Granica plastyczności σ_y | **25** ±3 | MPa | [Sobieraj & Rimnac, J. Mech. Behav. Biomed. Mater. (2009)](https://doi.org/10.1016/j.jmbbm.2008.07.002) · [Sci-Hub](https://sci-hub.pl/10.1016/j.jmbbm.2008.07.002) |
| Wydłużenie przy zerwaniu | **350** ±50 | % | [AZoM ID:1831 — UHMWPE](https://www.azom.com/article.aspx?ArticleID=1831) |
| Odporność na pękanie K_IC | ~2,0 | MPa·m^0.5 | [Sobieraj & Rimnac, J. Mech. Behav. Biomed. Mater. (2009)](https://doi.org/10.1016/j.jmbbm.2008.07.002) · [Sci-Hub](https://sci-hub.pl/10.1016/j.jmbbm.2008.07.002) |
| Gęstość | **940** | kg/m³ | [AZoM ID:1831](https://www.azom.com/article.aspx?ArticleID=1831) |

### Właściwości termiczne

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Przewodnictwo cieplne k | **0,44** | W/m·K | [AZoM ID:1831](https://www.azom.com/article.aspx?ArticleID=1831) |
| Pojemność cieplna Cp | **1 850** | J/kg·K | [Kurtz (ed.), UHMWPE Biomaterials Handbook (2009)](https://doi.org/10.1016/B978-0-12-374721-1.00002-7) · [Sci-Hub](https://sci-hub.pl/10.1016/B978-0-12-374721-1.00002-7) |
| Zakres temperatur | **−150 … +80** | °C | [Google Doc — dane projektu](https://docs.google.com/document/d/1SUNR-o6LlR9Npx723FPGlJ8TDAnhCzqREIrAE7FIKa0/edit) — cytat: „at higher temperatures, UHMWPE performance declined below Kevlar" |

### Wykresy

![A — krzywa naprężenie–odkształcenie M9](plots/m9_A_stress_strain.png)

![B — UTS vs. temperatura M9](plots/m9_B_uts_vs_temp.png)

*Dramatyczny spadek UTS po 23 °C — materiał bardzo wrażliwy termicznie. Źródło: Kurtz ed. 2009.*

![C — moduł Younga vs. temperatura M9](plots/m9_C_modulus_vs_temp.png)

![D — przewodnictwo cieplne vs. temperatura M9](plots/m9_D_thermal_cond_vs_temp.png)

---

## 11. M10 — Kompozyt PE (Włókno UHMWPE / osnowa polimerowa)

### Charakterystyka

Laminaty z włókien UHMWPE (Dyneema SK75/SK76, Spectra 1000) zalane żywicą epoksydową lub HDPE. Drastycznie wyższe właściwości mechaniczne niż lity UHMWPE. Najniższa gęstość wśród kompozytów (≈1000 kg/m³). Temperatura pracy ograniczona osnową do ~120 °C.

### Właściwości mechaniczne (T = 23 °C)

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Wytrzymałość na rozciąganie (UTS) | **400** ±50 | MPa | [Koh et al., Int. J. Impact Eng. (2010)](https://doi.org/10.1016/j.ijimpeng.2009.11.010) · [Sci-Hub](https://sci-hub.pl/10.1016/j.ijimpeng.2009.11.010) |
| Moduł Younga (E) | **30** ±5 | GPa | [DSM Dyneema UD technical data](https://www.dsm.com/dyneema); [Koh et al. (2010)](https://doi.org/10.1016/j.ijimpeng.2009.11.010) · [Sci-Hub](https://sci-hub.pl/10.1016/j.ijimpeng.2009.11.010) |
| Wydłużenie przy zerwaniu | **1,5** | % | [Koh et al., Int. J. Impact Eng. (2010)](https://doi.org/10.1016/j.ijimpeng.2009.11.010) · [Sci-Hub](https://sci-hub.pl/10.1016/j.ijimpeng.2009.11.010) |
| Gęstość | **1 000** | kg/m³ | [DSM Dyneema UD technical data](https://www.dsm.com/dyneema) |

### Właściwości termiczne

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Przewodnictwo cieplne k | **0,35** | W/m·K | [AZoM ID:1831 — UHMWPE (matryca)](https://www.azom.com/article.aspx?ArticleID=1831) — szacunek kompozytowy |
| Pojemność cieplna Cp | **1 500** | J/kg·K | szacunek na bazie składowych (włókno + matryca HDPE) |
| Zakres temperatur | **−150 … +120** | °C | [DSM Dyneema UD technical data](https://www.dsm.com/dyneema) |

### Wykresy

![A — krzywa naprężenie–odkształcenie M10](plots/m10_A_stress_strain.png)

![B — UTS vs. temperatura M10](plots/m10_B_uts_vs_temp.png)

![C — moduł Younga vs. temperatura M10](plots/m10_C_modulus_vs_temp.png)

![D — przewodnictwo cieplne vs. temperatura M10](plots/m10_D_thermal_cond_vs_temp.png)

---

## 12. M11 — Kompozyt Kevlar (Kevlar / epoksyd)

### Charakterystyka

Laminat z tkaniny Kevlar-29/49 infuzowanej żywicą epoksydową (np. Hexcel 8552). Powszechnie stosowany w strukturze statków kosmicznych i rakiet nośnych. Zachowuje wysoką wytrzymałość przy niskich temperaturach; górna granica wyznaczona epoksydem (~180 °C).

### Właściwości mechaniczne (T = 23 °C)

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Wytrzymałość na rozciąganie (UTS) | **600** ±80 | MPa | [Duan et al., Int. J. Impact Eng. (2006)](https://doi.org/10.1016/j.ijimpeng.2005.07.007) · [Sci-Hub](https://sci-hub.pl/10.1016/j.ijimpeng.2005.07.007) |
| Moduł Younga (E) | **40** ±5 | GPa | [DuPont Kevlar Composite Design Guide (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/Kevlar_Design_Guide.pdf) |
| Wydłużenie przy zerwaniu | **1,8** | % | [Duan et al., Int. J. Impact Eng. (2006)](https://doi.org/10.1016/j.ijimpeng.2005.07.007) · [Sci-Hub](https://sci-hub.pl/10.1016/j.ijimpeng.2005.07.007) |
| Gęstość | **1 380** | kg/m³ | [DuPont Kevlar Composite Design Guide (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/Kevlar_Design_Guide.pdf) |

### Właściwości termiczne

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Przewodnictwo cieplne k | **0,12** | W/m·K | [DuPont Kevlar Technical Guide (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/Kevlar_Technical_Guide.pdf) |
| Pojemność cieplna Cp | **1 300** | J/kg·K | [DuPont Kevlar Technical Guide (PDF)](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/Kevlar_Technical_Guide.pdf) |
| Zakres temperatur | **−55 … +180** | °C | [Hexcel 8552 epoxy datasheet (PDF)](https://www.hexcel.com/user_upload/assets/datasheets/Prepreg_Data_Sheets/8552_eu.pdf) |

### Wykresy

![A — krzywa naprężenie–odkształcenie M11](plots/m11_A_stress_strain.png)

![B — UTS vs. temperatura M11](plots/m11_B_uts_vs_temp.png)

*Dobra stabilność UTS od −55 do +180 °C — Kevlar stabilizuje osnowę epoksydową. Źródło: Duan et al. 2006.*

![C — moduł Younga vs. temperatura M11](plots/m11_C_modulus_vs_temp.png)

![D — przewodnictwo cieplne vs. temperatura M11](plots/m11_D_thermal_cond_vs_temp.png)

---

## 13. M12 — Kompozyt fenolowy (Węgiel / Żywica fenolowa)

### Charakterystyka

Węglowo-fenolowe (C/Ph) kompozyty to **złoty standard ablacyjnego TPS** dla rakiet i misji powrotnych. Stosowane w dyszach SRB (Space Shuttle), ablatorach PICA (Stardust, MSL Curiosity), osłonach cieplnych pojazdów powrotnych. Najwyższa K_IC spośród wszystkich 13 materiałów dzięki zbrojeniu węglowemu (15 MPa·m^0.5).

### Właściwości mechaniczne (T = 23 °C)

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Wytrzymałość na rozciąganie (UTS) | **350** ±50 | MPa | [Natali et al., Compos. Part A (2012)](https://doi.org/10.1016/j.compositesa.2011.10.009) · [Sci-Hub](https://sci-hub.pl/10.1016/j.compositesa.2011.10.009) |
| Moduł Younga (E) | **35** ±5 | GPa | [Natali et al., Compos. Part A (2012)](https://doi.org/10.1016/j.compositesa.2011.10.009) · [Sci-Hub](https://sci-hub.pl/10.1016/j.compositesa.2011.10.009) |
| Wydłużenie przy zerwaniu | **0,8** | % | [Natali et al., Compos. Part A (2012)](https://doi.org/10.1016/j.compositesa.2011.10.009) · [Sci-Hub](https://sci-hub.pl/10.1016/j.compositesa.2011.10.009) |
| Odporność na pękanie K_IC | **15** ±3 | MPa·m^0.5 | [Tran et al., J. Thermophys. Heat Transfer (2014)](https://doi.org/10.2514/1.T4165) · [Sci-Hub](https://sci-hub.pl/10.2514/1.T4165) |
| Gęstość | **1 550** | kg/m³ | [Natali et al., Compos. Part A (2012)](https://doi.org/10.1016/j.compositesa.2011.10.009) · [Sci-Hub](https://sci-hub.pl/10.1016/j.compositesa.2011.10.009) |
| Uzysk węglowy (TGA 1000 °C) | **~70** | % | [Natali et al., Compos. Part A (2012)](https://doi.org/10.1016/j.compositesa.2011.10.009) · [Sci-Hub](https://sci-hub.pl/10.1016/j.compositesa.2011.10.009) |

### Właściwości termiczne

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Przewodnictwo cieplne k | **2,0** | W/m·K | [Tran et al., J. Thermophys. Heat Transfer (2014)](https://doi.org/10.2514/1.T4165) · [Sci-Hub](https://sci-hub.pl/10.2514/1.T4165) |
| Pojemność cieplna Cp | **1 400** | J/kg·K | [Tran et al., J. Thermophys. Heat Transfer (2014)](https://doi.org/10.2514/1.T4165) · [Sci-Hub](https://sci-hub.pl/10.2514/1.T4165) |
| Zakres temperatur | **−55 … >2000** | °C (ablacyjny) | [Natali et al., Compos. Part A (2012)](https://doi.org/10.1016/j.compositesa.2011.10.009) · [Sci-Hub](https://sci-hub.pl/10.1016/j.compositesa.2011.10.009) |

### Wykresy

![A — krzywa naprężenie–odkształcenie M12](plots/m12_A_stress_strain.png)

![B — UTS vs. temperatura M12](plots/m12_B_uts_vs_temp.png)

*Doskonałe zachowanie UTS — laminat węglowy stabilizuje strukturę nawet przy 2000 °C. Źródło: Natali et al. 2012.*

![C — moduł Younga vs. temperatura M12](plots/m12_C_modulus_vs_temp.png)

![D — przewodnictwo cieplne vs. temperatura M12](plots/m12_D_thermal_cond_vs_temp.png)

*k = 2 W/m·K — najwyższe z 13 materiałów; ważne dla odprowadzania ciepła z warstwy ablacyjnej. Źródło: Tran et al. 2014.*

---

## 14. M13 — Kompozyt polisiloksanowy II (Klasa ogólna)

### Charakterystyka

Szersza rodzina kompozytów na osnowie polisiloksanowej, obejmująca warianty zbrojone włóknem węglowym, szklanym lub krzemionkowym. Analogiczne do M6 lecz produkowane przez różnych wytwórców lub przy innym stosunku wzmocnienia. Uzysk węglowy ~80%, zakres T do 1200 °C.

### Właściwości mechaniczne (T = 23 °C)

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Wytrzymałość na rozciąganie (UTS) | **150** ±30 | MPa | [McDermott et al., J. Compos. Mater. (2022)](https://doi.org/10.1177/00219983211038622) · [Sci-Hub](https://sci-hub.pl/10.1177/00219983211038622) — wariant o niższym zbrojeniu |
| Moduł Younga (E) | **25** ±5 | GPa | [McDermott et al., J. Compos. Mater. (2022)](https://doi.org/10.1177/00219983211038622) · [Sci-Hub](https://sci-hub.pl/10.1177/00219983211038622) |
| Wydłużenie przy zerwaniu | **0,7** | % | [PMC11945185 (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11945185/) — otwarty dostęp |
| Odporność na pękanie K_IC | ~2,0 | MPa·m^0.5 | [PMC11945185 (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11945185/) — otwarty dostęp |
| Gęstość | **1 450** | kg/m³ | [McDermott et al., J. Compos. Mater. (2022)](https://doi.org/10.1177/00219983211038622) · [Sci-Hub](https://sci-hub.pl/10.1177/00219983211038622) |
| Uzysk węglowy | **~80** | % | [Tate et al. — Techneglas (PDF)](https://www.techneglas.com) |

### Właściwości termiczne

| Właściwość | Wartość | Jednostka | Źródło |
|---|---|---|---|
| Przewodnictwo cieplne k | **0,50** | W/m·K | [McDermott et al., J. Compos. Mater. (2022)](https://doi.org/10.1177/00219983211038622) · [Sci-Hub](https://sci-hub.pl/10.1177/00219983211038622) |
| Pojemność cieplna Cp | **1 300** | J/kg·K | [McDermott et al., J. Compos. Mater. (2022)](https://doi.org/10.1177/00219983211038622) · [Sci-Hub](https://sci-hub.pl/10.1177/00219983211038622) |
| Zakres temperatur | **−60 … +1200** | °C | [Hou et al. — Techneglas (PDF)](https://www.techneglas.com/wp-content/uploads/2021/12/Yanan-Hou-Performance-of-a-Carbon-FiberPolysiloxane-Composite-Thermal-Ablation-Flammability-and-Mechanical-Characterization.pdf) |

### Wykresy

![A — krzywa naprężenie–odkształcenie M13](plots/m13_A_stress_strain.png)

![B — UTS vs. temperatura M13](plots/m13_B_uts_vs_temp.png)

![C — moduł Younga vs. temperatura M13](plots/m13_C_modulus_vs_temp.png)

![D — przewodnictwo cieplne vs. temperatura M13](plots/m13_D_thermal_cond_vs_temp.png)

---

## 15. Zestawienie porównawcze wszystkich materiałów

### 15.1 Zestawienie tabelaryczne (RT = 23 °C)

| # | Materiał | UTS [MPa] | E [GPa] | ρ [kg/m³] | T_min [°C] | T_max [°C] | k [W/m·K] | K_IC [MPa·m^0.5] | Główne źródło |
|---|---|---|---|---|---|---|---|---|---|
| M1 | Kapton | 231 | 2,5 | 1 420 | −269 | 400 | 0,12 | 3,5 | [DuPont Kapton HN datasheet](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/EI-10142_Kapton-HN-datasheet.pdf) |
| M2 | POSS-PI | 210 | 2,3 | 1 450 | −269 | 450 | 0,15 | 2,0 | [Brunsvold et al. (2004)](https://doi.org/10.1177/0954008304024680) · [Sci-Hub](https://sci-hub.pl/10.1177/0954008304024680) |
| M3 | Fen. żywica | 45 | 3,5 | 1 250 | −55 | 2 000* | 0,30 | 0,7 | [AZoM ID:475](https://www.azom.com/article.aspx?ArticleID=475); [Natali et al. (2012)](https://doi.org/10.1016/j.compositesa.2011.10.009) |
| M4 | Ftalonitryl | 65 | 4,0 | 1 250 | −55 | 375 | 0,20 | 1,0 | [Hergenrother et al. (2005)](https://doi.org/10.1016/j.polymer.2005.09.039) · [Sci-Hub](https://sci-hub.pl/10.1016/j.polymer.2005.09.039) |
| M5 | RTV Silikon | 6 | 0,003 | 1 175 | −115 | 300 | 0,25 | — | [AZoM ID:920](https://www.azom.com/properties.aspx?ArticleID=920); [MatWeb RTV566](https://www.matweb.com/search/datasheettext.aspx?matguid=70466aea960a4c84be3bbc5045c219aa) |
| M6 | Komp. Polisil. | 182 | 45,5 | 1 320 | −60 | 1 400* | 0,21 | 2,52 | [McDermott et al. (2022)](https://doi.org/10.1177/00219983211038622) · [Sci-Hub](https://sci-hub.pl/10.1177/00219983211038622) |
| M7a | Kevlar-29 | 3 600 | 70,5 | 1 440 | −196 | 430 | 0,04 | — | [DuPont Kevlar Tech. Guide](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/Kevlar_Technical_Guide.pdf) |
| M7b | Kevlar-49 | 3 800 | 125 | 1 440 | −196 | 430 | 0,04 | — | [DuPont Kevlar Tech. Guide](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/Kevlar_Technical_Guide.pdf) |
| M8 | Mylar BoPET | 200 | 3,95 | 1 395 | −70 | 150 | 0,15 | 3,5 | [DuPont Teijin Mylar A datasheet](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/DFC-H-81479-Mylar-A-Data-Sheet.pdf) |
| M9 | UHMWPE | 200 | 0,9 | 940 | −150 | 80 | 0,44 | 2,0 | [Kurtz ed. (2009)](https://doi.org/10.1016/B978-0-12-374721-1.00002-7); [Sobieraj & Rimnac (2009)](https://doi.org/10.1016/j.jmbbm.2008.07.002) |
| M10 | Komp. PE | 400 | 30 | 1 000 | −150 | 120 | 0,35 | — | [Koh et al. (2010)](https://doi.org/10.1016/j.ijimpeng.2009.11.010); [DSM Dyneema UD](https://www.dsm.com/dyneema) |
| M11 | Komp. Kevlar | 600 | 40 | 1 380 | −55 | 180 | 0,12 | — | [Duan et al. (2006)](https://doi.org/10.1016/j.ijimpeng.2005.07.007); [Hexcel 8552](https://www.hexcel.com/user_upload/assets/datasheets/Prepreg_Data_Sheets/8552_eu.pdf) |
| M12 | Komp. fen. | 350 | 35 | 1 550 | −55 | 2 000* | 2,00 | 15 | [Natali et al. (2012)](https://doi.org/10.1016/j.compositesa.2011.10.009); [Tran et al. (2014)](https://doi.org/10.2514/1.T4165) |
| M13 | Komp. Polisil. II | 150 | 25 | 1 450 | −60 | 1 200* | 0,50 | 2,0 | [McDermott et al. (2022)](https://doi.org/10.1177/00219983211038622); [PMC11945185](https://pmc.ncbi.nlm.nih.gov/articles/PMC11945185/) |

*\* T_max dla materiałów ablacyjnych oznacza skuteczną ochronę ablacyjną, nie ciągłą pracę strukturalną.*

### 15.2 Wykresy porównawcze

![Porównanie UTS](plots/compare_A_uts.png)

*Kevlar-49 i Kevlar-29 dominują o rząd wielkości nad pozostałymi.*

![Porównanie modułu Younga](plots/compare_B_modulus.png)

*Kevlar-49 (125 GPa) — najsztywniejszy. M5 RTV (3 MPa) — najmiększy.*

![Porównanie gęstości](plots/compare_C_density.png)

*UHMWPE (940 kg/m³) jest jedynym materiałem lżejszym od wody.*

![Zakresy temperatur pracy](plots/compare_D_temp_range.png)

*Materiały ablacyjne (M3, M6, M12, M13) pokrywają największy zakres. Krytyczny próg LEO (−150…+150 °C) zaznaczono punktowanymi liniami.*

![Wytrzymałość właściwa](plots/compare_E_spec_strength.png)

*Kevlar zdecydowanie dominuje — wytrzymałość właściwa 2,5 km²/s².*

---

## 16. Rekomendacja — Top 5 najlepszych materiałów ochronnych

### Metodologia oceny

| Kryterium | Waga | Uzasadnienie |
|---|---|---|
| Wytrzymałość właściwa (UTS/ρ) | 25% | Minimalizacja masy przy danej nośności |
| Zakres temperatur (T_max − T_min) | 20% | Pokrycie obu faz misji |
| Odporność na AO i UV | 20% | Degradacja powierzchniowa na LEO |
| Zdolność absorpcji ciepła (TPS/ablacja) | 20% | Start i ewentualny powrót |
| Odporność na pękanie K_IC / udarność | 15% | MMOD, drgania startowe |

### Wynik — Top-5

![Wykres radarowy Top-5](plots/compare_F_radar_top5.png)

---

### 🥇 1. Kapton / Poliimid HN (M1)

**Zastosowania:** folie MLI, substrat PCB, ekrany termiczne, przewody elastyczne

**Argumenty:**
- **Heritage kosmiczny 60+ lat** — jedyny materiał użyty na każdej misji od Apollo po JWST. Perfekcyjnie zbadany w środowisku kosmicznym
- **Zakres temperatur −269…+400 °C** pokrywa kriogeniczne podłoże zbiornika paliwa i nagrzewanie aerodynamiczne
- **Zero pełzania** i zero outgassingu w próżni — nie zanieczyszcza optyki i czujników (źródło: [DuPont Kapton HN datasheet](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/EI-10142_Kapton-HN-datasheet.pdf))
- **Odporność na promieniowanie** (γ, elektrony, protony) — certyfikowany do 10⁸ rad (źródło: [Google Doc — dane projektu](https://docs.google.com/document/d/1SUNR-o6LlR9Npx723FPGlJ8TDAnhCzqREIrAE7FIKa0/edit))
- **Ograniczenie:** erozja AO ~3×10⁻²⁴ cm³/atom — wymaga powłoki Al lub SiO₂ na stronach eksponowanych

---

### 🥈 2. Kevlar-29 / Kevlar-49 (M7)

**Zastosowania:** zbiorniki ciśnieniowe, tarcze Whipple'a, struktury nośne, preformy TPS

**Argumenty:**
- **Najwyższa wytrzymałość właściwa** ze wszystkich 13 materiałów: UTS/ρ = 2 500 kN·m/kg (źródło: [DuPont Kevlar Technical Guide](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/Kevlar_Technical_Guide.pdf))
- **Stabilność termiczna −196…+430 °C** — zachowuje >75% UTS w całym tym zakresie (źródło: [PMC12349578 (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12349578/))
- **Ochrona MMOD (Whipple shield):** tkanina Kevlaru jako tylna przeszkoda absorbuje resztki uderzenia; standard ISS i sond kosmicznych (źródło: [Duan et al. Int. J. Impact Eng. 2006](https://doi.org/10.1016/j.ijimpeng.2005.07.007) · [Sci-Hub](https://sci-hub.pl/10.1016/j.ijimpeng.2005.07.007))
- **Zbiorniki ciśnieniowe:** standardowe zbiorniki helowe i N₂ w satelitach to laminaty K-49

---

### 🥉 3. Kompozyt polisiloksanowy (M6)

**Zastosowania:** ablacyjny TPS stopni rakietowych, izolacja cieplna dyszy, pokrycia wejścia w atmosferę

**Argumenty:**
- **Zakres T −60…+1400 °C** — najszerszy po węglowych ablatorach; unikalny dla organiku (źródło: [Hou et al. Techneglas](https://www.techneglas.com/wp-content/uploads/2021/12/Yanan-Hou-Performance-of-a-Carbon-FiberPolysiloxane-Composite-Thermal-Ablation-Flammability-and-Mechanical-Characterization.pdf))
- **Uzysk węglowy 86,5%** — po pirolizie zachowuje integralność jako ceramika SiOC (źródło: [Tate et al. Techneglas](https://www.techneglas.com))
- **Odporność na AO** lepsza niż Kapton — pasywacja SiO₂ jest trwalsza (źródło: [McDermott et al. J. Compos. Mater. 2022](https://doi.org/10.1177/00219983211038622) · [Sci-Hub](https://sci-hub.pl/10.1177/00219983211038622))
- **Właściwości mechaniczne** (UTS 182 MPa, E 45,5 GPa) umożliwiają zastosowania strukturalno-ablacyjne (źródło: [PMC11945185 (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11945185/))

---

### 4. Kompozyt węglowo-fenolowy (M12)

**Zastosowania:** dysze SRB, TPS wejścia w atmosferę, pokrycia silnikowe

**Argumenty:**
- **Najwyższe K_IC = 15 MPa·m^0.5** (o rząd wyższe niż poliimidy) — jedyny materiał z listy łączący ablacyjność z odpornością na pękanie (źródło: [Tran et al. J. Thermophys. Heat Transfer 2014](https://doi.org/10.2514/1.T4165) · [Sci-Hub](https://sci-hub.pl/10.2514/1.T4165))
- **Ablacja do >2000 °C** — niezbędne dla komory spalania i dyszy (źródło: [Natali et al. Compos. Part A 2012](https://doi.org/10.1016/j.compositesa.2011.10.009) · [Sci-Hub](https://sci-hub.pl/10.1016/j.compositesa.2011.10.009))
- **k = 2 W/m·K** — umożliwia aktywne odprowadzanie ciepła przez warstwę zwęgloną (źródło: Tran et al. 2014)

---

### 5. POSS-Poliimid (M2)

**Zastosowania:** zewnętrzne folie MLI dla długoterminowych misji LEO, powłoki antystatyczne

**Argumenty:**
- **Lepsza odporność na AO** niż Kapton — nanocząstki POSS tworzą powłokę SiO₂ in situ, która samoregeneruje się po mikroerozji (źródło: [Brunsvold et al. High Perform. Polym. 2004](https://doi.org/10.1177/0954008304024680) · [Sci-Hub](https://sci-hub.pl/10.1177/0954008304024680))
- **T_max = 450 °C** (+50 °C vs. Kapton) przy analogicznych właściwościach mechanicznych (źródło: [Gouzman et al. Acta Astronaut. 2010](https://doi.org/10.1016/j.actaastro.2010.09.010) · [Sci-Hub](https://sci-hub.pl/10.1016/j.actaastro.2010.09.010))
- **Kluczowe dla 10+ lat misji LEO** — tlenowanie AO na 400 km jest ~10× agresywniejsze niż na 600 km
- Niskie outgassing — ASTM E595 (TML < 1%) — klasa zbliżona do Kaptonu

---

### Podsumowanie rekomendacji

| Ranga | Materiał | Główna rola | Kluczowa przewaga | Główne źródła |
|---|---|---|---|---|
| 🥇 | **Kapton (M1)** | Folie termiczne, substrat | Heritage, zakres T, promieniowanie | [DuPont datasheet](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/EI-10142_Kapton-HN-datasheet.pdf) |
| 🥈 | **Kevlar-29/49 (M7)** | Struktura, zbiorniki, MMOD | Wytrzymałość właściwa 2,5 km²/s² | [DuPont Tech. Guide](https://www.dupont.com/content/dam/dupont/amer/us/en/products/ei-transformation/documents/Kevlar_Technical_Guide.pdf) |
| 🥉 | **Komp. Polisiloks. (M6)** | TPS ablacyjny, izolacja | T_max 1400 °C, uzysk 86,5% | [McDermott et al. 2022](https://doi.org/10.1177/00219983211038622) |
| 4 | **Komp. fenolowy (M12)** | Dysze, TPS wejścia | K_IC 15 MPa·m^0.5, T > 2000 °C | [Natali et al. 2012](https://doi.org/10.1016/j.compositesa.2011.10.009); [Tran et al. 2014](https://doi.org/10.2514/1.T4165) |
| 5 | **POSS-Poliimid (M2)** | Folie na LEO długoterm. | Odporność AO, T_max +50 °C vs. M1 | [Brunsvold et al. 2004](https://doi.org/10.1177/0954008304024680) |

---

## 17. Wnioski

1. **M9 (UHMWPE) i M10 (Komp. PE)** wykluczone z aplikacji termicznych (T_max ≤ 120 °C) — nadają się wyłącznie do zimnych komponentów i osłon MMOD w zacienionych orbitach.
2. **M8 (Mylar BoPET)** pełni wartościową rolę pomocniczą jako reflektor w MLI, jednak T_max = 150 °C wyklucza go z TPS.
3. **M5 (RTV Silikon)** niezastąpiony jako uszczelnienie i klej — żaden inny materiał z listy nie daje zakresu T przy wydłużeniu 400%.
4. **M4 (Ftalonitryl)** wyróżnia się stałym UTS do 375 °C przy zerowym outgassingu — obiecujący dla elementów w układzie napędowym.
5. **Hierarchia dla ochrony:** M12 > M6 (ablacja) → M7 (struktura/MMOD) → M1/M2 (folie/substrat) → M5 (uszczelnienia).

---

*Wykresy wygenerowano skryptem `plots/generate_plots_all.py`. Dane dla M5–M8 — szczegółowe źródła w `../Filip/raport_filip.md`. Dane dla M1 — DuPont Kapton HN datasheet + [Google Doc — dane projektu](https://docs.google.com/document/d/1SUNR-o6LlR9Npx723FPGlJ8TDAnhCzqREIrAE7FIKa0/edit).*
