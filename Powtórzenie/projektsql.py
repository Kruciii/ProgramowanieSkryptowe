import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=10.44.140.92, 21433"
                      "Database=db223435;"
                      "Trusted_Connection=yes;"
                      "UID=st223435;"
                      "PWD=p223435;")

cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Hotele')

for row in cursor:
    print('row = %r' % (row,))