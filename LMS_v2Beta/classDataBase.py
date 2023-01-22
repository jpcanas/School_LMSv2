import sqlite3

# ---------- backend database for LMS class data ---------------------------

def classData():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\class.db")
	cur = conn.cursor()
	cur.execute("""CREATE TABLE IF NOT EXISTS myclass (id INTEGER PRIMARY KEY,department TEXT, school_year TEXT,
			school_head TEXT, grade TEXT,section TEXT,
			adviser TEXT, strand TEXT, sem TEXT) """)
	conn.commit()
	conn.close()

def addClassRec(department, school_year, school_head,  grade, section, adviser, strand, sem):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\class.db")
	cur = conn.cursor()

	# ------------ create placeholder entry for table -------------
	cur.execute("INSERT INTO myclass VALUES (NULL, ?,?,?,?,?,?,?,?)", \
				(department, school_year, school_head,  grade, section, adviser, strand, sem))

	conn.commit()
	conn.close()

def updateClassRec(schoolHead, classAdv, semester, idNum):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\class.db")
	cur = conn.cursor()

	cur.execute("""UPDATE myclass SET
							school_head = :sh, 
							adviser = :adv,
							sem = :s
						WHERE oid = :oid""",	
						{
							'sh':schoolHead, 'adv':classAdv, 's':semester,  'oid': idNum					
						})
	conn.commit()
	conn.close()

def viewDataclass():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\class.db")
	cur = conn.cursor()

	cur.execute("SELECT * FROM myclass")
	classrows = cur.fetchall()
	conn.close()

	return classrows

def deleteClassRec(id):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\class.db")
	cur = conn.cursor()

	cur.execute("DELETE FROM myclass WHERE id=?", (id,))
	conn.commit()
	conn.close()

def deleteALLClass():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\class.db")
	cur = conn.cursor()

	cur.execute("DELETE FROM myclass")
	conn.commit()
	conn.close()


