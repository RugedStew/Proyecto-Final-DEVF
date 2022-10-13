#Importando las librerias necesarias
import json
import pandas as pd
import requests
import time

def consultaMensual(paises, fechas, status):
    consultados = {}
    for aux in paises:
        consultadosF = []
        for aux2 in fechas:
            #Consulta para el historial de casos de covid 19 y algunos detalles, los resultados son mostrados por el pais solicitado
            country = aux #Ingrese el país a buscar
            date_i = aux2[0]
            date_f = aux2[1]
            covid_url = f"https://api.covid19api.com/country/{country}/status/{status}?from={date_i}&to={date_f}"
            response = requests.get(covid_url)
            #Obtenemos las estadísticas de COVID 19 por el país y algunos datos extra
            data = response.json()
            df1 = pd.DataFrame(data)
            consultadosF.append(df1.Cases.sum())
            consultados[aux] = consultadosF
            time.sleep(0.5)
    return consultados

def consultaDiaria(country, status, date_i, date_f):
    covid_url = f"https://api.covid19api.com/country/{country}/status/{status}?from={date_i}&to={date_f}"
    response = requests.get(covid_url)
    data = response.json()
    return pd.DataFrame(data)