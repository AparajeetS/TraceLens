"""Render the benchmark summary figure from results.csv."""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parent
with (ROOT / "results" / "results.csv").open(newline="", encoding="utf-8") as stream:
    rows = list(csv.DictReader(stream))
rows.sort(key=lambda row: float(row["visibility"]))
x = [float(row["visibility"]) for row in rows]
recall = [float(row["recall"]) for row in rows]
recall_low = [float(row["recall_ci_low"]) for row in rows]
recall_high = [float(row["recall_ci_high"]) for row in rows]
masked_fpr = [float(row["masked_recurrence_fpr"]) for row in rows]
adaptive_fpr = [float(row["within_episode_frequency_fpr"]) for row in rows]
raw_fpr = [float(row["raw_recurrence_fpr"]) for row in rows]

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9})
fig, ax = plt.subplots(figsize=(7.2, 3.6), dpi=180)
ax.plot(x, recall, color="#2459A6", marker="o", linewidth=2.4, label="Masked recurrence: recall")
ax.fill_between(x, recall_low, recall_high, color="#2459A6", alpha=0.13, linewidth=0)
ax.plot(x, masked_fpr, color="#2F8F68", marker="o", linewidth=2, label="Masked recurrence: false positives")
ax.plot(x, adaptive_fpr, color="#D78928", marker="s", linewidth=2, label="Local frequency filter: false positives")
ax.plot(x, raw_fpr, color="#B74444", marker="^", linewidth=2, label="Raw recurrence: false positives")
ax.set_xlim(0.2, 1.03)
ax.set_ylim(-0.04, 1.04)
ax.set_xticks(x, [f"{value:.0%}" for value in x])
ax.set_yticks([0, .2, .4, .6, .8, 1.0], ["0%", "20%", "40%", "60%", "80%", "100%"])
ax.set_xlabel("Fraction of messages visible to the monitor")
ax.set_ylabel("Rate")
ax.grid(axis="y", color="#DCE3EC", linewidth=.7)
ax.spines[["top", "right"]].set_visible(False)
ax.spines[["left", "bottom"]].set_color("#9BA8B7")
ax.legend(frameon=False, ncol=2, loc="upper center", bbox_to_anchor=(.5, -.20), fontsize=7.7)
fig.subplots_adjust(left=.11, right=.985, top=.96, bottom=.31)
fig.savefig(ROOT / "results" / "visibility_results.png", bbox_inches="tight", facecolor="white")
