from PyQt5 import QtCore, QtGui, QtWidgets, uic
from db import Database
import sqlite3
import sys
import matplotlib.pyplot as plt
import numpy as np
import math as m
import pandas as pd
import seaborn as sns
from functools import partial
from users import User
from matplotlib.patches import Rectangle

def truncate(num,n):
    temp = str(num)
    for x in range(len(temp)):
        if temp[x] == '.':
            try:
                return float(temp[:x+n+1])
            except:
                return float(temp)      
    return float(temp)

class Dialog(QtWidgets.QDialog):
    
    def __init__(self):
        """ Ta metoda to jest konstruktor, który inicjuje całe okno dialogowe.
        """
        super().__init__()
        self.layout = QtWidgets.QHBoxLayout()
        self.window = QtWidgets.QWidget()
        self.window.setFixedSize(200,150)
        self.setWindowTitle("CREDITS")
        self.label = QtWidgets.QLabel("Twórcy: Jan Biskupski, Jakub Wojciechowski")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

class Calc(QtWidgets.QMainWindow):
    def __init__(self,user):
        super(Calc, self).__init__()
        uic.loadUi("calc.ui", self)
        if user[4] == 'USA':
            print('bezpieczne czasy: 1/48, 1/60, 1/120')
        self.text = user[1]
        self.camname.setText(user[5])
        self.sensorres.setText(str(user[6])+'x'+str(user[7]))
        self.aspratio.setText(str(user[12])+':'+str(user[13]))
        self.sensordim.setText(str(user[9])+'x'+str(user[10])+'mm')

        c1 = m.sqrt((36**2)+(24**2))
        c2 = m.sqrt((user[9]**2)+(user[10]**2))
        cropfirst = c1/c2
        cropfirst = truncate(cropfirst,2)
        self.cropfactor.setText(str(cropfirst))
        
        self.calc.clicked.connect(partial(self.danehehe,user))
        self.tworcy.clicked.connect(self.tworcyf)

    def tworcyf(self):
        """Metoda wywołująca okno dialogowe z informacją o twórcach tego programu.
        """
        dial = Dialog()
        dial.exec_()

    def danehehe(self,user):
        self.plot.setStyleSheet("background-color: rgb(34, 35, 35);color: rgb(198, 202, 202);font-weight: 600;font-size: 16px;border: 1px solid rgb(27, 28, 28);border-radius: 8px;")
        resx = self.resx.text()
        #print(resx)
        resx = int(resx)
        resy = self.resy.text()
        resy = int(resy)
        #print(user[7])
        yprzezy = resy/user[7]
        print(yprzezy)
        cropdimy = user[10]*yprzezy
        c3 = m.sqrt((36**2)+(24**2))
        c4 = m.sqrt((user[9]**2)+(cropdimy**2))
        cropparttwo = c3/c4
        cropparttwo = truncate(cropparttwo,2)
        asprcalc = resx/resy
        asprcalc = truncate(asprcalc,2)
        self.cropfactorcalc.setText(str(cropparttwo))
        self.aspratiocalc.setText(str(asprcalc)+':1')
        self.plot.clicked.connect(partial(self.stats,user,user[9],cropdimy))



    
    def stats(self,user,cropdimx,cropdimy):
        """Ta metoda wyświetla wykres radarowy statystyk danego pokemona
        """
        plt.figure("STATS")
        #define Matplotlib figure and axis
        fig, ax = plt.subplots()


            #add rectangle to plot
        ax.add_patch(Rectangle((1, 1), int(cropdimx), int(cropdimy),
                        edgecolor = 'red',
                        facecolor = 'red',
                        fill=True,
                        lw=1))

        #display plot
        plt.show()

class Info(QtWidgets.QMainWindow):
    def __init__(self,user):
        super(Info, self).__init__()
        uic.loadUi("info.ui", self)
        self.text = user[1]
        self.pokemon = User(user[0],user[1],user[2],user[3],user[4],user[5],user[6],user[7],user[8],user[9],user[10],user[11],user[12],user[13])
        self.Name.setText(user[1]+' '+user[2])
        self.email.setText(user[4])
        self.camname.setText(user[5])
        self.sensorres.setText(str(user[6])+'x'+str(user[7]))
        self.codec.setText(user[8])
        self.sensordim.setText(str(user[9])+'x'+str(user[10])+'mm')
        self.aspratio.setText(str(user[12])+':'+str(user[13]))
        self.tworcy.clicked.connect(self.tworcyf)
        self.calc.clicked.connect(self.calcWindow)



    def getOne(self, index):
        """Ta metoda akceptuje zaznaczony indeks z tabeli z bazy danych i zwraca nam tablice z danymi danego wiersza o tym indeksie

        Args:
            index
                indeks zaznaczonego/przekazanego elementu z tabeli w bazie danych

        Returns:
            result
                zwraca nam tablice z danymi wiersza o danym indeksie
        """
        conn = sqlite3.connect("mydatabase.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE id = {}".format(int(index)))
        result = c.fetchone()
        conn.commit()
        conn.close()
        return result

    def calcWindow(self):
        conn = sqlite3.connect("mydatabase.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE id = {}".format(int(0)))
        #iksde = self.tableWidget.selectedIndexes()
        #index = iksde[0].data()
        user = self.getOne(1)
        print(user)
        self.ui = Calc(user)
        self.ui.show()
    
    def tworcyf(self):
        """Metoda wywołująca okno dialogowe z informacją o twórcach tego programu.
        """
        dial = Dialog()
        dial.exec_()

    def save(self):
        """zapis opisu o pokemonie do pliku, mozliwe jest tez przywrocenie domyslnych danych za pomoca
        """
        f = open('info.txt','w')
        s = self.text
        f.write(s)
        f.close()
    
    
    def load(self):
        """odczyt opisu o pokemonie z pliku, jednak nie zapisuje tego do obiektu Pokemon, tylko wyświetla tymczasowo na ekranie
        """
        f = open('info.txt')
        ll = ''
        for line in f.readlines():
            ll += line
        f.close()
        self.dataentry.setText(ll)

class Gui(QtWidgets.QMainWindow):
    def __init__(self):
        """ Ta metoda to jest konstruktor, który inicjuje całe okno.
        """
        super(Gui, self).__init__()
        uic.loadUi("main.ui", self)
        user = self.getOne(1)
        self.label.setText('  Witaj, '+user[1])
        #self.tableWidget.itemDoubleClicked.connect(self.infoWindow)
        self.info.clicked.connect(self.infoWindow)
        self.calc.clicked.connect(self.calcWindow)
        self.tworcy.clicked.connect(self.tworcyf)
        #self.tableWidget.verticalHeader().hide()
        self.loadDB()

    def getOne(self, index):
        conn = sqlite3.connect("mydatabase.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE id = {}".format(int(index)))
        result = c.fetchone()
        conn.commit()
        conn.close()
        return result

    def loadDB(self):
        nowa = Database("mydatabase.db", "users")
        nowa.createTable()
        nowa.addToTable("sample.txt")
        res = nowa.getResult()
    
    def tworcyf(self):
        """Metoda wywołująca okno dialogowe z informacją o twórcach tego programu.
        """
        dial = Dialog()
        dial.exec_()
        
    def infoWindow(self, row):
        """
        
        Args:
            index
                indeks zaznaczonego/przekazanego elementu z tabeli w bazie danych
        """
        conn = sqlite3.connect("mydatabase.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE id = {}".format(int(0)))
        #iksde = self.tableWidget.selectedIndexes()
        #index = iksde[0].data()
        user = self.getOne(1)
        print(user)
        self.ui = Info(user)
        self.ui.show()

    def calcWindow(self):
        conn = sqlite3.connect("mydatabase.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE id = {}".format(int(0)))
        #iksde = self.tableWidget.selectedIndexes()
        #index = iksde[0].data()
        user = self.getOne(1)
        print(user)
        self.ui = Calc(user)
        self.ui.show()


def main():
    """Ta metoda nie akceptuje zadnego argumentu, inicjuje, konfiguruje i pokazuje nam główne okno programu Pokedex
    """
    app = QtWidgets.QApplication(sys.argv)
    main = Gui()
    main.show()
    main.setFixedSize(620, 600)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()    