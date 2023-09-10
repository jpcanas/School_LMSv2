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
                       AND CASE
                      WHEN {sem} = 1 
                           THEN p.status IN ("Enrolled (1st and 2nd sem)", "Enrolled 1st Sem, No 2nd Sem", "Pending")
                           ELSE p.status IN ("Enrolled (1st and 2nd sem)", "No 1st Sem, Enrolled 2nd Sem", "Pending")
                           END;
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


def findAverage(upd_gSHS):
    grade_with_ave = []
    for i in range(0, (len(upd_gSHS)-3), 2):
        perSubjectGrade = upd_gSHS[i: i+2]

        for sub in perSubjectGrade:  # add per subject grade to list whether empty or not
            if sub:
                grade_with_ave.append(int(sub))
            else:
                grade_with_ave.append(sub)

        if all(perSubjectGrade):  # Check if all 2 items are not empty
            subjAverage = sum(map(int, perSubjectGrade)) / len(perSubjectGrade)  # compute for average
            grade_with_ave.append(subjAverage)
        else:
            grade_with_ave.append(None)

    grade_with_ave.append(upd_gSHS[-3])  # append table row count
    grade_with_ave.append(upd_gSHS[-2])  # append selected SHS ID
    grade_with_ave.append(upd_gSHS[-1])  # append semester
    return grade_with_ave


def finalShsGrade(gradesWithAve):
    gradesWithFinal = gradesWithAve
    subjectCount = gradesWithFinal[-3] - 1
    for i in range(3):
        allSubjPerQuarter = []
        for j in range(subjectCount):
            index = i + (j*3)
            allSubjPerQuarter.append(gradesWithFinal[index])

        if all(allSubjPerQuarter):
            quarterFinal = sum(allSubjPerQuarter) / len(allSubjPerQuarter)
            gradesWithFinal.insert(((subjectCount*3)+i), quarterFinal)
        else:
            gradesWithFinal.insert(((subjectCount*3)+i), None)

    return gradesWithFinal


def updateGradesSHSData(mainDbName: str, upd_gSHS):
    u = findAverage(upd_gSHS)
    gradesWithFinal = finalShsGrade(u)
    subjectCount = gradesWithFinal[-3] - 1
    sem = gradesWithFinal[-1]
    updateQuery = f"UPDATE gradesSem{sem}Table \nSET "

    if sem == 1:
        for i in range(subjectCount):
            updateQuery += f"subj{i + 1}Q1Sem{sem} = ?, subj{i + 1}Q2Sem{sem} = ?, subj{i + 1}FinalSem{sem} = ?,\n"

        updateQuery += f"aveQ1Sem{sem} = ?, aveQ2Sem{sem} = ?, genAveSem{sem}  = ?,\n"

    else:
        for i in range(subjectCount):
            updateQuery += f"subj{i + 1}Q3Sem{sem} = ?, subj{i + 1}Q4Sem{sem} = ?, subj{i + 1}FinalSem{sem} = ?,\n"

        updateQuery += f"aveQ3Sem{sem} = ?, aveQ4Sem{sem} = ?, genAveSem{sem} = ?,\n"

    updateQuery = updateQuery[:-2]  # remove last two characters( [/n] ,)
    updateQuery += "\nWHERE  oid = :oid"

    gradesWithFinal.pop(-3)   # remove subject count data
    gradesWithFinal.pop(-1)  # remove sem data

    gradesSHSToUpdate = tuple(gradesWithFinal)

    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute(updateQuery, gradesSHSToUpdate)  # database update
    conn.commit()
    conn.close()


