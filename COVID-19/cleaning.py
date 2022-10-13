import pandas as pd

def clean(Dict, mes):
    Dict['Date'] = mes
    Dict.pop('date',None)
    df = pd.DataFrame(Dict)
    df = df.drop(11)
    df.Date = pd.to_datetime(df.Date)
    df = df.set_index('Date')
    return df
def cleanDf(df):
    df.drop(df.columns[0:7],axis=1, inplace=True)
    df.drop('Status',axis=1, inplace=True)
    df.Date = pd.to_datetime(df.Date)
    df = df.set_index('Date')
    return df