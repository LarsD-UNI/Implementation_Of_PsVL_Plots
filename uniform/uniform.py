import matplotlib.pyplot as plt

x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

# Wall Clock
psvl_box08 = [90.965, 117.7736, 125.9526, 186.6596, 203.4062, 229.6516, 417.0372, 458.5148, 499.0524, 543.402]

psvl_box10 = [83.2962, 89.9444, 91.5596, 96.0786, 115.89, 122.3816, 176.8028, 188.7564, 199.9006, 224.1932]

psvl_box15 = [82.6184, 81.7242, 75.1562, 83.3086, 84.1442, 75.6196, 80.664, 79.2234, 84.3874, 84.5686]

psvl_box20 = [112.3584, 97.5944, 92.0588, 88.0176, 82.5954, 77.8154, 74.3344, 73.6772, 73.0126, 73.2294]



vlc_box08 = [78.6466, 97.6032, 105.4468, 141.5738, 154.3604, 166.1318, 280.5402, 297.8608, 328.8692, 363.4972]

vlc_box10 = [76.329, 79.4686, 82.696, 82.5894, 96.4774, 119.6134, 128.0704, 137.971, 145.1866, 154.2182]

vlc_box15 = [80.457, 77.0634, 72.7378, 70.227, 70.431, 69.6924, 72.2574, 75.15, 75.6912, 84.3052]

vlc_box20 = [106.2362, 92.3004, 86.3452, 81.8578, 84.7442, 77.559, 94.3376, 90.948, 86.1238, 80.8764]


# Colors
blue_dark   = '#1f77b4'
orange_dark = '#ff7f0e'

def plot_box(box_label, psvl, vlc, filename):
    plt.figure(figsize=(6, 4))
    plt.plot(x, psvl, marker='o', linestyle='-',  color='#1f77b4', label=f'PSVL - {box_label}')
    plt.plot(x, vlc,  marker='v', linestyle='--', color='#ff7f0e', label=f'VLC  - {box_label}')
    plt.xlabel("skin size factor")
    plt.ylabel("Wall-clock time [s]")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename, bbox_inches="tight")
    plt.show()
    plt.close()

plot_box("Box 08", psvl_box08, vlc_box08,  "wall_clock_box08.pdf")
plot_box("Box 10", psvl_box10, vlc_box10,  "wall_clock_box10.pdf")
plot_box("Box 15", psvl_box15, vlc_box15,  "wall_clock_box15.pdf")
plot_box("Box 20", psvl_box20, vlc_box20,  "wall_clock_box20.pdf")