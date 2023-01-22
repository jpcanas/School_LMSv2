import sqlite3


################### backend database for Month and No. of School Days ############
################### 2 rows (month and no of school days) #########################

def month_data():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\att_month.db")
	cur = conn.cursor()
	cur.execute("""CREATE TABLE IF NOT EXISTS month (
			month1 TEXT, month2 TEXT, month3 TEXT, month4 TEXT, month5 TEXT, month6 TEXT, 
			month7 TEXT, month8 TEXT, month9 TEXT, month10 TEXT,  month11 TEXT,  month12 TEXT)     
		""")
	conn.commit()
	conn.close()

def insertMonth(month1, month2, month3, month4, month5,month6, month7, month8, month9, month10, month11, month12):
	
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\att_month.db")
	cur = conn.cursor()

# ------------ create placeholder entry for table ---------------------------------------------------

	cur.execute("INSERT INTO month VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", \
				(month1, month2, month3, month4, month5, month6, month7, month8, month9, month10, month11, month12))
	conn.commit()
	conn.close()

def updMonthData(data):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\att_month.db")
	cur = conn.cursor()

	cur.execute("""UPDATE month SET 
					month1 = :n_month1, month2 = :n_month2, month3 = :n_month3, month4 = :n_month4, month5 = :n_month5, month6 = :n_month6, 
					month7 = :n_month7, month8 = :n_month8, month9 = :n_month9, month10 = :n_month10, month11 = :n_month11, month12 = :n_month12
					WHERE oid = :oid """, data)
	conn.commit()
	conn.close()

def viewMonth():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\att_month.db")
	cur = conn.cursor()

	cur.execute("SELECT * FROM month")
	monthrow = cur.fetchall()
	conn.close()

	return monthrow

def deletemonth():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\att_month.db")
	cur = conn.cursor()

	cur.execute("DELETE FROM month WHERE id=?", (id,))
	conn.commit()
	conn.close()


################### backend database for no. of days present and absent #####################################

def att_data():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\att_present.db")
	cur = conn.cursor()
	cur.execute("""CREATE TABLE IF NOT EXISTS att (
			id INTEGER PRIMARY KEY,	name TEXT, 	lrn TEXT,	
			days1 TEXT, days2 TEXT, days3 TEXT, days4 TEXT, days5 TEXT,	days6 TEXT, days7 TEXT, days8 TEXT, days9 TEXT, days10 TEXT, days11 TEXT, days12 TEXT,  daystotal TEXT, 
			pres1 TEXT, pres2 TEXT, pres3 TEXT, pres4 TEXT, pres5 TEXT,	pres6 TEXT, pres7 TEXT, pres8 TEXT, pres9 TEXT, pres10 TEXT, pres11 TEXT, pres12 TEXT,  prestotal TEXT, 
			abs1 TEXT, abs2 TEXT, abs3 TEXT, abs4 TEXT, abs5 TEXT, abs6 TEXT, abs7 TEXT, abs8 TEXT, abs9 TEXT, abs10 TEXT, abs11 TEXT, abs12 TEXT, abstotal TEXT)     
		""")
	conn.commit()
	conn.close()

def insert_att(name, lrn,
				days1, days2, days3, days4, days5, days6, days7, days8, days9, days10, days11, days12, daystotal,
				pres1, pres2, pres3, pres4, pres5, pres6, pres7, pres8, pres9, pres10, pres11, pres12, prestotal, 
				abs1, abs2,	abs3, abs4, abs5, abs6, abs7, abs8, abs9, abs10, abs11, abs12, abstotal):
	
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\att_present.db")
	cur = conn.cursor()

	cur.execute("INSERT INTO att VALUES (NULL, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", \
				(name, lrn,
				days1, days2, days3, days4, days5, days6, days7, days8, days9, days10, days11, days12, daystotal,
				pres1, pres2, pres3, pres4, pres5, pres6, pres7, pres8, pres9, pres10, pres11, pres12, prestotal, 
				abs1, abs2,	abs3, abs4, abs5, abs6, abs7, abs8, abs9, abs10, abs11, abs12, abstotal))
	conn.commit()
	conn.close()

def updNameLRNAtt(upName, upLrn, idNum):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\att_present.db")
	cur = conn.cursor()
	cur.execute("""UPDATE att SET
							name = :n_name, lrn = :n_lrn
						WHERE oid = :oid""",	
						{
							'n_name':upName, 'n_lrn':upLrn, 'oid': idNum	 				
						})
	conn.commit()
	conn.close()

def updNumDays(numDays, daysTotal, idNum):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\att_present.db")
	cur = conn.cursor()
	cur.execute("""UPDATE att SET
						days1 = :n_days1, days2 = :n_days2, days3 = :n_days3, 
						days4 = :n_days4, days5 = :n_days5, days6 = :n_days6, 
						days7 = :n_days7, days8 = :n_days8, days9 = :n_days9, 
						days10 = :n_days10, days11 = :n_days11, days12 = :n_days12,
						daystotal = :n_daystotal  

						WHERE oid = :oid""",
						{
							'n_days1':numDays[0], 'n_days2':numDays[1], 'n_days3':numDays[2],  
							'n_days4':numDays[3], 'n_days5':numDays[4], 'n_days6':numDays[5],
							'n_days7':numDays[6], 'n_days8':numDays[7], 'n_days9':numDays[8],
							'n_days10':numDays[9], 'n_days11':numDays[10], 'n_days12':numDays[11],
							'n_daystotal':daysTotal, 'oid':idNum	 				
						})
	conn.commit()
	conn.close()

def updateAtt(presData, absData, idNum):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\att_present.db")
	cur = conn.cursor()
	cur.execute("""UPDATE att SET
							pres1 = :n_pres1, pres2 = :n_pres2, pres3 = :n_pres3, pres4 = :n_pres4, pres5 = :n_pres5, pres6 = :n_pres6, 
							pres7 = :n_pres7, pres8 = :n_pres8, pres9 = :n_pres9, pres10 = :n_pres10, pres11 = :n_pres11, pres12 = :n_pres12, 
							abs1 = :n_abs1, abs2 = :n_abs2, abs3 = :n_abs3, abs4 = :n_abs4, abs5 = :n_abs5, abs6 = :n_abs6, 
							abs7 = :n_abs7, abs8 = :n_abs8, abs9 = :n_abs9, abs10 = :n_abs10, abs11 = :n_abs11, abs12 = :n_abs12 
							    
						WHERE oid = :oid""",
						{
							'n_pres1':presData[0], 'n_pres2':presData[1], 'n_pres3':presData[2], 'n_pres4':presData[3], 'n_pres5':presData[4], 'n_pres6':presData[5],
							'n_pres7':presData[6], 'n_pres8':presData[7], 'n_pres9':presData[8], 'n_pres10':presData[9], 'n_pres11':presData[10], 'n_pres12':presData[11],
							'n_abs1':absData[0], 'n_abs2':absData[1], 'n_abs3':absData[2], 'n_abs4':absData[3], 'n_abs5':absData[4], 'n_abs6':absData[5],
							'n_abs7':absData[6], 'n_abs8':absData[7], 'n_abs9':absData[8], 'n_abs10':absData[9], 'n_abs11':absData[10], 'n_abs12':absData[11],
							'oid':idNum	 				
						})
	conn.commit()
	conn.close()

def updateTotal(presTotal, absTotal, idNum):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\att_present.db")
	cur = conn.cursor()
	cur.execute("""UPDATE att SET
							prestotal = :n_prestotal, abstotal = :n_abstotal 
							    
						WHERE oid = :oid""",
						{
							'n_prestotal':presTotal, 'n_abstotal':absTotal, 
							'oid':idNum	 				
						})
	conn.commit()
	conn.close()

def view_att():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\att_present.db")
	cur = conn.cursor()

	cur.execute("SELECT * FROM att")
	att_row = cur.fetchall()
	conn.close()

	return att_row

def delete_att(id):
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\att_present.db")
	cur = conn.cursor()

	cur.execute("DELETE FROM att WHERE id=?", (id,))
	conn.commit()
	conn.close()

def delete_AllAtt():
	conn = sqlite3.connect("C:\\LMS_appVer2\\database\\att_present.db")
	cur = conn.cursor()

	cur.execute("DELETE FROM att")
	conn.commit()
	conn.close()


# def add_att():

# 	learner = profileDataBase.viewstudentData()
# 	if len(learner) != 0:    

#  		for dataJHS in learner:

# 		    if dataJHS[4] == "" or dataJHS[4] == " ":
# 		    	midname = "-"
# 		    else:
# 		    	midname = dataJHS[4]

# 		    nameJHS = str(f"{dataJHS[2]}, {dataJHS[3]} {midname[0]}. {dataJHS[5]}")

# 		    insert_att(nameJHS, dataJHS[1],\
# 		    				'','','','','','','','','','','','','',\
# 		    				'','','','','','','','','','','','','',\
# 		    				'','','','','','','','','','','','','')
