#--== Python ==--
#Kalkulator prosty (+-*/).
#(c) by Jan T. Biernat
#
#Opis:
#Napisz program, który poprosi użytkownika
#o podanie dwóch liczb, następnie poprosi
#o wybranie działania (+-*/) jakie
#ma wykonać.
#
a = float(input("A: "))                                                 #1.
b = float(input("B: "))                                                 #2.
dz = str(input("Jakie wykonać działanie?:"))                            #3.
if(dz == '+'): print(a, " + ", b, " = ", (a+b))                         #4.
elif(dz == '-'): print(a, " - ", b, " = ", (a-b))                       #5.
elif(dz == '*'): print(a, " * ", b, " = ", (a*b))                       #6.
else:                                                                   #7.
    if(b == 0): print("BŁĄD -?Dzielenie przez zero jest niewykonalne!") #8.
    else: print(a, " / ", b, " = ", (a/b))                              #9.
"""
Legenda:
1. Zadeklarowanie zmiennej "a" i przypisanie do niej liczby
   podanej przez użytkowania za pomocą klawiatury.
2. Zadeklarowanie zmiennej "b" i przypisanie do niej liczby
   podanej przez użytkowania za pomocą klawiatury.
3. Zadeklarowanie zmiennej "dz" i przypisanie do niej znaku
   określającego działanie matematyczne (tj. +-*/).
4. Jeżeli podanym znakiem jest znak +, to wykonaj dodawanie
   podanych liczb.
5. Jeżeli podanym znakiem jest znak -, to wykonaj odejmowanie
   podanych liczb.
6. Jeżeli podanym znakiem jest znak *, to wykonaj mnożenie
   podanych liczb.
7. Jeżeli podanym znakiem jest znak / lub użytkownik pomylił znak,
   to wykonaj dzielenie podanych liczb.
8. Jeżeli druga podana liczba jest 0, to wyświetl komunikat
   o braku możliwości wykonania dzielenie liczb.
   W innym przypadku wykonaj dzielenie dwóch liczb.
9. Wykonaj dzielenie dwóch liczb i wyświetl te liczby oraz
   wynik na ekranie.
"""