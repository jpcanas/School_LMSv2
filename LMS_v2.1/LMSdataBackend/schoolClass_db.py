import sqlite3
from absPath import resource_path


# ---------- backend database setup for school data ---------------------------
def createSchoolData():
    conn = sqlite3.connect(resource_path("data\\schoolData.db"))
    cur = conn.cursor()
    cur.execute("""
                    CREATE TABLE IF NOT EXISTS schoolTable (
                    id INTEGER PRIMARY KEY,
                    school_name TEXT, school_id TEXT, 
                    district TEXT, division TEXT,
                    region TEXT )
    			    """)
    conn.commit()
    conn.close()


def addSchoolData(school_data: tuple):
    conn = sqlite3.connect(resource_path("data\\schoolData.db"))
    cur = conn.cursor()
    # index for tuple parameter
    # [0]school_name, [1]school_id, [2]district, [3]division, [4]region
    cur.execute("INSERT INTO schoolTable VALUES (NULL, ?,?,?,?,?)",
                (school_data[0], school_data[1], school_data[2], school_data[3], school_data[4]))
    conn.commit()
    conn.close()


def viewSchoolData():
    conn = sqlite3.connect(resource_path("data\\schoolData.db"))
    cur = conn.cursor()

    cur.execute("SELECT * FROM schoolTable")
    fromSchoolData = cur.fetchall()
    conn.close()

    return fromSchoolData


# ---------- backend database setup for class data ---------------------------
def createClassData():
    conn = sqlite3.connect(resource_path("data\\classData.db"))
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS classTable (
                id INTEGER PRIMARY KEY,
                department TEXT, school_year TEXT, 
                school_head TEXT, grade TEXT,
                section TEXT, adviser TEXT, 
			    strand TEXT, sem TEXT )
			    """)
    conn.commit()
    conn.close()


def addClassData(class_data: tuple):
    conn = sqlite3.connect(resource_path("data\\classData.db"))
    cur = conn.cursor()
    # ------------ create placeholder entry for table -------------
    # index for tuple parameter
    # [0]department, [1]school_year, [2]school_head, [3]grade, [4]section, [5]adviser,
    # [6]strand, [7]sem
    cur.execute("INSERT INTO classTable VALUES (NULL, ?,?,?,?,?,?,?,?)",
                (class_data[0], class_data[1], class_data[2], class_data[3],
                 class_data[4], class_data[5], class_data[6], class_data[7]))
    conn.commit()
    conn.close()


def updateClassData(schoolHead, classAdv, semester, idNum):
    conn = sqlite3.connect(resource_path("data\\classData.db"))
    cur = conn.cursor()

    cur.execute("""UPDATE classTable SET
					school_head = :sh, 
					adviser = :adv,
					sem = :s
				    WHERE oid = :oid""",
                {
                    'sh': schoolHead, 'adv': classAdv, 's': semester, 'oid': idNum
                })
    conn.commit()
    conn.close()


def viewClassData():
    conn = sqlite3.connect("data\\classData.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM classTable")
    fromClassData = cur.fetchall()
    conn.close()

    return fromClassData


def deleteClassRec(classId):
    conn = sqlite3.connect("data\\classData.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM classTable WHERE id=?", (classId,))
    conn.commit()
    conn.close()


