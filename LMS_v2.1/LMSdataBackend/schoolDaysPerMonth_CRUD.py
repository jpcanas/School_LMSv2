import sqlite3
from absPath import resource_path
import calendar


# ---------- backend database setup for school calendar and number of school days per month--------------------------
def createDaysPerMonthData(mainDbName: str):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute("""
                    CREATE TABLE IF NOT EXISTS DaysPerMonthTable (
                    mId INTEGER PRIMARY KEY,
                    month1 TEXT,      month2 TEXT,      month3 TEXT,      month4 TEXT,
                    month5 TEXT,      month6 TEXT,      month7 TEXT,      month8 TEXT,
                    month9 TEXT,      month10 TEXT,     month11 TEXT,     month12 TEXT, 
                    schoolDayTotal INT)
    			""")
    conn.commit()
    conn.close()


def addDaysPerMonthData(mainDbName: str, daysPerMonth_data: tuple):
    if len(daysPerMonth_data) == 1:
        month = list(calendar.month_name)
        classStartMonth = daysPerMonth_data[0]
        startMonthIndex = month.index(classStartMonth)
        monthDataList = month[startMonthIndex:] + month[1:startMonthIndex]
        monthDataList.append(None)
        daysPerMonth_data = tuple(monthDataList)

    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute("INSERT INTO DaysPerMonthTable VALUES (NULL, ?,?,?,?,?,?,?,?,?,?,?,?,?)",
                daysPerMonth_data)
    monthID = cur.lastrowid
    conn.commit()
    conn.close()

    return monthID


def viewDaysPerMonthData(mainDbName, monthId=None):
    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute('''SELECT  *
                     FROM  DaysPerMonthTable 
                    WHERE  mId = COALESCE(?, mId)
                   ''', (monthId,))
    fromDaysPerMonthData = cur.fetchall()
    conn.close()

    return fromDaysPerMonthData


def updateDaysPerMonthData(mainDbName: str, monthData: tuple, monthID: int, autoComplete: bool):
    if monthID == 2:
        schoolDays = []
        if autoComplete:
            for day in monthData[0:12]:  # excluding total days
                if day != 0:
                    schoolDays.append(str(day))  # add days (str type)
                else:
                    schoolDays.append(None)

            schoolDays.append(monthData[-1])  # add the total school days (int type)
            schoolDays.append(2)  # add monthID
            monthData = tuple(schoolDays)
        else:
            schoolDays = list(monthData)
            schoolDays[-1] = int(schoolDays[-1])  # convert total school days to int type
            schoolDays.append(2)  # add monthID
            monthData = tuple(schoolDays)

    conn = sqlite3.connect(resource_path(f"data\\{mainDbName}.db"))
    cur = conn.cursor()
    cur.execute("""UPDATE  DaysPerMonthTable 
                      SET  month1 = ?,      month2  = ?,      month3  = ?,      month4  = ?,
                           month5  = ?,     month6  = ?,      month7  = ?,      month8  = ?,
                           month9  = ?,     month10  = ?,     month11  = ?,     month12  = ?, 
                           schoolDayTotal  = ?
                    WHERE  oid = :oid""", monthData)
    conn.commit()
    conn.close()
