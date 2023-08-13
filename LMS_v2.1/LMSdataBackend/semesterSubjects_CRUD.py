import sqlite3
from absPath import resource_path


# ---------- backend database setup for semester subjects ---------------------------
def createSemSubjects(mainDbName: str):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute("""
                    CREATE TABLE IF NOT EXISTS semSubjectsTable (
                    semSubjID INTEGER PRIMARY KEY,     
                    shsSubjectCat TEXT,
                    shsSubjectName TEXT,    
                    semester INTEGER)
    			""")
    conn.commit()
    conn.close()


def addSemSubjects(mainDbName: str, semSubject: list):  # execute to many
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.executemany('''INSERT INTO semSubjectsTable 
                               (shsSubjectCat,
                                shsSubjectName,
                                semester)
                        VALUES (?, ?, ?)''',
                    semSubject)
    conn.commit()
    conn.close()


def viewSemSubjects(mainDbName: str, sem=None):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute("""
                    SELECT semSubjID,
                           shsSubjectCat,
                           shsSubjectName,
                           semester
                      FROM semSubjectsTable
                     WHERE semester = COALESCE(?, semester)
        		""", (sem,))
    fromSemSubjects = cur.fetchall()
    conn.close()

    return fromSemSubjects
