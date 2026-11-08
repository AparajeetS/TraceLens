"""Generate publication-quality Figure 2 for the TraceLens-Gateway benchmark."""

from __future__ import annotations

import json
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent
results_file = ROOT / "results" / "gateway_results.json"

with open(results_file, encoding="utf-8") as f:
    data = json.load(f)

# Categories and defense performance
defenses = ["Isolated Review\n(Per-Request)", "Time-Window\nHeuristic (60s)", "Action-Dependency\nDAG (TraceLens)"]
recalls = [data["isolated"]["recall"] * 100, data["time_window"]["recall"] * 100, data["action_dag"]["recall"] * 100]
bypass_rates = [100 - r for r in recalls]
fprs = [data["isolated"]["fpr"] * 100, data["time_window"]["fpr"] * 100, data["action_dag"]["fpr"] * 100]

# Threat categories breakdown loaded dynamically from benchmark output
cat_data = data.get("category_recall", {})
categories = ["DevOps Execution\nSlicing (10)", "Cloud / IAM\nEscalation (10)", "Financial AML\nStructuring (10)"]
cat_keys = ["devops", "cloud", "finance"]

cat_isolated = [cat_data.get(k, {}).get("isolated", 0.0) * 100 for k in cat_keys]
cat_time_window = [cat_data.get(k, {}).get("time_window", 0.0) * 100 for k in cat_keys]
cat_action_dag = [cat_data.get(k, {}).get("action_dag", 1.0) * 100 for k in cat_keys]

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5})
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 2.7), dpi=200)

# ----------------- PANEL A: Overall Attack Bypass vs Detection Rate -----------------
bar_width = 0.38
x_pos = np.arange(len(defenses))

bars_det = ax1.bar(x_pos - bar_width/2, recalls, width=bar_width, label="Attack Interception (Recall)", color="#1F519B", edgecolor="none")
bars_byp = ax1.bar(x_pos + bar_width/2, bypass_rates, width=bar_width, label="Attack Bypass Rate", color="#D9534F", edgecolor="none")

ax1.set_title("(a) Attack Interception vs. Slicing Bypass Rate", fontsize=9.2, fontweight="bold", pad=8)
ax1.set_xticks(x_pos)
ax1.set_xticklabels(defenses, fontsize=7.8)
ax1.set_ylabel("Percentage (%)", fontsize=8.5)
ax1.set_ylim(0, 115)
ax1.set_yticks([0, 25, 50, 75, 100])
ax1.grid(axis="y", color="#E2E8F0", linestyle="--", linewidth=0.7)
ax1.spines[["top", "right"]].set_visible(False)
ax1.spines[["left", "bottom"]].set_color("#94A3B8")

for bar in bars_det:
    h = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, h + 2, f"{h:.1f}%", ha="center", va="bottom", fontsize=7.2, fontweight="bold", color="#1F519B")
for bar in bars_byp:
    h = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, h + 2, f"{h:.1f}%", ha="center", va="bottom", fontsize=7.2, fontweight="bold", color="#D9534F")

ax1.legend(loc="upper center", bbox_to_anchor=(0.5, -0.28), frameon=False, fontsize=7.5, ncol=2)

# ----------------- PANEL B: Detection by Threat Slicing Category -----------------
cat_x = np.arange(len(categories))
c_w = 0.25

b1 = ax2.bar(cat_x - c_w, cat_isolated, width=c_w, label="Isolated Review", color="#94A3B8")
b2 = ax2.bar(cat_x, cat_time_window, width=c_w, label="Time-Window", color="#F59E0B")
b3 = ax2.bar(cat_x + c_w, cat_action_dag, width=c_w, label="Action-Dependency DAG", color="#10B981")

ax2.set_title("(b) Slicing Detection by Threat Domain", fontsize=9.2, fontweight="bold", pad=8)
ax2.set_xticks(cat_x)
ax2.set_xticklabels(categories, fontsize=7.8)
ax2.set_ylabel("Recall (%)", fontsize=8.5)
ax2.set_ylim(0, 115)
ax2.set_yticks([0, 25, 50, 75, 100])
ax2.grid(axis="y", color="#E2E8F0", linestyle="--", linewidth=0.7)
ax2.spines[["top", "right"]].set_visible(False)
ax2.spines[["left", "bottom"]].set_color("#94A3B8")

for bar in b3:
    h = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, h + 2, f"{h:.0f}%", ha="center", va="bottom", fontsize=7.0, fontweight="bold", color="#059669")

ax2.legend(loc="upper center", bbox_to_anchor=(0.5, -0.28), frameon=False, fontsize=7.5, ncol=3)

fig.subplots_adjust(left=0.08, right=0.98, top=0.90, bottom=0.30, wspace=0.28)
out_path = ROOT / "results" / "gateway_results.png"
fig.savefig(out_path, bbox_inches="tight", facecolor="white")
print(f"Saved {out_path}")
