#Importando las librerias necesarias
import pandas as pd
import matplotlib
from consultaApi import consultaMensual, consultaDiaria
from cleaning import clean, cleanDf
from graphics import printDf, printOneDf
paises = ['France']
fechas = [['2020-03-31T00:00:00Z','2020-03-31T23:59:59Z'],['2020-04-30T00:00:00Z','2020-04-30T23:59:59Z'],['2020-05-31T00:00:00Z','2020-05-31T23:59:59Z'],
          ['2020-06-30T00:00:00Z','2020-06-30T23:59:59Z'],['2020-07-31T00:00:00Z','2020-07-31T23:59:59Z'],['2020-08-31T00:00:00Z','2020-08-31T23:59:59Z'],
          ['2020-09-30T00:00:00Z','2020-09-30T23:59:59Z'],['2020-10-31T00:00:00Z','2020-10-31T23:59:59Z'],['2020-11-30T00:00:00Z','2020-11-30T23:59:59Z'],
          ['2020-12-31T00:00:00Z','2020-12-31T23:59:59Z'],['2021-01-31T00:00:00Z','2021-01-31T23:59:59Z'],['2021-02-28T00:00:00Z','2021-02-28T23:59:Z']]
mes = ['03-2020','04-2020','05-2020','06-2020','07-2020','08-2020','09-2020','10-2020','11-2020','12-2020','01-2021','02-2021']  

aux = consultaMensual(paises, fechas, 'deaths')
df = clean(aux, mes)
printDf(df, paises, 'deaths')

dfBrazil = consultaDiaria('Brazil','confirmed','2020-10-01T00:00:00Z','2022-05-31T00:00:00Z')

dfBrazil = cleanDf(dfBrazil)

printOneDf(dfBrazil,'Brazil','confirmed')
