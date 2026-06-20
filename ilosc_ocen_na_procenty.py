'''
--== % udział poszczególnych ocen w całkowitej ilości ocen ==--
Copyright (c)by Jan T. Biernat
'''
licznik = 0
ocena = 0
suma = 0
procent = 0
oceny = []
#
print("\n--== % udział poszczególnych ocen w całkowitej ilości ocen ==-- \n")
#
#Wprowadzanie danych.
while (licznik < 6):
    ocena = int(input(f"Ocena {licznik+1}: "))
    if(ocena < 0): ocena = 0
    oceny.append(ocena)
    suma += ocena
    licznik+= 1
#
#Procentowy udział poszczególnych ocen w całkowitej ilości ocen.
licznik = 0
print("\nSuma ocen: ", suma)
print("\n Ocena | Ilość |   % ")
print("-"*23)
while(licznik < 6):
    procent = 0
    procent = round(oceny[licznik]*100/suma, 2)
    print(f" {licznik+1:5} | {oceny[licznik]:5} | {procent:5}")
    licznik+= 1
#
#Czekaj, aż użytkownik naciśnie klawisz ENTER.
input("\n \nNaciśnij klawisz ENTER ...")