class Duree:
    def __init__(self,heure,minute,seconde):
        self.__heure = heure
        self.__minute = minute
        self.__seconde = seconde

    def __str__(self):
        return (str(self.__heure)+"h"+str(self.__minute)+"m"+str(self.__seconde)+"s")

    def __add__(self, other):
        seconde = self.__seconde + other.__seconde
        minute = self.__minute + other.__minute + (seconde//60)
        heure = self.__heure + other.__heure   + (minute//60)
        return Duree(heure,minute%60,seconde%60)

heure1 = Duree(13,15,50)
heure2 = Duree(2,50,28)
print(heure1)
print(heure1+heure2)
