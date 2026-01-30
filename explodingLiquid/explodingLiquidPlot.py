import matplotlib.pyplot as plt

# =======================
# Farben fest
# =======================
blue_dark   = '#1f77b4'   # PSVL
orange_dark = '#ff7f0e'   # VLC

# =======================
# X-Achse
# =======================
x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

# =======================
# WALL CLOCK — AVG
# =======================
psvl_box08 = [50.0654, 50.1982, 51.0794, 51.4464, 51.1196, 49.0618, 50.93,   50.3292, 50.1968, 50.7188]
vlc_box08  = [50.6198, 49.8338, 51.432,  50.9884, 51.7144, 49.2562, 50.4764, 50.625,  49.8948, 51.0182]

psvl_box10 = [46.732,  45.8874, 46.4364, 46.2264, 45.9586, 45.8518, 46.8426, 46.0648, 46.119,  45.938]
vlc_box10  = [46.0822, 46.4554, 44.9498, 51.0562, 47.0124, 46.0086, 44.8852, 45.7774, 46.5482, 45.8684]

psvl_box15 = [62.085,  61.3008, 64.941,  64.191,  61.9578, 61.3988, 62.267,  61.3524, 61.174,  65.5498]
vlc_box15  = [46.3038, 47.2692, 47.0936, 47.456,  49.0888, 56.8672, 49.1612, 48.173,  49.2522, 49.3382]

psvl_box20 = [53.8836, 50.4206, 50.411,  47.3458, 49.6074, 49.3776, 48.5266, 48.8732, 48.38,   48.9154]
vlc_box20  = [51.0836, 49.239,  56.3742, 49.7538, 49.2078, 48.6194, 49.0594, 47.3064, 46.9042, 45.2362]

# =======================
# Plot-Funktion
# =======================
def plot_box(box_label, psvl, vlc, filename):
    plt.figure(figsize=(6, 4))
    plt.plot(x, psvl, marker='o', linestyle='-',  color=blue_dark,   label='PSVL')
    plt.plot(x, vlc,  marker='v', linestyle='--', color=orange_dark, label='VLC')

    plt.xlabel("skin size factor")
    plt.ylabel("Wall-clock time [s]")
    plt.title(f"Box length {box_label}")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename, bbox_inches="tight")
    plt.show()
    plt.close()

# =======================
# 4 Diagramme
# =======================
plot_box("08", psvl_box08, vlc_box08, "wall_clock_box08.pdf")
plot_box("10", psvl_box10, vlc_box10, "wall_clock_box10.pdf")
plot_box("15", psvl_box15, vlc_box15, "wall_clock_box15.pdf")
plot_box("20", psvl_box20, vlc_box20, "wall_clock_box20.pdf")