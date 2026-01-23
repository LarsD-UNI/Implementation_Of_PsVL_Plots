import matplotlib.pyplot as plt

x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

# Pseudo Verlet Lists
psvl_c18 = [83.21,   73.6482, 76.914,  85.4738, 87.4154, 94.0144]
psvl_c08 = [65.874,  55.4186, 54.3382, 58.4594, 58.5614, 61.1774]

# Linked Cells
lc_c18   = [66.8906, 69.1436, 77.0866, 86.258,  89.405,  95.997]
lc_c08   = [43.2818, 44.9372, 47.7644, 52.5008, 53.5476, 56.8968]

# Verlet Linked Cells
vlc_c18  = [62.8658, 62.1164, 67.0644, 73.7366, 78.5444, 84.9708]
vlc_c08  = [37.8664, 36.6082, 38.0538, 40.5698, 42.8364, 45.3556]



blue_light   = '#aec7e8'   # PSVL c18
blue_dark    = '#1f77b4'   # PSVL c08

green_light  = '#98df8a'   # LC c18
green_dark   = '#2ca02c'   # LC c08

orange_light = '#ffbb78'   # VLC c18
orange_dark  = '#ff7f0e'   # VLC c08

# PSVL
plt.plot(x, psvl_c18, marker='o', color=blue_light,  label='PSVL - c18')
plt.plot(x, psvl_c08, marker='o', linestyle='--', color=blue_dark, label='PSVL - c08')

# LC
plt.plot(x, lc_c18, marker='s', color=green_light, label='LC - c18')
plt.plot(x, lc_c08, marker='s', linestyle='--', color=green_dark, label='LC - c08')

# VLC
plt.plot(x, vlc_c18, marker='v', color=orange_light, label='VLC - c18')
plt.plot(x, vlc_c08, marker='v', linestyle='--', color=orange_dark, label='VLC - c08')


plt.xlabel('skin size factor')
plt.ylabel('Wall-clock time [s]')

plt.ylim(35, 100)

plt.legend(
    loc='upper left',
    ncol=3
)

plt.grid(True)
plt.tight_layout()

plt.savefig("falling_traversals_avg.pdf", format="pdf", bbox_inches="tight")

plt.show()
