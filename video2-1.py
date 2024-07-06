import pandas as pd

df = pd.read_csv("light.csv") # чтение csv файла в датафрейм df. датафрейм это таблица с данными по строкам и столбцам
# print(df["цена"]) # вывод столбца цены

# df.fillna(5000, inplace=True) # замена пропусков
# print(df["цена"])

# df.dropna(inplace=True)# удаление пропусков
# print(df["цена"])
df["test"] = [new for new in range(48)] # добавление столбца с ценой

# group = df.groupby("цена")["test"].mean() # группировка по цене и средней цены
