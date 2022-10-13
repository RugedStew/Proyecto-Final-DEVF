import pandas as pd
import matplotlib
def printDf(df, paises, status):
    for aux in paises:
        # makes the plot and assign it to a variable
        df_open = df[aux].plot(title = status,xlabel='Fecha',ylabel=status,legend=aux)

        # changes the size of the graph
        fig = df_open.get_figure()
        fig.set_size_inches(13.5, 9)

def printOneDf(df, pais, status):
    df_open = df.plot(title = pais,xlabel='Fecha',ylabel=status,legend=pais)
    # changes the size of the graph
    fig = df_open.get_figure()
    fig.set_size_inches(13.5, 9)