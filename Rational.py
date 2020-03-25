from decimal import Decimal
class Rational:
    def __init__(self,num,denum):
        self.__num = num
        self.__denum = denum

    def __str__(self):
        return (f"le rationnel est {self.__num} / {self.__denum}")

    def __add__(self, other):
        if self.__denum == other.__denum:
            return Rational(self.__num + other.__num,self.__denum)
        else:
            num = self.__num * other.__denum + other.__num * self.__denum
            denum = self.__denum * other.__denum
            return Rational(num,denum)
    def __sub__(self, other):
        if self.__denum == other.__denum:
            return Rational(self.__num - other.__num,self.__denum)
        else:
            num = self.__num * other.__denum - other.__num * self.__denum
            denum = self.__denum * other.__denum
            return Rational(num,denum)

    def __mul__(self, other):
        return Rational(self.__num*other.__num,self.__denum*other.__denum)


ratio1 = Rational(6,5)
ratio2 = Rational(4,5)
print(ratio1)
print(ratio2)
print(ratio1+ratio2)
print(ratio1-ratio2)
print(ratio1*ratio2)
