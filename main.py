import pandas as pd

# Загрузка данных из CSV-файла в DataFrame
df = pd.read_csv('test_data.csv')

# Преобразование затрат (Spend) из строкового формата в числовой
# df['Revenue_ad1d'] = df['Revenue_ad1d'].str.replace(',', '').astype(float)

# Преобразование столбцов Revenue_in_app1d, Revenue_in_app7d и Revenue_in_app30d из строкового формата в числовой (еще (Spend))
revenue_columns = ['Spend','Revenue_in_app1d', 'Revenue_in_app7d', 'Revenue_in_app30d', 'Revenue_ad1d']
for col in revenue_columns:
    df[col] = df[col].str.replace(',', '').str.replace('"', '').astype(float)

# # Расчет CPI (Cost Per Install) для каждой кампании
# df['CPI'] = df['Spend'] / df['Installs']
# print(df['CPI'].sort_values(ascending=True).head(3))

# # Расчет CTR (Click-through Rate) для каждой кампании
# df['CTR'] = df['Clicks'] / df['Impressions'] * 100
# print(df['CTR'].sort_values(ascending=False).head(3))

# # Расчет CPC (Cost Per Click) для каждой кампании
# df['CPC'] = df['Spend'] / df['Clicks']
# print(df['CPC'].sort_values(ascending=True).head(3))

# # Расчет CR (Conversion Rate) - число установок к числу кликов
# df['CR'] = df['Installs'] / df['Clicks']  * 100
# print(df['CR'].sort_values(ascending=False).head(3))

# # Расчет CR (Conversion Rate) - число регистраций к числу кликов
# df['CR_R'] = df['Registrations'] / df['Clicks']  * 100
# print(df['CR_R'].sort_values(ascending=False).head(3))

# ROI (Return on Investment) Отношение прибыли к затратам на рекламу на первый день их жизни
df['ROI'] = df['Revenue_ad1d'] / df['Spend']  * 100
print(df['ROI'].sort_values(ascending=False).head(3))

# # ROI (Return on Investment) Отношение прибыли к затратам на рекламу на первый день их жизни
# df['ROI_1'] = df['Revenue_in_app1d'] / df['Spend']  * 100
# print(df['ROI_1'].sort_values(ascending=False).head(3))

# # ARPU (Average Revenue Per User) - Средняя выручка с одного пользователя на первый день
# df['ARPU'] = df['Revenue_ad1d'] / df['Payers1d']  * 100
# print(df['ARPU'].sort_values(ascending=False).head(3))

# # ARPU (Average Revenue Per User) - Средняя выручка с одного пользователя на первый день
# df['ARPU_1'] = df['Revenue_in_app1d'] / df['Payers1d']  * 100
# print(df['ARPU_1'].sort_values(ascending=False).head(3))

# # Cost per Conversion - Средняя стоимость привлечения одной установки
# df['Cost_per_Conversion'] = df['Spend'] / df['Installs']
# print(df['Cost_per_Conversion'].sort_values(ascending=True).head(3))

# # Cost per Conversion - Средняя стоимость привлечения одной регистрации
# df['Cost_per_Conversion_r'] = df['Spend'] / df['Registrations']
# print(df['Cost_per_Conversion_r'].sort_values(ascending=True).head(3))


# Группировка данных по геопозиции (Geo) и нахождение среднего CPI для каждой геопозиции
# geo_cpi = df.groupby('Geo')['CPI'].mean().sort_values(ascending=False)

# # Группировка данных по медиабайеру (Buyer) и нахождение средней выручки на 30-й день для каждого медиабайера
# buyer_revenue = df.groupby('Buyer')['Revenue_in_app30d'].mean().sort_values(ascending=False)

# # Группировка данных по кампании (Campaign_id) и нахождение минимальной выручки на 30-й день для каждой кампании
# campaign_min_revenue = df.groupby('Campaign_id')['Revenue_in_app30d'].min().sort_values()

# # Вывод результатов
# print("Геопозиции с наибольшим CPI:")
# print(geo_cpi.head(3))S

# print("\nЛучшие медиабайеры по средней выручке на 30-й день:")
# print(buyer_revenue.head(3))

# print("\nКампании с наименьшим CPI:")
# print(campaign_min_revenue.head(3))