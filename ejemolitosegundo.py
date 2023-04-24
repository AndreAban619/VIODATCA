"""import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd=" ", db="viodatcadb")

cursor = db.cursor()

cursor.execute("SELECT * FROM viodatcadb")

for fila in cursor.fetchall():
    print(fila)

db.close()"""


import sqlite3

# Crear una conexión a la base de datos
conn = sqlite3.connect('ViodatcaCitas.db')

# Crear un objeto cursor
c = conn.cursor()

# Crear una tabla
"""c.execute('''CREATE TABLE informacion (
    author VARCHAR(255),
    cita TEXT,
    seconds INT
)''')"""

"""
c.execute('SELECT * FROM informacion')
results = c.fetchall()
for row in results:
    print(row)

# Guardar los cambios
conn.commit()
c.execute('SELECT * FROM informacion')
results = c.fetchall()
for row in results:
    print(row)
    
   c.execute('''INSERT INTO informacion (author, cita, seconds)
VALUES ('Marie Curie', 'Nada en la vida debe ser temido, solamente comprendido. Ahora es el momento de comprender más, para que temamos menos.', 9),
('Maquiavelo', 'No hay nada más difícil de llevar a cabo, ni más peligroso de manejar, ni más incierto en su éxito, que liderar la introducción de un nuevo orden de cosas.', 12)''')
"""


# Cerrar la conexión
conn.close()
