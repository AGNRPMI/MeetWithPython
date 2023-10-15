# Данный код работает в https://colab.research.google.com

# # Задача 40: Работать с файлом california_housing_train.csv,
# который находится в папке sample_data. Определить среднюю
# стоимость дома, где кол-во людей от 0 до 500 (population).

# # Задача 42: Узнать какая максимальная households в
# зоне минимального значения population.
import pandas as pd
df = pd.read_csv('/content/sample_data/california_housing_train.csv')


# Задача 40:
print("Средняя цена дома:")
print(df['median_house_value'].mean())

print("Средняя цена дома при популяции менее 500:")
df[df['population']<501]['median_house_value'].mean()

# Задача 42:
print("минимальная популяция:")
min_pop =df['population'].min()
print(min_pop)
print("максимум домовладений:")
min_house =df['households'].max()
print(min_house)

print("максимальная households в зоне минимального значения population:")
#df[['population', 'households']]
#house=df[df['population'] <= min_pop]['households']
house=df[df['population']<=min_pop]['households'].max()
print("минимальная популяция:", min_pop)
print("Количество домовладений:",house)

#print("Количество домовладений:",df[df['population'] <= min_pop]['households'])

#df[df['population'] <=min_pop]['population'],['households']

