import pyodbc

connetti =r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Dario\Desktop\prova.accdb;UID="";PWD=""'
conn=pyodbc.connect(connetti)
cursor = conn.cursor()
cursor.execute('SELECT nome FROM generalita WHERE cognome = fumagalli')

for row in cursor.fetchall():
    print (row)

conn.close()
