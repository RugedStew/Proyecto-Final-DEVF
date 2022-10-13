import pandas as pd
import sqlite3

df = pd.read_csv('C:\\Users\\ramss\\Desktop\\ProyectoDEVF\\app\\database\\dfDeaths.csv', delimiter=',') # también se puede usar la función read_table

conn = sqlite3.connect('decesos_database')
c = conn.cursor()
df.to_sql('deaths', conn, if_exists='replace', index = False)
c.execute('''  
SELECT * FROM deaths
          ''')
for row in c.fetchall():
    print (row)