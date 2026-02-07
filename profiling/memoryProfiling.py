import matplotlib.pyplot as plt

blue_dark   = '#1f77b4'
orange_dark = '#ff7f0e'
gray_base   = '#b0b0b0'

# =======================
# Data (GB)
# =======================
data_gb = {
    "PSVL": {"container": 2.8, "linkedbase": 1.5},
    "VLC":  {"container": 3.0, "linkedbase": 1.5},
}

def plot_stacked_memory(filename):
    labels = ["PSVL", "VLC"]

    linkedbase = [
        data_gb["PSVL"]["linkedbase"],
        data_gb["VLC"]["linkedbase"],
    ]
    container = [
        data_gb["PSVL"]["container"],
        data_gb["VLC"]["container"],
    ]

    plt.figure(figsize=(4.5, 4))

    lb = plt.bar(
        labels,
        linkedbase,
        color=gray_base,
        label="VerletListsLinkedBase"
    )

    plt.bar(
        labels,
        container,
        bottom=linkedbase,
        color=[blue_dark, orange_dark]
    )

    # Dummy-Handles für Legende
    psvl_handle = plt.Rectangle((0, 0), 1, 1, color=blue_dark)
    vlc_handle  = plt.Rectangle((0, 0), 1, 1, color=orange_dark)

    plt.ylabel("Memory [GB]")
    plt.title("Memory usage (stacked)")
    plt.grid(axis="y")

    max_total = max(
        data_gb["PSVL"]["container"] + data_gb["PSVL"]["linkedbase"],
        data_gb["VLC"]["container"]  + data_gb["VLC"]["linkedbase"],
    )
    plt.ylim(0, max_total * 1.35)

    plt.legend(
        handles=[lb[0], psvl_handle, vlc_handle],
        labels=[
            "VerletListsLinkedBase",
            "PseudoVerletLists",
            "VerletListsCells"
        ],
        loc="upper left"
    )

    plt.tight_layout()
    plt.savefig(filename, bbox_inches="tight")
    plt.show()
    plt.close()

plot_stacked_memory("memory_stacked.pdf")
