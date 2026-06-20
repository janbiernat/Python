'''
--== Tablica ASCII 2, f ==--
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
print("\n--==Tablica ASCII 2, f ==--\n")
print(" Znak | Kod | HEX | BIN")
print('-'*30)
for znak in range(95):
    print("  ", f"{chr(znak+32):2} | {znak+32:3} | {hex(znak+32).upper()[2:]:3} | {dec2bin(znak+32):9} ")
#
#Czekaj, aż użytkownik naciśnie klawisz ENTER.
input("\nNaciśnij klawisz ENTER ...")
'''
 Tablica kodów ASCII (ang. American Standard Code for Information 
 Interchange) stanowi zestaw kodów używanych do reprezentacji znaków 
 (liter, cyfr, znaków specjalnych np. @, $, # itp.). 
 Każdy znak w tabeli ma przyporządkowaną wartość liczbową dziesiętną, 
 np. litera duża "A"  ma wartość dziesiętną 65. 
 Tablica ASCII składa się 255 znaków, które podzielone są na kilka grup: 
   > Od 0 do 31 - znaki sterujące np. klawiszem ENTER, TAB, drukarką; 
   > Od 32 do 126 - znaki podstawowe; 
   > Od 127 do 255 - znaki dodatkowe (zawierają znaki graficzne, 
                     oraz znaki polskie itp.). 
 Podstawowa tabela ASCII (tj. od 0 do 127) nie podlega wymianie, 
 natomiast rozszerzona tablica (tj. od 128 do 255) może ulegać zmianie 
 np. w celu zakodowania polskich znaków.
 =
 Legenda:
 Zapis hex(255)[2:] zwróci ff
 Zapis hex(255)     zwróci 0xff
 Zapis bin(10)[2:] zwróci 1010
 Zapis bin(10)     zwróci 0b1010
'''
