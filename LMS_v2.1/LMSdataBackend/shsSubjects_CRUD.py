import sqlite3
from absPath import resource_path


# database already created
def viewSubjectsShs(subjID=None, subjCat=None, subjSource=None):
    try:
        conn = sqlite3.connect(resource_path("data\\shsSubjectsData.db"))
        cur = conn.cursor()
        cur.execute('''SELECT shsSubject_id,
                              shsSubject_cat,
                              shsSubject_name,
                              shsSubject_source
                         FROM shsSubjectsTable 
                        WHERE shsSubject_id = COALESCE(?, shsSubject_id)
                          AND shsSubject_cat = COALESCE(?, shsSubject_cat)
                          AND shsSubject_source = COALESCE(?, shsSubject_source)
                   ''', (subjID, subjCat, subjSource))
        fromShsSubjects = cur.fetchall()
        conn.commit()
        conn.close()
        return fromShsSubjects

    except Exception as err:
        print(err)


def viewSubjNameAndCat():
    try:
        conn = sqlite3.connect(resource_path("data\\shsSubjectsData.db"))
        cur = conn.cursor()
        cur.execute('''SELECT shsSubject_cat,
                              shsSubject_name
                         FROM shsSubjectsTable  
                   ''')
        fromSubjNameCat = cur.fetchall()
        conn.commit()
        conn.close()
        return fromSubjNameCat

    except Exception as err:
        print(err)


def addSubjectsShs(customSubject: tuple):
    conn = sqlite3.connect(resource_path("data\\shsSubjectsData.db"))
    cur = conn.cursor()
    cur.execute('''INSERT INTO shsSubjectsTable 
                               (shsSubject_cat,
                                shsSubject_name,
                                shsSubject_source)
                        VALUES (?, ?, ?)''',
                customSubject)
    subjectID = cur.lastrowid
    conn.commit()
    conn.close()

    return subjectID
