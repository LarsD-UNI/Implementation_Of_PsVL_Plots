import matplotlib.pyplot as plt

# Colors
blue_dark   = '#1f77b4'
orange_dark = '#ff7f0e'

data_ns = {
    "0.3": {
        "PSVL": {"compute": 1326289, "rebuild": 644903},
        "VLC":  {"compute":  877475, "rebuild": 118985},
    },
    "0.7": {
        "PSVL": {"compute": 2262185, "rebuild": 280792},
        "VLC":  {"compute": 1684029, "rebuild":  63958},
    }
}

def ns_to_ms(ns):
    return ns / 1_000_000

def plot_single_metric_ms(skin, metric, ylabel, filename):
    labels = ["PSVL", "VLC"]
    values_ms = [
        ns_to_ms(data_ns[skin]["PSVL"][metric]),
        ns_to_ms(data_ns[skin]["VLC"][metric]),
    ]

    plt.figure(figsize=(4.5, 4))
    plt.bar(labels, values_ms, color=[blue_dark, orange_dark])

    plt.ylabel(ylabel)
    plt.title(f"{metric} (skin size factor = {skin})")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(filename, bbox_inches="tight")
    plt.show()
    plt.close()

plot_single_metric_ms(
    "0.3", "compute",
    "computeInteractions (ms)",
    "computeInteractions_0.3.pdf"
)

plot_single_metric_ms(
    "0.3", "rebuild",
    "rebuildNeighborLists (ms)",
    "rebuildNeighborLists_0.3.pdf"
)

plot_single_metric_ms(
    "0.7", "compute",
    "computeInteractions (ms)",
    "computeInteractions_0.7.pdf"
)

plot_single_metric_ms(
    "0.7", "rebuild",
    "rebuildNeighborLists (ms)",
    "rebuildNeighborLists_0.7.pdf"
)