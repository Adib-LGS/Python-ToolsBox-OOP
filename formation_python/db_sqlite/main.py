import sqlite3


try:
    conexion = sqlite3.connect("dbsql2.db")
    cursor = conexion.cursor()
    req = cursor.execute('SELECT * FROM users')

    for row in req.fetchall():
        print(row)

except Exception as e:
    print('[ERROR]', e)
    conexion.rollback()

finally:
    conexion.close()




