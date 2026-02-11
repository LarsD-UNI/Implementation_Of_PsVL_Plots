import matplotlib.pyplot as plt

blue_dark   = '#1f77b4'
orange_dark = '#ff7f0e'

data_ns = {
    "0.6": {
        "PSVL": {"compute": 1039909, "rebuild": 9117},
        "VLC":  {"compute": 1134345, "rebuild": 2014},
    },
}

def plot_single_metric_ns(skin, metric, ylabel, filename):
    labels = ["PSVL", "VLC"]
    values_ns = [
        data_ns[skin]["PSVL"][metric],
        data_ns[skin]["VLC"][metric],
    ]

    plt.figure(figsize=(4.5, 4))
    plt.bar(labels, values_ns, color=[blue_dark, orange_dark])

    plt.ylabel(ylabel, fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(filename, bbox_inches="tight")
    plt.show()
    plt.close()


plot_single_metric_ns(
    "0.6", "compute",
    "computeInteractions [ns]",
    "computeInteractions_0.6.pdf"
)

plot_single_metric_ns(
    "0.6", "rebuild",
    "rebuildNeighborLists [ns]",
    "rebuildNeighborLists_0.6.pdf"
)