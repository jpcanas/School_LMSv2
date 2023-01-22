import sqlite3

# ---------- backend database for LMS (SUBJECTS) for Senior High School only (1st and 2nd Semester) -----------------------------

def subj_SHS():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\subjectSHS.db")
	cur = conn.cursor()
	cur.execute("""CREATE TABLE IF NOT EXISTS shs_subj (id INTEGER PRIMARY KEY,
			subSHS1 TEXT, subSHS2 TEXT, subSHS3 TEXT, subSHS4 TEXT, subSHS5 TEXT, subSHS6 TEXT, subSHS7 TEXT, subSHS8 TEXT, subSHS9 TEXT, 
			subSHS10 TEXT, subSHS11 TEXT, subSHS12 TEXT, subSHS13 TEXT, subSHS14 TEXT, subSHS15 TEXT)     
		""")
	conn.commit()
	conn.close()

def insertSubjSHS(subjects):
	
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\subjectSHS.db")
	cur = conn.cursor()

	data = "INSERT INTO shs_subj VALUES "
	modify = (f'{data} {subjects}')

	cur.execute(modify)
	conn.commit()
	conn.close()

	print("success")

def viewSubjSHS():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\subjectSHS.db")
	cur = conn.cursor()

	cur.execute("SELECT * FROM shs_subj")
	subjrowSHS = cur.fetchall()
	conn.close()

	return subjrowSHS

def deleteSubjSHS(id):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\subjectSHS.db")
	cur = conn.cursor()

	cur.execute("DELETE FROM shs_subj WHERE id=?", (id,))
	conn.commit()
	conn.close()

def deleteALLSubjSHS():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\subjectSHS.db")
	cur = conn.cursor()

	cur.execute("DELETE FROM shs_subj")
	conn.commit()
	conn.close()
