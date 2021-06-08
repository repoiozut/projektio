import sqlite3
from file import File

class Database:
    def __init__(self, dbName, tableName):
        """
        Te metoda inicjuje obiekt klasy Database, przypisująca mu podane wartości.

        Args:
            dbName
                nazwa bazy danych
            tableName
                nazwa tablicy w bazie danych
        """
        self.db = dbName
        self.table = tableName

    def createTable(self):
        """Te metody tworzy tabele w bazie danych



        """
        conn = sqlite3.connect("mydatabase.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS "users" (
                            "id"	INTEGER UNIQUE,
                            "name"	TEXT,
                            "surname" TEXT,
                            "region" TEXT,
                            "email"	TEXT,
                            "camera" TEXT,
                            "res_width"	INTEGER,
                            "res_height" INTEGER,
                            "codec" TEXT,
                            "sensor_width" REAL,
                            "sensor_height" REAL,
                            "exp_time" REAL,
                            "ar_width" INTEGER,
                            "ar_height" INTEGER
        )""")
        conn.commit()
        conn.close()
        
    def addToTable(self, fileName):
        """
        Te metoda dodaje zestaw danych do bazy danych. Zestaw jest dostarczany jako plik .txt

        Args:
            fileName
                nazwa pliku z zestawem danych
        """
        conn = sqlite3.connect("mydatabase.db")
        c = conn.cursor()
        f = File(fileName)
        f.read()
        array = f.get()
        for r in enumerate(array):
            query = "INSERT OR IGNORE INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            val = (r[1].id, r[1].name, r[1].surname, r[1].region, r[1].email, r[1].camera, r[1].res_width, r[1].res_height, r[1].codec, r[1].sensor_width, r[1].sensor_height, r[1].exp_time, r[1].ar_width, r[1].ar_height)
            c.execute(query, val)
        conn.commit()
        conn.close()

    def getResult(self):
        """Ta metoda zwraca całą zawartość bazy danych

        Returns:
            result
                zwraca całą zawartość bazy danych
        """
        conn = sqlite3.connect("mydatabase.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        result = c.fetchall()
        conn.commit()
        conn.close()
        return result
