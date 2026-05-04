"""
Generate all material property plots for M5-M8 (Filip's assignment).
A comparison of selected organic materials for low orbiting spacecraft.

Run from the repo root:
    python Filip/plots/generate_plots.py
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec

from data.material_properties import (
    silicone_rtv, polysiloxane_comp, kevlar_29, kevlar_49, mylar_pet, ALL_MATERIALS
)

OUT_DIR = os.path.dirname(__file__)

STYLE = {
    'figure.facecolor':  'white',
    'axes.facecolor':    '#F8F9FA',
    'axes.edgecolor':    '#CCCCCC',
    'axes.grid':         True,
    'grid.color':        '#E0E0E0',
    'grid.linestyle':    '--',
    'grid.linewidth':    0.7,
    'font.family':       'DejaVu Sans',
    'font.size':         11,
    'axes.titlesize':    13,
    'axes.labelsize':    11,
    'xtick.labelsize':   9,
    'ytick.labelsize':   10,
    'legend.fontsize':   9,
    'figure.dpi':        150,
}
plt.rcParams.update(STYLE)

COLORS  = [m['color'] for m in ALL_MATERIALS]
LABELS  = [m['short'] for m in ALL_MATERIALS]
HATCHES = ['/', '\\', 'x', '+', 'o']

def save(fig, name):
    path = os.path.join(OUT_DIR, name)
    fig.savefig(path, bbox_inches='tight', dpi=150)
    plt.close(fig)
    print(f"  Saved: {name}")


# ════════════════════════════════════════════════════════════════════════════
# 1. ULTIMATE TENSILE STRENGTH (bar chart, log scale)
# ════════════════════════════════════════════════════════════════════════════
def plot_uts():
    vals  = [m['uts_mpa'] for m in ALL_MATERIALS]
    errs  = [m['uts_err'] for m in ALL_MATERIALS]

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(LABELS, vals, color=COLORS, edgecolor='white',
                  linewidth=1.2, hatch=None, yerr=errs,
                  capsize=5, error_kw={'elinewidth':1.5, 'ecolor':'#555'})

    ax.set_yscale('log')
    ax.set_ylabel('Ultimate Tensile Strength [MPa]')
    ax.set_title('Ultimate Tensile Strength — M5 to M8 Materials\n'
                 '(logarithmic scale due to large range)')
    ax.set_ylim(1, 10000)

    for bar, val in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width()/2, val * 1.8,
                f'{val:.0f} MPa', ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax.annotate('Note: Kevlar values are for single fiber;\ncomposite/laminate values are lower.',
                xy=(0.98, 0.03), xycoords='axes fraction', ha='right', va='bottom',
                fontsize=8, color='gray',
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='gray', alpha=0.7))
    fig.tight_layout()
    save(fig, 'plot_01_tensile_strength.png')


# ════════════════════════════════════════════════════════════════════════════
# 2. YOUNG'S MODULUS (log scale)
# ════════════════════════════════════════════════════════════════════════════
def plot_modulus():
    vals = [m['youngs_gpa'] * 1000 for m in ALL_MATERIALS]   # convert to MPa
    errs = [m['youngs_err'] * 1000 for m in ALL_MATERIALS]

    labels_mod = ['RTV Silicone\n(~3 MPa)', 'Polysiloxane\nComposite\n(45,500 MPa)',
                  'Kevlar-29\n(70,500 MPa)', 'Kevlar-49\n(125,000 MPa)',
                  'Mylar\n(3,950 MPa)']

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(labels_mod, vals, color=COLORS, edgecolor='white',
                  linewidth=1.2, yerr=errs,
                  capsize=5, error_kw={'elinewidth':1.5, 'ecolor':'#555'})
    ax.set_yscale('log')
    ax.set_ylabel("Young's Modulus [MPa]")
    ax.set_title("Young's Modulus — M5 to M8 Materials\n"
                 "(logarithmic scale; range spans ~7 orders of magnitude)")
    ax.set_ylim(0.1, 200000)

    ax2 = ax.twinx()
    ax2.set_yscale('log')
    ax2.set_ylim(0.1/1000, 200)
    ax2.set_ylabel("Young's Modulus [GPa]", color='gray')
    ax2.tick_params(axis='y', labelcolor='gray')

    for bar, val in zip(bars, vals):
        label = f'{val:.0f}' if val >= 1 else f'{val:.2f}'
        ax.text(bar.get_x() + bar.get_width()/2, val * 2.5,
                label + ' MPa', ha='center', va='bottom', fontsize=8, fontweight='bold')

    fig.tight_layout()
    save(fig, 'plot_02_youngs_modulus.png')


# ════════════════════════════════════════════════════════════════════════════
# 3. DENSITY
# ════════════════════════════════════════════════════════════════════════════
def plot_density():
    vals = [m['density'] for m in ALL_MATERIALS]
    errs = [m['density_err'] for m in ALL_MATERIALS]

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(LABELS, vals, color=COLORS, edgecolor='white',
                  linewidth=1.2, yerr=errs,
                  capsize=5, error_kw={'elinewidth':1.5, 'ecolor':'#555'})
    ax.set_ylabel('Density [kg/m³]')
    ax.set_title('Density — M5 to M8 Materials')
    ax.set_ylim(0, 1900)

    for bar, val in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width()/2, val + 25,
                f'{val:.0f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

    fig.tight_layout()
    save(fig, 'plot_03_density.png')


# ════════════════════════════════════════════════════════════════════════════
# 4. THERMAL CONDUCTIVITY
# ════════════════════════════════════════════════════════════════════════════
def plot_thermal_conductivity():
    vals = [m['therm_cond'] for m in ALL_MATERIALS]
    errs = [m['therm_cond_err'] for m in ALL_MATERIALS]

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(LABELS, vals, color=COLORS, edgecolor='white',
                  linewidth=1.2, yerr=errs,
                  capsize=5, error_kw={'elinewidth':1.5, 'ecolor':'#555'})
    ax.set_ylabel('Thermal Conductivity [W/m·K]')
    ax.set_title('Thermal Conductivity — M5 to M8 Materials')
    ax.set_ylim(0, 0.40)

    for bar, val in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width()/2, val + 0.01,
                f'{val:.3f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

    ax.annotate('Kevlar value is transverse (across fiber);\naxial conductivity is ~3.5–4.0 W/m·K (not shown).',
                xy=(0.98, 0.92), xycoords='axes fraction', ha='right', va='top',
                fontsize=8, color='gray',
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='gray', alpha=0.7))
    fig.tight_layout()
    save(fig, 'plot_04_thermal_conductivity.png')


# ════════════════════════════════════════════════════════════════════════════
# 5. SPECIFIC HEAT CAPACITY
# ════════════════════════════════════════════════════════════════════════════
def plot_heat_capacity():
    vals = [m['heat_cap'] for m in ALL_MATERIALS]
    errs = [m['heat_cap_err'] for m in ALL_MATERIALS]

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(LABELS, vals, color=COLORS, edgecolor='white',
                  linewidth=1.2, yerr=errs,
                  capsize=5, error_kw={'elinewidth':1.5, 'ecolor':'#555'})
    ax.set_ylabel('Specific Heat Capacity [J/kg·K]')
    ax.set_title('Specific Heat Capacity — M5 to M8 Materials')
    ax.set_ylim(0, 2000)

    for bar, val in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width()/2, val + 30,
                f'{val:.0f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

    fig.tight_layout()
    save(fig, 'plot_05_heat_capacity.png')


# ════════════════════════════════════════════════════════════════════════════
# 6. OPERATING TEMPERATURE RANGE (horizontal range bars)
# ════════════════════════════════════════════════════════════════════════════
def plot_operating_temp():
    materials  = ALL_MATERIALS
    labels_rev = [m['short'] for m in reversed(materials)]
    t_mins     = [m['t_min'] for m in reversed(materials)]
    t_maxs     = [m['t_max'] for m in reversed(materials)]
    cols_rev   = list(reversed(COLORS))

    fig, ax = plt.subplots(figsize=(11, 5))
    y_pos = np.arange(len(labels_rev))

    for i, (tmin, tmax, col) in enumerate(zip(t_mins, t_maxs, cols_rev)):
        ax.barh(y_pos[i], tmax - tmin, left=tmin, height=0.5,
                color=col, edgecolor='white', linewidth=1.2, alpha=0.9)
        ax.text(tmax + 15, y_pos[i], f'{tmax:.0f}°C', va='center', fontsize=9)
        ax.text(tmin - 15, y_pos[i], f'{tmin:.0f}°C', va='center', ha='right', fontsize=9)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels_rev)
    ax.set_xlabel('Temperature [°C]')
    ax.set_title('Operating Temperature Range — M5 to M8 Materials')
    ax.axvline(0, color='black', linewidth=0.8, linestyle='-', alpha=0.5)
    ax.axvline(20, color='gray', linewidth=0.6, linestyle=':', alpha=0.4, label='RT (20°C)')
    ax.set_xlim(-300, 1600)
    ax.legend(loc='lower right', fontsize=8)
    fig.tight_layout()
    save(fig, 'plot_06_operating_temperature.png')


# ════════════════════════════════════════════════════════════════════════════
# 7. FRACTURE TOUGHNESS (only where available)
# ════════════════════════════════════════════════════════════════════════════
def plot_fracture_toughness():
    available = [(m['short'], m['fracture_tough'], m.get('fracture_tough_err', 0), m['color'])
                 for m in ALL_MATERIALS if m['fracture_tough'] is not None]
    labels_ft = [x[0] for x in available]
    vals_ft   = [x[1] for x in available]
    errs_ft   = [x[2] for x in available]
    cols_ft   = [x[3] for x in available]

    fig, ax = plt.subplots(figsize=(7, 4.5))
    bars = ax.bar(labels_ft, vals_ft, color=cols_ft, edgecolor='white',
                  linewidth=1.2, yerr=errs_ft,
                  capsize=5, error_kw={'elinewidth':1.5, 'ecolor':'#555'})
    ax.set_ylabel('Fracture Toughness K$_{IC}$ [MPa·m$^{0.5}$]')
    ax.set_title('Fracture Toughness — M5 to M8 Materials\n'
                 '(only materials with available data shown)')
    ax.set_ylim(0, 8)

    for bar, val in zip(bars, vals_ft):
        ax.text(bar.get_x() + bar.get_width()/2, val + 0.15,
                f'{val:.2f}', ha='center', va='bottom', fontsize=11, fontweight='bold')

    ax.annotate('RTV Silicone: characterized by tear energy, not K$_{IC}$\n'
                'Kevlar fibers: brittle fibrillation, K$_{IC}$ not established\n'
                'Mylar estimate: bulk PET range 2–5 MPa·m$^{0.5}$',
                xy=(0.98, 0.92), xycoords='axes fraction', ha='right', va='top',
                fontsize=8, color='gray',
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='gray', alpha=0.7))
    fig.tight_layout()
    save(fig, 'plot_07_fracture_toughness.png')


# ════════════════════════════════════════════════════════════════════════════
# 8. STRESS–STRAIN CURVES (representative / schematic)
# ════════════════════════════════════════════════════════════════════════════
def plot_stress_strain():
    fig = plt.figure(figsize=(14, 10))
    gs  = GridSpec(2, 2, figure=fig, hspace=0.42, wspace=0.35)
    axes = [fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1]),
            fig.add_subplot(gs[1, 0]), fig.add_subplot(gs[1, 1])]

    # ── Panel A: RTV Silicone (Neo-Hookean elastomer) ──
    ax = axes[0]
    eps = np.linspace(0, 4.0, 500)            # strain 0 to 400%
    lam = 1 + eps
    # Neo-Hookean: σ = G*(λ - λ^-2); tune G to match UTS ~ 6 MPa at 400%
    G = 0.85
    sig = G * (lam - lam**(-2))
    ax.plot(eps * 100, sig, color=silicone_rtv['color'], lw=2.5)
    ax.axvline(400, color='red', lw=1.2, ls='--', alpha=0.7, label='Failure point')
    ax.scatter([400], [6.0], color='red', zorder=5, s=60)
    ax.set_xlabel('Strain [%]')
    ax.set_ylabel('Stress [MPa]')
    ax.set_title('M5 — RTV Silicone Rubber\n(Neo-Hookean, elastomeric)')
    ax.set_xlim(0, 450); ax.set_ylim(0, 10)
    ax.legend(fontsize=8)
    ax.text(0.05, 0.92, 'E ≈ 1–5 MPa\nUTS ≈ 2–10 MPa\nεf ≈ 100–800%',
            transform=ax.transAxes, fontsize=8, va='top',
            bbox=dict(boxstyle='round', fc='white', ec='gray', alpha=0.8))

    # ── Panel B: Polysiloxane Composite CF/UHTR (brittle) ──
    ax = axes[1]
    eps_c = np.linspace(0, 0.0097, 300)
    sig_c = 45500 * eps_c   # E=45.5 GPa in MPa
    ax.plot(eps_c * 100, sig_c, color=polysiloxane_comp['color'], lw=2.5)
    ax.axvline(0.97, color='red', lw=1.2, ls='--', alpha=0.7, label='Failure point')
    ax.scatter([0.97], [182], color='red', zorder=5, s=60)
    ax.set_xlabel('Strain [%]')
    ax.set_ylabel('Stress [MPa]')
    ax.set_title('M6 — Polysiloxane Composite (CF/UHTR)\n(linear elastic, brittle failure)')
    ax.set_xlim(0, 1.3); ax.set_ylim(0, 250)
    ax.legend(fontsize=8)
    ax.text(0.05, 0.92, 'E ≈ 45.5 GPa\nUTS ≈ 182 MPa\nεf ≈ 0.97%',
            transform=ax.transAxes, fontsize=8, va='top',
            bbox=dict(boxstyle='round', fc='white', ec='gray', alpha=0.8))

    # ── Panel C: Kevlar-29 & Kevlar-49 (brittle, linear) ──
    ax = axes[2]
    # Kevlar-29
    eps_k29 = np.linspace(0, 0.036, 300)
    sig_k29 = 70500 * eps_k29
    ax.plot(eps_k29 * 100, sig_k29, color=kevlar_29['color'], lw=2.5, label='Kevlar-29')
    ax.scatter([3.6], [3600], color=kevlar_29['color'], zorder=5, s=60, marker='x', linewidths=2)
    # Kevlar-49
    eps_k49 = np.linspace(0, 0.024, 300)
    sig_k49 = 125000 * eps_k49
    ax.plot(eps_k49 * 100, sig_k49, color=kevlar_49['color'], lw=2.5,
            linestyle='--', label='Kevlar-49')
    ax.scatter([2.4], [3800], color=kevlar_49['color'], zorder=5, s=60, marker='x', linewidths=2)
    ax.set_xlabel('Strain [%]')
    ax.set_ylabel('Stress [MPa]')
    ax.set_title('M7 — Kevlar-29 / Kevlar-49 (Aramid Fiber)\n(linear elastic, brittle failure at high UTS)')
    ax.set_xlim(0, 4.5); ax.set_ylim(0, 5000)
    ax.legend(fontsize=8)
    ax.text(0.05, 0.92,
            'K-29: E=70.5 GPa, UTS=3600 MPa, εf=3.6%\nK-49: E=125 GPa, UTS=3800 MPa, εf=2.4%\n(×) = failure',
            transform=ax.transAxes, fontsize=8, va='top',
            bbox=dict(boxstyle='round', fc='white', ec='gray', alpha=0.8))

    # ── Panel D: Mylar / BoPET (semi-ductile) ──
    ax = axes[3]
    E    = 3950.0    # MPa
    sy   = 67.5      # yield MPa
    uts  = 200.0     # MPa
    ef   = 1.375     # strain at failure
    ey   = sy / E    # ~0.017

    # Elastic region
    eps_e = np.linspace(0, ey, 100)
    sig_e = E * eps_e

    # Post-yield region (power-law hardening to UTS)
    eps_p = np.linspace(ey, ef, 400)
    n     = np.log(uts / sy) / np.log(ef / ey)
    sig_p = sy * (eps_p / ey) ** n

    eps_full = np.concatenate([eps_e, eps_p])
    sig_full = np.concatenate([sig_e, sig_p])

    ax.plot(eps_full * 100, sig_full, color=mylar_pet['color'], lw=2.5)
    ax.axvline(ef * 100, color='red', lw=1.2, ls='--', alpha=0.7, label='Failure point')
    ax.scatter([ef * 100], [uts], color='red', zorder=5, s=60)
    ax.axvline(ey * 100, color='gray', lw=1.0, ls=':', alpha=0.6, label='Yield point')
    ax.scatter([ey * 100], [sy], color='gray', zorder=5, s=50, marker='D')
    ax.set_xlabel('Strain [%]')
    ax.set_ylabel('Stress [MPa]')
    ax.set_title('M8 — Mylar / BoPET Film\n(semi-ductile; biaxially oriented)')
    ax.set_xlim(0, 160); ax.set_ylim(0, 250)
    ax.legend(fontsize=8)
    ax.text(0.05, 0.92,
            'E ≈ 3.95 GPa\nσ_y ≈ 67.5 MPa\nUTS ≈ 200 MPa\nεf ≈ 115–160%',
            transform=ax.transAxes, fontsize=8, va='top',
            bbox=dict(boxstyle='round', fc='white', ec='gray', alpha=0.8))

    fig.suptitle('Representative Stress–Strain Curves — M5 to M8 Materials\n'
                 '(schematic based on literature data; scales differ per panel)',
                 fontsize=12, fontweight='bold', y=1.01)
    save(fig, 'plot_08_stress_strain_curves.png')


# ════════════════════════════════════════════════════════════════════════════
# 9. SUMMARY RADAR CHART (normalized properties)
# ════════════════════════════════════════════════════════════════════════════
def plot_radar():
    categories = ['UTS\n(norm.)', "Young's E\n(norm.)", 'Density\n(inv. norm.)',
                  'Therm. Cond.\n(inv. norm.)', 'Heat Cap.\n(norm.)',
                  'Op. Temp.\nRange (norm.)']

    # Normalize: higher = better (invert density and thermal cond. — lower is better for insulation/weight)
    uts_vals   = [m['uts_mpa']    for m in ALL_MATERIALS]
    E_vals     = [m['youngs_gpa'] * 1000 for m in ALL_MATERIALS]
    dens_vals  = [m['density']    for m in ALL_MATERIALS]
    k_vals     = [m['therm_cond'] for m in ALL_MATERIALS]
    cp_vals    = [m['heat_cap']   for m in ALL_MATERIALS]
    dt_vals    = [m['t_max'] - m['t_min'] for m in ALL_MATERIALS]

    def norm(arr):
        a = np.array(arr, dtype=float)
        return (a - a.min()) / (a.max() - a.min() + 1e-12)

    def inv_norm(arr):
        return 1 - norm(arr)

    data = np.column_stack([
        norm(uts_vals),
        norm(E_vals),
        inv_norm(dens_vals),
        inv_norm(k_vals),
        norm(cp_vals),
        norm(dt_vals),
    ])

    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    for i, (mat, dat) in enumerate(zip(ALL_MATERIALS, data)):
        vals_r = dat.tolist() + dat[:1].tolist()
        ax.plot(angles, vals_r, color=mat['color'], lw=2.0, label=mat['short'])
        ax.fill(angles, vals_r, color=mat['color'], alpha=0.12)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, size=9)
    ax.set_ylim(0, 1)
    ax.set_yticks([0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(['0.25', '0.50', '0.75', '1.00'], size=7, color='gray')
    ax.set_title('Normalized Property Radar — M5 to M8\n'
                 '(1 = best in category; density & conductivity inverted)',
                 size=12, fontweight='bold', pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.35, 1.15), fontsize=9)
    fig.tight_layout()
    save(fig, 'plot_09_radar_summary.png')


# ════════════════════════════════════════════════════════════════════════════
# 10. ABLATION DATA — Polysiloxane composite only
# ════════════════════════════════════════════════════════════════════════════
def plot_ablation():
    labels_abl = ['Mass Loss Rate\n[g/s]', 'Linear Recession\n[mm/s]', 'Char Yield\n[%]']
    vals_abl   = [polysiloxane_comp['mass_loss_rate'],
                  polysiloxane_comp['linear_recession'],
                  polysiloxane_comp['char_yield_pct'] / 100]  # normalise % to fraction

    fig, axes = plt.subplots(1, 3, figsize=(11, 4.5))

    units  = ['g/s', 'mm/s', '%']
    mult   = [1, 1, 100]

    for ax, label, val, unit, m in zip(axes, labels_abl, vals_abl, units, mult):
        ax.bar([label], [val * m], color=polysiloxane_comp['color'],
               edgecolor='white', linewidth=1.2, width=0.4)
        ax.set_ylabel(f'Value [{unit}]')
        ax.text(0, val * m * 1.05, f'{val*m:.3f} {unit}',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
        ax.set_ylim(0, val * m * 1.5)

    fig.suptitle('Ablation Properties — M6 Polysiloxane Composite (F1 formulation)\n'
                 'Source: Tate et al., Techneglas; Hou et al., Techneglas',
                 fontsize=11, fontweight='bold')
    fig.tight_layout()
    save(fig, 'plot_10_ablation_polysiloxane.png')


# ════════════════════════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print("Generating plots...")
    plot_uts()
    plot_modulus()
    plot_density()
    plot_thermal_conductivity()
    plot_heat_capacity()
    plot_operating_temp()
    plot_fracture_toughness()
    plot_stress_strain()
    plot_radar()
    plot_ablation()
    print(f"\nAll plots saved to: {OUT_DIR}")
