import sqlite3
from absPath import resource_path


# ---------- backend database setup for learner's profile data ---------------------------
def createProfileData(mainDbName: str):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
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


def addProfileData(mainDbName: str, profile_data: tuple):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    # index and value for tuple parameter
    # [0]lrn,           [1]last_name,       [2]first_name,  [3]middle_nme,  [4]name_ext
    # [5]birthdate,     [6]sex,             [7]age,         [8]address,     [9]mother_name
    # [10]father_name,  [11]guardian_name,  [12]modality,   [13]status
    cur.execute("INSERT INTO profileTable VALUES (NULL, ?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                profile_data)
    learnerID = cur.lastrowid
    conn.commit()
    conn.close()

    return learnerID


def viewProfileData(mainDbName: str, lrn="", sex=None, fullName="", address="", modality=None, status=None):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute('''SELECT * FROM  profileTable
                               WHERE  lrn LIKE ?
                                 AND  ((last_name LIKE ? OR first_name LIKE ?) OR 
                                       (last_name || ' ' || first_name) LIKE ? OR 
                                       (first_name || ' ' || last_name) LIKE ?)
                                 AND  sex = COALESCE(?, sex)
                                 AND  address LIKE ?
                                 AND  modality = COALESCE(?, modality)
                                 AND  status = COALESCE(?, status)
                            ORDER BY  last_name
                    ''', (f"{lrn}%",
                          f"{fullName}%", f"{fullName}%", f"{fullName}%", f"{fullName}%",
                          sex,
                          f"{address}%",
                          modality,
                          status))
    fromProfileData = cur.fetchall()
    conn.close()

    return fromProfileData


def updateProfileData(mainDbName: str, upd_profile_data: tuple):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
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
                    WHERE   oid = :oid""", upd_profile_data)
    conn.commit()
    conn.close()


def deleteProfileData(mainDbName: str, profileId):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute("DELETE FROM profileTable WHERE id=?", (profileId,))
    conn.commit()
    conn.close()
