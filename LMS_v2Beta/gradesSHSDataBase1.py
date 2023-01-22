import sqlite3
# import profileDataBase

# ---------- backend database for LMS (grades) for Senior High School only 1st Semester -----------------------------

def gradesDataSem1():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\sem1SHS.db")
	cur = conn.cursor()
	cur.execute("""CREATE TABLE IF NOT EXISTS sem1grades (
			id INTEGER PRIMARY KEY,	name TEXT, lrn TEXT, sex TEXT, age TEXT,
			sub1Q1 TEXT,sub1Q2 TEXT,sub1Fin TEXT,  sub2Q1 TEXT,sub2Q2 TEXT,sub2Fin TEXT,  sub3Q1 TEXT,sub3Q2 TEXT,sub3Fin TEXT,  sub4Q1 TEXT,sub4Q2 TEXT,sub4Fin TEXT,  sub5Q1 TEXT,sub5Q2 TEXT,sub5Fin TEXT,
			sub6Q1 TEXT,sub6Q2 TEXT,sub6Fin TEXT,  sub7Q1 TEXT,sub7Q2 TEXT,sub7Fin TEXT,  sub8Q1 TEXT,sub8Q2 TEXT,sub8Fin TEXT,  sub9Q1 TEXT,sub9Q2 TEXT,sub9Fin TEXT,  sub10Q1 TEXT,sub10Q2 TEXT,sub10Fin TEXT,
			sub11Q1 TEXT,sub11Q2 TEXT,sub11Fin TEXT,  sub12Q1 TEXT,sub12Q2 TEXT,sub12Fin TEXT,  sub13Q1 TEXT,sub13Q2 TEXT,sub13Fin TEXT,  sub14Q1 TEXT,sub14Q2 TEXT,sub14Fin TEXT,  sub15Q1 TEXT,sub15Q2 TEXT,sub15Fin TEXT)     
		""")
	conn.commit()
	conn.close()

def insertGradeSem1(name, lrn, sex,	age,
				sub1Q1,sub1Q2,sub1Fin,  sub2Q1,sub2Q2,sub2Fin,  sub3Q1,sub3Q2,sub3Fin,  sub4Q1,sub4Q2,sub4Fin,  sub5Q1,sub5Q2,sub5Fin,
				sub6Q1,sub6Q2,sub6Fin,  sub7Q1,sub7Q2,sub7Fin,  sub8Q1,sub8Q2,sub8Fin,  sub9Q1,sub9Q2,sub9Fin,  sub10Q1,sub10Q2,sub10Fin,
				sub11Q1,sub11Q2,sub11Fin,  sub12Q1,sub12Q2,sub12Fin,  sub13Q1,sub13Q2,sub13Fin,  sub14Q1,sub14Q2,sub14Fin,  sub15Q1,sub15Q2,sub15Fin):
	
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\sem1SHS.db")
	cur = conn.cursor()
 
	# ------------ create placeholder entry for table -----------------------------------------
	cur.execute("INSERT INTO sem1grades VALUES (NULL, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", \
				(name, lrn, sex,	age,
				sub1Q1,sub1Q2,sub1Fin,  sub2Q1,sub2Q2,sub2Fin,  sub3Q1,sub3Q2,sub3Fin,  sub4Q1,sub4Q2,sub4Fin,  sub5Q1,sub5Q2,sub5Fin,
				sub6Q1,sub6Q2,sub6Fin,  sub7Q1,sub7Q2,sub7Fin,  sub8Q1,sub8Q2,sub8Fin,  sub9Q1,sub9Q2,sub9Fin,  sub10Q1,sub10Q2,sub10Fin,
				sub11Q1,sub11Q2,sub11Fin,  sub12Q1,sub12Q2,sub12Fin,  sub13Q1,sub13Q2,sub13Fin,  sub14Q1,sub14Q2,sub14Fin,  sub15Q1,sub15Q2,sub15Fin))

	conn.commit()
	conn.close()

def updNameLRNsem1(upName, upLrn, upSex, upAge, idNum):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\sem1SHS.db")
	cur = conn.cursor()
	cur.execute("""UPDATE sem1grades SET
							name = :n_name, lrn = :n_lrn, sex = :n_sex, age = :n_age 
						WHERE oid = :oid""",	
						{
							'n_name':upName, 'n_lrn':upLrn, 'n_sex':upSex, 'n_age':upAge, 'oid': idNum	 				
						})
	conn.commit()
	conn.close()

def updSem1Grade(gradeSem1, idNum):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\sem1SHS.db")
	cur = conn.cursor()
	cur.execute("""UPDATE sem1grades SET
							sub1Q1 = :n_sub1Q1, sub1Q2 = :n_sub1Q2,     sub2Q1 = :n_sub2Q1, sub2Q2 = :n_sub2Q2,
							sub3Q1 = :n_sub3Q1, sub3Q2 = :n_sub3Q2,     sub4Q1 = :n_sub4Q1, sub4Q2 = :n_sub4Q2, 
							sub5Q1 = :n_sub5Q1, sub5Q2 = :n_sub5Q2,     sub6Q1 = :n_sub6Q1, sub6Q2 = :n_sub6Q2, 
							sub7Q1 = :n_sub7Q1, sub7Q2 = :n_sub7Q2,     sub8Q1 = :n_sub8Q1, sub8Q2 = :n_sub8Q2, 
							sub9Q1 = :n_sub9Q1, sub9Q2 = :n_sub9Q2,		sub10Q1 = :n_sub10Q1, sub10Q2 = :n_sub10Q2, 
							sub11Q1 = :n_sub11Q1, sub11Q2 = :n_sub11Q2, sub12Q1 = :n_sub12Q1, sub12Q2 = :n_sub12Q2, 
							sub13Q1 = :n_sub13Q1, sub13Q2 = :n_sub13Q2,	sub14Q1 = :n_sub14Q1, sub14Q2 = :n_sub14Q2, 
							sub15Q1 = :n_sub15Q1, sub15Q2 = :n_sub15Q2    
						WHERE oid = :oid""",
						{
							'n_sub1Q1':gradeSem1[0], 'n_sub1Q2':gradeSem1[1], 'n_sub2Q1':gradeSem1[2], 'n_sub2Q2':gradeSem1[3], 
							'n_sub3Q1':gradeSem1[4], 'n_sub3Q2':gradeSem1[5], 'n_sub4Q1':gradeSem1[6], 'n_sub4Q2':gradeSem1[7],
							'n_sub5Q1':gradeSem1[8], 'n_sub5Q2':gradeSem1[9], 'n_sub6Q1':gradeSem1[10], 'n_sub6Q2':gradeSem1[11],
							'n_sub7Q1':gradeSem1[12], 'n_sub7Q2':gradeSem1[13], 'n_sub8Q1':gradeSem1[14], 'n_sub8Q2':gradeSem1[15],
							'n_sub9Q1':gradeSem1[16], 'n_sub9Q2':gradeSem1[17], 'n_sub10Q1':gradeSem1[18], 'n_sub10Q2':gradeSem1[19],
							'n_sub11Q1':gradeSem1[20], 'n_sub11Q2':gradeSem1[21], 'n_sub12Q1':gradeSem1[22], 'n_sub12Q2':gradeSem1[23],
							'n_sub13Q1':gradeSem1[24], 'n_sub13Q2':gradeSem1[25], 'n_sub14Q1':gradeSem1[26], 'n_sub14Q2':gradeSem1[27],
							'n_sub15Q1':gradeSem1[28], 'n_sub15Q2':gradeSem1[29], 'oid':idNum	 				
						})
	conn.commit()
	conn.close()

def updSem1Final(finSem1, idNum):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\sem1SHS.db")
	cur = conn.cursor()
	cur.execute("""UPDATE sem1grades SET
							sub1Fin = :n_sub1Fin, sub2Fin = :n_sub2Fin, sub3Fin = :n_sub3Fin, 
							sub4Fin = :n_sub4Fin, sub5Fin = :n_sub5Fin, sub6Fin = :n_sub6Fin,
							sub7Fin = :n_sub7Fin, sub8Fin = :n_sub8Fin, sub9Fin = :n_sub9Fin, 
							sub10Fin = :n_sub10Fin, sub11Fin = :n_sub11Fin, sub12Fin = :n_sub12Fin,
							sub13Fin = :n_sub13Fin, sub14Fin = :n_sub14Fin, sub15Fin = :n_sub15Fin    
						WHERE oid = :oid""",	
						{
							'n_sub1Fin':finSem1[0],	 'n_sub2Fin':finSem1[1],   'n_sub3Fin':finSem1[2],
							'n_sub4Fin':finSem1[3],	 'n_sub5Fin':finSem1[4],   'n_sub6Fin':finSem1[5],
							'n_sub7Fin':finSem1[6],  'n_sub8Fin':finSem1[7],   'n_sub9Fin':finSem1[8],
							'n_sub10Fin':finSem1[9], 'n_sub11Fin':finSem1[10], 'n_sub12Fin':finSem1[11],
							'n_sub13Fin':finSem1[12], 'n_sub14Fin':finSem1[13], 'n_sub15Fin':finSem1[14],
							'oid': idNum	 				
						})
	conn.commit()
	conn.close()

def viewGradesem1():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\sem1SHS.db")
	cur = conn.cursor()

	cur.execute("SELECT * FROM sem1grades")
	studentrow = cur.fetchall()
	conn.close()

	return studentrow

def deleteGradesem1(id):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\sem1SHS.db")
	cur = conn.cursor()

	cur.execute("DELETE FROM sem1grades WHERE id=?", (id,))
	conn.commit()
	conn.close()

def deleteALLGradesem1():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\sem1SHS.db")
	cur = conn.cursor()

	cur.execute("DELETE FROM sem1grades")
	conn.commit()
	conn.close()


