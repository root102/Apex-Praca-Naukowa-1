"""
Material properties data for Filip's assignment (M5-M8)
A comparison of selected organic materials for low orbiting spacecraft

Sources:
- M5 (RTV Silicone): MatWeb, AZoM ID:920, Barucci et al. Cryogenics 1998,
  Wegner et al. Int. J. Adhesion 2018, SpaceMat DB RTV566
- M6 (Polysiloxane composite): McDermott et al. J. Composite Materials 2022,
  Hou et al. Techneglas, PMC11945185 (2025), Tate et al. Techneglas
- M7 (Kevlar): MatWeb DuPont Kevlar 29/49, Ventura & Martelli Cryogenics 2009,
  DuPont Tech Guide, PMC12349578 (2025)
- M8 (Mylar/BoPET): DuPont Teijin Films Mylar A datasheet,
  AZoM ID:2047, FSRI Materials DB, Thermtest
"""

# ─── M5: Silicone Rubber / RTV ──────────────────────────────────────────────
silicone_rtv = {
    "name": "Silicone Rubber\n(RTV)",
    "short": "RTV Silicone",
    "color": "#E67E22",

    # Mechanical
    "uts_mpa":          6.0,      # typical filled grade; range 2-10 MPa
    "uts_err":          2.0,
    "youngs_gpa":       0.003,    # ~1-5 MPa; very elastomeric
    "youngs_err":       0.001,
    "yield_mpa":        None,     # elastomer – no yield point
    "elongation_pct":   400.0,    # range 100-800 %
    "elongation_err":   200.0,
    "fracture_tough":   None,     # not characterized classically

    # Thermal
    "therm_cond":       0.25,     # W/m·K; range 0.20-0.30
    "therm_cond_err":   0.05,
    "heat_cap":         1400.0,   # J/kg·K; range 1300-1500
    "heat_cap_err":     100.0,
    "density":          1175.0,   # kg/m³; range 1100-1250
    "density_err":      75.0,

    # Service temperature [°C]
    "t_min":           -115.0,    # glass transition (Tg)
    "t_max":            300.0,    # specialized grades; standard up to 200°C

    # Ablation
    "mass_loss_rate":   None,
    "char_yield_pct":   None,

    # Stress-strain curve parameters (Neo-Hookean elastomer model)
    "ss_model":         "elastomer",
    "ss_E_MPa":         2.0,      # initial modulus MPa
    "ss_uts":           6.0,
    "ss_strain_fail":   4.0,      # 400%
}

# ─── M6: Polysiloxane Matrix Composite ──────────────────────────────────────
polysiloxane_comp = {
    "name": "Polysiloxane\nMatrix Composite",
    "short": "Polysiloxane Composite",
    "color": "#8E44AD",

    # Mechanical (2.5D silica/polysiloxane, McDermott et al. 2022;
    #             CF/UHTR Hou et al. Techneglas)
    "uts_mpa":          182.0,    # 2.5D silica composite; range 13-182
    "uts_err":          9.6,
    "youngs_gpa":       45.5,     # CF/UHTR (Hou et al.); 6.6 Msi
    "youngs_err":       5.0,
    "yield_mpa":        None,
    "elongation_pct":   0.97,
    "elongation_err":   0.1,
    "fracture_tough":   2.52,     # SiO2f/SiO2 composite (PMC11945185)
    "fracture_tough_err": 0.2,

    # Thermal
    "therm_cond":       0.21,     # W/m·K (2.5D composite, McDermott 2022)
    "therm_cond_err":   0.03,
    "heat_cap":         1400.0,
    "heat_cap_err":     100.0,
    "density":          1320.0,   # kg/m³ (2.5D, ~1.32 g/cm³)
    "density_err":      100.0,

    # Service temperature [°C]
    "t_min":           -60.0,
    "t_max":            1400.0,   # char form; pyrolysis 300-550°C

    # Ablation
    "mass_loss_rate":   0.021,    # g/s (F1 formulation, Tate et al.)
    "linear_recession": 0.031,    # mm/s
    "char_yield_pct":   86.5,     # neat UHTR resin TGA at 1000°C

    # Stress-strain
    "ss_model":         "brittle",
    "ss_E_GPa":         45.5,
    "ss_uts":           182.0,
    "ss_strain_fail":   0.0097,
}

# ─── M7a: Kevlar-29 ──────────────────────────────────────────────────────────
kevlar_29 = {
    "name": "Kevlar-29\n(Aramid Fiber)",
    "short": "Kevlar-29",
    "color": "#F1C40F",

    # Mechanical (DuPont datasheet, MatWeb)
    "uts_mpa":          3600.0,
    "uts_err":          200.0,
    "youngs_gpa":       70.5,
    "youngs_err":       2.0,
    "yield_mpa":        None,     # brittle fiber – no yield
    "elongation_pct":   3.6,
    "elongation_err":   0.2,
    "fracture_tough":   None,     # not classically defined for fiber

    # Thermal (Ventura & Martelli, Cryogenics 2009)
    "therm_cond":       0.04,     # W/m·K transverse
    "therm_cond_err":   0.005,
    "heat_cap":         1420.0,
    "heat_cap_err":     50.0,
    "density":          1440.0,
    "density_err":      10.0,

    # Service temperature [°C]
    "t_min":           -196.0,    # retains properties at LN2
    "t_max":            430.0,    # onset of degradation

    # Ablation
    "mass_loss_rate":   None,
    "char_yield_pct":   None,

    # Stress-strain (linear elastic to failure)
    "ss_model":         "brittle_linear",
    "ss_E_GPa":         70.5,
    "ss_uts":           3600.0,
    "ss_strain_fail":   0.036,
}

# ─── M7b: Kevlar-49 ──────────────────────────────────────────────────────────
kevlar_49 = {
    "name": "Kevlar-49\n(Aramid Fiber)",
    "short": "Kevlar-49",
    "color": "#D4AC0D",

    # Mechanical (DuPont datasheet, MatWeb)
    "uts_mpa":          3800.0,
    "uts_err":          200.0,
    "youngs_gpa":       125.0,
    "youngs_err":       5.0,
    "yield_mpa":        None,
    "elongation_pct":   2.4,
    "elongation_err":   0.2,
    "fracture_tough":   None,

    # Thermal
    "therm_cond":       0.04,
    "therm_cond_err":   0.005,
    "heat_cap":         1420.0,
    "heat_cap_err":     50.0,
    "density":          1440.0,
    "density_err":      10.0,

    # Service temperature [°C]
    "t_min":           -196.0,
    "t_max":            430.0,

    # Ablation
    "mass_loss_rate":   None,
    "char_yield_pct":   None,

    # Stress-strain
    "ss_model":         "brittle_linear",
    "ss_E_GPa":         125.0,
    "ss_uts":           3800.0,
    "ss_strain_fail":   0.024,
}

# ─── M8: Mylar / BoPET Film ──────────────────────────────────────────────────
mylar_pet = {
    "name": "Mylar / BoPET\n(PET Film)",
    "short": "Mylar (BoPET)",
    "color": "#2980B9",

    # Mechanical (DuPont Teijin Films Mylar A datasheet, ASTM D882)
    "uts_mpa":          200.0,    # avg MD/TD: (190+210)/2
    "uts_err":          10.0,
    "youngs_gpa":       3.95,     # avg MD/TD: (3.8+4.1)/2
    "youngs_err":       0.15,
    "yield_mpa":        67.5,     # bulk PET 55-80 MPa
    "yield_err":        12.5,
    "elongation_pct":   137.5,    # MD/TD avg 115-160 %
    "elongation_err":   22.5,
    "fracture_tough":   3.5,      # bulk PET estimate 2-5 MPa·m^0.5
    "fracture_tough_err": 1.5,

    # Thermal (DuPont Teijin datasheet, Thermtest, AZoM)
    "therm_cond":       0.15,     # W/m·K
    "therm_cond_err":   0.01,
    "heat_cap":         1275.0,   # J/kg·K; range 1200-1350
    "heat_cap_err":     75.0,
    "density":          1395.0,   # kg/m³; range 1390-1400
    "density_err":      5.0,

    # Service temperature [°C]
    "t_min":           -70.0,
    "t_max":            150.0,    # continuous; Tg~80°C, melt 254-260°C

    # Ablation
    "mass_loss_rate":   None,
    "char_yield_pct":   None,

    # Stress-strain (semi-ductile biaxially oriented film)
    "ss_model":         "semi_ductile",
    "ss_E_GPa":         3.95,
    "ss_yield":         67.5,
    "ss_uts":           200.0,
    "ss_strain_fail":   1.375,    # 137.5%
}

# Aggregated list for iteration
ALL_MATERIALS = [silicone_rtv, polysiloxane_comp, kevlar_29, kevlar_49, mylar_pet]
