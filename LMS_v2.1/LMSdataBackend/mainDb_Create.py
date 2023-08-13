import sqlite3
from absPath import resource_path
from datetime import datetime
import os


# ============== Creating main database for lms class datas (run only for register class)===========
def createMainDb(mainDbName):
    mainDbPath = resource_path(f"data\\{mainDbName}.db")
    today = datetime.now().strftime("%m/%d/%Y %H:%M")

    if not os.path.isfile(mainDbPath):  # create the class database if not exist
        conn = sqlite3.connect(mainDbPath)
        conn.close()

    deleteAllTables(mainDbPath)

    prev_dbNames = viewDbNames(None)  # fetch DbNames record if any
    hasDuplicateName = False
    if len(prev_dbNames) > 0:  # check if lms_dbNames.db has previous entry
        for db in prev_dbNames:
            updateDbNamesStatus(0, db[0])  # set prev entries active status to 0
            if db[1] == mainDbName:  # check if mainDbName has the same name with prev entries
                updateDbNamesStatus(1, db[0])  #
                hasDuplicateName = True

    if not hasDuplicateName:
        insertDbNames(mainDbName, 1, today)  # insert new database name to lms_dbNames.db (set active to 1)


def deleteAllTables(mainDbPath):
    conn = sqlite3.connect(mainDbPath)
    cur = conn.cursor()
    # Fetch all table names
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cur.fetchall()
    # Delete each table
    for table in tables:
        cur.execute(f"DROP TABLE IF EXISTS {table[0]}")

    conn.commit()
    conn.close()


# ======================== Creating database for storing names of created lms datas =========================
def createDbNames():  # run every start of app (checkDataClass)
    conn = sqlite3.connect(resource_path("data\\lms_dbNames.db"))
    cur = conn.cursor()
    cur.execute("""
                    CREATE TABLE IF NOT EXISTS DbNamesTable (
                        database_id INTEGER PRIMARY KEY,
                        db_Names TEXT, 
                        isActive INT,
                        created_on TEXT)
        		""")
    conn.commit()
    conn.close()


def insertDbNames(dbName, isActive, created_on):  # run only for register class
    conn = sqlite3.connect(resource_path("data\\lms_dbNames.db"))
    cur = conn.cursor()
    cur.execute("INSERT INTO DbNamesTable VALUES (NULL, ?,?,?)",
                (dbName, isActive, created_on))
    conn.commit()
    conn.close()


def viewDbNames(isActive):  # run every start of app (checkDataClass)
    conn = sqlite3.connect(resource_path("data\\lms_dbNames.db"))
    cur = conn.cursor()
    cur.execute('''SELECT * FROM DbNamesTable 
                           WHERE isActive = COALESCE(?, isActive)''',
                                 (isActive,))
    fromDbNames = cur.fetchall()
    conn.commit()
    conn.close()

    return fromDbNames


def deleteDbNames(database_id):
    conn = sqlite3.connect(resource_path("data\\lms_dbNames.db"))
    cur = conn.cursor()
    cur.execute('''DELETE FROM DbNamesTable 
                         WHERE database_id=?''', (database_id,))
    conn.commit()
    conn.close()


def updateDbNamesStatus(isActive, database_id):  # 1 for active, 0 for idle
    conn = sqlite3.connect(resource_path("data\\lms_dbNames.db"))
    cur = conn.cursor()
    cur.execute('''UPDATE DbNamesTable 
                      SET isActive = ?
                    WHERE database_id = ?''', (isActive, database_id))
    conn.commit()
    conn.close()
