import math

T = float(input("donner T"))
DH=6009.5
R=8.314
DC=37.87
try :
    lndea = ((-DH / R) * ((1 / T) - (1 / 273.15))) - ((DC / R) * ((T - 273.15) / T) - (math.log(T / 273.15)))
    print("ln(alfa)=",-lndea)
    alfa = math.exp(lndea)
    print("alfa est de ", alfa)
except :
    print("erreur")
