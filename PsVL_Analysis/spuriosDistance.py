import random
import numpy as np
import matplotlib.pyplot as plt
import math

# ----------------------------
# Data structures
# ----------------------------
class Particle:
    __slots__ = ("x", "y", "z")

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


# ----------------------------
# Parameters
# ----------------------------
r_c = 1.0
CELLS_PER_DIM = 3
NUM_CELLS = CELLS_PER_DIM ** 3
CENTER_CELL_INDEX = 13  # (1,1,1)


# ----------------------------
# Helpers
# ----------------------------
def calculateVerlet(r_s: float) -> float:
    return (r_c ** 3) / ((r_c + r_s) ** 3)

def distance(p1: Particle, p2: Particle) -> float:
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dz = p1.z - p2.z
    return math.sqrt(dx * dx + dy * dy + dz * dz)

def normalize(vec):
    x, y, z = vec
    length = math.sqrt(x * x + y * y + z * z)
    if length == 0.0:
        raise ValueError("Cannot normalize zero vector")
    return [x / length, y / length, z / length]

def one_to_three_d(ind: int):
    # dims fixed: 3x3x3
    d0, d1 = 3, 3
    z = ind // (d0 * d1)
    y = (ind - z * d0 * d1) // d0
    x = ind - d0 * (y + d1 * z)
    # offsets in {-1,0,1}
    return [x - 1, y - 1, z - 1]

def insert_particle_into_cell(particle: Particle, cells):
    # coords in [0, 3*r_c] -> floor gives 0..3, clamp to 0..2
    cx = math.floor(particle.x / r_c)
    cy = math.floor(particle.y / r_c)
    cz = math.floor(particle.z / r_c)

    cx = min(max(cx, 0), 2)
    cy = min(max(cy, 0), 2)
    cz = min(max(cz, 0), 2)

    cell_index = (cz * 3 + cy) * 3 + cx  # 0..26
    cells[cell_index].append(particle)


# ----------------------------
# Core logic
# ----------------------------
def build_cells(particleCount: int, seed: int = 42):
    """Generate ONE particle configuration and insert into 3x3x3 cells."""
    random.seed(seed)
    cells = [[] for _ in range(NUM_CELLS)]

    for _ in range(particleCount):
        par = Particle(
            random.uniform(0, 3 * r_c),
            random.uniform(0, 3 * r_c),
            random.uniform(0, 3 * r_c),
        )
        insert_particle_into_cell(par, cells)

    return cells

def evalDirectSum(particles):
    interactions = 0
    spurious = 0
    n = len(particles)
    for i in range(n):
        for j in range(n):
            if i != j:
                interactions += 1
                if distance(particles[i], particles[j]) > r_c:
                    spurious += 1
    return interactions, spurious

def evalPsvl(cells, neighborIndex, r_s):
    interactions = 0
    spurious = 0

    direction = normalize(one_to_three_d(neighborIndex))  # unit vector from cell-offset

    for p_center in cells[CENTER_CELL_INDEX]:
        dCenter = direction[0] * p_center.x + direction[1] * p_center.y + direction[2] * p_center.z

        for p_neighbor in cells[neighborIndex]:
            dNeighbor = direction[0] * p_neighbor.x + direction[1] * p_neighbor.y + direction[2] * p_neighbor.z

            # Candidate by pseudo-Verlet projection rule
            if abs(dCenter - dNeighbor) < (r_c + r_s):
                interactions += 1
                if distance(p_center, p_neighbor) > r_c:
                    spurious += 1
    spurious += 1
    return interactions, spurious

def calculatePsVL_from_cells(cells, r_s: float) -> float:
    particleInteractions = 0
    particleSpurious = 0

    for i in range(NUM_CELLS):
        if i == CENTER_CELL_INDEX:
            inter, spur = evalDirectSum(cells[i])
        else:
            inter, spur = evalPsvl(cells, i, r_s)

        particleInteractions += inter
        particleSpurious += spur

    if particleInteractions == 0:
        return 0.0

    return 1.0 - (particleSpurious / particleInteractions)

# ----------------------------
# Plot (thesis-quality)
# ----------------------------
particleCount = 2000
cells_fixed = build_cells(particleCount, seed=3)

r_s_values = np.linspace(0, 0.5 * r_c, 200)

verlet_values = [calculateVerlet(r_s) for r_s in r_s_values]
psvl_values = [calculatePsVL_from_cells(cells_fixed, r_s) for r_s in r_s_values]

# NEW: create figure with size + dpi
fig, ax = plt.subplots(figsize=(6.5, 4.0), dpi=200)  # ~ thesis-friendly size

ax.plot(r_s_values / r_c, verlet_values, label="Verlet list", linewidth=2)
ax.plot(r_s_values / r_c, psvl_values, label="Pseudo-Verlet lists",
        linestyle="--", linewidth=2)

ax.set_xlabel(r"$r_s / r_c$", fontsize=12)
ax.set_ylabel(r"Ratio of pairs within $r_c$", fontsize=12)
ax.set_xlim(0, 0.5)
ax.set_ylim(0, 1)

ax.tick_params(labelsize=11)
ax.grid(True, alpha=0.25)
ax.legend(fontsize=11)

fig.tight_layout()

# NEW: export high-quality
fig.savefig("psvl_vs_verlet.pdf", bbox_inches="tight")     # best for thesis
fig.savefig("psvl_vs_verlet.png", dpi=300, bbox_inches="tight")  # if you need PNG

plt.show()

