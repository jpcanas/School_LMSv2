import sqlite3


# ---------- backend database for Observe Values (Both SHS and JHS) -----------------------------

def values_data():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\ov.db")
	cur = conn.cursor()
	cur.execute("""CREATE TABLE IF NOT EXISTS val (
			id INTEGER PRIMARY KEY,	name TEXT, 	lrn TEXT,	
			val1 TEXT, val2 TEXT, val3 TEXT, val4 TEXT, val5 TEXT, val6 TEXT, val7 TEXT, val8 TEXT,   
			val9 TEXT, val10 TEXT, val11 TEXT, val12 TEXT, val13 TEXT, val14 TEXT, val15 TEXT, val16 TEXT,	   
			val17 TEXT, val18 TEXT, val19 TEXT, val20 TEXT, val21 TEXT, val22 TEXT, val23 TEXT, val24 TEXT,	   
			val25 TEXT, val26 TEXT, val27 TEXT, val28 TEXT)     
		""")
	conn.commit()
	conn.close()

def insert_values(name, lrn,
				val1, val2, val3, val4, val5, val6, val7, val8,   
				val9, val10, val11, val12, val13, val14, val15, val16,	   
				val17, val18, val19, val20, val21, val22, val23, val24,	   
				val25, val26, val27, val28):
	
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\ov.db")
	cur = conn.cursor()

	cur.execute("INSERT INTO val VALUES (NULL, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", \
				(name, lrn,
				val1, val2, val3, val4, val5, val6, val7, val8,   
				val9, val10, val11, val12, val13, val14, val15, val16,	   
				val17, val18, val19, val20, val21, val22, val23, val24,	   
				val25, val26, val27, val28))
	conn.commit()
	conn.close()

def updNameLRNAov(upName, upLrn, idNum):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\ov.db")
	cur = conn.cursor()
	cur.execute("""UPDATE val SET
							name = :n_name, lrn = :n_lrn
						WHERE oid = :oid""",	
						{
							'n_name':upName, 'n_lrn':upLrn, 'oid': idNum	 				
						})
	conn.commit()
	conn.close()

def updOV(ovData, idNum):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\ov.db")
	cur = conn.cursor()
	cur.execute("""UPDATE val SET
						val1 = :n_val1, val2 = :n_val2, val3 = :n_val3, val4 = :n_val4, 
						val5 = :n_val5, val6 = :n_val6, val7 = :n_val7, val8 = :n_val8, 
						val9 = :n_val9, val10 = :n_val10, val11 = :n_val11, val12 = :n_val12,
						val13 = :n_val13, val14 = :n_val14, val15 = :n_val15, val16 = :n_val16, 
						val17 = :n_val17, val18 = :n_val18, val19 = :n_val19, val20 = :n_val20, 
						val21 = :n_val21, val22 = :n_val22, val23 = :n_val23, val24 = :n_val24, 
						val25 = :n_val25, val26 = :n_val26, val27 = :n_val27, val28 = :n_val28 
							    
						WHERE oid = :oid""",
						{
							'n_val1':ovData[0], 'n_val2':ovData[1], 'n_val3':ovData[2], 'n_val4':ovData[3], 
							'n_val5':ovData[4], 'n_val6':ovData[5], 'n_val7':ovData[6], 'n_val8':ovData[7],
							'n_val9':ovData[8], 'n_val10':ovData[9], 'n_val11':ovData[10], 'n_val12':ovData[11],
							'n_val13':ovData[12], 'n_val14':ovData[13], 'n_val15':ovData[14], 'n_val16':ovData[15],
							'n_val17':ovData[16], 'n_val18':ovData[17], 'n_val19':ovData[18], 'n_val20':ovData[19],
							'n_val21':ovData[20], 'n_val22':ovData[21], 'n_val23':ovData[22], 'n_val24':ovData[23],
							'n_val25':ovData[24], 'n_val26':ovData[25], 'n_val27':ovData[26], 'n_val28':ovData[27],
							'oid':idNum	 				
						})
	conn.commit()
	conn.close()

def view_values():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\ov.db")
	cur = conn.cursor()

	cur.execute("SELECT * FROM val")
	val_row = cur.fetchall()
	conn.close()

	return val_row

def delete_values(id):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\ov.db")
	cur = conn.cursor()

	cur.execute("DELETE FROM val WHERE id=?", (id,))
	conn.commit()
	conn.close()

def deleteALLvalues():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\ov.db")
	cur = conn.cursor()

	cur.execute("DELETE FROM val")
	conn.commit()
	conn.close()

# def add_ov():

# 	learner = profileDataBase.viewstudentData()
# 	if len(learner) != 0:    

#  		for dataJHS in learner:

# 		    if dataJHS[4] == "" or dataJHS[4] == " ":
# 		    	midname = "-"
# 		    else:
# 		    	midname = dataJHS[4]

# 		    nameJHS = str(f"{dataJHS[2]}, {dataJHS[3]} {midname[0]}. {dataJHS[5]}")

# 		    insert_values(nameJHS, dataJHS[1],\
# 		    				'','','','','','','','','','','','','','',\
# 		    				'','','','','','','','','','','','','','')
# 	print("done")





