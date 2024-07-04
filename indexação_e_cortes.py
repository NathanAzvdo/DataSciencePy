import requests
import pandas as pd
from urllib.request import urlretrieve
import matplotlib.pyplot as plt


url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

urlretrieve(url, 'covid_cases.csv')

DF_covid = pd.read_csv('covid_cases.csv')
# print(DF_covid['Lat']) exibe apenas a coluna Lat
DF_covid.drop(['Lat', 'Long'], axis=1, inplace=True)##Remove o Lat e Long, o inplace ele faz com que o DF original já seja atualizado dessa exclusão
DF_country  = DF_covid.groupby('Country/Region').sum()##Agrupa pelo pais e soma número de casos de todas as linhas daquele pais

Dates = DF_country.loc['Brazil'].index
cases = DF_country.loc['Brazil'].values

print(plt.bar(Dates, cases))