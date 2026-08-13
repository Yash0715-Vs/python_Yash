import numpy as np
import pandas as pd

data = {
    "Name": ["Yash", "Rahul", "Amit", "Neha", "Priya", "Karan"],
    "Math": [85, 67, 92, 55, 78, 95],
    "Python": [90, 72, 88, 60, 82, 91],
    "DSA": [80, 65, 95, 58, 75, 89]
}
df = pd.DataFrame(data)

df["Average"] = np.mean(
    df[["Math","Python","DSA"]],
    axis = 1
)

df["total"] = df["Math"]+ df["Python"] +df["DSA"]

df["result"] = np.where(
    (df["Math"] >= 60) &
    (df["Python"] >= 60) &  #np.where(condition,"pass","fail")
    (df["DSA"] >= 60),
    "Pass",
    "Fail"
    )

print("Complete DataFrame:")
print(df)



print(f"\nStudent with highest average: \n{df.loc[df["Average"].idxmax()]}")
 #df.loc:-- gives complete student's row
 #idxmax()&idxmin():-- index of high & low average


# 6. Student with lowest average
print(f"\nStudent with lowest average: \n{df.loc[df["Average"].idxmin()]}")



# 7. Students with average greater than 80
print(f"\nStudents with average greater than 80: \n{df[df["Average"] > 80]}")



# 8. Overall class average
print("\nOverall class average:", df["Average"].mean())


# 9. Highest mark in each subject
print(f"\nHighest mark in each subject: \n{df[["Math", "Python", "DSA"]].max()}")



# 10. Lowest mark in each subject
print(f"\nLowest mark in each subject: \n{df[["Math", "Python", "DSA"]].min()}")
