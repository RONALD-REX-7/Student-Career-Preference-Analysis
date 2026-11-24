# STUDENT CAREER PREFERENCE ANALYSIS
# PHASE 3: EXPLORATORY DATA ANALYSIS (EDA)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Project folder
project_folder = Path(__file__).resolve().parent.parent

# Load cleaned data
file_path = project_folder / "data" / "processed" / "student_career_cleaned.csv"

df = pd.read_csv(file_path)

# Create charts folder
charts_folder = project_folder / "images"
charts_folder.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid")

print("=" * 50)
print("STUDENT CAREER PREFERENCE ANALYSIS")
print("=" * 50)

# ------------------------------------------
# ANALYSIS 1: CAREER SECTOR PREFERENCE
# ------------------------------------------

sector_counts = df["Preferred_Sector"].value_counts()

print("\n1. CAREER SECTOR PREFERENCE")
print(sector_counts)

sector_percentage = df["Preferred_Sector"].value_counts(normalize=True) * 100

print("\nCareer Preference Percentage:")
print(sector_percentage.round(2))

plt.figure(figsize=(8, 5))

sns.barplot(
    x=sector_counts.index,
    y=sector_counts.values
)

plt.title("Student Preference: Government vs Private Jobs")
plt.xlabel("Preferred Career Sector")
plt.ylabel("Number of Students")

plt.tight_layout()

plt.savefig(charts_folder / "career_preference.png")
plt.show()


# ------------------------------------------
# ANALYSIS 2: CAREER REASONS
# ------------------------------------------

reason_counts = df["Career_Reason"].value_counts()

print("\n2. MAIN CAREER MOTIVATIONS")
print(reason_counts)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=reason_counts.values,
    y=reason_counts.index
)

plt.title("Reasons Behind Students' Career Preferences")
plt.xlabel("Number of Students")
plt.ylabel("Career Motivation")

plt.tight_layout()

plt.savefig(charts_folder / "career_reasons.png")
plt.show()


# ------------------------------------------
# ANALYSIS 3: EXPECTED SALARY
# ------------------------------------------

print("\n3. EXPECTED MONTHLY SALARY")
print(df["Expected_Salary"].describe())

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="Expected_Salary",
    bins=20,
    kde=True
)

plt.title("Distribution of Expected Monthly Salary")
plt.xlabel("Expected Salary (₹)")
plt.ylabel("Number of Students")

plt.tight_layout()

plt.savefig(charts_folder / "salary_distribution.png")
plt.show()


# ------------------------------------------
# ANALYSIS 4: GOVERNMENT EXAM PREPARATION
# ------------------------------------------

exam_counts = df["Preparation_Status"].value_counts()

print("\n4. GOVERNMENT EXAM PREPARATION STATUS")
print(exam_counts)

plt.figure(figsize=(8, 5))

plt.pie(
    exam_counts.values,
    labels=exam_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Government Exam Preparation Status")

plt.tight_layout()

plt.savefig(charts_folder / "exam_preparation.png")
plt.show()


# ------------------------------------------
# ANALYSIS 5: CAREER PREFERENCE BY DEGREE
# ------------------------------------------

degree_analysis = pd.crosstab(
    df["Degree"],
    df["Preferred_Sector"]
)

print("\n5. CAREER PREFERENCE BY DEGREE")
print(degree_analysis)

degree_analysis.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Career Preference by Degree")
plt.xlabel("Degree")
plt.ylabel("Number of Students")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(charts_folder / "preference_by_degree.png")
plt.show()


# ------------------------------------------
# FINAL SUMMARY
# ------------------------------------------

print("\n" + "=" * 50)
print("EDA COMPLETED SUCCESSFULLY!")
print("=" * 50)

print("\nTotal Students:", len(df))

print("\nCharts saved in:")
print(charts_folder)