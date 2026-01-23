import matplotlib.pyplot as plt

x = [0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6]

# Pseudo Verlet Lists
psvl_c18 = [24.3842, 23.3172, 21.6622, 23.2634, 23.7578, 23.4836, 23.9618, 24.2872]
psvl_c08 = [22.5864, 21.2348, 19.967, 21.193, 21.1404, 21.6702, 21.4314, 21.9812]

# Linked Cells
lc_c18 = [21.3930, 20.1450, 21.7204, 21.6402, 22.0760, 22.2656, 22.3926, 22.9328]
lc_c08 = [19.2756, 18.2512, 18.4524, 18.4916, 18.7570, 18.8200, 18.9570, 19.1828]

# Verlet Linked Cells
vlc_c18 = [21.0224, 18.7702, 19.1558, 19.1908, 19.7364, 19.5808, 19.6618, 19.4530]
vlc_c08 = [19.8156, 18.7858, 18.6218, 18.7154, 19.0912, 19.7220, 18.8606, 18.1100]


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

plt.ylim(18, 26)

plt.legend(
    loc='upper right',
    ncol=3
)

plt.grid(True)
plt.tight_layout()
plt.show()
