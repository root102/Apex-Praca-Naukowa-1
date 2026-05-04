"""
Generuje wykresy właściwości materiałów M5–M8 — po 4 wykresy na materiał:
  A  Krzywa naprężenie–odkształcenie
  B  Wytrzymałość na rozciąganie vs. temperatura
  C  Moduł Younga vs. temperatura
  D  Przewodnictwo cieplne vs. temperatura

Uruchom z katalogu Filip/:
    python plots/generate_plots.py
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

OUT = os.path.dirname(__file__)

# ── styl globalny ────────────────────────────────────────────────────────────
plt.rcParams.update({
    'figure.facecolor':  'white',
    'axes.facecolor':    '#F8F9FA',
    'axes.edgecolor':    '#CCCCCC',
    'axes.grid':         True,
    'grid.color':        '#DDDDDD',
    'grid.linestyle':    '--',
    'grid.linewidth':    0.7,
    'font.family':       'DejaVu Sans',
    'font.size':         11,
    'axes.titlesize':    13,
    'axes.titleweight':  'bold',
    'axes.labelsize':    11,
    'xtick.labelsize':   10,
    'ytick.labelsize':   10,
    'legend.fontsize':   9,
    'legend.framealpha': 0.85,
    'figure.dpi':        150,
    'lines.linewidth':   2.2,
    'lines.markersize':  7,
})

COL = {
    'M5': '#E67E22',   # pomarańczowy
    'M6': '#8E44AD',   # fioletowy
    'M7a': '#D4AC0D',  # żółty ciemny – Kevlar-29
    'M7b': '#F39C12',  # żółty jasny  – Kevlar-49
    'M8': '#2980B9',   # niebieski
}

def save(fig, name):
    p = os.path.join(OUT, name)
    fig.savefig(p, bbox_inches='tight', dpi=150)
    plt.close(fig)
    print(f"  Zapisano: {name}")

# ════════════════════════════════════════════════════════════════════════════
#  M5 – Guma silikonowa / RTV
# ════════════════════════════════════════════════════════════════════════════

def m5_A():
    """Krzywa naprężenie–odkształcenie (Neo-Hookean, T = 23 °C)"""
    eps = np.linspace(0, 4.0, 600)
    lam = 1 + eps
    G   = 0.85          # [MPa] – moduł ścinający
    sig = G * (lam - lam**(-2))

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(eps * 100, sig, color=COL['M5'])
    ax.scatter([400], [6.0], color='red', zorder=5, s=70, label='Zerwanie (UTS ≈ 6 MPa)')
    ax.axvline(400, color='red', lw=1.2, ls='--', alpha=0.6)
    ax.set_xlabel('Odkształcenie [%]')
    ax.set_ylabel('Naprężenie [MPa]')
    ax.set_title('M5 — Guma silikonowa / RTV\nKrzywa naprężenie–odkształcenie (T = 23 °C)')
    ax.set_xlim(0, 450); ax.set_ylim(0, 9)
    ax.legend()
    ax.text(0.04, 0.92,
            'Model: Neo-Hookean\nBrak granicy plastyczności\n(elastomer)',
            transform=ax.transAxes, fontsize=9, va='top',
            bbox=dict(boxstyle='round', fc='white', ec='#CCC', alpha=0.9))
    fig.tight_layout(); save(fig, 'm5_A_stress_strain.png')

def m5_B():
    """Wytrzymałość na rozciąganie vs. temperatura"""
    T   = np.array([-115, -80, -50,  0, 23, 100, 150, 200, 250, 300])
    UTS = np.array([ 30,   15,  11, 7.5, 6.0,  5.0,  4.5,  4.0,  3.5,  3.0])

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(T, UTS, color=COL['M5'], marker='o')
    ax.axvline(-115, color='gray', lw=1.2, ls=':', alpha=0.7, label='T_g = −115 °C')
    ax.axvline( 23,  color='green', lw=1.0, ls='--', alpha=0.5, label='RT (23 °C)')
    ax.set_xlabel('Temperatura [°C]')
    ax.set_ylabel('Wytrzymałość na rozciąganie [MPa]')
    ax.set_title('M5 — Guma silikonowa / RTV\nWytrzymałość na rozciąganie vs. temperatura')
    ax.legend()
    ax.annotate('Obszar zeszklenia\n(T < T_g)',
                xy=(-115, 28), xytext=(-70, 22),
                arrowprops=dict(arrowstyle='->', color='gray'),
                fontsize=9, color='gray')
    fig.tight_layout(); save(fig, 'm5_B_uts_vs_temp.png')

def m5_C():
    """Moduł Younga vs. temperatura — dramatyczne zmiany w pobliżu T_g"""
    T = np.array([-115, -100,  -80,  -75, -50, -20,   0,  23, 100, 200, 300])
    E = np.array([2000,  800,  100,   40,   8,   4,   3,  2.0, 1.6, 1.2, 0.9])

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.semilogy(T, E, color=COL['M5'], marker='o')
    ax.axvline(-115, color='gray', lw=1.2, ls=':', alpha=0.7, label='T_g = −115 °C')
    ax.axvline( -75, color='purple', lw=1.2, ls=':', alpha=0.6, label='Początek krystalizacji (−75 °C)')
    ax.axvline(  23, color='green',  lw=1.0, ls='--', alpha=0.5, label='RT (23 °C)')
    ax.set_xlabel('Temperatura [°C]')
    ax.set_ylabel('Moduł Younga [MPa]  (skala log)')
    ax.set_title("M5 — Guma silikonowa / RTV\nModuł Younga vs. temperatura")
    ax.legend(fontsize=8)
    ax.text(0.04, 0.15,
            'Źródło: Wegner et al. (2018)\nInt. J. Adhesion and Adhesives',
            transform=ax.transAxes, fontsize=8, color='gray',
            bbox=dict(boxstyle='round', fc='white', ec='#CCC', alpha=0.85))
    fig.tight_layout(); save(fig, 'm5_C_modulus_vs_temp.png')

def m5_D():
    """Przewodnictwo cieplne vs. temperatura — dane Barucci et al. 1998"""
    T_K = np.array([  1.2,   5,   10,   20,   30,   50,   80,  100,  150,  200,  220,  250,  300])
    k   = np.array([0.002, 0.010, 0.025, 0.060, 0.095, 0.140, 0.185, 0.205, 0.240, 0.265, 0.290, 0.285, 0.275])

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.semilogx(T_K, k, color=COL['M5'], marker='o')
    ax.set_xlabel('Temperatura [K]  (skala log)')
    ax.set_ylabel('Przewodnictwo cieplne [W/m·K]')
    ax.set_title('M5 — Guma silikonowa / RTV\nPrzewodnictwo cieplne vs. temperatura')
    ax.axvline(220, color='gray', lw=1.0, ls='--', alpha=0.6, label='Maks. k ≈ 0.29 W/m·K @ 220 K')
    ax.legend()
    ax.text(0.04, 0.92,
            'Źródło: Barucci et al. (1998)\nCryogenics, 38, 227',
            transform=ax.transAxes, fontsize=8, color='gray',
            bbox=dict(boxstyle='round', fc='white', ec='#CCC', alpha=0.85))
    fig.tight_layout(); save(fig, 'm5_D_thermal_cond_vs_temp.png')


# ════════════════════════════════════════════════════════════════════════════
#  M6 – Kompozyt polisiloksanowy
# ════════════════════════════════════════════════════════════════════════════

def m6_A():
    """Krzywa naprężenie–odkształcenie (liniowo–sprężysta, kruche pęknięcie)"""
    E_MPa = 45500.0
    uts   = 182.0
    ef    = uts / E_MPa          # ~0.0040 = 0.40 %… ale dane mówią 0.97%
    ef    = 0.0097

    eps = np.linspace(0, ef, 400)
    sig = E_MPa * eps

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(eps * 100, sig, color=COL['M6'])
    ax.scatter([ef * 100], [uts], color='red', zorder=5, s=70, label='Zerwanie (UTS = 182 MPa)')
    ax.axvline(ef * 100, color='red', lw=1.2, ls='--', alpha=0.6)
    ax.set_xlabel('Odkształcenie [%]')
    ax.set_ylabel('Naprężenie [MPa]')
    ax.set_title('M6 — Kompozyt polisiloksanowy (CF/UHTR)\nKrzywa naprężenie–odkształcenie (T = 23 °C)')
    ax.set_xlim(0, 1.3); ax.set_ylim(0, 230)
    ax.legend()
    ax.text(0.04, 0.92,
            'E = 45 500 MPa\nUTS = 182 MPa\nεf = 0.97 %\n(pęknięcie kruche)',
            transform=ax.transAxes, fontsize=9, va='top',
            bbox=dict(boxstyle='round', fc='white', ec='#CCC', alpha=0.9))
    ax.text(0.65, 0.18,
            'Źródło: McDermott et al. (2022)\nJ. Composite Materials, 56, 685',
            transform=ax.transAxes, fontsize=8, color='gray',
            bbox=dict(boxstyle='round', fc='white', ec='#CCC', alpha=0.85))
    fig.tight_layout(); save(fig, 'm6_A_stress_strain.png')

def m6_B():
    """Wytrzymałość na rozciąganie vs. temperatura (dane szacunkowe + piroliza)"""
    T   = np.array([  23,  100,  200,  300,  400,  500])
    UTS = np.array([182,   160,  130,   90,   55,   25])

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(T[:5], UTS[:5], color=COL['M6'], marker='o', label='Zakres kompozytu')
    ax.plot(T[4:], UTS[4:], color=COL['M6'], marker='o', ls='--', alpha=0.5, label='Strefa pirolizy (szac.)')
    ax.axvspan(300, 550, alpha=0.08, color='red', label='Piroliza matrycy (300–550 °C)')
    ax.set_xlabel('Temperatura [°C]')
    ax.set_ylabel('Wytrzymałość na rozciąganie [MPa]')
    ax.set_title('M6 — Kompozyt polisiloksanowy\nWytrzymałość na rozciąganie vs. temperatura')
    ax.set_xlim(0, 550); ax.set_ylim(0, 220)
    ax.legend(fontsize=8)
    ax.text(0.04, 0.15,
            '* Dane częściowo szacunkowe\n  (brak pełnych danych exp.)',
            transform=ax.transAxes, fontsize=8, color='gray',
            bbox=dict(boxstyle='round', fc='white', ec='#CCC', alpha=0.85))
    fig.tight_layout(); save(fig, 'm6_B_uts_vs_temp.png')

def m6_C():
    """Moduł Younga vs. temperatura"""
    T = np.array([ 23,  100,  200,  300])
    E = np.array([45500, 40000, 32000, 22000])   # MPa

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(T, E / 1000, color=COL['M6'], marker='o')
    ax.set_xlabel('Temperatura [°C]')
    ax.set_ylabel('Moduł Younga [GPa]')
    ax.set_title("M6 — Kompozyt polisiloksanowy (CF/UHTR)\nModuł Younga vs. temperatura")
    ax.set_ylim(0, 55)
    ax.text(0.04, 0.92,
            'Źródło: Hou et al., Techneglas\n(CF/UHTR laminate, dane częściowe)',
            transform=ax.transAxes, fontsize=8, va='top', color='gray',
            bbox=dict(boxstyle='round', fc='white', ec='#CCC', alpha=0.85))
    fig.tight_layout(); save(fig, 'm6_C_modulus_vs_temp.png')

def m6_D():
    """Przewodnictwo cieplne vs. temperatura (dane Tate et al., formuła F1)"""
    T = np.array([ 50,  149,  260,  600])
    k = np.array([0.68, 0.63, 0.65, 0.85])

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(T, k, color=COL['M6'], marker='o')
    ax.axvspan(300, 550, alpha=0.08, color='red', label='Strefa pirolizy (300–550 °C)')
    ax.set_xlabel('Temperatura [°C]')
    ax.set_ylabel('Przewodnictwo cieplne [W/m·K]')
    ax.set_title('M6 — Kompozyt polisiloksanowy (F1)\nPrzewodnictwo cieplne vs. temperatura')
    ax.set_ylim(0, 1.1)
    ax.legend(fontsize=8)
    ax.text(0.04, 0.92,
            'Źródło: Tate et al., Techneglas\n(formulacja F1)',
            transform=ax.transAxes, fontsize=8, va='top', color='gray',
            bbox=dict(boxstyle='round', fc='white', ec='#CCC', alpha=0.85))
    fig.tight_layout(); save(fig, 'm6_D_thermal_cond_vs_temp.png')


# ════════════════════════════════════════════════════════════════════════════
#  M7 – Kevlar-29 / Kevlar-49
# ════════════════════════════════════════════════════════════════════════════

def m7_A():
    """Krzywa naprężenie–odkształcenie — K-29 i K-49 (liniowa, krucha)"""
    fig, ax = plt.subplots(figsize=(8, 5))

    for label, E_GPa, uts, ef, col, ls in [
        ('Kevlar-29', 70.5,  3600, 0.036, COL['M7a'], '-'),
        ('Kevlar-49', 125.0, 3800, 0.024, COL['M7b'], '--'),
    ]:
        eps = np.linspace(0, ef, 400)
        sig = E_GPa * 1000 * eps
        ax.plot(eps * 100, sig, color=col, ls=ls, label=label)
        ax.scatter([ef * 100], [uts], color=col, zorder=5, s=70, marker='X')

    ax.set_xlabel('Odkształcenie [%]')
    ax.set_ylabel('Naprężenie [MPa]')
    ax.set_title('M7 — Kevlar-29 / Kevlar-49 (włókno aramidowe)\nKrzywa naprężenie–odkształcenie (T = 23 °C)')
    ax.set_xlim(0, 4.5); ax.set_ylim(0, 5000)
    ax.legend()
    ax.text(0.04, 0.92,
            'Brak granicy plastyczności\n(pęknięcie liniowo-sprężyste)\n(×) = zerwanie',
            transform=ax.transAxes, fontsize=9, va='top',
            bbox=dict(boxstyle='round', fc='white', ec='#CCC', alpha=0.9))
    ax.text(0.55, 0.12,
            'Źródło: DuPont Kevlar Tech Guide;\nMatWeb – Kevlar 29/49',
            transform=ax.transAxes, fontsize=8, color='gray',
            bbox=dict(boxstyle='round', fc='white', ec='#CCC', alpha=0.85))
    fig.tight_layout(); save(fig, 'm7_A_stress_strain.png')

def m7_B():
    """Wytrzymałość na rozciąganie vs. temperatura — K-29 i K-49"""
    T = np.array([-196, -100,   0,  23, 100, 200, 300, 430])
    UTS_29 = np.array([4200, 3900, 3700, 3600, 3200, 2600, 1800, 400])
    UTS_49 = np.array([4600, 4200, 3900, 3800, 3400, 2800, 2000, 500])

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(T, UTS_29, color=COL['M7a'], marker='o', label='Kevlar-29')
    ax.plot(T, UTS_49, color=COL['M7b'], marker='s', ls='--', label='Kevlar-49')
    ax.axvline( 23, color='green', lw=1.0, ls='--', alpha=0.5)
    ax.axvline(430, color='red',   lw=1.2, ls=':',  alpha=0.7, label='Początek degradacji (430 °C)')
    ax.set_xlabel('Temperatura [°C]')
    ax.set_ylabel('Wytrzymałość na rozciąganie [MPa]')
    ax.set_title('M7 — Kevlar-29 / Kevlar-49\nWytrzymałość na rozciąganie vs. temperatura')
    ax.set_ylim(0, 5500)
    ax.legend()
    ax.text(0.55, 0.92,
            'Źródło: DuPont Kevlar Tech Guide;\nPMC12349578 (2025)',
            transform=ax.transAxes, fontsize=8, va='top', color='gray',
            bbox=dict(boxstyle='round', fc='white', ec='#CCC', alpha=0.85))
    fig.tight_layout(); save(fig, 'm7_B_uts_vs_temp.png')

def m7_C():
    """Moduł Younga vs. temperatura — K-29 i K-49"""
    T = np.array([-196, -100,   0,  23, 100, 200, 300])
    E_29 = np.array([72.0, 71.5, 71.0, 70.5, 68.0, 63.0, 55.0])
    E_49 = np.array([128,  127,  126,  125,  122,  116,  105 ])

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(T, E_29, color=COL['M7a'], marker='o', label='Kevlar-29')
    ax.plot(T, E_49, color=COL['M7b'], marker='s', ls='--', label='Kevlar-49')
    ax.axvline(23, color='green', lw=1.0, ls='--', alpha=0.5, label='RT (23 °C)')
    ax.set_xlabel('Temperatura [°C]')
    ax.set_ylabel("Moduł Younga [GPa]")
    ax.set_title("M7 — Kevlar-29 / Kevlar-49\nModuł Younga vs. temperatura")
    ax.set_ylim(0, 160)
    ax.legend()
    fig.tight_layout(); save(fig, 'm7_C_modulus_vs_temp.png')

def m7_D():
    """Przewodnictwo cieplne vs. temperatura (Ventura & Martelli 2009, kierunek poprzeczny)"""
    T_K = np.array([ 7,  10,  15,  20,  30,  50,  77, 100, 150, 200, 250, 290])
    k   = np.array([0.010, 0.012, 0.015, 0.018, 0.022, 0.028, 0.033, 0.036, 0.038, 0.039, 0.040, 0.040])

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.semilogx(T_K, k, color=COL['M7a'], marker='o', label='Kevlar-49 (kierunek poprzeczny)')
    ax.axhline(3.8, color=COL['M7b'], lw=1.5, ls='--', alpha=0.7, label='Kierunek osiowy ~3.5–4.0 W/m·K (RT)')
    ax.set_xlabel('Temperatura [K]  (skala log)')
    ax.set_ylabel('Przewodnictwo cieplne [W/m·K]')
    ax.set_title('M7 — Kevlar-49\nPrzewodnictwo cieplne vs. temperatura')
    ax.legend()
    ax.text(0.04, 0.92,
            'Źródło: Ventura & Martelli (2009)\nCryogenics, 49, 509\n(materiał silnie anizotropowy)',
            transform=ax.transAxes, fontsize=8, va='top', color='gray',
            bbox=dict(boxstyle='round', fc='white', ec='#CCC', alpha=0.85))
    fig.tight_layout(); save(fig, 'm7_D_thermal_cond_vs_temp.png')


# ════════════════════════════════════════════════════════════════════════════
#  M8 – Mylar / BoPET
# ════════════════════════════════════════════════════════════════════════════

def m8_A():
    """Krzywa naprężenie–odkształcenie (pół-ciągliwy, orientacja dwuosiowa)"""
    E    = 3950.0   # MPa
    sy   = 67.5
    uts  = 200.0
    ef   = 1.375
    ey   = sy / E   # ~0.0171

    eps_e = np.linspace(0, ey, 120)
    eps_p = np.linspace(ey, ef, 480)
    n     = np.log(uts / sy) / np.log(ef / ey)
    sig_e = E * eps_e
    sig_p = sy * (eps_p / ey) ** n
    eps_f = np.concatenate([eps_e, eps_p])
    sig_f = np.concatenate([sig_e, sig_p])

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(eps_f * 100, sig_f, color=COL['M8'])
    ax.scatter([ey * 100], [sy],   color='purple', zorder=5, s=70, marker='D',
               label=f'Granica plastyczności ≈ {sy:.0f} MPa')
    ax.scatter([ef * 100], [uts],  color='red',    zorder=5, s=70,
               label=f'Zerwanie (UTS ≈ {uts:.0f} MPa)')
    ax.axvline(ey * 100, color='purple', lw=1.0, ls=':', alpha=0.5)
    ax.axvline(ef * 100, color='red',    lw=1.2, ls='--', alpha=0.6)
    ax.set_xlabel('Odkształcenie [%]')
    ax.set_ylabel('Naprężenie [MPa]')
    ax.set_title('M8 — Mylar® / BoPET\nKrzywa naprężenie–odkształcenie (T = 23 °C)')
    ax.set_xlim(0, 160); ax.set_ylim(0, 240)
    ax.legend()
    ax.text(0.55, 0.18,
            'Źródło: DuPont Teijin Films\nMylar® A datasheet (ASTM D882)',
            transform=ax.transAxes, fontsize=8, color='gray',
            bbox=dict(boxstyle='round', fc='white', ec='#CCC', alpha=0.85))
    fig.tight_layout(); save(fig, 'm8_A_stress_strain.png')

def m8_B():
    """Wytrzymałość na rozciąganie vs. temperatura"""
    T   = np.array([-70, -40, -20,   0,  23,  60,  80, 100, 120, 150])
    UTS = np.array([280, 255, 240, 225, 200, 160, 120,  80,  50,  25])

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(T, UTS, color=COL['M8'], marker='o')
    ax.axvline( 23, color='green',  lw=1.0, ls='--', alpha=0.5, label='RT (23 °C)')
    ax.axvline( 80, color='purple', lw=1.2, ls=':',  alpha=0.7, label='T_g ≈ 80 °C')
    ax.axvline(150, color='red',    lw=1.2, ls=':',  alpha=0.7, label='Maks. temp. pracy (150 °C)')
    ax.set_xlabel('Temperatura [°C]')
    ax.set_ylabel('Wytrzymałość na rozciąganie [MPa]')
    ax.set_title('M8 — Mylar® / BoPET\nWytrzymałość na rozciąganie vs. temperatura')
    ax.set_ylim(0, 320)
    ax.legend(fontsize=8)
    ax.text(0.55, 0.92,
            'Źródło: DuPont Teijin Films datasheet;\nAZoM ID:2047',
            transform=ax.transAxes, fontsize=8, va='top', color='gray',
            bbox=dict(boxstyle='round', fc='white', ec='#CCC', alpha=0.85))
    fig.tight_layout(); save(fig, 'm8_B_uts_vs_temp.png')

def m8_C():
    """Moduł Younga vs. temperatura"""
    T = np.array([-70, -40, -20,   0,  23,  60,  80, 100, 120, 150])
    E = np.array([7000, 6000, 5500, 5000, 3950, 2500, 1200, 500, 200, 100])

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.semilogy(T, E, color=COL['M8'], marker='o')
    ax.axvline( 23, color='green',  lw=1.0, ls='--', alpha=0.5, label='RT (23 °C)')
    ax.axvline( 80, color='purple', lw=1.2, ls=':',  alpha=0.7, label='T_g ≈ 80 °C')
    ax.set_xlabel('Temperatura [°C]')
    ax.set_ylabel("Moduł Younga [MPa]  (skala log)")
    ax.set_title("M8 — Mylar® / BoPET\nModuł Younga vs. temperatura")
    ax.legend()
    ax.text(0.04, 0.15,
            'Źródło: DuPont Teijin Films datasheet;\nAZoM ID:2047',
            transform=ax.transAxes, fontsize=8, color='gray',
            bbox=dict(boxstyle='round', fc='white', ec='#CCC', alpha=0.85))
    fig.tight_layout(); save(fig, 'm8_C_modulus_vs_temp.png')

def m8_D():
    """Przewodnictwo cieplne vs. temperatura"""
    T = np.array([-70,   0,  23,  80, 150])
    k = np.array([0.12, 0.14, 0.15, 0.17, 0.18])

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(T, k, color=COL['M8'], marker='o')
    ax.axvline(23,  color='green',  lw=1.0, ls='--', alpha=0.5, label='RT (23 °C)')
    ax.axvline(80,  color='purple', lw=1.2, ls=':',  alpha=0.7, label='T_g ≈ 80 °C')
    ax.axvline(150, color='red',    lw=1.2, ls=':',  alpha=0.7, label='Maks. temp. pracy (150 °C)')
    ax.set_xlabel('Temperatura [°C]')
    ax.set_ylabel('Przewodnictwo cieplne [W/m·K]')
    ax.set_title('M8 — Mylar® / BoPET\nPrzewodnictwo cieplne vs. temperatura')
    ax.set_ylim(0.08, 0.24)
    ax.legend(fontsize=8)
    ax.text(0.04, 0.92,
            'Źródło: Thermtest; Professional Plastics\n(dane częściowe)',
            transform=ax.transAxes, fontsize=8, va='top', color='gray',
            bbox=dict(boxstyle='round', fc='white', ec='#CCC', alpha=0.85))
    fig.tight_layout(); save(fig, 'm8_D_thermal_cond_vs_temp.png')


# ════════════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print("Generowanie wykresów M5–M8...")
    m5_A(); m5_B(); m5_C(); m5_D()
    m6_A(); m6_B(); m6_C(); m6_D()
    m7_A(); m7_B(); m7_C(); m7_D()
    m8_A(); m8_B(); m8_C(); m8_D()
    print(f"\nWszystkie wykresy zapisane w: {OUT}")
