import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Kiran"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)
print(df)
print("\nTop rows:")
print(df.head())
print("\nAverage Marks:", df["Marks"].mean())
