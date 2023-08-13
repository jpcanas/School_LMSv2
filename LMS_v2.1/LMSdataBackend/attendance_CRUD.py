import sqlite3
from absPath import resource_path


# ---------- backend database setup for learner's attendance data (Monthly)---------------------------
def createAttendanceData(mainDbName: str):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute("""
                    CREATE TABLE IF NOT EXISTS attendanceTable (
                    id INTEGER NOT NULL,
                    presentM1 INT,      presentM2 INT,      presentM3 INT,      presentM4 INT,
                    presentM5 INT,      presentM6 INT,      presentM7 INT,      presentM8 INT,
                    presentM9 INT,      presentM10 INT,     presentM11 INT,     presentM12 INT, 
                    presentTotal INT,  
                    absentM1 INT,       absentM2 INT,       absentM3 INT,       absentM4 INT, 
                    absentM5 INT,       absentM6 INT,       absentM7 INT,       absentM8 INT, 
                    absentM9 INT,       absentM10 INT,      absentM11 INT,      absentM12 INT,  
                    absentTotal INT)
    			""")
    conn.commit()
    conn.close()


def addAttendanceData(mainDbName: str, attId: int, att_data=None):
    if att_data is None:
        default_att_data = [None] * 26
        att_data = tuple(default_att_data)

    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute("INSERT INTO attendanceTable VALUES (?,"
                "?,?,?,?,?,?,?,?,?,?,?,?,?,"  # 13 items
                "?,?,?,?,?,?,?,?,?,?,?,?,?)",  # 13 items
                (attId,) + att_data)
    attendanceId = cur.lastrowid
    conn.commit()
    conn.close()

    return attendanceId


def viewAttendanceData(mainDbName, attId=None):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute('''SELECT p.id,
                     CASE 
                          WHEN p.middle_name != '' 
                          THEN p.last_name || ", " || p.first_name || ' ' || SUBSTRING(p.middle_name, 1, 1) || '.'
                          ELSE p.last_name || ", " || p.first_name 
                  END AS  fullname,
                          p.lrn,
                          p.sex,
                          p.age,
                          a.presentM1,      a.presentM2,      a.presentM3,      a.presentM4,
                          a.presentM5,      a.presentM6,      a.presentM7,      a.presentM8,
                          a.presentM9,      a.presentM10,     a.presentM11,     a.presentM12, 
                          a.presentTotal,  
                          a.absentM1,       a.absentM2,       a.absentM3,       a.absentM4, 
                          a.absentM5,       a.absentM6,       a.absentM7,       a.absentM8, 
                          a.absentM9,       a.absentM10,      a.absentM11,      a.absentM12,  
                          a.absentTotal
                    FROM  attendanceTable a
               LEFT JOIN  profileTable p 
                      ON  p.id = a.id
                   WHERE  p.id = COALESCE(?, p.id)
                   ''', (attId,))

    fromAttendanceData = cur.fetchall()
    conn.close()

    return fromAttendanceData


def updateAttendanceData(mainDbName: str, attendanceData: tuple, autoComplete: bool):
    if not autoComplete:
        presAbsDay = []
        for day in attendanceData:
            if day is not None:
                presAbsDay.append(int(day))  # add days (int type)
            else:
                presAbsDay.append(None)

        attendanceData = tuple(presAbsDay)

    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute("""UPDATE  attendanceTable 
                      SET  presentM1 = ?,      presentM2 = ?,      presentM3 = ?,      presentM4 = ?,
                           presentM5 = ?,      presentM6 = ?,      presentM7 = ?,      presentM8 = ?,
                           presentM9 = ?,      presentM10 = ?,     presentM11 = ?,     presentM12 = ?, 
                           presentTotal = ?,  
                           absentM1 = ?,       absentM2 = ?,       absentM3 = ?,       absentM4 = ?, 
                           absentM5 = ?,       absentM6 = ?,       absentM7 = ?,       absentM8 = ?, 
                           absentM9 = ?,       absentM10 = ?,      absentM11 = ?,      absentM12 = ?,  
                           absentTotal = ?
                    WHERE  oid = :oid""", attendanceData)
    conn.commit()
    conn.close()


def deleteAttData(mainDbName: str, attId):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute("DELETE FROM attendanceTable WHERE id=?", (attId,))
    conn.commit()
    conn.close()