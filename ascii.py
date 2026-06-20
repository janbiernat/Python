'''
--== Tablica ASCII ==--
Copyright (c)by Jan T. Biernat
'''
print("\n--==Tablica ASCII ==--\n")
print(" Znak | Kod | HEX | BIN")
print('-'*30)
for znak in range(95):
    print("  ", f"{chr(znak+32):2} | {znak+32:3} | {hex(znak+32).upper()[2:]:3} | {bin(znak+32)[2:]} ")
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