import pandas as pd

df = pd.read_csv("World-happiness-report-2024 2.csv")
#print(df)
#print(df.head(6))
#print(df.tail(6))
#print(df.info())
#print(df.describe()) # описательная статистика (минимум, максимум, среднее, медиана, межквартильный размах)
#print(df[["Country name", "Regional indicator", "Ladder score"]])
#print(df.loc[57]) # вывод строки с индексом 57
#print(df.loc[56,"Healthy life expectancy"]) # вывод значения в строке с индексом 56 и столбцом Healthy life expectancy (выборка)
#print(df[df["Healthy life expectancy"] > 0.7]) # вывод строк с уровнем здоровья больше 0.7 (выборка)
