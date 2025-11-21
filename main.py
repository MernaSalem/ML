import pandas as pd
import numpy as np
import gender_guesser.detector as gender
df=pd.read_csv("D:/DataScience/Data/StudentPrediction/student_performance_updated_1000.csv")
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
missing_name_gender = df[df['Name'].isna() & df['Gender'].isna()]
print("Rows with both missing:", missing_name_gender.shape[0])
df = df.drop(missing_name_gender.index)
d = gender.Detector()
df['Gender'] = df.apply(lambda row: d.get_gender(row['Name'])
                        if pd.isna(row['Gender']) and pd.notna(row['Name'])
                        else row['Gender'], axis=1)
print(df)


import pandas as pd
import numpy as np
import gender_guesser.detector as gender
from sklearn.impute import SimpleImputer
df=pd.read_csv("D:\DataScience\Data\StudentPrediction\student_performance_updated_1000.csv")
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
missing_name_gender = df[df['Name'].isna() & df['Gender'].isna()]
print("Rows with both missing:", missing_name_gender.shape[0])
df = df.drop(missing_name_gender.index)
d = gender.Detector()
df['Gender'] = df.apply(lambda row: d.get_gender(row['Name'])
                        if pd.isna(row['Gender']) and pd.notna(row['Name'])
                        else row['Gender'], axis=1)

df = df.drop(['StudentID', 'Name'], axis=1)
# Step 3a: Convert StudyHoursPerWeek to per day (assuming 5-day week)
df['StudyHoursPerDay_Calc'] = df['StudyHoursPerWeek'] / 5

# Step 3b: Recalculate StudyHoursPerWeek from StudyHoursPerDay
df['StudyHoursPerWeek_Calc'] = df['Study Hours'] * 5

# Step 3c: Create average columns (blended)
df['StudyHoursPerDay_Avg'] = (df['StudyHoursPerDay_Calc'] + df['Study Hours']) / 2
df['StudyHoursPerWeek_Avg'] = (df['StudyHoursPerWeek_Calc'] + df['StudyHoursPerWeek']) / 2

# Step 3d: Drop originals and intermediate calculation columns, keep only average per week
df = df.drop(['StudyHoursPerWeek', 'Study Hours', 'StudyHoursPerDay_Calc', 'StudyHoursPerWeek_Calc', 'StudyHoursPerDay_Avg'], axis=1)
df['StudyHoursPerWeek_Avg'] = df['StudyHoursPerWeek_Avg'].abs()
# Numeric columns: AttendanceRate, PreviousGrade, FinalGrade, Attendance (%), StudyHoursPerWeek_Avg
numeric_cols = ['AttendanceRate', 'PreviousGrade', 'FinalGrade', 'Attendance (%)', 'StudyHoursPerWeek_Avg']
numeric_imputer = SimpleImputer(strategy='mean')
df[numeric_cols] = numeric_imputer.fit_transform(df[numeric_cols])

# Categorical columns: ExtracurricularActivities, ParentalSupport, Online Classes Taken, Gender
categorical_cols = ['ExtracurricularActivities', 'ParentalSupport', 'Online Classes Taken', 'Gender']
categorical_imputer = SimpleImputer(strategy='most_frequent')
df[categorical_cols] = categorical_imputer.fit_transform(df[categorical_cols])
df = df.drop(['Attendance (%)'], axis=1)