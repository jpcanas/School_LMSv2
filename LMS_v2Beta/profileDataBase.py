import sqlite3

# ---------- backend database for Learner's Profile -------------

def studentData():
    conn = sqlite3.connect("C:\\LMS_appVer2\\database\\profileData.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS profile (
            id INTEGER PRIMARY KEY,
            lrn TEXT,           last_n TEXT,
            first_n TEXT,       middle_n TEXT,
            name_ext TEXT,      sex TEXT,
            age TEXT,           address TEXT,
            dob TEXT,       mother_name TEXT,
            father_name TEXT,   guardian_name TEXT, modality TEXT, eligibility TEXT)     
        """)
    conn.commit()
    conn.close()

def addStdRec(lrn, last_n, first_n, middle_n, name_ext, sex, age, address, dob, mother_name, father_name, guardian_name, modality, eligibility):
    conn = sqlite3.connect("C:\\LMS_appVer2\\database\\profileData.db")
    cur = conn.cursor()

    # ------------ create placeholder entry for table -----------------------------------------
    cur.execute("INSERT INTO profile VALUES (NULL, ?,?,?,?,?,?,?,?,?,?,?,?,?,?)", \
                (lrn, last_n, first_n, middle_n, name_ext, sex, age, address, dob, mother_name, father_name, guardian_name, modality, eligibility))

    conn.commit()
    conn.close()

def updateStdRec(uplrn, uplast_n, upfirst_n, upmiddle_n, upname_ext, upsex, upage, upaddress, updob, upmother_name, upfather_name, upguardian_name, upmodality, upeligibility, idNum):
    conn = sqlite3.connect("C:\\LMS_appVer2\\database\\profileData.db")
    cur = conn.cursor()

    cur.execute("""UPDATE profile SET
                            lrn = :n_lrn, last_n = :n_last_n, first_n = :n_first_n, middle_n = :n_middle_n,  
                            name_ext = :n_name_ext, sex = :n_sex, age = :n_age, address = :n_address, 
                            dob = :n_dob, mother_name = :n_mother_name, father_name = :n_father_name, 
                            guardian_name = :n_guardian_name, modality = :n_modality, eligibility = :n_eligibility 

                        WHERE oid = :oid""",    
                        {
                            'n_lrn':uplrn, 'n_last_n':uplast_n, 'n_first_n':upfirst_n, 'n_middle_n':upmiddle_n,  
                            'n_name_ext':upname_ext, 'n_sex':upsex, 'n_age':upage, 'n_address':upaddress, 
                            'n_dob':updob, 'n_mother_name':upmother_name, 'n_father_name':upfather_name, 
                            'n_guardian_name':upguardian_name, 'n_modality':upmodality, 'n_eligibility':upeligibility, 'oid': idNum                 
                        })
    conn.commit()
    conn.close()

def viewstudentData():
    conn = sqlite3.connect("C:\\LMS_appVer2\\database\\profileData.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM profile")
    studentrow = cur.fetchall()
    conn.close()

    return studentrow

def deleteStdRec(id):
    conn = sqlite3.connect("C:\\LMS_appVer2\\database\\profileData.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM profile WHERE id=?", (id,))
    conn.commit()
    conn.close()

def deleteALLStdRec():
    conn = sqlite3.connect("C:\\LMS_appVer2\\database\\profileData.db")
    cur = conn.cursor()

    cur.execute('DELETE FROM profile')
    
    conn.commit()
    conn.close()


# studentData()

# addStdRec('112536245879','MORAL','JOYCRIS','TORDILLO','','FEMALE','18','TARUM, LIBMANAN, CAMARINES SUR','AUGUST 12, 2001','LUCY MORAL','CARDO TORDILLO','','MODULAR','')
# addStdRec('123520125468','OLIVA','JHON KEVIN','MORATALLA','','MALE','19','CAMAMBUGAN, LIBMANAN, CAMARINES SUR','FEBRUARY 16, 2000','JOCELYN MORATALLA','RICHARD OLIVA','','MODULAR','')

