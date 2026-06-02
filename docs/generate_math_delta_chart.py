import matplotlib.pyplot as plt
import numpy as np
import os

# d:\Projects\M-SB-GRPO\compare\open-r1\.venv\Scripts\python.exe docs\generate_math_delta_chart.py

# Data extracted from Table 4 (MATH Sub-category Analysis)
categories = [
    "Algebra",
    "Counting & Probability",
    "Geometry",
    "Intermediate Algebra",
    "Number Theory",
    "Prealgebra",
    "Precalculus",
]
m_grpo = [89.39, 64.56, 56.99, 49.83, 70.56, 81.63, 51.28]
sb_grpo = [89.13, 67.09, 57.62, 54.71, 73.52, 82.43, 56.96]

# Calculate absolute deltas (SB-GRPO - M-GRPO)
deltas = [sb - m for sb, m in zip(sb_grpo, m_grpo)]

# Setup styling
plt.style.use("ggplot")
fig, ax = plt.subplots(figsize=(12, 5.5))

# Override ggplot's default gray background
ax.set_facecolor("white")
fig.patch.set_facecolor("white")

# Define premium academic colors (Steel Blue for positive, Muted Red for negative)
pos_color = "#2b5c8f"
neg_color = "#c94c4c"
colors = [pos_color if d > 0 else neg_color for d in deltas]

# Create horizontal bar chart
y_pos = np.arange(len(categories))
bars = ax.barh(
    y_pos,
    deltas,
    color=colors,
    height=0.8,
    alpha=0.9,
    edgecolor="#222222",
    linewidth=0.8,
)

# Add data labels
for i, (bar, delta) in enumerate(zip(bars, deltas)):
    offset = 0.15 if delta > 0 else -0.15
    ha = "left" if delta > 0 else "right"
    color = pos_color if delta > 0 else neg_color
    sign = "+" if delta > 0 else ""
    ax.text(
        delta + offset,
        bar.get_y() + bar.get_height() / 2,
        f"{sign}{delta:.2f}%",
        va="center",
        ha=ha,
        fontsize=11,
        fontweight="bold",
        color=color,
    )

# Add baseline at x=0
ax.axvline(0, color="black", linewidth=1.2, alpha=0.8)

# Styling details
ax.set_yticks(y_pos)
ax.set_yticklabels(categories, fontsize=12, fontweight="bold")
ax.set_xlabel(
    "Absolute Performance Gain (%)", fontsize=12, fontweight="bold", labelpad=10
)
ax.set_title(
    "Performance Gain of SB-GRPO vs M-GRPO on MATH Sub-categories",
    fontsize=14,
    fontweight="bold",
    pad=20,
)

# Remove top and right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_color("#333333")

# Set x limits to give labels room
ax.set_xlim(min(deltas) - 1, max(deltas) + 1.5)

# Grid
ax.grid(axis="x", color="#e0e0e0", linestyle="--", alpha=0.7)
ax.grid(axis="y", visible=False)

plt.tight_layout()

# Save the plot
output_png = r"d:\Projects\M-SB-GRPO\report-newest\SB_GRPO__Semantic_Balanced_GRPO_for_Enhanced_LLM_Reasoning_new\math_delta_chart.png"
output_pdf = r"d:\Projects\M-SB-GRPO\report-newest\SB_GRPO__Semantic_Balanced_GRPO_for_Enhanced_LLM_Reasoning_new\math_delta_chart.pdf"

plt.savefig(output_png, dpi=300, bbox_inches="tight")
plt.savefig(output_pdf, bbox_inches="tight")

print(f"Successfully generated new charts at:\n{output_png}\n{output_pdf}")
