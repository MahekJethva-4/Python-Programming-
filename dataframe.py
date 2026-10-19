import pandas as pd

#Create a Dataframe
data = {
    "Name": ["Mahek","Hetvi","Monika", "Kunjal"],
    "Age": [21, 20, 22, 21],
    "Marks": [89, 78,92, 85]
}

df = pd.DataFrame(data)
#Display the  complete Dataframe
print("Student Data:")
print(df)

#Display the first two raws
print("\nFirst Two Rows:")
print(df.head(2))

#Dispay basic information
print("\nDataFrame Information:")
print(df.into())

#Calculate average marks
print("\nAverageMarks:", df["Marks"].mean())

#Find maximum marks
print("Maximum Marks:", df["Marks"].max())

#Find minimum marks
print("Minimum Marks:", df["Marks"].min())

#Display statistical summary
print("\nStatistical Summary:")
print(df.describe())




