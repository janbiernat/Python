'''
--== Dec2Bin ==--
Copyright (c)by Jan T. Biernat
'''
liczba = 0
tmp = 0
spacja = 0
bin_ = ""
#
print("\n--== Dec2Bin ==-- \n")
#
#Pobranie danych.
liczba = int(input("Liczba (DEC): "))
if(liczba < 1): liczba = 1
tmp = liczba
#
#Przelicz z systemu dziesiętnego (DEC) na dwójkowy (BIN).
while(liczba > 0):
    if(spacja > 3):
        bin_ = ' '+bin_
        spacja = 0
    spacja+= 1
    if(liczba % 2 == 0): bin_ = '0'+bin_
    else: bin_ = '1'+bin_
    liczba = liczba // 2
print("\n", tmp, " = ", bin_)
#
#Czekaj, aż użytkownik naciśnie klawisz ENTER.
input("\nNaciśnij klawisz ENTER ...")