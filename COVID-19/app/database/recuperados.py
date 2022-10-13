import pandas as pd
import sqlite3

df = pd.read_csv('C:\\Users\\ramss\\Desktop\\ProyectoDEVF\\app\\database\\dfRecovered.csv', delimiter=',') # también se puede usar la función read_table

conn = sqlite3.connect('recuperados_database')
c = conn.cursor()
df.to_sql('recovered', conn, if_exists='replace', index = False)
c.execute('''  
SELECT * FROM recovered
          ''')
for row in c.fetchall():
    print (row)