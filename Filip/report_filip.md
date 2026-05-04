# Material Properties Report — Filip's Assignment (M5–M8)
## *A comparison of selected organic materials for low orbiting spacecraft*

**Author:** Filip Zdrojewski  
**Date:** 2026-05-05  
**Scope:** Materials M5–M8 (Silicone Rubber/RTV · Polysiloxane Composite · Kevlar · Mylar/BoPET)

---

## 1. Introduction

This report summarises the key mechanical and thermal properties of four organic/hybrid material groups assigned to Filip for the paper *"A comparison of selected organic materials for low orbiting spacecraft"*. Data were collected from peer-reviewed journal articles, manufacturer datasheets, and curated materials databases. All values are referenced to their primary source.

The materials covered are:

| ID | Material | Category |
|---|---|---|
| M5 | Silicone Rubber / RTV (Room Temperature Vulcanizing) | Organico-inorganic hybrid — elastomeric |
| M6 | Polysiloxane Matrix Composite (CF/UHTR, SiO₂f/SiO₂) | Organico-inorganic hybrid — ablative composite |
| M7 | Kevlar®-29 / Kevlar®-49 (Aramid Fiber) | Structural reinforcement — high-strength fiber |
| M8 | Mylar® / BoPET Film (Biaxially Oriented PET) | Structural film — thermal blankets (MLI) |

---

## 2. Properties Sought

For each material the following properties were collected:

1. **Ultimate Tensile Strength (UTS)** — stress at fracture [MPa]
2. **Young's Modulus (E)** — elastic stiffness [GPa or MPa]
3. **Yield Strength (σ_y)** — onset of plastic deformation [MPa] *(where applicable)*
4. **Stress–Strain Behaviour** — curve type; combined yield/UTS plot per material
5. **Thermal Conductivity (k)** [W/m·K]
6. **Specific Heat Capacity (c_p)** [J/kg·K]
7. **Operating Temperature Range** [°C]
8. **Fracture Toughness (K_IC)** [MPa·m⁰·⁵] *(where characterised)*
9. **Density (ρ)** [kg/m³]
10. **Heat of Ablation / Mass Loss Rate** *(where applicable)*

---

## 3. M5 — Silicone Rubber / RTV

### 3.1 Material Description

Room Temperature Vulcanizing (RTV) silicones are polydimethylsiloxane (PDMS)-based elastomers cross-linked at ambient temperature. In spacecraft applications, aerospace-grade formulations such as **RTV 566** (Momentive/GE) are used as adhesives, sealants, potting compounds, and vibration-damping mounts. Key characteristics are extreme flexibility, chemical inertness, and stability across a wide temperature range.

### 3.2 Mechanical Properties

| Property | Value | Unit | Notes / Source |
|---|---|---|---|
| Ultimate Tensile Strength | 2–10 (typical **6**) | MPa | Filled grades; AZoM ID:920; MatWeb Silicone RTV |
| Young's Modulus (E) | **1–5** | MPa | Elastomeric — 3–4 orders of magnitude below metals |
| Yield Strength (σ_y) | — | — | **Not applicable** — elastomers have no yield point |
| Elongation at Break | 100–800 (typical **400**) | % | AZoM ID:920; Nagase Chemtex datasheet |
| Fracture Toughness K_IC | — | — | Elastomers characterised by tear energy, not K_IC |

> **Stress–Strain behaviour:** Highly non-linear elastomeric (hyperelastic). No yield point. Behaves according to Neo-Hookean / Mooney-Rivlin models. Deforms reversibly up to several hundred percent strain.

**Temperature dependence of modulus (Wegner et al., 2018):**

| Temperature | Modulus | Notes |
|---|---|---|
| +23 °C (RT) | 1–2.5 MPa | Baseline |
| −75 °C | Rising sharply | Crystallisation onset |
| −80 °C | Up to ~40× RT value | Crystallisation confirmed |
| −115 °C (T_g) | Glass transition | Material becomes rigid/glassy |

### 3.3 Thermal Properties

| Property | Value | Unit | Source |
|---|---|---|---|
| Thermal Conductivity | **0.20–0.30** | W/m·K | Barucci et al., *Cryogenics* 38 (1998) 227 |
| Specific Heat Capacity | **1 300–1 500** | J/kg·K | Wegner et al., *Int. J. Adhesion* (2018) |
| Operating Temperature | **−115 to +300** | °C | Standard grades up to +200 °C; T_g at −115 °C |
| Density | **1 100–1 250** | kg/m³ | AZoM ID:920; MatWeb |

### 3.4 Ablation / Mass Loss

Not applicable for standard RTV formulations. Silicone ablatives (different formulation) produce ~63–86% SiO₂/SiC char yield.

### 3.5 Key References
- Barucci, M. *et al.* (1998). Thermal conductivity of a RTV silicone elastomer between 1.2 and 300 K. *Cryogenics*, **38**, 227. https://doi.org/10.1016/S0011-2275(97)00146-X
- Wegner, P. *et al.* (2018). Thermomechanical Behaviour of Aerospace-grade RTV. *Int. J. Adhesion and Adhesives*. https://doi.org/10.1016/j.ijadhadh.2018.07.012
- MatWeb. Momentive RTV 566. https://www.matweb.com
- SpaceMat Database. RTV 566. https://www.spacematdb.com
- AZoM. Overview of Materials for Silicone Rubber. Article ID:920. https://www.azom.com

---

## 4. M6 — Polysiloxane Matrix Composite

### 4.1 Material Description

Polysiloxane matrices are silicon-oxygen backbone pre-ceramic resins used in Thermal Protection System (TPS) composites. Key systems are:

- **CF/UHTR (Carbon Fibre / Ultra-High Temperature Resin)** — Hou et al. / Techneglas
- **2.5D Silica/Polysiloxane** — McDermott et al. 2022 (*J. Composite Materials*)
- **SiO₂f/SiO₂** — derived from polysiloxane ceramic precursors (PMC11945185, 2025)

On heating, the matrix pyrolyses (300–550 °C) into an amorphous SiO₂/Si–O–C ceramic char, making these materials suitable for high-temperature ablative applications.

### 4.2 Mechanical Properties

| Property | Value | Unit | Notes / Source |
|---|---|---|---|
| UTS (2.5D SiO₂/polysiloxane composite) | **182 ± 9.6** | MPa | McDermott et al., *J. Composite Mater.* (2022) |
| UTS (nanoporous silicone composite) | 13–42.9 | MPa | ScienceDirect (2025) |
| UTS (SiO₂f/SiO₂ flexural) | 63.3 | MPa | PMC11945185 (2025) |
| Young's Modulus (CF/UHTR laminate) | **45.5** | GPa | Hou et al., Techneglas (6.6 Msi) |
| Yield Strength | — | — | Not defined; brittle failure |
| Elongation at Break (CF/UHTR) | **0.97** | % | Hou et al., Techneglas |
| Fracture Toughness K_IC (SiO₂f/SiO₂) | **2.52** | MPa·m⁰·⁵ | PMC11945185 (2025) |
| Density | 400–1 340 | kg/m³ | Depends on formulation; McDermott: ~1 320 kg/m³ |

### 4.3 Thermal Properties

| Property | Value | Unit | Source |
|---|---|---|---|
| Thermal Conductivity (2.5D composite) | **0.21** | W/m·K | McDermott et al. (2022) — 58.8% lower than reference |
| Thermal Conductivity (nanoporous) | 0.033–0.07 | W/m·K | ScienceDirect (2025) |
| Thermal Conductivity (S/UHTR, 149–260 °C) | 0.63–0.65 | W/m·K | Tate et al., Techneglas |
| Specific Heat Capacity | ~1 300–1 500 | J/kg·K | Estimated from neat silicone data |
| Operating Temperature (char form) | up to **+1 400** | °C | Pyrolysis zone 300–550 °C; char stable >1 200 °C |

### 4.4 Ablation / Mass Loss Rate

| Property | Value | Unit | Source |
|---|---|---|---|
| Mass Loss Rate (F1 formulation) | **0.021** | g/s | Tate et al., Techneglas |
| Linear Recession Rate (F1) | **0.031** | mm/s | Tate et al., Techneglas |
| Char Yield — neat UHTR resin (TGA 1 000 °C) | **86.5** | % | Hou et al., Techneglas |
| Char Yield — composite samples | 95.8–97.5 | % | Hou et al., Techneglas |

### 4.5 Key References
- McDermott, R.M., Tate, J.S., & Koo, J.H. (2022). Exploration of a new affordable TPS utilising 2.5D silica/polysiloxane composite. *J. Composite Materials*, **56**, 685. https://doi.org/10.1177/00219983211038622
- Hou, Y. *et al.* Performance of a Carbon Fibre/Polysiloxane Composite Thermal Ablative. Techneglas. https://www.techneglas.com
- Tate, J.S. *et al.* Experimental Characterisation of Novel Silica/Polysiloxane Ablative. Techneglas. https://www.techneglas.com
- PMC11945185 (2025). Performance Optimisation of SiO₂f/SiO₂ Composites Derived from Polysiloxane Ceramic Precursors. https://pmc.ncbi.nlm.nih.gov/articles/PMC11945185/

---

## 5. M7 — Kevlar® / Aramid Fiber (Kevlar-29 and Kevlar-49)

### 5.1 Material Description

Kevlar® (DuPont) is a para-aramid synthetic fiber. Two grades are used in spacecraft:

- **Kevlar-29**: standard grade; excellent impact/ballistic resistance; used in debris shielding (Whipple shields)
- **Kevlar-49**: high-modulus grade; stiffer (~78% higher E than K-29); used in structural composites and pressure vessels

Both grades are **linearly elastic to failure** — no yield plateau. Failure is sudden and brittle with fibrillation.

### 5.2 Mechanical Properties

| Property | Kevlar-29 | Kevlar-49 | Unit | Source |
|---|---|---|---|---|
| Ultimate Tensile Strength | **3 600** | **3 000–3 800** | MPa | MatWeb; DuPont Tech Guide |
| Young's Modulus (E) | **70–70.5** | **112–131** | GPa | MatWeb; DuPont datasheet |
| Yield Strength | — | — | — | **Not applicable** — brittle linear elastic |
| Elongation at Break | **3.6** | **2.4** | % | DuPont; SubsTech |
| Fracture Toughness | — | — | — | Not classically characterised for fiber |
| Density | **1 440** | **1 440** | kg/m³ | MatWeb; DuPont |

> **Stress–Strain behaviour:** Linear elastic to failure (no yield). High specific strength (UTS/ρ) makes Kevlar one of the best structural fibres per unit mass.

### 5.3 Thermal Properties

| Property | Value | Unit | Source |
|---|---|---|---|
| Thermal Conductivity (transverse, RT) | **0.04** | W/m·K | Ventura & Martelli, *Cryogenics* 49 (2009) 509 |
| Thermal Conductivity (axial) | **3.5–4.0** | W/m·K | Highly anisotropic |
| Specific Heat Capacity | **1 420** | J/kg·K | material-properties.org/kevlar |
| Max. Service Temperature | **~430** | °C | Charring onset; DuPont |
| Min. Service Temperature | **−196** | °C | Retains properties at LN₂; NIST Cryogenics DB |

**Temperature-dependent thermal conductivity (Ventura & Martelli, 2009):**

| T [K] | k [W/m·K] |
|---|---|
| 7 | ~0.01 |
| 77 | ~0.04 |
| 200 | ~0.04 |
| 290 (RT) | ~0.04 |

### 5.4 Ablation / Mass Loss

Not applicable as primary ablative. In Kevlar-reinforced phenolic composites, aramid fiber decomposes at ~430–500 °C contributing to the char matrix.

### 5.5 Key References
- MatWeb. DuPont™ Kevlar® 29. https://www.matweb.com/search/datasheet.aspx?MatGUID=7323d8a43cce4fe795d772b67207eac8
- MatWeb. DuPont™ Kevlar® 49. https://www.matweb.com/search/datasheet.aspx?MatGUID=77b5205f0dcc43bb8cbe6fee7d36cbb5
- Ventura, G. & Martelli, V. (2009). Thermal conductivity of Kevlar 49 between 7 and 290 K. *Cryogenics*, **49**, 509. https://doi.org/10.1016/j.cryogenics.2009.03.006
- Ventura, G. & Martelli, V. (2009). Very low temperature thermal conductivity of Kevlar 49. *Cryogenics*, **49**, 376. https://doi.org/10.1016/j.cryogenics.2009.02.007
- NIST Cryogenic Materials Database — Kevlar 49 Fiber. https://trc.nist.gov/cryogenics/materials/Kevlar49/kevlarfiber.htm
- PMC12349578 (2025). Strain-Rate-Dependent Tensile Behaviour of Kevlar® 29. *Polymers*. https://pmc.ncbi.nlm.nih.gov/articles/PMC12349578/

---

## 6. M8 — Mylar® / BoPET Film (Biaxially Oriented PET)

### 6.1 Material Description

Mylar® (DuPont Teijin Films) is a biaxially oriented polyethylene terephthalate (BoPET) film. In spacecraft, it is the primary layer of **Multi-Layer Insulation (MLI)** thermal blankets, often aluminized on one or both sides. High strength-to-thickness ratio, excellent barrier properties, and UV resistance make it indispensable for passive thermal control in LEO.

### 6.2 Mechanical Properties

| Property | Value (MD) | Value (TD) | Unit | Source |
|---|---|---|---|---|
| Ultimate Tensile Strength | **190** | **210** | MPa | DuPont Teijin Mylar A datasheet (ASTM D882) |
| Young's Modulus (E) | **3 800** | **4 100** | MPa | DuPont Teijin Mylar A datasheet |
| Yield Strength (σ_y) | ~55–80 (bulk PET) | | MPa | AZoM ID:2047; Curbell Plastics |
| Elongation at Break | **115–140** | **120–160** | % | DuPont Teijin Mylar A datasheet |
| Fracture Toughness K_IC | ~2–5 (bulk PET est.) | | MPa·m⁰·⁵ | Estimated; strongly orientation-dependent |
| Density | **1 390–1 400** | | kg/m³ | DuPont Teijin datasheet; FSRI Materials DB |

> **Stress–Strain behaviour:** Semi-ductile. Initial linear elastic region (E ≈ 4 GPa) transitions at yield (~68 MPa) to strain-hardening, reaching UTS ≈ 200 MPa at 115–160% elongation. No sharp yield plateau due to biaxial orientation.

### 6.3 Thermal Properties

| Property | Value | Unit | Source |
|---|---|---|---|
| Thermal Conductivity | **0.14–0.16** | W/m·K | Thermtest; Professional Plastics |
| Specific Heat Capacity | **1 200–1 350** | J/kg·K | FSRI Materials DB; AZoM ID:2047 |
| Glass Transition Temperature (T_g) | **78–85** | °C | AZoM; NETZSCH |
| Melting Point | **254–260** | °C | AZoM; NETZSCH |
| Max. Continuous Service Temp. | **+150** | °C | DuPont Teijin; UL 746B |
| Min. Service Temperature | **−70** | °C | DuPont Teijin; OSTI report |

### 6.4 Ablation / Mass Loss

Not applicable. Mylar is used exclusively in passive thermal insulation (MLI). It melts at ~254 °C and decomposes above ~400 °C.

### 6.5 Key References
- DuPont Teijin Films. *Mylar® A Physical & Thermal Properties* datasheet. https://usa.dupontteijinfilms.com/wp-content/uploads/2017/01/Mylar_Physical_Properties.pdf
- MatWeb. DuPont Teijin Films Mylar® A, 500 Gauge. https://www.matweb.com
- AZoM. Properties of PET Polyester. Article ID:2047. https://www.azom.com/article.aspx?ArticleID=2047
- FSRI Materials Database. Polyethylene terephthalate (PET). https://materials.fsri.org
- Thermtest. Thermal conductivity of Mylar film. https://thermtest.com/application/thermal-conductivity-of-mylar-film
- OSTI. Thermal testing of aluminized Mylar. https://www.osti.gov/biblio/5787464

---

## 7. Summary Comparison Table

| Property | M5: RTV Silicone | M6: Polysiloxane Composite | M7a: Kevlar-29 | M7b: Kevlar-49 | M8: Mylar/BoPET |
|---|---|---|---|---|---|
| **UTS [MPa]** | 2–10 | 13–182 (composite) | **3 600** | 3 000–3 800 | 190–210 |
| **Young's E** | 1–5 MPa | 45.5 GPa | 70.5 GPa | 112–131 GPa | 3.8–4.1 GPa |
| **Yield Strength** | N/A (elastomer) | N/A | N/A (brittle) | N/A (brittle) | ~55–80 MPa |
| **Density [kg/m³]** | 1 100–1 250 | 400–1 340 | 1 440 | 1 440 | 1 390–1 400 |
| **Thermal Cond. [W/m·K]** | 0.20–0.30 | 0.21 (2.5D) | 0.04 (transv.) | 0.04 (transv.) | 0.14–0.16 |
| **Specific Heat [J/kg·K]** | 1 300–1 500 | ~1 300–1 500 | 1 420 | 1 420 | 1 200–1 350 |
| **Op. Temp. Range** | −115 to +300 °C | up to +1 400 °C | −196 to +430 °C | −196 to +430 °C | −70 to +150 °C |
| **Fracture Tough. [MPa·m⁰·⁵]** | N/A | **2.52** | N/A | N/A | ~2–5 (est.) |
| **Elongation at Break** | 100–800 % | 0.97 % | 3.6 % | 2.4 % | 115–160 % |
| **Behaviour type** | Elastomeric | Brittle (char) | Brittle fiber | Brittle fiber | Semi-ductile |
| **Mass Loss Rate** | N/A | 0.021 g/s | N/A | N/A | N/A |

---

## 8. Generated Plots

| File | Content |
|---|---|
| `plots/plot_01_tensile_strength.png` | Bar chart — UTS comparison (log scale) |
| `plots/plot_02_youngs_modulus.png` | Bar chart — Young's modulus comparison (log scale) |
| `plots/plot_03_density.png` | Bar chart — Density comparison |
| `plots/plot_04_thermal_conductivity.png` | Bar chart — Thermal conductivity comparison |
| `plots/plot_05_heat_capacity.png` | Bar chart — Specific heat capacity comparison |
| `plots/plot_06_operating_temperature.png` | Horizontal range bars — Operating temperature |
| `plots/plot_07_fracture_toughness.png` | Bar chart — Fracture toughness (available data only) |
| `plots/plot_08_stress_strain_curves.png` | 2×2 subplot — Representative stress–strain curves per material |
| `plots/plot_09_radar_summary.png` | Radar/spider chart — Normalized multi-property comparison |
| `plots/plot_10_ablation_polysiloxane.png` | Bar chart — Ablation data for M6 polysiloxane composite |

> **Note on stress–strain curves:** Curves in `plot_08` are representative / schematic, constructed from literature-reported E, UTS, and elongation values using appropriate constitutive models (Neo-Hookean for silicone, linear elastic for Kevlar, power-law hardening for Mylar). They are not directly digitised from a single experimental paper.

---

## 9. Notes and Limitations

1. **M5 (RTV Silicone):** Properties vary significantly with filler content (unfilled PDMS vs. aerospace-grade RTV 566). Values given are for typical filled grades. At cryogenic temperatures, modulus increases dramatically as crystallisation sets in near −75 °C.

2. **M6 (Polysiloxane Composite):** Properties depend strongly on reinforcement architecture (2D laminate vs. 2.5D needled vs. nanoporous). The Young's modulus value (45.5 GPa) corresponds to CF/UHTR; the UTS (182 MPa) to 2.5D silica composite. These are not from the same system.

3. **M7 (Kevlar):** Single-fiber values are given. Composite laminate values will be lower due to crimp, fiber–matrix interface, and processing effects. Thermal conductivity is highly anisotropic: 0.04 W/m·K transverse vs. ~3.5–4.0 W/m·K axial.

4. **M8 (Mylar):** Properties are for biaxially oriented film (MD/TD). Unoriented bulk PET has lower UTS (~80 MPa) and yield strength (~55 MPa). Fracture toughness (K_IC) is estimated from bulk PET data; thin-film K_IC is not directly reported in the literature reviewed.

5. **Yield strength and stress–strain combined plot:** As noted in the original brief, yield strength and UTS can be presented together on a stress–strain curve. This is done in `plot_08_stress_strain_curves.png` where applicable (Mylar has a marked yield point; Kevlar and polysiloxane composite do not).

---

*Report generated: 2026-05-05*  
*Plots generated by: `Filip/plots/generate_plots.py`*  
*Data source file: `Filip/data/material_properties.py`*
