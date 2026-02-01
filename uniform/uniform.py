import matplotlib.pyplot as plt

# =======================
# X-Achse
# =======================
x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

# =======================
# WALL CLOCK — AVG
# =======================
psvl_box08 = [56.9114, 54.74,   54.4842, 55.3902, 53.9646, 54.7842, 52.061,  51.3362, 51.9902, 52.5806]
psvl_box10 = [55.5582, 55.425,  53.6154, 55.8314, 54.46,   51.1962, 53.0292, 52.982,  51.6814, 51.7404]
psvl_box15 = [69.9224, 63.8142, 61.738,  55.4454, 56.9092, 56.5498, 52.5262, 51.6932, 52.3664, 52.4152]
psvl_box20 = [104.4998, 87.966, 80.4064, 74.9838, 68.8872, 63.8276, 60.8332, 59.4036, 56.8698, 58.041]

vlc_box08 = [53.9194, 51.0214, 55.4034, 55.2022, 55.86,   53.0042, 52.4426, 50.5218, 50.8854, 50.3938]
vlc_box10 = [53.1068, 56.1246, 54.4262, 50.9316, 54.1914, 53.3128, 53.6606, 50.6712, 50.8294, 50.5024]
vlc_box15 = [51.5368, 55.5306, 50.8052, 53.3764, 53.9744, 54.4402, 50.8904, 51.261,  50.3428, 50.0038]
vlc_box20 = [54.6076, 53.389,  52.4,    51.1172, 51.1082, 50.533,  49.5272, 47.439,  46.8146, 46.926]

# =======================
# Farben: pro Box-Länge eine Farbe
# =======================
colors = {
    "Box_length_08": "#1f77b4",
    "Box_length_10": "#ff7f0e",
    "Box_length_15": "#2ca02c",
    "Box_length_20": "#d62728",
}

def plot_box(box_label, psvl, vlc, color, filename):
    plt.figure(figsize=(6, 4))
    plt.plot(x, psvl, marker='o', linestyle='-',  color=color, label=f'PSVL - {box_label}')
    plt.plot(x, vlc,  marker='v', linestyle='--', color=color, label=f'VLC  - {box_label}')
    plt.xlabel("skin size factor")
    plt.ylabel("Wall-clock time [s]")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename, bbox_inches="tight")
    plt.show()
    plt.close()

# =======================
# 4 Diagramme (je Box size)
# =======================
plot_box("Box 08", psvl_box08, vlc_box08, colors["Box_length_08"], "wall_clock_box08.pdf")
plot_box("Box 10", psvl_box10, vlc_box10, colors["Box_length_10"], "wall_clock_box10.pdf")
plot_box("Box 15", psvl_box15, vlc_box15, colors["Box_length_15"], "wall_clock_box15.pdf")
plot_box("Box 20", psvl_box20, vlc_box20, colors["Box_length_20"], "wall_clock_box20.pdf")