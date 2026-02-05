# -----------------------------------------------------------
# 1.  ENVIRONMENT
# -----------------------------------------------------------
# !pip install kaggle pandas matplotlib seaborn --quiet


import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


# -----------------------------------------------------------
# 2.  DOWNLOAD DATA SET FROM KAGGLE
# -----------------------------------------------------------
# Ensure you have kaggle.json in ~/.kaggle/ or set env vars:
# KAGGLE_USERNAME and KAGGLE_KEY
os.system("kaggle datasets download -d pornhub/2023-year-in-review --force")


# Unzip the bundle (contains multiple CSVs; we need Categories.csv)
import zipfile
with zipfile.ZipFile("2023-year-in-review.zip", "r") as z:
    z.extractall("data")


# -----------------------------------------------------------
# 3.  LOAD AND INSPECT
# -----------------------------------------------------------
cat = pd.read_csv("data/Categories.csv")


# Quick sanity check
print("Shape:", cat.shape)
print(cat.head())


# -----------------------------------------------------------
# 4.  FILTER AGE / DEMOGRAPHIC TAGS
# -----------------------------------------------------------
# The CSV has columns: Category, Views, Section (Straight, Gay, Trans)
demo_keywords = ["teen", "mature", "Twenties", "thirties", "forties", "hunk", "femboy", "twink", "skinny", "fat", "Black", "BBC", "Asian", "Hispanic", "white", "bear", "daddy", "dilf",
                 "milf", "gilf", "older", "young", "barelylegal",
                 "jock", "hunk", "muscle", "chub", "chaser", "trans"]


mask = cat["Category"].str.lower().str.contains("|".join(demo_keywords), na=False)
demo = cat[mask].copy()
demo["Category"] = demo["Category"].str.title()


# -----------------------------------------------------------
# 5.  BUILD PIE #1 – OVERALL SHARE
# -----------------------------------------------------------
plt.figure(figsize=(8, 8))
plot_data = demo.groupby("Category")["Views"].sum().sort_values(ascending=False)
plt.pie(plot_data.values, labels=plot_data.index, autopct="%1.1f%%", startangle=90)
plt.title("Relative popularity of age/demographic tags on PornHub (2023)")
plt.tight_layout()
plt.savefig("demographic_share_pie.png", dpi=300)
plt.show()


# -----------------------------------------------------------
# 6.  BUILD PIE #2 – SHARE BY SECTION
# -----------------------------------------------------------
# Re-use the same demo slice
section_totals = demo.groupby("Section")["Views"].sum()
plt.figure(figsize=(6, 6))
plt.pie(section_totals.values, labels=section_totals.index, autopct="%1.1f%%", startangle=90)
plt.title("Age/demographic tag views by site section (2023)")
plt.tight_layout()
plt.savefig("demographic_by_section_pie.png", dpi=300)






