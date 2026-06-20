'''
--== Dec2Bin ==--
Copyright (c)by Jan T. Biernat
'''
liczba = 0
tmp = 0
spacja = 0
bin = ""
#
print("\n--== Dec2Bin ==-- \n")
#
#Pobranie danych.
liczba = int(input("Liczba (DEC): "))
if(liczba < 0): liczba = 0
tmp = liczba
#
#Przelicz z systemu dziesiętnego (DEC) na dwójkowy (BIN).
while(liczba > 0):
    if(spacja > 3):
        bin = ' '+bin
        spacja = 0
    spacja+= 1
    if(liczba % 2 == 0): bin = '0'+bin
    else: bin = '1'+bin
    liczba = liczba // 2
print("\n", tmp, " = ", bin)
#
#Czekaj, aż użytkownik naciśnie klawisz ENTER.
input("\nNaciśnij klawisz ENTER ...")
