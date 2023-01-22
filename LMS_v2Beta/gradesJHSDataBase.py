import sqlite3

# ---------- backend database for LMS (grades) for Junior High School only -----------------------------

def gradesDataJHS():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\grades_JHS.db")
	cur = conn.cursor()
	cur.execute("""CREATE TABLE IF NOT EXISTS jhsgrades (
			id INTEGER PRIMARY KEY,	name TEXT, 	lrn TEXT,	sex TEXT,	age TEXT,
			fil1 TEXT, fil2 TEXT, fil3 TEXT, fil4 TEXT, fil5 TEXT, eng1 TEXT, eng2 TEXT, eng3 TEXT, eng4 TEXT, eng5 TEXT,
			math1 TEXT, math2 TEXT, math3 TEXT, math4 TEXT, math5 TEXT, sci1 TEXT, sci2 TEXT, sci3 TEXT, sci4 TEXT, sci5 TEXT,
			ap1 TEXT, ap2 TEXT, ap3 TEXT, ap4 TEXT, ap5 TEXT, esp1 TEXT, esp2 TEXT, esp3 TEXT, esp4 TEXT, esp5 TEXT,
			tle1 TEXT, tle2 TEXT, tle3 TEXT, tle4 TEXT, tle5 TEXT, mapeh1 TEXT, mapeh2 TEXT, mapeh3 TEXT, mapeh4 TEXT, mapeh5 TEXT,
			music1 TEXT, music2 TEXT, music3 TEXT, music4 TEXT, music5 TEXT, arts1 TEXT, arts2 TEXT, arts3 TEXT, arts4 TEXT, arts5 TEXT,
			pe1 TEXT, pe2 TEXT, pe3 TEXT, pe4 TEXT, pe5 TEXT, health1 TEXT, health2 TEXT, health3 TEXT, health4 TEXT, health5 TEXT)     
		""")
	conn.commit()
	conn.close()

def insertGradeJHS(name, lrn, sex,	age,
				fil1, fil2, fil3, fil4, fil5, eng1, eng2, eng3, eng4, eng5,
				math1, math2, math3, math4, math5, sci1, sci2, sci3, sci4, sci5,
				ap1, ap2, ap3, ap4, ap5, esp1, esp2, esp3, esp4, esp5,
				tle1, tle2, tle3, tle4, tle5, mapeh1, mapeh2, mapeh3, mapeh4, mapeh5,
				music1, music2, music3, music4, music5, arts1, arts2, arts3, arts4, arts5,
				pe1, pe2, pe3, pe4, pe5, health1, health2, health3, health4, health5):
	
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\grades_JHS.db")
	cur = conn.cursor()

	# ------------ create placeholder entry for table -----------------------------------------
	cur.execute("INSERT INTO jhsgrades VALUES (NULL, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,\
												?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", \
				(name, lrn, sex,	age,
				fil1, fil2, fil3, fil4, fil5, eng1, eng2, eng3, eng4, eng5,
				math1, math2, math3, math4, math5, sci1, sci2, sci3, sci4, sci5,
				ap1, ap2, ap3, ap4, ap5, esp1, esp2, esp3, esp4, esp5,
				tle1, tle2, tle3, tle4, tle5, mapeh1, mapeh2, mapeh3, mapeh4, mapeh5,
				music1, music2, music3, music4, music5, arts1, arts2, arts3, arts4, arts5,
				pe1, pe2, pe3, pe4, pe5, health1, health2, health3, health4, health5))

	conn.commit()
	conn.close()

def updNameLRNjhs(upName, upLrn, upSex, upAge, idNum):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\grades_JHS.db")
	cur = conn.cursor()
	cur.execute("""UPDATE jhsgrades SET
							name = :n_name, lrn = :n_lrn, sex = :n_sex, age = :n_age 
						WHERE oid = :oid""",	
						{
							'n_name':upName, 'n_lrn':upLrn, 'n_sex':upSex, 'n_age':upAge, 'oid': idNum	 				
						})
	conn.commit()
	conn.close()

def updJHSGrade(gradeJHS, idNum):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\grades_JHS.db")
	cur = conn.cursor()
	cur.execute("""UPDATE jhsgrades SET
							fil1 = :n_fil1, fil2 = :n_fil2, fil3 = :n_fil3, fil4 = :n_fil4,  
							eng1 = :n_eng1, eng2 = :n_eng2, eng3 = :n_eng3, eng4 = :n_eng4,
							math1 = :n_math1, math2 = :n_math2, math3 = :n_math3, math4 = :n_math4,  
							sci1 = :n_sci1, sci2 = :n_sci2, sci3 = :n_sci3, sci4 = :n_sci4, 
							ap1 = :n_ap1, ap2 = :n_ap2, ap3 = :n_ap3, ap4 = :n_ap4,  
							esp1 = :n_esp1, esp2 = :n_esp2, esp3 = :n_esp3, esp4 = :n_esp4, 
							tle1 = :n_tle1, tle2 = :n_tle2, tle3 = :n_tle3, tle4 = :n_tle4,  
							music1 = :n_music1, music2 = :n_music2, music3 = :n_music3, music4 = :n_music4,  
							arts1 = :n_arts1, arts2 = :n_arts2, arts3 = :n_arts3, arts4 = :n_arts4,
							pe1 = :n_pe1, pe2 = :n_pe2, pe3 = :n_pe3, pe4 = :n_pe4,  
							health1 = :n_health1, health2 = :n_health2, health3 = :n_health3, health4 = :n_health4 
							   
						WHERE oid = :oid""",
						{
							'n_fil1':gradeJHS[0], 'n_fil2':gradeJHS[1], 'n_fil3':gradeJHS[2], 'n_fil4':gradeJHS[3], 
							'n_eng1':gradeJHS[4], 'n_eng2':gradeJHS[5], 'n_eng3':gradeJHS[6], 'n_eng4':gradeJHS[7],
							'n_math1':gradeJHS[8], 'n_math2':gradeJHS[9], 'n_math3':gradeJHS[10], 'n_math4':gradeJHS[11],
							'n_sci1':gradeJHS[12], 'n_sci2':gradeJHS[13], 'n_sci3':gradeJHS[14], 'n_sci4':gradeJHS[15],
							'n_ap1':gradeJHS[16], 'n_ap2':gradeJHS[17], 'n_ap3':gradeJHS[18], 'n_ap4':gradeJHS[19],
							'n_esp1':gradeJHS[20], 'n_esp2':gradeJHS[21], 'n_esp3':gradeJHS[22], 'n_esp4':gradeJHS[23],
							'n_tle1':gradeJHS[24], 'n_tle2':gradeJHS[25], 'n_tle3':gradeJHS[26], 'n_tle4':gradeJHS[27],
							'n_music1':gradeJHS[28], 'n_music2':gradeJHS[29], 'n_music3':gradeJHS[30], 'n_music4':gradeJHS[31],
							'n_arts1':gradeJHS[32], 'n_arts2':gradeJHS[33], 'n_arts3':gradeJHS[34], 'n_arts4':gradeJHS[35],
							'n_pe1':gradeJHS[36], 'n_pe2':gradeJHS[37], 'n_pe3':gradeJHS[38], 'n_pe4':gradeJHS[39],
							'n_health1':gradeJHS[40], 'n_health2':gradeJHS[41], 'n_health3':gradeJHS[42], 'n_health4':gradeJHS[43],
							'oid':idNum	 				
						})
	conn.commit()
	conn.close()

def updMapehGrade(mapehList, idNum):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\grades_JHS.db")
	cur = conn.cursor()
	cur.execute("""UPDATE jhsgrades SET 
							mapeh1 = :n_mapeh1, mapeh2 = :n_mapeh2, mapeh3 = :n_mapeh3, mapeh4 = :n_mapeh4
							   
						WHERE oid = :oid""",
						{
							'n_mapeh1':mapehList[0], 'n_mapeh2':mapehList[1], 'n_mapeh3':mapehList[2], 'n_mapeh4':mapehList[3], 
							'oid':idNum	 				
						})
	conn.commit()
	conn.close()

def updJHSFinal(finalJHS, idNum):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\grades_JHS.db")
	cur = conn.cursor()
	cur.execute("""UPDATE jhsgrades SET
							fil5 = :n_fil5, eng5 = :n_eng5, math5 = :n_math5, sci5 = :n_sci5,
							ap5 = :n_ap5, esp5 = :n_esp5, tle5 = :n_tle5, mapeh5 = :n_mapeh5,
							music5 = :n_music5, arts5 = :n_arts5, pe5 = :n_pe5, health5 = :n_health5 
							    
						WHERE oid = :oid""",	
						{
							'n_fil5':finalJHS[0], 'n_eng5':finalJHS[1], 'n_math5':finalJHS[2], 'n_sci5':finalJHS[3],
							'n_ap5':finalJHS[4], 'n_esp5':finalJHS[5], 'n_tle5':finalJHS[6], 'n_mapeh5':finalJHS[7],
							'n_music5':finalJHS[8], 'n_arts5':finalJHS[9], 'n_pe5':finalJHS[10], 'n_health5':finalJHS[11], 
							'oid': idNum	 				
						})
	conn.commit()
	conn.close()

def viewGradeJHS():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\grades_JHS.db")
	cur = conn.cursor()

	cur.execute("SELECT * FROM jhsgrades")
	studentrow = cur.fetchall()
	conn.close()

	return studentrow

def deleteGradeJHS(id):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\grades_JHS.db")
	cur = conn.cursor()

	cur.execute("DELETE FROM jhsgrades WHERE id=?", (id,))
	conn.commit()
	conn.close()

def deleteALLGradeJHS():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\grades_JHS.db")
	cur = conn.cursor()

	cur.execute("DELETE FROM jhsgrades")
	conn.commit()
	conn.close()
