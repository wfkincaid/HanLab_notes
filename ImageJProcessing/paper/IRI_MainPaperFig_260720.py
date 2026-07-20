#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter.font import BOLD
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.colors import to_rgb
from pathlib import Path

plt.style.use("default")

# ---------------------- Publication styling ----------------------
plt.rcParams.update({
    "figure.dpi": 150,
    "savefig.dpi": 600,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "axes.edgecolor": "#333333",
    "axes.linewidth": 1.0,

    "font.family": "sans-serif",
    "font.sans-serif": ["Arial Unicode MS", "Helvetica", "DejaVu Sans"],
    "font.size": 9.7,

    "axes.titlesize": 11,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    
    #----- Only do for bottom half -----
    
    #    "axes.grid": True,
    #    "grid.color": "gray",
    #    "grid.alpha": 0.28,
    #    "grid.linestyle": "--",
    #    "grid.linewidth": 0.6,

    #    "axes.spines.top": False,
    #    "axes.spines.right": False,
    #    "xtick.direction": "out",
    #    "ytick.direction": "out",
    #    "xtick.major.size": 4,
    #    "ytick.major.size": 4,
})

save_path = "./Figures/IRI_assay_gly_suc_tre_nice_WKpaper_260720.pdf"

# ---------------------------------
# Load Chemdraw of PVA + solutes
# ---------------------------------
pva_sticks = cv2.imread("./Chemdraw/pva.png", cv2.IMREAD_UNCHANGED)
glycerol_sticks = cv2.imread("./Chemdraw/glycerol.png", cv2.IMREAD_UNCHANGED)
sucrose_chair = cv2.imread("./Chemdraw/sucrose.png", cv2.IMREAD_UNCHANGED)
trehalose_chair = cv2.imread("./Chemdraw/trehalose.png", cv2.IMREAD_UNCHANGED)

#path_b = './Baselines/'
# ---------------------------------------------------
# 0) Load saved b=0 fit CSVs for FIRST ROW replacement
# ---------------------------------------------------
# Glycerol
gly = pd.read_csv("./Baselines/Glycerol/fit_summary.csv")
gly1 = pd.read_csv("./Baselines/Glycerol/trial_fit_Trial_1.csv")
gly2 = pd.read_csv("./Baselines/Glycerol/trial_fit_Trial_2.csv")
gly3 = pd.read_csv("./Baselines/Glycerol/trial_fit_Trial_3.csv")

# Sucrose
suc = pd.read_csv("./Baselines/Sucrose/fit_summary.csv")
suc1 = pd.read_csv("./Baselines/Sucrose/trial_fit_Trial_1.csv")
suc2 = pd.read_csv("./Baselines/Sucrose/trial_fit_Trial_2.csv")
suc3 = pd.read_csv("./Baselines/Sucrose/trial_fit_Trial_3.csv")

# Trehalose
tre = pd.read_csv("./Baselines/Trehalose/fit_summary.csv")
tre1 = pd.read_csv("./Baselines/Trehalose/trial_fit_Trial_1.csv")
tre2 = pd.read_csv("./Baselines/Trehalose/trial_fit_Trial_2.csv")
tre3 = pd.read_csv("./Baselines/Trehalose/trial_fit_Trial_3.csv")

csv_sources = {
    "Glycerol":  {"summary": gly, "trials": [gly1, gly2, gly3]},
    "Sucrose":   {"summary": suc, "trials": [suc1, suc2, suc3]},
    "Trehalose": {"summary": tre, "trials": [tre1, tre2, tre3]},
}

# ---------------------------------------
# With PVA - trendlines
# ---------------------------------------
gly_PVA = pd.read_csv("./Trendlines_wPVA/Glycerol/summary.csv")
suc_PVA = pd.read_csv("./Trendlines_wPVA/Sucrose/summary.csv")
tre_PVA = pd.read_csv("./Trendlines_wPVA/Trehalose/summary.csv")

# ---------------------------------------------------
# 1) Load images - Update WK 3/30/26
# ---------------------------------------------------
buf_Gly_cnt = cv2.imread("./WK_images/gly5pct_0mgmLPVA_120min_Proc322_T0024_t1.tif", cv2.IMREAD_GRAYSCALE) #./Baselines/Glycerol/3/Image_14046_2 hour mark_with scale bar.tif
buf_Suc_cnt = cv2.imread("./WK_images/suc18pct_0mgmLPVA_120min_Proc313_T0024_t3.tif", cv2.IMREAD_GRAYSCALE) #./Baselines/Sucrose/2/Image_13951.tif
buf_Tre_cnt = cv2.imread("./WK_images/tre18pct_0mgmLPVA_120min_Proc321_T0024_t3.tif", cv2.IMREAD_GRAYSCALE) #./Baselines/Trehalose/3/Process_321_T0025.tif

pva_Gly_02 = cv2.imread("./WK_images/gly5pct_0p2mgmLPVA_120min_Proc408_T0024_t2.tif", cv2.IMREAD_GRAYSCALE) #./With_PVA/Glycerol/1/Image.jpg
pva_Suc_02 = cv2.imread("./WK_images/suc18pct_0p2mgmLPVA_120min_Proc404_T0024_t3.tif", cv2.IMREAD_GRAYSCALE) #./With_PVA/Sucrose/2/Image.tif
pva_Tre_02 = cv2.imread("./WK_images/tre18pct_0p2mgmLPVA_120min_Proc337_T0024_t2.tif", cv2.IMREAD_GRAYSCALE) #./With_PVA/Trehalose/2/Image.tif

# Exclude + 1 mg/mL PVA, glycerol image difficulty? 
# pva_gly_1 = cv2.imread("./WK_images/gly5pct_1mgmLPVA_120min_251211_untitled79.tif", cv2.IMREAD_GRAYSCALE) #PVA_IRI/Glycerol/10mgPVA/image_27.jpg
# pva_suc_1 = cv2.imread("./WK_images/suc18pct_1mgmLPVA_120min_12_sucrose_PTpic.tif", cv2.IMREAD_GRAYSCALE) #./TH_image/12.tif
# pva_tre_1 = cv2.imread("./WK_images/tre18pct_1mgmLPVA_120min_22_trehalose_PTpic.tif", cv2.IMREAD_GRAYSCALE) #./TH_image/22.tif

# ---------------------------------------------------
# 2) Bar plot data
# ---------------------------------------------------
df = pd.read_csv("./barplot_data_update.csv")
possible_label_cols = ["Solute", "solute", "Buffer", "buffer", "Name"]
for col in possible_label_cols:
    if col in df.columns:
        vals = df[col].astype(str).str.strip().values
        if ("Glycerol" in vals) or ("Sucrose" in vals) or ("Trehalose" in vals):
            df = df.set_index(col)
            break

if isinstance(df.index, pd.Index) and df.index.dtype == object:
    df.index = df.index.map(lambda x: x.strip() if isinstance(x, str) else x)

def get_row(label, fallback_pos):
    return df.loc[label] if label in df.index else df.iloc[fallback_pos]

row_gly = get_row("Glycerol", 0)
row_suc = get_row("Sucrose", 1)
row_tre = get_row("Trehalose", 2)

col_map = {
    "buf_mean": "Buffer_Mean",
    "buf_err":  "Buffer_Error",
    "pva_mean": "PVA_Mean",
    "pva_err": "PVA_Error",
    "pva_mean_wk": "PVA_Mean_new",
    "pva_err_wk":  "PVA_Error_new",
}
for needed in col_map.values():
    if needed not in df.columns:
        raise KeyError(f"Missing '{needed}' in barplot_data.csv. Found: {list(df.columns)}")

Gly_buff, Gly_buff_err, Gly_pva, Gly_pva_err = map(float, [
    row_gly[col_map["buf_mean"]], row_gly[col_map["buf_err"]],
    row_gly[col_map["pva_mean_wk"]], row_gly[col_map["pva_err_wk"]],
])
Suc_buff, Suc_buff_err, Suc_pva, Suc_pva_err = map(float, [
    row_suc[col_map["buf_mean"]], row_suc[col_map["buf_err"]],
    row_suc[col_map["pva_mean_wk"]], row_suc[col_map["pva_err_wk"]],
])
Tre_buff, Tre_buff_err, Tre_pva, Tre_pva_err = map(float, [
    row_tre[col_map["buf_mean"]], row_tre[col_map["buf_err"]],
    row_tre[col_map["pva_mean_wk"]], row_tre[col_map["pva_err_wk"]],
])

# ---------------------------------------------------
# 3) Helpers
# ---------------------------------------------------
def plot_img_borderless(ax, img, show_ticks=False):
    """
    """
    if img is not None:
        ax.imshow(
            img,
            extent = (0,1,0,1),
            origin = "upper",
            interpolation = "nearest",
            aspect = "auto",
        )
    else:
        ax.set_facecolor("lightgrey")
        ax.text(0.5, 0.5, "Image not Available",
                ha="center", va="center", color="red",
                transform=ax.transAxes, fontsize=10)

        for spine in ax.spine.values():
            spine.set_visible(False)
        ax.set_xticks([])
        ax.set_yticks([])
        
        if show_ticks == False:
            ax.tick_params(axis="both", which="both",
                           length=0, labelbottom=False, labelleft=False)
        ax.grid(False)
        ax.set_aspect("auto")

def style_axis_with_frame(ax, lw=0.85, color="#444444"):
    for spine in ax.spines.values():
        spine.set_edgecolor(color)
        spine.set_linewidth(lw)

def label_panel(ax, text, x=0.012, y=1.0, fs=16):
    ax.text(
        x, y, text, transform=ax.transAxes,
        ha="left", va="bottom",
        fontsize=fs, fontweight="bold",
        color="black", zorder=10, clip_on=False
    )

def set_axis_title(ax, text, fontsize=11, x=0.5, y=1.02):
    ax.text(
        x, y, text, transform=ax.transAxes,
        ha="center", va="bottom",
        fontsize=fontsize, fontweight="bold"
    )

# Do not use
# def lighten(color, factor=0.82):
#    r, g, b = to_rgb(color)
#    return (1 - factor) + factor * r, (1 - factor) + factor * g, (1 - factor) + factor * b

def annotate_bars_across_break(top_ax, bot_ax, xs, ys, yerrs, fmt="{:,.0f}", pad_frac=0.02):
    colors = ["#1f77b4", "#2ca02c"]  # buffer, PVA
    for i, (x, y) in enumerate(zip(xs, ys)):
        err = float(yerrs[i])
        y = float(y)
        y_top = y + err

        b0, b1 = bot_ax.get_ylim()
        ax = bot_ax if (b0 <= y_top <= b1) else top_ax

        ymin, ymax = ax.get_ylim()
        pad = pad_frac * (ymax - ymin)

        ax.text(
            x, y_top + pad,
            f"{fmt.format(y)} ± {err:.1f}",
            ha="center", va="bottom",
            fontsize=8.4, fontweight="bold",
            color=colors[0] if x < 0.5 else colors[1],
            clip_on=False, zorder=8
        )


#This will now be old
def plot_first_row_from_csv(ax, trial_dfs, summary_df, title,
                            colors=("C0", "C1", "C2"),
                            trial_labels=("Trial 1", "Trial 2", "Trial 3")):
    """Experimental points + b=0 fitted lines; legend includes R2_b0."""
    trial_dfs = [d for d in trial_dfs if d is not None]

    # Try to map R2 by trial name if summary has "trial" column; else row order.
    r2_map = {}
    if ("trial" in summary_df.columns) and ("R2_b0" in summary_df.columns):
        r2_map = dict(zip(summary_df["trial"].astype(str), summary_df["R2_b0"].astype(float)))

    for i, df_i in enumerate(trial_dfs):
        # trial name
        if "trial" in df_i.columns:
            tr = str(df_i["trial"].iloc[0])
        else:
            tr = trial_labels[i] if i < len(trial_labels) else f"Trial {i+1}"

        # r2 value
        if r2_map:
            r2 = r2_map.get(tr, np.nan)
        else:
            r2_vals = summary_df["R2_b0"].values if ("R2_b0" in summary_df.columns) else [np.nan]
            r2 = r2_vals[i] if i < len(r2_vals) else np.nan

        ax.plot(df_i["time_min"], df_i["R3_exp_nm3"], "o",
                color=colors[i % len(colors)], markersize=6,
                label=f"{tr} (R²={r2:.4f})")

        ax.plot(df_i["time_min"], df_i["R3_fit_b0_nm3"], "-",
                color=colors[i % len(colors)], linewidth=2, alpha=0.7)

    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_xlabel("Time (min)", fontsize=12)
    ax.grid(True, alpha=0.3, linestyle="--")
    ax.legend(fontsize=9, loc="best", framealpha=0.9)

# ---------------------------------------------------
# 4) Figure layout
# ---------------------------------------------------
plt.close("all")
fig = plt.figure(figsize=(18, 14.5))

gs = gridspec.GridSpec( # Full figure grid
    2, 1, figure=fig,
    height_ratios=[3, 2],
    hspace=0.15
)

top_outer = gridspec.GridSpecFromSubplotSpec( # Sub grid of top half NOW WANT 3
    1, 3, subplot_spec=gs[0],
    width_ratios=[1.0, 2.15, 1.0],
    wspace=0.13
)

cd_img_gs = gridspec.GridSpecFromSubplotSpec( # Grid of left of top_outer
    2, 2, subplot_spec=top_outer[0],
    wspace=0.15,
    hspace=0.15
)
    
img_gs = gridspec.GridSpecFromSubplotSpec( # Grid of *MIDDLE of top_outer
    3, 2, subplot_spec=top_outer[1],
    wspace=0.15,
    hspace=0.15
)

bar_gs = gridspec.GridSpecFromSubplotSpec( # Grid of right of top_corner, bar plots
    3, 1, subplot_spec=top_outer[2],
    hspace=0.20
)

r3_gs = gridspec.GridSpecFromSubplotSpec( # Sub grid of bottom half, Make grids for r^3 plots
    1, 2, subplot_spec=gs[1],
    wspace=0.2,
    hspace=0.3
)

# ---------------------------------------------------
# Plot Chemdraw of each species
# ---------------------------------------------------

chem_drawings = [
    [glycerol_sticks, sucrose_chair],
    [trehalose_chair, pva_sticks],
]

cd_zoom_x = 1.0
cd_zoom_y = 1.0
cd_cropy = 0
cd_cropx = 0

cd_img_axes = [[fig.add_subplot(cd_img_gs[r, c]) for c in range(2)] for r in range(2)]

for r in range(2):
    for c in range(2):
        ax = cd_img_axes[r][c]
        img = chem_drawings[r][c]
      
        plot_img_borderless(ax, img)

panel_labels = ["A","B","C","D"]    # ,"E","F","G","H","I"]
for ax, lab in zip([ax for row in cd_img_axes for ax in row], panel_labels):
    label_panel(ax, lab + ")", fs=16)


# ---------------------------------------------------
# 5) 3×2 (was 3) images (A–F) + zoom
# ---------------------------------------------------

images = [
    [buf_Gly_cnt, pva_Gly_02], #, pva_gly_1],
    [ buf_Suc_cnt,  pva_Suc_02], #,  pva_suc_1],
    [ buf_Tre_cnt,   pva_Tre_02], #,  pva_tre_1],
]
col_titles= ["Control", "PVA (0.2 mg/mL)"]      # , "PVA (1.0 mg/mL)"]
row_titles= ["Glycerol (5%)", "Sucrose (18%)", "Trehalose (18%)"]

zoom_x = 1.0 #2.2
zoom_y = 1.0 #1.8
crop_x = 0 #1.0 - 1.0 / zoom_x
crop_y = 0 #1.0 - 1.0 / zoom_y
x0, x1 = 0.0, 1.0 #1.0 - crop_x, 1.0
y0, y1 = 0.0, 1.0 #0.0, crop_y

axes_img = [[fig.add_subplot(img_gs[r, c]) for c in range(2)] for r in range(3)]

for r in range(3):
    for c in range(2):
        ax = axes_img[r][c]
        img = images[r][c]

        if img is not None:
            if c == 0:
                clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(8, 8)) # Why not do this for all images
                img = clahe.apply(img)

            ax.imshow(
                img, cmap="gray",
                extent=(0, 1, 0, 1),
                origin="upper",
                interpolation="nearest",
                aspect="auto"
            )
            ax.set_xlim(x0, x1)
            ax.set_ylim(y0, y1)
        else:
            ax.set_facecolor("lightgray")
            ax.text(0.5, 0.5, "Image not available",
                    ha="center", va="center", color="red",
                    transform=ax.transAxes, fontsize=10)

        ax.set_xticks([])
        ax.set_yticks([])

        if r == 0:
            set_axis_title(ax, col_titles[c], fontsize=14)
        if c == 0:
            ax.set_ylabel(row_titles[r], fontsize=14, fontweight="bold",
                          rotation=90, labelpad=8)

        style_axis_with_frame(ax, lw=0.85)

panel_labels = ["E", "F", "G", "H", "I", "J"] # ,"G","H","I"]
for ax, lab in zip([ax for row in axes_img for ax in row], panel_labels):
    label_panel(ax, lab + ")", fs=16)

# ---------------------------------------------------
# 6) Broken-axis bar charts (J–L)
# ---------------------------------------------------
error_params = dict(capsize=4, capthick=1.4, elinewidth=1.4, ecolor="black", fmt="none")
bar_width = 0.12

vals_plus_err = np.array([
    Suc_buff + Suc_buff_err, Suc_pva + Suc_pva_err,
    Tre_buff + Tre_buff_err, Tre_pva + Tre_pva_err,
], float)
bottom_max = float(np.max(vals_plus_err)) * 1.25
bottom_max = max(1200.0, min(1800.0, bottom_max))
bottom_ylim = (0.0, bottom_max)

all_plus_err = np.array([
    Gly_buff + Gly_buff_err, Gly_pva + Gly_pva_err,
    Suc_buff + Suc_buff_err, Suc_pva + Suc_pva_err,
    Tre_buff + Tre_buff_err, Tre_pva + Tre_pva_err,
], float)
top_max = float(np.max(all_plus_err)) * 1.18
top_min = bottom_ylim[1] * 1.08
if top_max < top_min + 500:
    top_max = top_min + 500
top_ylim = (top_min, top_max)

def add_broken_bar_simple(subplot_spec, buf_mean, buf_err, pva_mean, pva_err, sol_color, title, add_legend=False):
    sub_gs = gridspec.GridSpecFromSubplotSpec(
        2, 1, subplot_spec=subplot_spec,
        height_ratios=[1, 3], hspace=0.05
    )
    top_ax = fig.add_subplot(sub_gs[0, 0])
    bot_ax = fig.add_subplot(sub_gs[1, 0], sharex=top_ax)

    top_ax.bar(0.4, buf_mean, width=bar_width, color=,       #"#aec7e8",
               label="Buffer" if add_legend else None)
    top_ax.bar(0.6, pva_mean, width=bar_width, color=,       #"#98df8a",
               label="PVA" if add_legend else None)
    bot_ax.bar(0.4, buf_mean, width=bar_width, color=,       #"#aec7e8")
    bot_ax.bar(0.6, pva_mean, width=bar_width, color=,       #"#98df8a")

    top_ax.errorbar([0.4, 0.6], [buf_mean, pva_mean], yerr=[buf_err, pva_err], **error_params)
    bot_ax.errorbar([0.4, 0.6], [buf_mean, pva_mean], yerr=[buf_err, pva_err], **error_params)

    top_ax.set_ylim(*top_ylim)
    bot_ax.set_ylim(*bottom_ylim)

    set_axis_title(top_ax, title, fontsize=14, x=0.6, y=0.5)

    top_ax.spines["bottom"].set_visible(False)
    bot_ax.spines["top"].set_visible(False)
    top_ax.tick_params(axis="x", bottom=False, labelbottom=False)

    top_ax.tick_params(axis="y", labelsize=8.6)
    bot_ax.tick_params(axis="y", labelsize=8.6)

    bot_ax.set_xticks([0.4, 0.6])
    bot_ax.set_xticklabels(["Buffer", "Buffer+PVA"], fontsize=11, fontweight="bold")

    d = 0.5
    kwargs = dict(marker=[(-1, -d), (1, d)], markersize=8, linestyle="none",
                  color="k", mec="k", mew=1, clip_on=False)
    top_ax.plot([0], [0], transform=top_ax.transAxes, **kwargs)
    bot_ax.plot([0], [1], transform=bot_ax.transAxes, **kwargs)

    top_ax.grid(False)
    bot_ax.grid(axis="y", linestyle="--", alpha=0.25)

    annotate_bars_across_break(
        top_ax, bot_ax,
        xs=[0.4, 0.6],
        ys=[buf_mean, pva_mean],
        yerrs=[buf_err, pva_err],
        pad_frac=0.02
    )

    style_axis_with_frame(top_ax, lw=0.9)
    style_axis_with_frame(bot_ax, lw=0.9)

    return top_ax, bot_ax

gly_top, gly_bot = add_broken_bar_simple(bar_gs[0], Gly_buff, Gly_buff_err, Gly_pva, Gly_pva_err, "Glycerol (5%)", add_legend=True)
suc_top, suc_bot = add_broken_bar_simple(bar_gs[1], Suc_buff, Suc_buff_err, Suc_pva, Suc_pva_err, "Sucrose (18%)")
tre_top, tre_bot = add_broken_bar_simple(bar_gs[2], Tre_buff, Tre_buff_err, Tre_pva, Tre_pva_err, "Trehalose (18%)")

suc_bot.set_ylabel("Average area ($\\mu m^2$)", fontsize=14, fontweight="bold")
for ax in (suc_top, tre_top, tre_bot):
    ax.set_ylabel("")

handles, labels_ = gly_top.get_legend_handles_labels()
if handles:
    fig.legend(handles, labels_, loc="upper right",
               bbox_to_anchor=(0.90, 0.69), fontsize=11, frameon=False)

label_panel(gly_top, "G)") #"J)")
label_panel(suc_top, "H)") #"K)")
label_panel(tre_top, "I)") #"L)")

# ---------------------------------------------------
# 7) Bottom: R^3 plots (J-O) # was (M–R) 
#    FIRST ROW: replaced using your CSV plot (experimental + b0 fit).
#    SECOND ROW: keep as-is (raw With PVA).
# ---------------------------------------------------

# --- New plotting funcs ---
def plot_combined_solutes(ax, data_dict, title, color_dict, marker_dict, 
                          xlabel='', ylabel='', show_legend=True, 
                          alpha=0.90, lw=1.8):
    """
    """
    
    for solute, (x_data, y_data) in data_dict.items():
        if x_data is None or y_data is None or len(x_data) == 0:
            continue
            
        # Get color (use first color from the list)
        colors = color_dict.get(solute, ["#000000"])
        base_color = colors[0]  # Use primary color
        
        # Get marker configuration
        marker_cfg = marker_dict.get(solute, {})
        marker = marker_cfg.get('marker', 'o')
        mec = marker_cfg.get('mec', base_color)  # Default to base color if not specified
        
        # Plot the data
        ax.plot(x_data, y_data, 
                marker=marker, 
                markersize=8,
                color=base_color,
                markerfacecolor=base_color, 
                markeredgecolor=mec,
                markeredgewidth=marker_cfg.get('mew', 0.3),
                linestyle='-', 
                linewidth=lw,
                alpha=alpha,
                label=solute)
    
    # Styling
    for spine in ax.spines.values():
        spine.set_alpha(0.35)
    
    ax.grid(True, which="major", linestyle="--", linewidth=0.6, alpha=0.4)
    ax.grid(True, which="minor", linestyle=":", linewidth=0.5, alpha=0.12)
    ax.minorticks_on()
    ax.tick_params(axis="both", labelsize=9)
    
    # Set labels
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=12)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=14, fontweight="bold")
    
    # Set title
    ax.set_title(title, fontsize=12, fontweight="bold", pad=10)
    
    # Legend
    if show_legend:
        ax.legend(loc='best', fontsize=10, framealpha=0.9)
    
    return ax


def plot_combined_panel(fig, gs_spec, csv_sources, pva_data, 
                        base_colors, marker_info, panel_labels=['a', 'b']):
    """
    """
        ax_left = fig.add_subplot(gs_spec[0, 0])
    ax_right = fig.add_subplot(gs_spec[0, 1])
    
    # Prepare data for "Without PVA" (left panel)
    without_pva_data = {}
    for solute in csv_sources.keys():
        # Extract data from CSV sources
        # Adjust this based on your actual data structure
        x_data = csv_sources[solute].get('time', None)  # Replace with actual key
        y_data = csv_sources[solute].get('r3', None)    # Replace with actual key
        without_pva_data[solute] = (x_data, y_data)
    
    # Prepare data for "With PVA" (right panel)
    with_pva_data = {}
    for solute in pva_data.keys():
        # Extract data from PVA sources
        x_data = pva_data[solute].get('time', None)  # Replace with actual key
        y_data = pva_data[solute].get('r3', None)    # Replace with actual key
        with_pva_data[solute] = (x_data, y_data)
    
    # Plot left panel - Without PVA
    plot_combined_solutes(
        ax_left, 
        without_pva_data,
        title="Without PVA",
        color_dict=base_colors,
        marker_dict=marker_info,
        xlabel='Time (min)',
        ylabel=r'$R^3$ ($\mu$m$^3$)',
        show_legend=True,
        alpha=0.90,
        lw=1.8
    )
    
    # Add panel label
    ax_left.text(0.02, 0.98, f"{panel_labels[0]})", transform=ax_left.transAxes,
                 fontsize=12, fontweight='bold', va='top')
    
    # Plot right panel - With PVA
    plot_combined_solutes(
        ax_right, 
        with_pva_data,
        title="With PVA",
        color_dict=base_colors,
        marker_dict=marker_info,
        xlabel='Time (min)',
        ylabel='',  # Remove ylabel for right panel
        show_legend=False,  # Turn off if you want only one legend
        alpha=0.90,
        lw=1.8
    )
    
    # Add panel label
    ax_right.text(0.02, 0.98, f"{panel_labels[1]})", transform=ax_right.transAxes,
                  fontsize=12, fontweight='bold', va='top')
    
    # Optionally synchronize y-limits
    ylim_left = ax_left.get_ylim()
    ylim_right = ax_right.get_ylim()
    ymin = min(ylim_left[0], ylim_right[0])
    ymax = max(ylim_left[1], ylim_right[1])
    ax_left.set_ylim(ymin, ymax)
    ax_right.set_ylim(ymin, ymax)
    
    return ax_left, ax_right
   
--- --- --- --- --- ---


data = {
    "With PVA": {
        "Glycerol": {
            #"Trial 1": [(10,1290.038),(20,1550.049),(30,1697.384),(40,1658.181),(50,1772.072),(60,1722.100),(70,1826.649),(80,1779.004),(90,1835.586),(100,1865.447),(110,1834.890),(125,1798.182)],
            #"Trial 2": [(10,1608.765),(20,2330.020),(30,2845.937),(40,2984.776),(50,3239.076),(60,3442.241),(70,3526.387),(80,3895.752),(90,4052.725),(100,4013.273),(110,4201.708),(125,4319.026)],
            #"Trial 3": [(10,2077.640),(20,2895.841),(30,3818.276),(40,4162.645),(50,4459.466),(60,4668.042),(70,4666.494),(80,4952.710),(90,5200.761),(100,5364.308),(110,5389.444),(120,5398.939)],
            "Trial 1": [
                (5,2166.093),
                (20,2179.469),
                (40,1871.492),
                (60,1559.103),
                (80,1274.828),
                (100,1422.078),
                (120,837.118),
            ],
            "Trial 2": [
                (5,1257.354),
                (20,2736.810),
                (40,3507.305),
                (60,4129.700),
                (80,4180.776),
                (100,4030.183),
                (120,5201.051),
            ],
            "Trial 3": [
                (5,2357.177),
                (20,4050.906),
                (40,4903.820),
                (60,6411.208),
                (80,4506.458),
                (100,3339.451),
                (120,3742.128),
            ],   
        },
        "Sucrose": {
            #"Trial 1": [
            #    (5,130.485),
            #    (20,248.131),
            #    (40,283.714),
            #    (60,294.429),
            #    (80,445.946),
            #    (100,740.370),
            #    (120,398.309),
            #],
            "Trial 1": [     # Was Trial 2
                (5,47.228),
                (20,63.785),
                (40,46.325),
                (60,25.328),
                (80,23.233),
                (100,19.503),
                (120,20.051),
            ],
            "Trial 2": [     # Was Trial 3
                (5,42.186),
                (20,51.004),
                (40,28.898),
                (60,58.223),
                (80,56.162),
                (100,55.914),
                (120,57.934),
            ],
            "Trial 3": [     # Was Trial 4
                (5,45.816),
                (20,62.489),
                (40,48.758),
                (60,35.451),
                (80,34.505),
                (100,33.854),
                (120,36.802),
            ]  
            #"Trial 1": [(0,72.95),(10,97.64),(20,147.9),(30,148.9),(40,145.9),(55,187.0),(70,212.7),(85,224.0),(100,259.1),(120,293.0)]
            #"Trial 1": [(5,18.746),(20,35.422),(40,48.633),(60,58.302),(80,64.732),(100,67.417),(120,85.029)],
            #"Trial 2": [(5,9.083),(20,10.886),(40,11.769),(60,15.404),(80,16.395),(100,15.718),(120,16.085)],
            #"Trial 3": [(5,22.109),(20,29.097),(40,35.803),(60,34.176),(80,35.074),(100,37.762),(120,34.613)],
        },
        "Trehalose": {
            #"Trial 1": [(10,111.1),(20,106.3),(30,111.7),(40,103.3),(55,140.4),  # Older
            #            (70,132.7),(85,148.8),(100,180.6),(110,184.8),(120,204.4)],
            #"Trial 2": [(10,99.38),(20,99.38),(30,90.40),(40,112.93),(55,103.77),   # Older
            #            (70,122.62),(85,134.22),(100,140.02),(110,144.21),(120,165.29)],
            "Trial 1": [
                (5,24.152),
                (20,30.384),
                (40,27.397),
                (60,37.042), # Updated, RE trhd
                (80,23.072),
                (100,22.647),
                (120,22.365),
            ],
            "Trial 2": [
                (5,22.563),
                (20,29.611),
                (40,37.540),
                (60,37.237),
                (80,35.371),
                (100,40.602),
                (120,35.307),
            ],
            "Trial 3": [
                (5,30.789),
                (20,31.576),
                (40,31.469),
                (60,32.573),
                (80,35.193),
                (100,34.427),
                (120,37.165),
            ]
            #"Trial 1": [(5,4.344),(20,5.228),(40,4.462),(60,3.503),(80,3.948),(100,3.781),(120,3.643)],
            #"Trial 2": [(5,4.081),(20,5.132),(40,5.853),(60,6.260),(80,5.879),(100,5.370),(120,5.620)],
            #"Trial 3": [(5,4.966),(20,5.084),(40,5.372),(60,5.190),(80,5.751),(100,5.499),(120,6.137)],
        }
    }
}

trial_alpha = 0.90
trial_lw = 1.8
base_colors = {
        "Glycerol": ["#208EA3", "#4178BC", "#7A71F6"],
        "Sucrose": ["#E37CFF", "#EA4E9D", "#FCA7E4"],
        "Trehalose": ["#A4C61A", "#62BB35", "#37A862"],
        }
        # old: {"Glycerol": "#1f77b4", "Sucrose": "#ff7f0e", "Trehalose": "#2ca02c"}

marker_info = {
        "Glycerol": marker:'o', mec:"#8D9F9B", mew:0.3, #need mfc in loop (trial color)
        "Sucrose": marker:'o', # Unnecess for fill? mec:'#', mew:, mfc:,
        "Trehalose": marker:'D', mec:"#8D9F9B", mew:0.3, #need mfc in loop (trial color), mfc:'from bc',
        }

# glycerol_colors = {"Trial 1": "

def gather_points_from_csv(sol):
    t_vals, y_vals = [], []
    for df_i in csv_sources[sol]["trials"]:
        if df_i is None:
            continue
        t_vals.extend(df_i["time_min"].astype(float).values.tolist())
        y_vals.extend(df_i["R3_exp_nm3"].astype(float).values.tolist())
    return np.array(t_vals, float), np.array(y_vals, float)

def gather_points_with_pva(sol):
    t_vals, y_vals = [], []
    for trial_data in data["With PVA"][sol].values():
        for (t, y) in trial_data:
            t_vals.append(t)
            y_vals.append(y)
    return np.array(t_vals, float), np.array(y_vals, float)

def plot_with_pva_raw_only(ax, sol, base_color, marker):
    trials = list(data["With PVA"][sol].items())
    #shades = np.linspace(0.70, 1.0, len(trials)) if trials else np.array([1.0])

    for shade, (trial_name, trial_data) in zip(shades, trials):
        trial_data = sorted(trial_data, key=lambda p: p[0])
        t = [p[0] for p in trial_data]
        y = [p[1] for p in trial_data]
        ax.plot(
            t, y, linestyle="none", marker="o", ms=4.8,
            color=lighten(base_color, shade),
            alpha=trial_alpha, lw=trial_lw,
            label=trial_name, zorder=3
        )
    ax.legend(loc="best", fontsize=8.8, framealpha=0.9)

solutes = ["Glycerol", "Sucrose", "Trehalose"]
panel_tags = ["J", "K", "L", "M", "N", "O"]     #["M", "N", "O", "P", "Q", "R"]
panel_i = 0



#for col, sol in enumerate(solutes):
#    base_color = base_colors[sol]
#
    # ---------- FIRST ROW: CSV-BASED (replace) ----------
#    axTop = fig.add_subplot(r3_gs[0, col])
    plot_first_row_from_csv(
        axTop,
        trial_dfs=csv_sources[sol]["trials"],
        summary_df=csv_sources[sol]["summary"],
        title=sol
    )

    if col == 0:
        axTop.set_ylabel(r"$R^3$ (μm$^3$)", fontsize=14, fontweight="bold")
    else:
        axTop.set_ylabel("")

    axTop.text(0.02, 0.95, "Without PVA", transform=axTop.transAxes,
               fontsize=9.6, color="black", alpha=0.85, va="top")

    # ---------- SECOND ROW: KEEP AS-IS ----------
    axBot = fig.add_subplot(r3_gs[1, col])
    plot_with_pva_raw_only(axBot, sol, base_color)
    axBot.set_xlabel("Time (min)", fontsize=12)

    if col == 0:
        axBot.set_ylabel(r"$R^3$ (μm$^3$)", fontsize=14, fontweight="bold")
    else:
        axBot.set_ylabel("")

    axBot.text(0.02, 0.95, "With PVA", transform=axBot.transAxes,
               fontsize=9.6, color="black", alpha=0.85, va="top")

    # ---- autoscale axes (top from CSV exp; bottom from raw With PVA) ----
    tL, yL = gather_points_from_csv(sol)
    tR, yR = gather_points_with_pva(sol)

    if tL.size and yL.size:
        xmin, xmax = float(np.min(tL)), float(np.max(tL))
        ymin, ymax = float(np.min(yL)), float(np.max(yL))
        axTop.set_xlim(xmin - 0.05*(xmax-xmin+1), xmax + 0.05*(xmax-xmin+1))
        axTop.set_ylim(max(0.0, ymin - 0.10*(ymax-ymin+1)), ymax + 0.10*(ymax-ymin+1))

    if tR.size and yR.size:
        xmin, xmax = float(np.min(tR)), float(np.max(tR))
        ymin, ymax = float(np.min(yR)), float(np.max(yR))
        axBot.set_xlim(0, xmax + 0.05*(xmax-xmin+1)) # xmin - 0.05*(xmax-xmin+1), xmax + 0.05*(xmax-xmin+1))
        axBot.set_ylim(0, ymax + 0.10*(ymax-ymin+1)) # max(0.0, ymin - 0.10*(ymax-ymin+1)), ymax + 0.10*(ymax-ymin+1))

    # Styling consistent with your figure
    for ax in (axTop, axBot):
        for spine in ax.spines.values():
            spine.set_alpha(0.35)
        ax.grid(True, which="major", linestyle="--", linewidth=0.6, alpha=0.4)
        ax.grid(True, which="minor", linestyle=":",  linewidth=0.5, alpha=0.12)
        ax.minorticks_on()
        ax.tick_params(axis="both", labelsize=9)

    # Panel labels M–R
    label_panel(axTop, panel_tags[panel_i] + ")"); panel_i += 1
    label_panel(axBot, panel_tags[panel_i] + ")"); panel_i += 1

# ---------------------------------------------------
# 8) Save + show
# ---------------------------------------------------
Path(save_path).parent.mkdir(parents=True, exist_ok=True)
plt.savefig(save_path, bbox_inches="tight", facecolor="white")
plt.show()
