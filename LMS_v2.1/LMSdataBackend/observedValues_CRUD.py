import sqlite3
from absPath import resource_path


# ---------- backend database setup for learner's observed values ---------------------------
def createObValData(mainDbName: str):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute("""
                        CREATE TABLE IF NOT EXISTS ObValTable (
                        id INTEGER NOT NULL,     
                        val_1AQ1 INTEGER,   val_1AQ2 INTEGER,   val_1AQ3 INTEGER,   val_1AQ4 INTEGER,
                        val_1BQ1 INTEGER,   val_1BQ2 INTEGER,   val_1BQ3 INTEGER,   val_1BQ4 INTEGER,
                        val_2AQ1 INTEGER,   val_2AQ2 INTEGER,   val_2AQ3 INTEGER,   val_2AQ4 INTEGER,
                        val_2BQ1 INTEGER,   val_2BQ2 INTEGER,   val_2BQ3 INTEGER,   val_2BQ4 INTEGER,
                        val_3AQ1 INTEGER,   val_3AQ2 INTEGER,   val_3AQ3 INTEGER,   val_3AQ4 INTEGER,
                        val_4AQ1 INTEGER,   val_4AQ2 INTEGER,   val_4AQ3 INTEGER,   val_4AQ4 INTEGER,
                        val_4BQ1 INTEGER,   val_4BQ2 INTEGER,   val_4BQ3 INTEGER,   val_4BQ4 INTEGER  
                        )
        			""")
    conn.commit()
    conn.close()


def addObValData(mainDbName: str, ObValId: int, ObVal_data=None):
    if ObVal_data is None:
        default_obValData = [None] * 28
        ObVal_data = tuple(default_obValData)

    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute("INSERT INTO ObValTable VALUES (?,"
                "?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,"  # 16 items
                "?,?,?,?,?,?,?,?,?,?,?,?)",  # 12 items
                (ObValId,) + ObVal_data)
    obValId = cur.lastrowid
    conn.commit()
    conn.close()

    return obValId


def viewObValData(mainDbName, ovId=None):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute('''SELECT p.id,
                     CASE 
                          WHEN p.middle_name != '' 
                          THEN p.last_name || ", " || p.first_name || ' ' || SUBSTRING(p.middle_name, 1, 1) || '.'
                          ELSE p.last_name || ", " || p.first_name 
                  END AS  fullname,
                          p.lrn,
                          p.sex,
                          p.age,
                          ov.val_1AQ1,   ov.val_1AQ2,   ov.val_1AQ3,   ov.val_1AQ4,
                          ov.val_1BQ1,   ov.val_1BQ2,   ov.val_1BQ3,   ov.val_1BQ4,
                          ov.val_2AQ1,   ov.val_2AQ2,   ov.val_2AQ3,   ov.val_2AQ4,
                          ov.val_2BQ1,   ov.val_2BQ2,   ov.val_2BQ3,   ov.val_2BQ4,
                          ov.val_3AQ1,   ov.val_3AQ2,   ov.val_3AQ3,   ov.val_3AQ4,
                          ov.val_4AQ1,   ov.val_4AQ2,   ov.val_4AQ3,   ov.val_4AQ4,
                          ov.val_4BQ1,   ov.val_4BQ2,   ov.val_4BQ3,   ov.val_4BQ4 
                    FROM  ObValTable ov
               LEFT JOIN  profileTable p 
                      ON  p.id = ov.id
                   WHERE  p.id = COALESCE(?, p.id)
                   ''', (ovId,))

    fromObValData = cur.fetchall()
    conn.close()

    return fromObValData


def updateObValData(mainDbName: str, ObValData: tuple):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute("""UPDATE  ObValTable 
                      SET  val_1AQ1 = ?,   val_1AQ2 = ?,   val_1AQ3 = ?,   val_1AQ4 = ?,
                           val_1BQ1 = ?,   val_1BQ2 = ?,   val_1BQ3 = ?,   val_1BQ4 = ?,
                           val_2AQ1 = ?,   val_2AQ2 = ?,   val_2AQ3 = ?,   val_2AQ4 = ?,
                           val_2BQ1 = ?,   val_2BQ2 = ?,   val_2BQ3 = ?,   val_2BQ4 = ?,
                           val_3AQ1 = ?,   val_3AQ2 = ?,   val_3AQ3 = ?,   val_3AQ4 = ?,
                           val_4AQ1 = ?,   val_4AQ2 = ?,   val_4AQ3 = ?,   val_4AQ4 = ?,
                           val_4BQ1 = ?,   val_4BQ2 = ?,   val_4BQ3 = ?,   val_4BQ4 = ? 
                    WHERE  oid = :oid""", ObValData)
    conn.commit()
    conn.close()


def deleteObValData(mainDbName: str, ObValId):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute("DELETE FROM ObValTable WHERE id=?", (ObValId,))
    conn.commit()
    conn.close()