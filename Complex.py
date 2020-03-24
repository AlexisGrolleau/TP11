class Complex:
    def __init__(self,re,im):
        self.__re = re
        self.__im = im

    def __add__(self, other):
        return Complex(self.__re + other.__re,self.__im + other.__im)
    def __sub__(self, other):
        return Complex(self.__re - other.__re,self.__im - other.__im)
    def __mul__(self, other):
        partre = self.__re * other.__re - self.__im * other.__im
        partim = self.__re * other.__im + self.__im * other.__re
        return Complex(partre,partim)
    def __truediv__(self, other):
        denum = other.__re ** 2 + other.__im **2
        partre = self.__re * other.__re + self.__im * other.__im
        partim = self.__im * other.__re - self.__re * other.__im
        return Complex(partre/denum,partim/denum)

    def __abs__(self):
        return (self.__re**2 + self.__im**2) ** (1/2)

    def __eq__(self, other):
        return (self.__re == other.__re) and (self.__im == other.__im)
    def __ne__(self, other):
        return not (self.__re == other.__re) and (self.__im == other.__im)
