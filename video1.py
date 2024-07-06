import pandas as pd

data = {
    "name":["Alice","Bob", "Roma", "Anna"],
    "age": [23,45,17,24],
    "city":["New York", "Los angeles", "Chicago", "Lipetsk"]
}

df = pd.DataFrame(data) # создание датафрейма из словаря data с названиями столбцов
df.to_csv("output.csv", index=False)
print(df)