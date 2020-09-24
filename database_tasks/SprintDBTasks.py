from database_tasks import DatabaseInstance as db


def insert_sprint(data):
    cursor = db.mydb.cursor()
    query = "INSERT IGNORE INTO sprint (idSprint, descripcion, fechaFin) VALUES (%s, %s, %s)"

    cursor.execute(query, data)
    db.mydb.commit()
    cursor.close()