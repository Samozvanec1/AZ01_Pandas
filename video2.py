import pandas as pd

df = pd.read_csv("3.csv")

df["test"] = [new for new in range(143)]

print(df)

#df.drop('test', axis=1, inplace=True) # удаление столбца, axis=1 - столбец, axis=0 - строка, inplace=True - удаление в текущем датафрейме

df.drop(142, axis=0, inplace=True) # удаление строки, axis=1 - столбец, axis=0 - строка, inplace=True - удаление в текущем датафрейме

print(df)