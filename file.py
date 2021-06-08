from users import User
from pathlib import Path
import os.path

class File:
    def __init__(self, fileName):
        """Ta metoda inicjuje obiekt klasy File, przypisująca mu podane wartości

        Args:
            fileName
                nazwa pliku z danymi
        """
        self.file = fileName
        self.users = []

    def check(self, line):
        """Ta metoda waliduje jedną linię z pliku z danymi

        Args:
            line
                linia tekstu

        Returns:
            True
                gdy linia tekstu jest poprawna
            False
                gdy linia tekstu jest niepoprawna
        """
        if not line:
            return False
        
        res = len([i for i in range(len(line)) if line.startswith(';', i)])
        print(res)
        if res != 13:
            return False

        array = line.split(';')
        for word in array:
            if not word:
                return False

        #if not(array[0].isdigit() and array[3].isdigit() and array[4].isdigit() and array[5].isdigit()):
        #    return False


        return True

    def add(self, line):
        """Te metoda dodaje do tablicy pokemon poprawne dane pobrane z linii tekstu dostarczonej z pliku tekstowego

        Args:
            line
                linia tekstu
        """
        array = line.split(';')
        self.users.append(User(int(array[0]), array[1], array[2], array[3], array[4], array[5], int(array[6]), int(array[7]),array[8],float(array[9]),float(array[10]),float(array[11]),int(array[12]),int(array[13])))
    
    def read(self):
        """Główna metoda odczytująca, walidująca i zapisująca dane z pliku
        """
        with open(self.file, 'r') as f:
            for line in f:
                line = line.rstrip()
                if self.check(line):
                    self.add(line)


    def get(self):
        """Metoda zwracająca tablicę z poprawnymi danymi
        """
        return self.users