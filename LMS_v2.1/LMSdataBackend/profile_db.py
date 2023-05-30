import sqlite3
from absPath import resource_path


# ---------- backend database setup for learner's profile data ---------------------------
def createProfileData():
    conn = sqlite3.connect(resource_path("data\\profileData.db"))
    cur = conn.cursor()
    cur.execute("""
                    CREATE TABLE IF NOT EXISTS profileTable (
                    id INTEGER PRIMARY KEY,
                    lrn TEXT,           last_name TEXT,
                    first_name TEXT,    middle_name TEXT,
                    name_ext TEXT,      birthdate TEXT, 
                    sex TEXT,           age TEXT,           
                    address TEXT,       mother_name TEXT,
                    father_name TEXT,   guardian_name TEXT, 
                    modality TEXT,      status TEXT)
    			""")
    conn.commit()
    conn.close()


def addProfileData(profile_data: tuple):
    conn = sqlite3.connect(resource_path("data\\profileData.db"))
    cur = conn.cursor()
    # index and value for tuple parameter
    # [0]lrn,           [1]last_name,       [2]first_name,  [3]middle_nme,  [4]name_ext
    # [5]birthdate,     [6]sex,             [7]age,         [8]address,     [9]mother_name
    # [10]father_name,  [11]guardian_name,  [12]modality,   [13]status
    cur.execute("INSERT INTO profileTable VALUES (NULL, ?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (profile_data[0], profile_data[1], profile_data[2], profile_data[3], profile_data[4],
                 profile_data[5], profile_data[6], profile_data[7], profile_data[8], profile_data[9],
                 profile_data[10], profile_data[11], profile_data[12], profile_data[13]))
    conn.commit()
    conn.close()


def viewProfileData():
    conn = sqlite3.connect(resource_path("data\\profileData.db"))
    cur = conn.cursor()

    cur.execute("SELECT * FROM profileTable")
    fromProfileData = cur.fetchall()
    conn.close()

    return fromProfileData


def updateProfileData(upd_profile_data: tuple):
    conn = sqlite3.connect(resource_path("data\\profileData.db"))
    cur = conn.cursor()
    cur.execute("""UPDATE   profileTable 
                      SET   lrn = :lrn, 
                            last_name = :last_name, 
                            first_name = :first_name, 
                            middle_name = :middle_name, 
                            name_ext = :name_ext, 
                            birthdate = :birthdate, 
                            sex = :sex, 
                            age = :age, 
                            address = :address,
                            mother_name = :mother_name, 
                            father_name = :father_name, 
                            guardian_name = :guardian_name,
                            modality = :modality, 
                            status = :status 
                    WHERE   oid = :oid""",
                        {
                            'lrn': upd_profile_data[0],
                            'last_name': upd_profile_data[1],
                            'first_name': upd_profile_data[2],
                            'middle_name': upd_profile_data[3],
                            'name_ext': upd_profile_data[4],
                            'birthdate': upd_profile_data[5],
                            'sex': upd_profile_data[6],
                            'age': upd_profile_data[7],
                            'address': upd_profile_data[8],
                            'mother_name': upd_profile_data[9],
                            'father_name': upd_profile_data[10],
                            'guardian_name': upd_profile_data[11],
                            'modality': upd_profile_data[12],
                            'status': upd_profile_data[13],
                            'oid': upd_profile_data[14]
                        })
    conn.commit()
    conn.close()


def deleteProfileData(profileId):
    conn = sqlite3.connect("data\\profileData.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM profileTable WHERE id=?", (profileId,))
    conn.commit()
    conn.close()
