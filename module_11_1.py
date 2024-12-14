# Домашнее задание по теме "Обзор сторонних библиотек Python"
import numpy as np
import pandas as pd
import requests

index = pd.date_range("12/15/2024", periods=8) # создаёт индекс в библиотеке Pandas,
# который представляет собой диапазон дат с 15 по 23 декабря 2024
print(index)
s = pd.Series((12,34, 45, 56, 67), index=["a", "b", "c", "d", "e"]) # создаем одномерный массив
print(s)
df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=["Москва", "Омск", "Иркутск"])
print(df)
print('________')

BASE_URL = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 56.0184,  # широта Красноярска
    "longitude": 92.8672,  # долгота Красноярска
    "daily": "temperature_2m_min,temperature_2m_max,precipitation_sum,sunrise,sunset",
    # минимальная и максимальная температура, сумма осадков, восход, закат солнца
    "timezone": "Asia/Krasnoyarsk"  # временная зона для Красноярска
}
response = requests.get(BASE_URL, params = params)
# Это GET-запрос. Он нужен для получения данных с сервера.
if response.status_code == 200:
   #статус 200 (OK) значит, что запрос успешно выполнен,
    data = response.json()
    #Метод response.json() в Python возвращает JSON-объект полученного результата.
    # Поскольку индекс 0 представляет собой данные на текущий день
    # индекс 1 будет представлять данные на завтра
    sunrise_ = data['daily']['sunrise'][1]
    sunset_ = data['daily']['sunset'][1]
    tomorrow_temp_min = data['daily']['temperature_2m_min'][1]
    tomorrow_temp_max = data['daily']['temperature_2m_max'][1]
    tomorrow_precipitation = data['daily']['precipitation_sum'][1]

    print(f"Прогноз погоды в Красноярске на завтра:")
    print(f"Минимальная температура: {tomorrow_temp_min}°C")
    print(f"Максимальная температура: {tomorrow_temp_max}°C")
    print(f"Ожидаемое количество осадков: {tomorrow_precipitation} мм")
    print(f'Восход солнца: {sunrise_}')
    print(f'Закат: {sunset_}')

