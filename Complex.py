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
        return (self.__re != other.__re) or (self.__im != other.__im)

    def __str__(self):
        return (str(self.__re) + " + i" + str(self.__im))

if __name__ == "__main__":
    complex1 = Complex(1,2)
    complex2 = Complex(2,1)
    print(complex1 + complex2)
    print(complex1 - complex2)
    print(complex1 * complex2)
    print(complex1 / complex2)
    print(abs(complex1))
    print(complex1 == complex2)
    print(complex1 != complex2)
