# PHASE 4: BUSINESS INSIGHTS
# Government vs Private Job Student Preference

import pandas as pd
from pathlib import Path

# Project location
project_folder = Path(__file__).resolve().parent.parent

# Load cleaned dataset
file_path = project_folder / "data" / "processed" / "student_career_cleaned.csv"

df = pd.read_csv(file_path)

# Create reports folder
report_folder = project_folder / "reports"
report_folder.mkdir(exist_ok=True)

# Start report
report = []

report.append("=" * 60)
report.append("STUDENT CAREER PREFERENCE ANALYSIS - INSIGHTS REPORT")
report.append("=" * 60)

report.append(f"\nTotal students analyzed: {len(df)}")

# ------------------------------------------
# INSIGHT 1: SECTOR PREFERENCE
# ------------------------------------------

sector_counts = df["Preferred_Sector"].value_counts()
sector_percentage = df["Preferred_Sector"].value_counts(normalize=True) * 100

report.append("\n1. CAREER SECTOR PREFERENCE")
report.append("-" * 40)

for sector, count in sector_counts.items():
    percentage = sector_percentage[sector]
    report.append(
        f"{sector}: {count} students ({percentage:.2f}%)"
    )

# ------------------------------------------
# INSIGHT 2: MAIN CAREER MOTIVATION
# ------------------------------------------

reason_counts = df["Career_Reason"].value_counts()

report.append("\n2. TOP CAREER MOTIVATIONS")
report.append("-" * 40)

for reason, count in reason_counts.head(5).items():
    report.append(f"{reason}: {count} students")

# ------------------------------------------
# INSIGHT 3: EXPECTED SALARY
# ------------------------------------------

report.append("\n3. EXPECTED MONTHLY SALARY")
report.append("-" * 40)

report.append(
    f"Average salary expectation: ₹{df['Expected_Salary'].mean():,.2f}"
)

report.append(
    f"Median salary expectation: ₹{df['Expected_Salary'].median():,.2f}"
)

report.append(
    f"Minimum salary expectation: ₹{df['Expected_Salary'].min():,}"
)

report.append(
    f"Maximum salary expectation: ₹{df['Expected_Salary'].max():,}"
)

# ------------------------------------------
# INSIGHT 4: SALARY BY CAREER SECTOR
# ------------------------------------------

salary_sector = df.groupby("Preferred_Sector")["Expected_Salary"].mean()

report.append("\n4. AVERAGE SALARY BY PREFERENCE")
report.append("-" * 40)

for sector, salary in salary_sector.items():
    report.append(f"{sector}: ₹{salary:,.2f}")

# ------------------------------------------
# INSIGHT 5: EXAM PREPARATION
# ------------------------------------------

preparation_counts = df["Preparation_Status"].value_counts()
preparation_percentage = (
    df["Preparation_Status"].value_counts(normalize=True) * 100
)

report.append("\n5. GOVERNMENT EXAM PREPARATION")
report.append("-" * 40)

for status, count in preparation_counts.items():
    percentage = preparation_percentage[status]
    report.append(f"{status}: {count} ({percentage:.2f}%)")

# ------------------------------------------
# INSIGHT 6: PREFERENCE BY DEGREE
# ------------------------------------------

degree_table = pd.crosstab(
    df["Degree"],
    df["Preferred_Sector"]
)

report.append("\n6. CAREER PREFERENCE BY DEGREE")
report.append("-" * 40)

report.append(degree_table.to_string())

# ------------------------------------------
# INSIGHT 7: SKILLS
# ------------------------------------------

skill_counts = df["Skills_Learning"].value_counts()

report.append("\n7. MOST POPULAR SKILLS")
report.append("-" * 40)

for skill, count in skill_counts.head(5).items():
    report.append(f"{skill}: {count} students")

# ------------------------------------------
# SAVE REPORT
# ------------------------------------------

report_text = "\n".join(report)

output_file = report_folder / "student_career_insights.txt"

with open(output_file, "w", encoding="utf-8") as file:
    file.write(report_text)

# Display report
print(report_text)

print("\n" + "=" * 60)
print("INSIGHTS REPORT CREATED SUCCESSFULLY!")
print("Saved at:", output_file)