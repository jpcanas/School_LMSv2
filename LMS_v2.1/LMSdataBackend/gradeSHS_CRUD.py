import sqlite3
from absPath import resource_path


# Note: Two tables can be created with this query (sem1 and sem2)
def createShsGradeQuery(subjectCount: int, sem: int) -> str:
    createQuery = f"CREATE TABLE IF NOT EXISTS gradesSem{sem}Table (\nid INTEGER NOT NULL, \n"
    if sem == 1:
        for i in range(subjectCount):
            createQuery += f"subj{i + 1}Q1Sem{sem} INTEGER, subj{i + 1}Q2Sem{sem} INTEGER, subj{i + 1}FinalSem{sem} REAL,\n"

        createQuery += f"aveQ1Sem{sem} REAL, aveQ2Sem{sem} REAL, genAveSem{sem} REAL,\n"
    else:
        for i in range(subjectCount):
            createQuery += f"subj{i + 1}Q3Sem{sem} INTEGER, subj{i + 1}Q4Sem{sem} INTEGER, subj{i + 1}FinalSem{sem} REAL,\n"

        createQuery += f"aveQ3Sem{sem} REAL, aveQ4Sem{sem} REAL, genAveSem{sem} REAL,\n"

    createQuery = createQuery[:-2]  # remove last two characters( [/n] ,)
    createQuery += ")"

    return createQuery


# ---------- backend database setup for SHS grades  ---------------------------
def createGradesSHSData(mainDbName: str, subjectCount: int, sem: int):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    createQuery = createShsGradeQuery(subjectCount, sem)
    cur.execute(createQuery)
    conn.commit()
    conn.close()


def addOneGradesSHSData(mainDbName: str, gSHSId: int, subjectCount: int, sem: int):  # adding ONE shs grade Data
    shsGradeDataColumn = (subjectCount * 3) + 3
    default_gSHSData = [None] * shsGradeDataColumn
    gradesSHS_data = tuple(default_gSHSData)

    nullValues = "?," * shsGradeDataColumn
    insertQuery = f"INSERT INTO gradesSem{sem}Table VALUES (?,\n{nullValues[: -1]})"

    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute(insertQuery, (gSHSId,) + gradesSHS_data)
    gradeSHSId = cur.lastrowid
    conn.commit()
    conn.close()

    return gradeSHSId


def addManyGradesSHSData(mainDbName: str, profileData: list, subjectCount: int, sem: int):  # adding MANY shs grade Data
    shsGradeDataColumn = (subjectCount * 3) + 3
    gradesSHS_data = []
    for profile in profileData:
        defGradeSHSLearner = [profile[0]]
        for nullValue in range(shsGradeDataColumn):
            defGradeSHSLearner.append(None)

        gradesSHS_data.append(tuple(defGradeSHSLearner))

    nullValues = "?," * shsGradeDataColumn
    insertQuery = f"INSERT INTO gradesSem{sem}Table VALUES (?,\n{nullValues[: -1]})"

    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.executemany(insertQuery, gradesSHS_data)
    gradeSHSId = cur.lastrowid
    conn.commit()
    conn.close()

    return gradeSHSId


def viewGradesSHSData(mainDbName: str, sem, shsID=None):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute(f'''SELECT p.id,
                      CASE 
                           WHEN p.middle_name != '' 
                           THEN p.last_name || ", " || p.first_name || ' ' || SUBSTRING(p.middle_name, 1, 1) || '.'
                           ELSE p.last_name || ", " || p.first_name 
                    END AS fullname,
                           p.lrn,
                           p.sex,
                           p.age,
                           g.*
                      FROM gradesSem{sem}Table g
                 LEFT JOIN profileTable p 
                        ON p.id = g.id
                     WHERE p.id = COALESCE(?, p.id)
                       ''', (shsID,))

    fromGradesSHSData = cur.fetchall()
    conn.close()

    return fromGradesSHSData


def deleteGradesSHSData(mainDbName: str, gSHSId: int, sem: int):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute(f"DELETE FROM gradesSem{sem}Table WHERE id=?", (gSHSId,))
    conn.commit()
    conn.close()


