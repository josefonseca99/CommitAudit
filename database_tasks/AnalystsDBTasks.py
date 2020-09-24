from database_tasks import DatabaseInstance as DBInst


def get_analysts_ids(analysts):
    cursor = DBInst.mydb.cursor()
    query = "SELECT idAnalista FROM analistas WHERE nombre = %s"

    for i in range(len(analysts)):

        cursor.execute(query, (analysts[i]["analyst_name"],))
        analyst_id = cursor.fetchone()

        if analyst_id:
            analysts[i]["analyst_id"] = analyst_id[0]
        else:
            analysts[i]["analyst_id"] = insert_analyst(analysts[i]["analyst_name"])

    cursor.close()
    return analysts


def insert_analyst(analyst):
    cursor = DBInst.mydb.cursor()
    query = "INSERT INTO analistas (idAnalista, nombre) VALUES (null, %s)"

    cursor.execute(query, (analyst,))
    DBInst.mydb.commit()

    last_id = cursor.lastrowid
    cursor.close()
    return last_id
