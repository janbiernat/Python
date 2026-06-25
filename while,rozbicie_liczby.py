#--== Rozbicie liczby ==--
#Copyright (c)by Jan T. Biernat
#
opis = [ "jedności"
       , "dziesiątki"
       , "setki"
       , "tysiące"
       , "dziesiątki tysięcy"
       , "setki tysięcy"
       , "miliony"
       , "dziesiątki milionów"
       , "setki milionów"
       , "miliard" ]
l = 0
a = 0
#
#Pobranie danych od użytkownika.
l = int(input("Liczba: "))
#
#Rozbij liczbę.
while (l > 0):
    if (a > 0): print(", \n", end="")
    print(f"{(a+1):2}) ", (l % 10), " - ", opis[a], end="")
    l //= 10
    a+= 1
print(". \n \n")