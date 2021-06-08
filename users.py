import matplotlib.pyplot as plt
import numpy as np
import math as m
import pandas as pd
import seaborn as sns

class User:

    def __init__(self, id, name, surname, region, email, camera, res_width, res_height, codec, sensor_width, sensor_height, exp_time, ar_width, ar_height):
        """Ta metoda inicjuje obiekt klasy Pokemon, przypisująca mu podane wartości

        Args:
            number
                numer pokemona w pokedexie
            name
                nazwa pokemona
            ptype
                typ pokemona
            atk
                atak pokemona wyrazona za pomoca liczby
            deff 
                obrona pokemona wyrazona za pomoca liczby
            spd
                szybkosc pokemona wyrazona za pomoca liczby
            desc
                opis pokemona
            img
                nazwa pliku zawierajacego obrazek pokemona

        """
        self.__id = id
        self.__name = name
        self.__surname = surname
        self.__region = region
        self.__email = email
        self.__camera = camera
        self.__res_width = res_width
        self.__res_height = res_height
        self.__codec = codec
        self.__sensor_width = sensor_width
        self.__sensor_height = sensor_height
        self.__exp_time = exp_time
        self.__ar_width = ar_width
        self.__ar_height = ar_height
    
    @property
    def id(self):
        """Ta metoda zwraca nam numer w pokedexie pokemona.
        ulatwia to zdobycie zmiennej prywatnej.
        """
        return self.__id

    @property
    def name(self):
        """Ta metoda zwraca nam nazwe pokemona.
        ulatwia to zdobycie zmiennej prywatnej.
        """
        return self.__name

    @property
    def surname(self):
        """Ta metoda zwraca nam typ pokemona.
        ulatwia to zdobycie zmiennej prywatnej.
        """
        return self.__surname

    @property
    def region(self):
        """Ta metoda zwraca nam nazwe pokemona.
        ulatwia to zdobycie zmiennej prywatnej.
        """
        return self.__region

    @property
    def email(self):
        """Ta metoda zwraca nam nazwe pokemona.
        ulatwia to zdobycie zmiennej prywatnej.
        """
        return self.__email

    @property
    def camera(self):
        """Ta metoda zwraca nam nazwe pokemona.
        ulatwia to zdobycie zmiennej prywatnej.
        """
        return self.__camera

    @property
    def res_width(self):
        return self.__res_width
    
    @property
    def res_height(self):
        return self.__res_height
    
    @property
    def codec(self):
        return self.__codec

    @property
    def sensor_width(self):
        return self.__sensor_width
    
    @property
    def sensor_height(self):
        return self.__sensor_height

    @property
    def exp_time(self):
        return self.__exp_time

    @property
    def ar_width(self):
        return self.__ar_width
    
    @property
    def ar_height(self):
        return self.__ar_height

    
    
    
    '''
    @atk.setter
    def atk(self, value):
        """Ta metoda sprawdza czy wprowadzona wartość jest mniejsza od minimalnej i w tym przypadku ustawia wartość ataku pokemona na minimum, czyli 10.

        Args:
                value
                    wartość ataku pokemona
        """
        if value >= 10:
            self.__atk = value
        else:
            self.__atk = 10

    @deff.setter
    def deff(self, value):
        """Ta metoda sprawdza czy wprowadzona wartość jest mniejsza od minimalnej i w tym przypadku ustawia wartość obrony pokemona na minimum, czyli 10.

        Args:
                value
                    wartość obrony pokemona
        """
        if value >= 10:
            self.__deff = value
        else:
            self.__deff = 10

    @spd.setter
    def spd(self, value):
        """Ta metoda sprawdza czy wprowadzona wartość jest mniejsza od minimalnej i w tym przypadku ustawia wartość szybkości pokemona na minimum, czyli 10.

        Args:
                value
                    wartość szybkości pokemona
        """
        if value >= 10:
            self.__spd = value
        else:
            self.__spd = 10
    '''