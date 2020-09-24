from database_tasks import DatabaseInstance as db


def insert_information(data, sprint_id):

    cursor = db.mydb.cursor()
    query = "INSERT IGNORE INTO informacion (idInfo, idAnalista, habilitadores, historias, Tareas, bug, " \
            "estadoNew, estadoActive, estadoClose, estadoPendiente, puntosDeHistoria, pullRequests, comits, " \
            "deudaTecnica, codeSmell, idSprint) VALUES (null, %(analyst_id)s, %(enabler_type)s, " \
            "%(user_story_type)s, %(no_scored)s, %(bug_type)s, %(new_state)s, %(active_state)s, %(closed_state)s, " \
            "%(impediment_state)s, %(engaged_to)s, %(pull_data)s, %(commit_data)s, %(technical_debt)s, " \
            "%(code_smells)s, "
    sprint_id_query = "%(sprint_id)s)" % {"sprint_id": sprint_id}

    final_query = query + sprint_id_query

    cursor.executemany(final_query, data)
    db.mydb.commit()
    cursor.close()