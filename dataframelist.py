import pandas as pd

#Create a list
data = [
    ["Mahek", 21, 98],
    ["Riya", 20, 78],
    ["Amit", 22, 92]
    ]
#Create DataFrame
df = pd.DataFrame(data, columns=["Name", "Age", "Marks"])

#Attributes
print("Shape:")
print(df.shape)

print("/nColumns:")
print(df.columns)

print("\nIndex:")
print(df.head())

print("\nStatistical Summary:")
print(df.describe())

print("\nDataFrame Information:")
df.info()
