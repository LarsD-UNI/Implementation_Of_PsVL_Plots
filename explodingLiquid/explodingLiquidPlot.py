import matplotlib.pyplot as plt

# =======================
# X-Achse (neue Benchmarks)
# =======================
x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

# =======================
# AVG — TRAVERSALS
# =======================
psvl_tr_c08 = [23.4454, 20.1434, 20.0586, 19.8486, 19.6096, 19.5312]
psvl_tr_c18 = [24.7660, 20.9850, 20.8118, 21.8278, 20.9444, 20.7050]

lc_tr_c08   = [20.3228, 19.5606, 20.0888, 19.8610, 19.7024, 21.0702]
lc_tr_c18   = [23.0626, 22.8236, 22.9720, 23.2892, 22.9728, 24.5878]

vlc_tr_c08  = [19.9790, 18.1262, 19.1002, 18.8502, 18.4968, 18.6830]
vlc_tr_c18  = [21.7028, 19.3948, 19.5266, 20.0688, 20.0978, 19.4024]

# =======================
# AVG — REBUILD FREQUENCY
# =======================
psvl_rf = [7.287538, 14.18238, 21.08734, 28.03772, 35.12928, 42.29336]
vlc_rf  = [7.299348, 14.16446, 21.13690, 28.02030, 35.12886, 42.25538]

# =======================
# AVG — UPDATE CONTAINER
# =======================
psvl_uc = [1.3906, 1.3844, 1.3940, 1.3912, 1.3888, 1.3852]
vlc_uc  = [1.4192, 1.3742, 1.3850, 1.4224, 1.3604, 1.3978]

# =======================
# AVG — FORCE UPDATE
# =======================
psvl_fu = [12.9368, 10.2330, 9.6258, 9.4718, 9.2934, 9.2362]
vlc_fu  = [9.4020, 8.4258, 8.7232, 8.3338, 8.6566, 8.5850]

# =======================
# Farben (wie in deinem Code)
# =======================
blue_light   = '#aec7e8'   # PSVL c18
blue_dark    = '#1f77b4'   # PSVL c08 / PSVL
green_light  = '#98df8a'   # LC c18
green_dark   = '#2ca02c'   # LC c08
orange_light = '#ffbb78'   # VLC c18
orange_dark  = '#ff7f0e'   # VLC c08 / VLC


# =======================
# 0) TRAVERSALS
# =======================
plt.figure(figsize=(6, 4))
plt.plot(x, psvl_tr_c18, marker='o', color=blue_light,  label='PSVL - c18')
plt.plot(x, psvl_tr_c08, marker='o', linestyle='--', color=blue_dark, label='PSVL - c08')

plt.plot(x, lc_tr_c18, marker='s', color=green_light, label='LC - c18')
plt.plot(x, lc_tr_c08, marker='s', linestyle='--', color=green_dark, label='LC - c08')

plt.plot(x, vlc_tr_c18, marker='v', color=orange_light, label='VLC - c18')
plt.plot(x, vlc_tr_c08, marker='v', linestyle='--', color=orange_dark, label='VLC - c08')

plt.xlabel("skin size factor")
plt.ylabel("Traversals [s]")
plt.grid(True)
plt.legend(ncol=2)
plt.tight_layout()
plt.savefig("wall_clock_avg.pdf", bbox_inches="tight")
plt.show()
plt.close()


# =======================
# 1) REBUILD FREQUENCY
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
# 2) UPDATE CONTAINER
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
# 3) FORCE UPDATE
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
