# Government vs Private Job Preference Project
# Generate 1,000 synthetic student records

import pandas as pd
import numpy as np
from pathlib import Path

# 1. Generate reproducible random data
np.random.seed(42)

# 2. Number of students
n = 1000

# 3. Student information
student_id = range(1001, 1001 + n)

age = np.random.randint(18, 26, n)

gender = np.random.choice(
    ["Male", "Female"],
    n
)

degree = np.random.choice(
    ["B.Sc", "B.Com", "B.A", "B.E", "B.Tech", "BCA", "BBA"],
    n
)

department = np.random.choice(
    ["Statistics", "Commerce", "Computer Science",
     "Economics", "Engineering", "Management", "Arts"],
    n
)

year = np.random.choice(
    ["1st Year", "2nd Year", "3rd Year", "4th Year"],
    n
)

# 4. Career preferences
preferred_sector = np.random.choice(
    ["Government", "Private", "Both"],
    n,
    p=[0.45, 0.40, 0.15]
)

# 5. Career motivations
career_reason = []

for sector in preferred_sector:

    if sector == "Government":
        reason = np.random.choice(
            ["Job Security", "Salary", "Work-Life Balance",
             "Social Status", "Family Preference"],
            p=[0.40, 0.15, 0.20, 0.15, 0.10]
        )

    elif sector == "Private":
        reason = np.random.choice(
            ["Career Growth", "Salary", "Skill Development",
             "Passion", "Work-Life Balance"],
            p=[0.30, 0.25, 0.20, 0.15, 0.10]
        )

    else:
        reason = np.random.choice(
            ["Salary", "Career Growth", "Job Security",
             "Work-Life Balance"],
            p=[0.25, 0.25, 0.25, 0.25]
        )

    career_reason.append(reason)

# 6. Expected monthly salary
expected_salary = np.random.randint(15000, 80001, n)

# 7. Career importance ratings (1 to 5)
job_security = np.random.randint(1, 6, n)
salary_importance = np.random.randint(1, 6, n)
career_growth = np.random.randint(1, 6, n)
work_life_balance = np.random.randint(1, 6, n)

# 8. Government exam preparation
preparation_status = np.random.choice(
    ["Preparing", "Planning", "Not Preparing"],
    n
)

government_exam = np.random.choice(
    ["TNPSC", "SSC", "Banking", "Railway", "Other", "None"],
    n
)

# 9. Private career interests
private_career = np.random.choice(
    ["IT", "Data Analytics", "Banking",
     "Core Industry", "Business", "None"],
    n
)

# 10. Skills students are learning
skills = np.random.choice(
    ["Python", "SQL", "Excel", "Power BI",
     "Communication", "Java", "Data Analysis"],
    n
)

# 11. Location preferences
location = np.random.choice(
    ["Chennai", "Other Tamil Nadu",
     "Bangalore", "Other India", "Anywhere"],
    n
)

# 12. Additional information
higher_studies = np.random.choice(
    ["Yes", "No", "Maybe"],
    n
)

internship = np.random.choice(
    ["Yes", "No"],
    n
)

confidence = np.random.randint(1, 6, n)

# 13. Create the dataset
df = pd.DataFrame({
    "Student_ID": student_id,
    "Age": age,
    "Gender": gender,
    "Degree": degree,
    "Department": department,
    "Year_of_Study": year,
    "Preferred_Sector": preferred_sector,
    "Career_Reason": career_reason,
    "Expected_Salary": expected_salary,
    "Job_Security_Importance": job_security,
    "Salary_Importance": salary_importance,
    "Growth_Importance": career_growth,
    "Work_Life_Balance": work_life_balance,
    "Preparation_Status": preparation_status,
    "Government_Exam": government_exam,
    "Private_Career": private_career,
    "Skills_Learning": skills,
    "Work_Location_Preference": location,
    "Higher_Studies": higher_studies,
    "Internship_Experience": internship,
    "Decision_Confidence": confidence
})

# 14. Save CSV file
project_folder = Path(__file__).resolve().parent.parent

output_folder = project_folder / "data" / "raw"

output_folder.mkdir(parents=True, exist_ok=True)

output_file = output_folder / "student_career_data.csv"

df.to_csv(output_file, index=False)

# 15. Display results
print("DATASET CREATED SUCCESSFULLY!")
print("----------------------------")
print("Total Students:", len(df))
print("Total Columns:", len(df.columns))
print("File Saved:", output_file)

print("\nFirst 5 Student Records:")
print(df.head())

print("\nCareer Preference Counts:")
print(df["Preferred_Sector"].value_counts())