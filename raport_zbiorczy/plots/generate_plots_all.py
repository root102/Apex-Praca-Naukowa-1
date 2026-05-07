"""
Material property plots — Collective Report M1-M13
Comparison of organic materials for spacecraft (LEO / launch)

Per-material plots:
  A – stress-strain curve (T = 23 °C)
  B – tensile strength vs. temperature
  C – Young's modulus vs. temperature
  D – thermal conductivity vs. temperature

Comparison plots (compare_*):
  compare_A_uts.png           – UTS (log scale)
  compare_B_modulus.png       – E (log scale)
  compare_C_density.png       – density
  compare_D_temp_range.png    – service temperature range
  compare_E_spec_strength.png – specific strength UTS/rho
  compare_F_radar_top5.png    – radar chart (Top-5)
  compare_G_table.png         – styled summary table 15.1
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

OUT = os.path.dirname(os.path.abspath(__file__))

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.labelsize": 10,
    "axes.grid": True,
    "grid.alpha": 0.30,
    "lines.linewidth": 2.0,
    "figure.dpi": 120,
})

# ════════════════════════════════════════════════════════════════
# 1.  MATERIAL METADATA (RT values)
# ════════════════════════════════════════════════════════════════
MATS = {
    "M1":  {"name": "Kapton (M1)",                "color": "#C0392B",
             "uts": 231,   "E": 2.50,   "rho": 1420, "k": 0.12,
             "Cp": 1090,   "t_min": -269, "t_max": 400,  "Kic": 3.5},
    "M2":  {"name": "POSS-Polyimide (M2)",        "color": "#E74C3C",
             "uts": 210,   "E": 2.30,   "rho": 1450, "k": 0.15,
             "Cp": 1050,   "t_min": -269, "t_max": 450,  "Kic": 2.0},
    "M3":  {"name": "Phenolic Resin (M3)",         "color": "#935116",
             "uts": 45,    "E": 3.50,   "rho": 1250, "k": 0.30,
             "Cp": 1200,   "t_min":  -55, "t_max": 2000, "Kic": 0.7},
    "M4":  {"name": "Phthalonitrile Resin (M4)",  "color": "#784212",
             "uts": 65,    "E": 4.00,   "rho": 1250, "k": 0.20,
             "Cp": 1200,   "t_min":  -55, "t_max": 375,  "Kic": 1.0},
    "M5":  {"name": "RTV Silicone (M5)",           "color": "#E67E22",
             "uts": 6,     "E": 0.003,  "rho": 1175, "k": 0.25,
             "Cp": 1400,   "t_min": -115, "t_max": 300,  "Kic": None},
    "M6":  {"name": "Polysiloxane Compos. (M6)",  "color": "#8E44AD",
             "uts": 182,   "E": 45.50,  "rho": 1320, "k": 0.21,
             "Cp": 1400,   "t_min":  -60, "t_max": 1400, "Kic": 2.52},
    "M7a": {"name": "Kevlar-29 (M7)",             "color": "#F1C40F",
             "uts": 3600,  "E": 70.50,  "rho": 1440, "k": 0.04,
             "Cp": 1420,   "t_min": -196, "t_max": 430,  "Kic": None},
    "M7b": {"name": "Kevlar-49 (M7)",             "color": "#D4AC0D",
             "uts": 3800,  "E": 125.00, "rho": 1440, "k": 0.04,
             "Cp": 1420,   "t_min": -196, "t_max": 430,  "Kic": None},
    "M8":  {"name": "Mylar BoPET (M8)",           "color": "#2980B9",
             "uts": 200,   "E": 3.95,   "rho": 1395, "k": 0.15,
             "Cp": 1275,   "t_min":  -70, "t_max": 150,  "Kic": 3.5},
    "M9":  {"name": "UHMWPE (M9)",                "color": "#27AE60",
             "uts": 200,   "E": 0.90,   "rho": 940,  "k": 0.44,
             "Cp": 1850,   "t_min": -150, "t_max":  80,  "Kic": 2.0},
    "M10": {"name": "PE Composite (M10)",         "color": "#1E8449",
             "uts": 400,   "E": 30.00,  "rho": 1000, "k": 0.35,
             "Cp": 1500,   "t_min": -150, "t_max": 120,  "Kic": None},
    "M11": {"name": "Kevlar Composite (M11)",     "color": "#B7950B",
             "uts": 600,   "E": 40.00,  "rho": 1380, "k": 0.12,
             "Cp": 1300,   "t_min":  -55, "t_max": 180,  "Kic": None},
    "M12": {"name": "Phenolic Composite (M12)",   "color": "#6E2F1A",
             "uts": 350,   "E": 35.00,  "rho": 1550, "k": 2.00,
             "Cp": 1400,   "t_min":  -55, "t_max": 2000, "Kic": 15.0},
    "M13": {"name": "Polysil. Compos. II (M13)",  "color": "#6C3483",
             "uts": 150,   "E": 25.00,  "rho": 1450, "k": 0.50,
             "Cp": 1300,   "t_min":  -60, "t_max": 1200, "Kic": 2.0},
}

# ════════════════════════════════════════════════════════════════
# 2.  TEMPERATURE-DEPENDENT DATA
#     uts: ([T °C], [UTS MPa])
#     E:   ([T °C], [E GPa])  — M5: E in MPa!
#     k:   ([T K],  [k W/m·K])
# ════════════════════════════════════════════════════════════════
TD = {
    "M1": {
        "uts": ([-100, 23, 100, 200, 300, 400],
                [270, 231, 195, 139, 95, 40]),
        "E":   ([-100, 23, 100, 200, 300, 400],
                [4.0, 2.5, 2.0, 1.5, 1.0, 0.5]),
        "k":   ([100, 200, 300, 400, 500, 600],
                [0.090, 0.110, 0.120, 0.135, 0.155, 0.190]),
    },
    "M2": {
        "uts": ([-100, 23, 100, 200, 300, 400, 450],
                [285, 210, 185, 140, 105, 55, 25]),
        "E":   ([-100, 23, 100, 200, 300, 400],
                [3.7, 2.3, 1.9, 1.5, 1.1, 0.6]),
        "k":   ([100, 200, 300, 400, 500],
                [0.11, 0.13, 0.15, 0.17, 0.20]),
    },
    "M3": {
        "uts": ([-55, 23, 100, 150, 200, 250],
                [55, 45, 40, 35, 28, 18]),
        "E":   ([-55, 23, 100, 150, 200, 250],
                [4.2, 3.5, 3.2, 2.8, 2.2, 1.5]),
        "k":   ([200, 250, 300, 350, 400],
                [0.25, 0.27, 0.30, 0.33, 0.38]),
    },
    "M4": {
        "uts": ([-55, 23, 100, 200, 300, 375],
                [78, 65, 63, 58, 50, 35]),
        "E":   ([-55, 23, 100, 200, 300, 375],
                [4.8, 4.0, 3.8, 3.5, 3.0, 2.2]),
        "k":   ([200, 250, 300, 350, 400],
                [0.17, 0.185, 0.20, 0.215, 0.23]),
    },
    "M5": {
        "uts": ([-115, -80, -40, 0, 23, 100, 200, 300],
                [15.0, 12.0, 10.0, 7.5, 6.0, 5.5, 4.5, 3.5]),
        # E in MPa (not GPa!) — range 0.9 to 2000 MPa
        "E":   ([-115, -100, -80, -75, -50, -20, 0, 23, 100, 200, 300],
                [2000, 800, 100, 40, 8, 4, 3, 2.0, 1.6, 1.2, 0.9]),
        "k":   ([4, 10, 20, 50, 100, 200, 300],
                [0.08, 0.11, 0.15, 0.19, 0.22, 0.25, 0.27]),
    },
    "M6": {
        "uts": ([-60, 23, 100, 300, 600, 1000, 1400],
                [210, 182, 170, 155, 130, 95, 60]),
        "E":   ([-60, 23, 100, 300, 600, 1000],
                [55, 45.5, 42, 36, 28, 18]),
        "k":   ([200, 300, 400, 600, 800, 1000],
                [0.18, 0.21, 0.23, 0.28, 0.35, 0.45]),
    },
    "M7": {
        "uts_29": ([-196, -100, 23, 100, 200, 300, 430],
                   [4100, 3900, 3600, 3500, 3400, 3250, 2800]),
        "uts_49": ([-196, -100, 23, 100, 200, 300, 430],
                   [4300, 4100, 3800, 3700, 3600, 3400, 3000]),
        "E_29":   ([-196, -100, 23, 100, 200, 300, 430],
                   [78, 74, 70.5, 68, 66, 64, 60]),
        "E_49":   ([-196, -100, 23, 100, 200, 300, 430],
                   [135, 130, 125, 122, 119, 116, 110]),
        "k":      ([7, 20, 50, 100, 150, 200, 250, 290],
                   [0.007, 0.013, 0.024, 0.033, 0.037, 0.039, 0.040, 0.041]),
    },
    "M8": {
        "uts": ([-70, -40, 0, 23, 50, 100, 130, 150],
                [290, 260, 230, 200, 170, 130, 90, 60]),
        "E":   ([-70, 0, 23, 50, 80, 100, 130, 150],
                [6.5, 5.0, 3.95, 3.2, 2.5, 1.8, 0.8, 0.4]),
        "k":   ([200, 250, 300, 350, 400],
                [0.13, 0.14, 0.15, 0.155, 0.16]),
    },
    "M9": {
        "uts": ([-50, 0, 23, 50, 70, 80],
                [280, 240, 200, 150, 100, 50]),
        "E":   ([-50, 0, 23, 50, 70, 80],
                [1.2, 1.0, 0.9, 0.7, 0.4, 0.15]),
        "k":   ([150, 200, 250, 300, 350],
                [0.35, 0.39, 0.42, 0.44, 0.45]),
    },
    "M10": {
        "uts": ([-100, -50, 23, 50, 80, 100, 120],
                [600, 520, 400, 350, 280, 200, 100]),
        "E":   ([-100, -50, 23, 50, 80, 100, 120],
                [45, 38, 30, 25, 18, 12, 6]),
        "k":   ([200, 250, 300, 350, 400],
                [0.28, 0.32, 0.35, 0.37, 0.38]),
    },
    "M11": {
        "uts": ([-55, 0, 23, 100, 150, 180],
                [720, 650, 600, 580, 560, 500]),
        "E":   ([-55, 0, 23, 100, 150, 180],
                [45, 42, 40, 38, 35, 30]),
        "k":   ([200, 250, 300, 350, 400],
                [0.10, 0.11, 0.12, 0.13, 0.135]),
    },
    "M12": {
        "uts": ([-55, 23, 100, 300, 600, 1000, 2000],
                [420, 350, 330, 300, 260, 210, 150]),
        "E":   ([-55, 23, 100, 300, 600, 1000],
                [42, 35, 33, 28, 20, 14]),
        "k":   ([200, 300, 400, 600, 800, 1000],
                [1.6, 2.0, 2.3, 2.8, 3.2, 3.5]),
    },
    "M13": {
        "uts": ([-60, 23, 100, 300, 600, 1000, 1200],
                [190, 150, 140, 120, 90, 65, 45]),
        "E":   ([-60, 23, 100, 300, 600, 1000],
                [30, 25, 22, 18, 12, 8]),
        "k":   ([200, 300, 400, 600, 800, 1000],
                [0.35, 0.50, 0.60, 0.75, 0.88, 1.00]),
    },
}

# ════════════════════════════════════════════════════════════════
# 3.  STRESS-STRAIN PARAMETERS
# ════════════════════════════════════════════════════════════════
SS = {
    "M1":  {"model": "semi_ductile",   "E_GPa": 2.50,  "sy":  69,  "su": 231,  "ef": 0.72},
    "M2":  {"model": "semi_ductile",   "E_GPa": 2.30,  "sy":  60,  "su": 210,  "ef": 0.40},
    "M3":  {"model": "brittle",        "E_GPa": 3.50,  "sy": None, "su":  45,  "ef": 0.010},
    "M4":  {"model": "brittle",        "E_GPa": 4.00,  "sy": None, "su":  65,  "ef": 0.015},
    "M5":  {"model": "elastomer",      "E_MPa": 2.00,  "sy": None, "su":   6,  "ef": 4.00},
    "M6":  {"model": "brittle",        "E_GPa": 45.5,  "sy": None, "su": 182,  "ef": 0.0097},
    "M7a": {"model": "brittle_linear", "E_GPa": 70.5,  "sy": None, "su": 3600, "ef": 0.036},
    "M7b": {"model": "brittle_linear", "E_GPa": 125.0, "sy": None, "su": 3800, "ef": 0.024},
    "M8":  {"model": "semi_ductile",   "E_GPa": 3.95,  "sy":  67.5,"su": 200,  "ef": 1.375},
    "M9":  {"model": "semi_ductile",   "E_GPa": 0.90,  "sy":  25,  "su": 200,  "ef": 3.50},
    "M10": {"model": "brittle",        "E_GPa": 30.0,  "sy": None, "su": 400,  "ef": 0.015},
    "M11": {"model": "brittle",        "E_GPa": 40.0,  "sy": None, "su": 600,  "ef": 0.018},
    "M12": {"model": "brittle",        "E_GPa": 35.0,  "sy": None, "su": 350,  "ef": 0.008},
    "M13": {"model": "brittle",        "E_GPa": 25.0,  "sy": None, "su": 150,  "ef": 0.007},
}

# ════════════════════════════════════════════════════════════════
# 4.  HELPER FUNCTIONS
# ════════════════════════════════════════════════════════════════

def savefig(fig, fname):
    fig.tight_layout()
    path = os.path.join(OUT, fname)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {fname}")


def compute_ss(ss):
    """Returns (strain [], stress [MPa])."""
    model = ss["model"]
    if model in ("brittle", "brittle_linear"):
        E_MPa = ss["E_GPa"] * 1000
        ef = ss["ef"]
        st = np.linspace(0, ef, 400)
        sg = E_MPa * st
        return st, sg
    elif model == "elastomer":
        G = ss["E_MPa"] / 3.0
        ef = ss["ef"]
        st = np.linspace(0, ef, 400)
        lam = 1 + st
        sg = G * (lam - lam ** -2)
        return st, sg
    elif model == "semi_ductile":
        E_MPa = ss["E_GPa"] * 1000
        sy = ss["sy"]
        su = ss["su"]
        ef = ss["ef"]
        ey = sy / E_MPa
        st_e = np.linspace(0, ey, 80)
        sg_e = E_MPa * st_e
        st_p = np.linspace(ey, ef, 300)
        ratio = ef / ey if ey > 0 else 1
        n = np.log(su / sy) / np.log(ratio) if ratio > 1 else 0.1
        sg_p = sy * (st_p / ey) ** n
        return np.concatenate([st_e, st_p]), np.concatenate([sg_e, sg_p])
    return np.array([0, 1]), np.array([0, 1])


def _style(ax, xlabel, ylabel, title):
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True, alpha=0.3)

# ════════════════════════════════════════════════════════════════
# 5.  INDIVIDUAL MATERIAL PLOTS
# ════════════════════════════════════════════════════════════════

def plot_A(code, name, color, ss):
    fig, ax = plt.subplots(figsize=(6, 4.5))
    st, sg = compute_ss(ss)
    ax.plot(st * 100, sg, color=color, lw=2)
    ax.scatter([st[-1] * 100], [sg[-1]], color=color, s=60, zorder=5,
               label=f"Fracture: {sg[-1]:.0f} MPa")
    if ss.get("sy"):
        ey = ss["sy"] / (ss["E_GPa"] * 1000)
        ax.axvline(ey * 100, ls="--", color="gray", alpha=0.7, lw=1.2,
                   label=f"Yield point: {ss['sy']:.0f} MPa")
    ax.legend(fontsize=8)
    _style(ax, "Strain ε [%]", "Stress σ [MPa]",
           f"A — Stress-Strain Curve\n{name}  (T = 23 °C)")
    savefig(fig, f"{code.lower()}_A_stress_strain.png")


def plot_B(code, name, color, td_uts):
    T, U = td_uts
    fig, ax = plt.subplots(figsize=(6, 4.5))
    ax.plot(T, U, "o-", color=color, lw=2)
    ax.axvline(23, ls=":", color="black", alpha=0.5, lw=1)
    _style(ax, "Temperature [°C]", "UTS [MPa]",
           f"B — Tensile Strength vs. T\n{name}")
    savefig(fig, f"{code.lower()}_B_uts_vs_temp.png")


def plot_C(code, name, color, td_E, E_in_MPa=False):
    T, E = td_E
    fig, ax = plt.subplots(figsize=(6, 4.5))
    if E_in_MPa:
        ax.semilogy(T, E, "s-", color=color, lw=2)
        ylabel = "Young's Modulus E [MPa]"
    else:
        ax.plot(T, E, "s-", color=color, lw=2)
        ylabel = "Young's Modulus E [GPa]"
    ax.axvline(23, ls=":", color="black", alpha=0.5, lw=1)
    _style(ax, "Temperature [°C]", ylabel,
           f"C — Young's Modulus vs. T\n{name}")
    savefig(fig, f"{code.lower()}_C_modulus_vs_temp.png")


def plot_D(code, name, color, td_k, logx=False):
    T_K, k = td_k
    fig, ax = plt.subplots(figsize=(6, 4.5))
    if logx:
        ax.semilogx(T_K, k, "^-", color=color, lw=2)
    else:
        T_C = [t - 273.15 for t in T_K]
        ax.plot(T_C, k, "^-", color=color, lw=2)
    xlabel = "Temperature [K]" if logx else "Temperature [°C]"
    _style(ax, xlabel, "Thermal Conductivity k [W/m·K]",
           f"D — Thermal Conductivity vs. T\n{name}")
    savefig(fig, f"{code.lower()}_D_thermal_cond_vs_temp.png")

# ════════════════════════════════════════════════════════════════
# 6.  SPECIAL PLOTS — M7 (Kevlar-29 and Kevlar-49 together)
# ════════════════════════════════════════════════════════════════

def plot_M7_A():
    fig, ax = plt.subplots(figsize=(6, 4.5))
    for key, ss, col in [("M7a", SS["M7a"], MATS["M7a"]["color"]),
                          ("M7b", SS["M7b"], MATS["M7b"]["color"])]:
        st, sg = compute_ss(ss)
        label = "Kevlar-29" if key == "M7a" else "Kevlar-49"
        ax.plot(st * 100, sg, color=col, lw=2, label=label)
        ax.scatter([st[-1] * 100], [sg[-1]], color=col, s=70, zorder=5,
                   marker="x", linewidths=2.5)
    ax.legend()
    _style(ax, "Strain ε [%]", "Stress σ [MPa]",
           "A — Stress-Strain Curve\nKevlar-29 / Kevlar-49  (T = 23 °C)")
    savefig(fig, "m7_A_stress_strain.png")


def plot_M7_B():
    fig, ax = plt.subplots(figsize=(6, 4.5))
    T29, U29 = TD["M7"]["uts_29"]
    T49, U49 = TD["M7"]["uts_49"]
    ax.plot(T29, U29, "o-", color=MATS["M7a"]["color"], lw=2, label="Kevlar-29")
    ax.plot(T49, U49, "s-", color=MATS["M7b"]["color"], lw=2, label="Kevlar-49")
    ax.axvline(23, ls=":", color="black", alpha=0.5, lw=1)
    ax.legend()
    _style(ax, "Temperature [°C]", "UTS [MPa]",
           "B — Tensile Strength vs. T\nKevlar-29 / Kevlar-49")
    savefig(fig, "m7_B_uts_vs_temp.png")


def plot_M7_C():
    fig, ax = plt.subplots(figsize=(6, 4.5))
    T29, E29 = TD["M7"]["E_29"]
    T49, E49 = TD["M7"]["E_49"]
    ax.plot(T29, E29, "o-", color=MATS["M7a"]["color"], lw=2, label="Kevlar-29")
    ax.plot(T49, E49, "s-", color=MATS["M7b"]["color"], lw=2, label="Kevlar-49")
    ax.axvline(23, ls=":", color="black", alpha=0.5, lw=1)
    ax.legend()
    _style(ax, "Temperature [°C]", "Young's Modulus E [GPa]",
           "C — Young's Modulus vs. T\nKevlar-29 / Kevlar-49")
    savefig(fig, "m7_C_modulus_vs_temp.png")


def plot_M7_D():
    T_K, k = TD["M7"]["k"]
    fig, ax = plt.subplots(figsize=(6, 4.5))
    ax.semilogx(T_K, k, "^-", color=MATS["M7a"]["color"], lw=2)
    _style(ax, "Temperature [K]", "Thermal Conductivity k [W/m·K]",
           "D — Thermal Conductivity vs. T (cryogenic)\nKevlar (Ventura & Martelli 2009)")
    savefig(fig, "m7_D_thermal_cond_vs_temp.png")

# ════════════════════════════════════════════════════════════════
# 7.  MAIN LOOP — individual material plots
# ════════════════════════════════════════════════════════════════

INDIVIDUAL = [
    "M1", "M2", "M3", "M4", "M5",
    "M6", "M8", "M9", "M10", "M11", "M12", "M13"
]

print("=== Generating individual material plots ===")
for code in INDIVIDUAL:
    m = MATS[code]
    td = TD[code]
    print(f"\n--- {code}: {m['name']} ---")
    plot_A(code, m["name"], m["color"], SS[code])
    plot_B(code, m["name"], m["color"], td["uts"])
    plot_C(code, m["name"], m["color"], td["E"],
           E_in_MPa=(code == "M5"))
    plot_D(code, m["name"], m["color"], td["k"],
           logx=(code == "M7"))

print("\n--- M7: Kevlar ---")
plot_M7_A()
plot_M7_B()
plot_M7_C()
plot_M7_D()

# ════════════════════════════════════════════════════════════════
# 8.  COMPARISON PLOTS
# ════════════════════════════════════════════════════════════════

COMP_KEYS = ["M1","M2","M3","M4","M5","M6","M7a","M7b",
             "M8","M9","M10","M11","M12","M13"]
COMP_LABELS = [
    "Kapton", "POSS-PI", "Phenolic Resin", "Phthalonitrile",
    "RTV Silicone", "Polysil. Compos.",
    "Kevlar-29", "Kevlar-49",
    "Mylar BoPET", "UHMWPE",
    "PE Composite", "Kevlar Composite",
    "Phenolic Compos.", "Polysil. Compos. II"
]
COMP_COLORS = [MATS[k]["color"] for k in COMP_KEYS]
COMP_UTS    = [MATS[k]["uts"]   for k in COMP_KEYS]
COMP_E      = [MATS[k]["E"]     for k in COMP_KEYS]
COMP_RHO    = [MATS[k]["rho"]   for k in COMP_KEYS]


def hbar(ax, values, labels, colors, xlabel, title, log=False):
    y = np.arange(len(labels))
    bars = ax.barh(y, values, color=colors, edgecolor="white", height=0.7)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=8.5)
    ax.set_xlabel(xlabel)
    ax.set_title(title)
    if log:
        ax.set_xscale("log")
    for bar, v in zip(bars, values):
        ax.text(bar.get_width() * (1.03 if not log else 1.15),
                bar.get_y() + bar.get_height() / 2,
                f"{v:.3g}", va="center", ha="left", fontsize=7.5)
    ax.grid(True, axis="x", alpha=0.3)


print("\n=== Comparison plots ===")

# ── compare_A: UTS ──────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 6.5))
hbar(ax, COMP_UTS, COMP_LABELS, COMP_COLORS,
     "UTS [MPa] — logarithmic scale",
     "Tensile Strength (UTS) Comparison", log=True)
savefig(fig, "compare_A_uts.png")

# ── compare_B: Young's Modulus ──────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 6.5))
hbar(ax, COMP_E, COMP_LABELS, COMP_COLORS,
     "Young's Modulus E [GPa] — logarithmic scale",
     "Young's Modulus Comparison", log=True)
savefig(fig, "compare_B_modulus.png")

# ── compare_C: Density ─────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 6.5))
hbar(ax, COMP_RHO, COMP_LABELS, COMP_COLORS,
     "Density ρ [kg/m³]",
     "Material Density Comparison")
savefig(fig, "compare_C_density.png")

# ── compare_D: Service Temperature Range ───────────────────────
RANGE_KEYS = ["M1","M2","M3","M4","M5","M6","M7a",
              "M8","M9","M10","M11","M12","M13"]
RANGE_LBLS = ["Kapton","POSS-PI","Phenolic Resin","Phthalonitrile",
              "RTV Silicone","Polysil. Compos.","Kevlar",
              "Mylar BoPET","UHMWPE","PE Composite",
              "Kevlar Composite","Phenolic Compos.","Polysil. Compos. II"]
RANGE_COLS = [MATS[k]["color"] for k in RANGE_KEYS]
T_MINS = [MATS[k]["t_min"] for k in RANGE_KEYS]
T_MAXS = [MATS[k]["t_max"] for k in RANGE_KEYS]

fig, ax = plt.subplots(figsize=(9, 6))
y = np.arange(len(RANGE_KEYS))
for i, (lo, hi, col, lbl) in enumerate(zip(T_MINS, T_MAXS, RANGE_COLS, RANGE_LBLS)):
    ax.barh(i, hi - lo, left=lo, color=col, alpha=0.75, height=0.65)
    ax.text(hi + 30, i, f"{hi}°C", va="center", fontsize=7.5)
ax.set_yticks(y)
ax.set_yticklabels(RANGE_LBLS, fontsize=8.5)
ax.set_xlabel("Temperature [°C]")
ax.set_title("Service Temperature Range of Materials")
ax.axvline(0, color="black", lw=0.8, alpha=0.5)
ax.axvline(23, color="blue", lw=0.8, ls="--", alpha=0.5, label="T = 23 °C")
ax.axvline(-150, color="cyan", lw=0.8, ls=":", alpha=0.6, label="LEO min ≈ −150 °C")
ax.axvline(150, color="red", lw=0.8, ls=":", alpha=0.6, label="LEO max ≈ +150 °C")
ax.legend(fontsize=8, loc="lower right")
ax.grid(True, axis="x", alpha=0.3)
savefig(fig, "compare_D_temp_range.png")

# ── compare_E: Specific Strength ───────────────────────────────
SPEC_STR = [u / r * 1000 for u, r in zip(COMP_UTS, COMP_RHO)]

fig, ax = plt.subplots(figsize=(9, 6.5))
hbar(ax, SPEC_STR, COMP_LABELS, COMP_COLORS,
     "Specific Strength UTS/ρ [kN·m/kg]",
     "Specific Strength (UTS / density)", log=True)
savefig(fig, "compare_E_spec_strength.png")

# ── compare_F: Radar Chart — Top-5 ─────────────────────────────
TOP5_KEYS  = ["M1", "M7a", "M12", "M6", "M2"]
TOP5_NAMES = ["Kapton\n(M1)", "Kevlar-29\n(M7)", "Phenolic Compos.\n(M12)",
              "Polysil. Compos.\n(M6)", "POSS-Polyimide\n(M2)"]
RAW = np.array([
    # sp_str  E_norm  T_max  AO_res  T_range
    [231/1420, 2.5,  400,   0.6,  669 ],
    [3600/1440, 70.5, 430,  0.9,  626 ],
    [350/1550, 35.0, 2000,  0.8,  2055],
    [182/1320, 45.5, 1400,  0.95, 1460],
    [210/1450, 2.3,  450,   0.95, 719 ],
])
col_max = RAW.max(axis=0)
col_max[col_max == 0] = 1
NORM = RAW / col_max

categories = ["Spec.\nStrength", "Young's\nModulus", "T_max", "AO\nResist.", "T\nRange"]
N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw={"projection": "polar"})
for i, (key, name_r) in enumerate(zip(TOP5_KEYS, TOP5_NAMES)):
    vals = NORM[i].tolist() + [NORM[i][0]]
    ax.plot(angles, vals, "o-", lw=2, color=MATS[key]["color"],
            label=name_r.replace("\n", " "))
    ax.fill(angles, vals, alpha=0.08, color=MATS[key]["color"])
ax.set_thetagrids(np.degrees(angles[:-1]), categories, fontsize=9)
ax.set_ylim(0, 1)
ax.set_title("Top-5 Materials — Radar Comparison\n(normalized values)", pad=20)
ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.15), fontsize=8.5)
savefig(fig, "compare_F_radar_top5.png")

# ════════════════════════════════════════════════════════════════
# 9.  STYLED SUMMARY TABLE (Table 15.1)
# ════════════════════════════════════════════════════════════════

def plot_G_table():
    """Render Table 15.1 as a styled graphic."""
    headers = [
        "Material",
        "UTS\n[MPa]",
        "E\n[GPa]",
        "ρ\n[kg/m³]",
        "T_min\n[°C]",
        "T_max\n[°C]",
        "k\n[W/m·K]",
        "Kᴵᶜ\n[MPa√m]",
    ]

    mat_keys  = ["M1","M2","M3","M4","M5","M6","M7a","M7b",
                 "M8","M9","M10","M11","M12","M13"]
    mat_names = [
        "M1   Kapton",           "M2   POSS-Polyimide",
        "M3   Phenolic Resin",   "M4   Phthalonitrile",
        "M5   RTV Silicone",     "M6   Polysil. Composite",
        "M7a  Kevlar-29",        "M7b  Kevlar-49",
        "M8   Mylar BoPET",      "M9   UHMWPE",
        "M10  PE Composite",     "M11  Kevlar Composite",
        "M12  Phenolic Composite","M13  Polysil. Compos. II",
    ]
    data_rows = [
        ["231",   "2.50",  "1 420", "−269", "400",    "0.12", "3.5"],
        ["210",   "2.30",  "1 450", "−269", "450",    "0.15", "2.0"],
        ["45",    "3.50",  "1 250", "−55",  "2000*",  "0.30", "0.7"],
        ["65",    "4.00",  "1 250", "−55",  "375",    "0.20", "1.0"],
        ["6",     "0.003", "1 175", "−115", "300",    "0.25", "—"],
        ["182",   "45.5",  "1 320", "−60",  "1400*",  "0.21", "2.52"],
        ["3 600", "70.5",  "1 440", "−196", "430",    "0.04", "—"],
        ["3 800", "125",   "1 440", "−196", "430",    "0.04", "—"],
        ["200",   "3.95",  "1 395", "−70",  "150",    "0.15", "3.5"],
        ["200",   "0.90",  "940",   "−150", "80",     "0.44", "2.0"],
        ["400",   "30.0",  "1 000", "−150", "120",    "0.35", "—"],
        ["600",   "40.0",  "1 380", "−55",  "180",    "0.12", "—"],
        ["350",   "35.0",  "1 550", "−55",  "2000*",  "2.00", "15"],
        ["150",   "25.0",  "1 450", "−60",  "1200*",  "0.50", "2.0"],
    ]
    mat_colors = [MATS[k]["color"] for k in mat_keys]

    n_rows = len(mat_names)
    n_cols = len(headers)

    fig_w = 16
    fig_h = 0.45 * n_rows + 1.4
    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    ax.axis("off")
    fig.patch.set_facecolor("#F5F6FA")

    # Column relative widths (sum = n_cols)
    col_w = [2.8, 1.0, 1.0, 1.1, 1.0, 1.0, 1.0, 1.1]
    col_w_norm = [w / sum(col_w) for w in col_w]

    # Row / col geometry in axes units [0,1]
    header_h = 0.13
    row_h    = (1.0 - header_h - 0.05) / n_rows
    y_top    = 0.97

    def draw_cell(ax, x, y, w, h, text, fc, tc="black",
                  bold=False, fontsize=8.5, va="center", ha="center"):
        rect = mpatches.FancyBboxPatch(
            (x + 0.001, y - h + 0.001), w - 0.002, h - 0.002,
            boxstyle="round,pad=0.01", linewidth=0,
            facecolor=fc, transform=ax.transAxes, clip_on=False)
        ax.add_patch(rect)
        ax.text(x + w / 2, y - h / 2, text,
                transform=ax.transAxes,
                fontsize=fontsize, color=tc,
                fontweight="bold" if bold else "normal",
                va=va, ha=ha, clip_on=False)

    # ── Draw header row ──────────────────────────────────────────
    x = 0.0
    for j, (hdr, cw) in enumerate(zip(headers, col_w_norm)):
        draw_cell(ax, x, y_top, cw, header_h, hdr,
                  fc="#2C3E50", tc="white", bold=True, fontsize=8.5)
        x += cw

    # ── Draw data rows ───────────────────────────────────────────
    stripe_colors = ["#FFFFFF", "#EEF0F5"]
    for i, (mname, mcolor, drow) in enumerate(
            zip(mat_names, mat_colors, data_rows)):
        y_row = y_top - header_h - i * row_h
        row_fc = stripe_colors[i % 2]

        x = 0.0
        # Material name cell
        draw_cell(ax, x, y_row, col_w_norm[0], row_h, mname,
                  fc=mcolor, tc="white", bold=True, fontsize=8.0,
                  ha="left")
        # Adjust text x slightly for left-aligned name
        # (redraw with proper x offset)
        ax.patches[-1].remove()
        rect = mpatches.FancyBboxPatch(
            (x + 0.001, y_row - row_h + 0.001),
            col_w_norm[0] - 0.002, row_h - 0.002,
            boxstyle="round,pad=0.01", linewidth=0,
            facecolor=mcolor, transform=ax.transAxes, clip_on=False)
        ax.add_patch(rect)
        ax.text(x + 0.008, y_row - row_h / 2, mname,
                transform=ax.transAxes, fontsize=8.0,
                color="white", fontweight="bold",
                va="center", ha="left", clip_on=False)
        x += col_w_norm[0]

        # Data cells
        for j, (val, cw) in enumerate(zip(drow, col_w_norm[1:]), 1):
            is_extreme = (
                (j == 1 and float(val.replace(" ", "")) >= 3000) or   # high UTS
                (j == 4 and val.lstrip("-−") != "" and
                 float(val.replace("−", "-").replace(" ", "")) <= -150) or  # very low T
                (j == 7 and val not in ("—", "?") and
                 float(val.replace(" ", "")) >= 10)   # high KIC
            )
            cell_fc = row_fc
            cell_tc = "#1A1A2E"
            if is_extreme:
                cell_fc = "#D5F5E3"
                cell_tc = "#145A32"
            draw_cell(ax, x, y_row, cw, row_h, val,
                      fc=cell_fc, tc=cell_tc, fontsize=8.5)
            x += cw

    # ── Footer note ──────────────────────────────────────────────
    ax.text(0.01, 0.01,
            "* T_max for ablative materials = effective ablative protection, "
            "not continuous structural service",
            transform=ax.transAxes, fontsize=7, color="#555555",
            va="bottom", ha="left")

    ax.set_title(
        "Table 15.1 — Material Properties Summary  (T = 23 °C)",
        fontsize=12, fontweight="bold", pad=8)

    savefig(fig, "compare_G_table.png")


print("\n--- Table 15.1 graphic ---")
plot_G_table()

print("\nAll plots generated successfully.")
