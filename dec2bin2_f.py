'''
--== Dec2Bin 2, f ==--
Copyright (c)by Jan T. Biernat
'''
def dec2bin(liczba): #Funkcja dec2bin konwertuje liczbę z systemu dziesiętnego na dwójkowy.
    bin_ = ""    
    spacja = 0
    if(liczba < 1): liczba = 1
    while(liczba > 0):
        if(spacja > 3):
            bin_ = ' '+bin_
            spacja = 0
        spacja+= 1
        if(liczba % 2 == 0): bin_ = '0'+bin_
        else: bin_ = '1'+bin_
        liczba = liczba // 2
    return bin_
#
#    
print("\n--== Dec2Bin 2, f ==-- \n")
liczba = int(input("Liczba (DEC): "))
print("\n", liczba, " = ", dec2bin(liczba))
#
#Czekaj, aż użytkownik naciśnie klawisz ENTER.
input("\nNaciśnij klawisz ENTER ...")