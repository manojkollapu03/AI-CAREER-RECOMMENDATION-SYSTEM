# 📊 Career Dataset Visualization in Google Colab
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =====================
# 1. Load Dataset
# =====================
data = {
    "Trait": [
        "Mathematical Ability", "Logical Thinking", "Creativity",
        "Tech Affinity", "Empathy", "Communication",
        "Leadership", "Analytical Skills", "Patience", "Organization"
    ],
    "Software Engineer": [80, 90, 40, 90, 30, 40, 50, 80, 40, 70],
    "Data Scientist": [90, 90, 50, 80, 30, 40, 40, 85, 35, 65],
    "Project Manager": [40, 60, 50, 60, 60, 75, 85, 70, 70, 90],
    "Sales Representative": [30, 40, 60, 50, 80, 90, 70, 40, 45, 60]
}

df = pd.DataFrame(data)

# Set style
sns.set(style="whitegrid")

# =====================
# 2. Line Chart
# =====================
plt.figure(figsize=(8,5))
for career in df.columns[1:]:
    plt.plot(df["Trait"], df[career], marker="o", label=career)
plt.xticks(rotation=45, ha="right")
plt.title("Line Chart - Trait Comparison")
plt.ylabel("Trait Score (%)")
plt.legend()
plt.show()

# =====================
# 3. Bar Chart
# =====================
df_melt = df.melt(id_vars="Trait", var_name="Career", value_name="Score")
plt.figure(figsize=(10,6))
sns.barplot(x="Trait", y="Score", hue="Career", data=df_melt)
plt.xticks(rotation=45, ha="right")
plt.title("Bar Chart - Trait vs Career")
plt.show()

# =====================
# 4. Histogram
# =====================
plt.figure(figsize=(8,5))
plt.hist(df["Software Engineer"], bins=5, alpha=0.7, label="Software Engineer")
plt.hist(df["Data Scientist"], bins=5, alpha=0.7, label="Data Scientist")
plt.title("Histogram - Trait Score Distribution")
plt.xlabel("Score (%)")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# =====================
# 5. Pie Chart
# =====================
plt.figure(figsize=(6,6))
plt.pie(df["Data Scientist"], labels=df["Trait"], autopct="%1.1f%%", startangle=140)
plt.title("Pie Chart - Data Scientist Trait Distribution")
plt.show()

# =====================
# 6. Heatmap
# =====================
plt.figure(figsize=(8,6))
sns.heatmap(df.set_index("Trait").T, annot=True, cmap="YlGnBu", cbar=True)
plt.title("Heatmap - Career vs Traits")
plt.show()
