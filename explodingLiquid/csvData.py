import matplotlib.pyplot as plt

# Colors
blue_dark   = '#1f77b4'
orange_dark = '#ff7f0e'

data_ns = {
    "0.3": {
        "PSVL": {
            "compute": 243594,
            "rebuild": 131938,
        },
        "VLC": {
            "compute": 214488,
            "rebuild": 19588,
        },
    },
    "0.6": {
        "PSVL": {
            "compute": 279196,
            "rebuild": 55336,
        },
        "VLC": {
            "compute": 232240,
            "rebuild": 8992,
        },
    },
}

def ns_to_ms(ns):
    return ns / 1_000_000  # nicht runden!

def plot_single_metric_ms(skin, metric, ylabel, filename):
    labels = ["PSVL", "VLC"]
    values_ms = [
        ns_to_ms(data_ns[skin]["PSVL"][metric]),
        ns_to_ms(data_ns[skin]["VLC"][metric]),
    ]

    plt.figure(figsize=(4.5, 4))
    plt.bar(labels, values_ms, color=[blue_dark, orange_dark])

    plt.ylabel(ylabel, fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    plt.ylabel(ylabel)
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(filename, bbox_inches="tight")
    plt.show()
    plt.close()

plot_single_metric_ms(
    "0.3",
    "compute",
    "computeInteractions (ms)",
    "computeInteractions_0.3.pdf"
)

plot_single_metric_ms(
    "0.3",
    "rebuild",
    "rebuildNeighborLists (ms)",
    "rebuildNeighborLists_0.3.pdf"
)

plot_single_metric_ms(
    "0.6",
    "compute",
    "computeInteractions (ms)",
    "computeInteractions_0.6.pdf"
)

plot_single_metric_ms(
    "0.6",
    "rebuild",
    "rebuildNeighborLists (ms)",
    "rebuildNeighborLists_0.6.pdf"
)