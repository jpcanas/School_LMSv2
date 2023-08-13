import sqlite3
from absPath import resource_path


# ---------- backend database setup for JHS grades  ---------------------------
def createGradesJHSData(mainDbName: str):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute("""
                    CREATE TABLE IF NOT EXISTS gradesJHSTable (
                    id INTEGER NOT NULL,     
                    fil1 INTEGER,     fil2 INTEGER,     fil3 INTEGER,     fil4 INTEGER,     filAve REAL,
                    eng1 INTEGER,     eng2 INTEGER,     eng3 INTEGER,     eng4 INTEGER,     engAve REAL,
                    math1 INTEGER,    math2 INTEGER,    math3 INTEGER,    math4 INTEGER,    mathAve REAL,
                    sci1 INTEGER,     sci2 INTEGER,     sci3 INTEGER,     sci4 INTEGER,     sciAve REAL,
                    ap1 INTEGER,      ap2 INTEGER,      ap3 INTEGER,      ap4 INTEGER,      apAve REAL,
                    esp1 INTEGER,     esp2 INTEGER,     esp3 INTEGER,     esp4 INTEGER,     espAve REAL,
                    tle1 INTEGER,     tle2 INTEGER,     tle3 INTEGER,     tle4 INTEGER,     tleAve REAL,
                    mapeh1 INTEGER,   mapeh2 INTEGER,   mapeh3 INTEGER,   mapeh4 INTEGER,   mapehAve REAL,
                    music1 INTEGER,   music2 INTEGER,   music3 INTEGER,   music4 INTEGER,   musicAve REAL,
                    arts1 INTEGER,    arts2 INTEGER,    arts3 INTEGER,    arts4 INTEGER,    artsAve REAL,
                    pe1 INTEGER,      pe2 INTEGER,      pe3 INTEGER,      pe4 INTEGER,      peAve REAL,
                    health1 INTEGER,  health2 INTEGER,  health3 INTEGER,  health4 INTEGER,  healthAve REAL,      
                    aveQ1 REAL,       aveQ2 REAL,       aveQ3 REAL,       aveQ4 REAL,       genAve REAL         
                    )
    			""")
    conn.commit()
    conn.close()


def addGradesJHSData(mainDbName: str, gJHSId: int, gradesJHS_data=None):
    if gradesJHS_data is None:
        default_gJHSData = [None] * 65
        gradesJHS_data = tuple(default_gJHSData)

    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute('''INSERT INTO gradesJHSTable VALUES (?,
                ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,  
                ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',  # 65 items
                (gJHSId,) + gradesJHS_data)
    gradeJHSId = cur.lastrowid
    conn.commit()
    conn.close()

    return gradeJHSId


# ======================================= updating grades ======================================
def MAPEHGrade(upd_gJHS):
    grades_with_Mapeh = list(upd_gJHS)
    mapehAll = grades_with_Mapeh[28:44]
    for i in range(4):  # music arts pe health
        mapehQuarter = []
        for j in range(4):  # Q1, Q2, Q3, Q4
            index = i + (j * 4)
            mapehQuarter.append(mapehAll[index])

        if all(mapehQuarter):
            quarterGrade = sum(map(int, mapehQuarter)) / len(mapehQuarter)
            grades_with_Mapeh.insert((28 + i), quarterGrade)
        else:
            grades_with_Mapeh.insert((28 + i), None)

    return grades_with_Mapeh


def findAverage(gradesWithMapeh):
    grade_with_ave = []
    for i in range(0, len(gradesWithMapeh) - 1, 4):
        perSubjectGrade = gradesWithMapeh[i:i + 4]

        for sub in perSubjectGrade:  # add per subject grade to list weather empty or not
            if sub:
                grade_with_ave.append(int(sub))
            else:
                grade_with_ave.append(sub)

        if all(perSubjectGrade):  # Check if all 4 items are not empty
            subjAverage = sum(map(int, perSubjectGrade)) / len(perSubjectGrade)  # compute for average
            grade_with_ave.append(subjAverage)
        else:
            grade_with_ave.append(None)

    grade_with_ave.append(gradesWithMapeh[-1])
    return grade_with_ave


def finalJhsGrade(gradesWithAve):
    gradesWithFinal = gradesWithAve
    for i in range(5):  # from Q1 to final
        allSubjPerQuarter = []
        for j in range(8):  # subjects from Fil to MAPEH
            index = i + (j*5)
            allSubjPerQuarter.append(gradesWithFinal[index])

        if all(allSubjPerQuarter):
            quarterFinal = sum(allSubjPerQuarter) / len(allSubjPerQuarter)
            gradesWithFinal.insert((60+i), quarterFinal)
        else:
            gradesWithFinal.insert((60+i), None)

    return gradesWithFinal


def updateGradesJHSData(mainDbName: str, upd_gJHS: tuple):
    m = MAPEHGrade(upd_gJHS)
    a = findAverage(m)
    upd_gJHS = finalJhsGrade(a)
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute("""UPDATE  gradesJHSTable 
                      SET  fil1 = ?,     fil2 = ?,     fil3 = ?,     fil4 = ?,     filAve = ?,
                           eng1 = ?,     eng2 = ?,     eng3 = ?,     eng4 = ?,     engAve = ?,
                           math1 = ?,    math2 = ?,    math3 = ?,    math4 = ?,    mathAve = ?,
                           sci1 = ?,     sci2 = ?,     sci3 = ?,     sci4 = ?,     sciAve = ?,
                           ap1 = ?,      ap2 = ?,      ap3 = ?,      ap4 = ?,      apAve = ?,
                           esp1 = ?,     esp2 = ?,     esp3 = ?,     esp4 = ?,     espAve = ?,
                           tle1 = ?,     tle2 = ?,     tle3 = ?,     tle4 = ?,     tleAve = ?,
                           mapeh1 = ?,   mapeh2 = ?,   mapeh3 = ?,   mapeh4 = ?,   mapehAve = ?,
                           music1 = ?,   music2 = ?,   music3 = ?,   music4 = ?,   musicAve = ?,
                           arts1 = ?,    arts2 = ?,    arts3 = ?,    arts4 = ?,    artsAve = ?,
                           pe1= ?,       pe2 = ?,      pe3 = ?,      pe4 = ?,      peAve = ?,
                           health1 = ?,  health2 = ?,  health3 = ?,  health4 = ?,  healthAve = ?,
                           aveQ1 = ?,    aveQ2 = ?,    aveQ3 = ?,    aveQ4 = ?,    genAve = ?  
                    WHERE  oid = :oid""", upd_gJHS)
    conn.commit()
    conn.close()


def viewGradesJHSData(mainDbName, jhsId=None):
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
                          g.*
                    FROM  gradesJHSTable g
               LEFT JOIN  profileTable p 
                      ON  p.id = g.id
                   WHERE  p.id = COALESCE(?, p.id)
                   ''', (jhsId,))

    fromGradesJHSData = cur.fetchall()
    conn.close()

    return fromGradesJHSData


def deleteGradesJHSData(mainDbName: str, gradeJHSId):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute("DELETE FROM gradesJHSTable WHERE id=?", (gradeJHSId,))
    conn.commit()
    conn.close()

