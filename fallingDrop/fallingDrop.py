import matplotlib.pyplot as plt

# =======================
# X-Achse
# =======================
x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

# =======================
# WALL CLOCK — AVG
# =======================
psvl_wc_c08 = [65.2174, 53.5868, 52.5788, 53.7934, 53.6636, 54.7796, 59.8236, 62.7462, 67.1818, 69.4588]
psvl_wc_c18 = [83.3740, 74.1106, 75.6858, 82.0882, 82.6056, 87.7058, 97.9624, 105.1610, 115.4066, 118.9556]

lc_wc_c08   = [43.4130, 45.1816, 48.2188, 53.2236, 54.0388, 57.8034, 63.9442, 68.3578, 75.8572, 76.3174]
lc_wc_c18   = [65.7108, 69.1258, 76.4106, 86.8684, 89.0082, 95.8990, 111.3898, 121.1220, 131.7598, 135.7514]

vlc_wc_c08  = [37.8294, 36.5728, 37.5444, 39.7174, 41.2034, 45.3984, 47.0802, 49.2474, 52.7188, 53.9024]
vlc_wc_c18  = [47.3290, 48.5554, 52.3718, 59.5804, 61.8190, 67.1890, 76.5174, 81.8248, 89.4128, 92.3218]

# =======================
# REBUILD FREQUENCY — AVG
# =======================
psvl_rf = [4.437598, 8.360854, 12.24764, 16.0937, 20.1087, 23.97794, 27.79054, 31.42182, 35.41418, 39.45428]
vlc_rf  = [4.412084, 8.320482, 12.25524, 15.99752, 20.03244, 23.91224, 27.59674, 31.86362, 35.31238, 39.30954]

# =======================
# UPDATE CONTAINER — AVG
# =======================
psvl_uc = [2.3004, 2.2648, 2.1242, 2.2370, 2.1854, 2.1620, 2.1164, 2.0890, 2.0910, 2.1060]
vlc_uc  = [2.4022, 2.3340, 2.2520, 2.2342, 2.2404, 2.2108, 2.1540, 2.1264, 2.1180, 2.0792]

# =======================
# FORCE UPDATE — AVG
# =======================
psvl_fu = [53.0858, 41.5778, 40.5678, 42.1434, 41.6650, 43.3150, 48.2632, 51.4086, 55.9830, 58.0664]
vlc_fu  = [25.1242, 24.0818, 25.3630, 27.7696, 29.3496, 33.5038, 35.5332, 37.7994, 41.4352, 42.6614]

blue_light   = '#aec7e8'   # PSVL c18
blue_dark    = '#1f77b4'   # PSVL c08

green_light  = '#98df8a'   # LC c18
green_dark   = '#2ca02c'   # LC c08

orange_light = '#ffbb78'   # VLC c18
orange_dark  = '#ff7f0e'   # VLC c08

# =======================
# 1) WALL CLOCK
# =======================
plt.figure(figsize=(6, 4))
plt.plot(x, psvl_wc_c18, marker='o', color=blue_light,  label='PSVL - c18')
plt.plot(x, psvl_wc_c08, marker='o', linestyle='--', color=blue_dark, label='PSVL - c08')

plt.plot(x, lc_wc_c18, marker='s', color=green_light, label='LC - c18')
plt.plot(x, lc_wc_c08, marker='s', linestyle='--', color=green_dark, label='LC - c08')

plt.plot(x, vlc_wc_c18, marker='v', color=orange_light, label='VLC - c18')
plt.plot(x, vlc_wc_c08, marker='v', linestyle='--', color=orange_dark, label='VLC - c08')

plt.xlabel("skin size factor")
plt.ylabel("Wall-clock time [s]")
plt.ylim(35, 140)
plt.grid(True)
plt.legend(ncol=2)
plt.tight_layout()
plt.savefig("wall_clock_avg.pdf", bbox_inches="tight")
plt.show()
plt.close()

# =======================
# 2) REBUILD FREQUENCY
# =======================
plt.figure(figsize=(6, 4))
plt.plot(x, psvl_rf, marker='o', label='PSVL', color=blue_dark)
plt.plot(x, vlc_rf, marker='v', linestyle='--', label='VLC', color=orange_dark)

plt.xlabel("skin size factor")
plt.ylabel("Rebuild frequency")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("rebuild_frequency_avg.pdf", bbox_inches="tight")
plt.show()
plt.close()

# =======================
# 3) UPDATE CONTAINER
# =======================
plt.figure(figsize=(6, 4))
plt.plot(x, psvl_uc, marker='o', label='PSVL', color=blue_dark)
plt.plot(x, vlc_uc, marker='v', linestyle='--', label='VLC', color=orange_dark)

plt.xlabel("skin size factor")
plt.ylabel("Update Container [s]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("update_container_avg.pdf", bbox_inches="tight")
plt.show()
plt.close()


# =======================
# 4) FORCE UPDATE
# =======================
plt.figure(figsize=(6, 4))
plt.plot(x, psvl_fu, marker='o', label='PSVL', color=blue_dark)
plt.plot(x, vlc_fu, marker='v', linestyle='--', label='VLC', color=orange_dark)

plt.xlabel("skin size factor")
plt.ylabel("Force Update [s]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("force_update_avg.pdf", bbox_inches="tight")
plt.show()
plt.close()
