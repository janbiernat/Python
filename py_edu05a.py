#--== Python ==--
#Ćwiczenie: Instrukcja warunkowa IF.
#
a = float(input("A: "))                                  #1
b = float(input("B: "))                                  #2
if(b == 0):                                              #3
 print("BŁĄD -?Dzielenie przez zero jest niewykonalne!") #4
else:                                                    #3
 print(a, " / ", b, " = ", (a/b))                        #5
print("")                                                #6
"""
Legenda:
1. Zadeklarowanie zmiennej "a" i przypisanie do niej wartości
   liczbowej, podanej przez użytkownika za pomocą klawiatury.
   Przed przypisaniem do zmiennej "a" liczby podanej przez
   użytkownika, następuje konwersja tej liczby do typu float
   (czyli do typu rzeczywistego).
=
2. Zadeklarowanie zmiennej "b" i przypisanie do niej wartości
   liczbowej, podanej przez użytkownika za pomocą klawiatury.
   Przed przypisaniem do zmiennej "b" liczby podanej przez
   użytkownika, następuje konwersja tej liczby do typu float
   (czyli do typu rzeczywistego).
=
3. Sprawdzenie za pomocą instrukcji warunkowej IF,
   czy zawartość zmiennej liczbowej rzeczywistej "b" jest
   równa zeru (czyli, czy lewa strona równania równa się
   prawej stronie).
   Jeżeli równanie jest prawdziwe (tzn. zawartość zmiennej
   "b" = 0), to wykonaj instrukcje umieszczone zaraz za warunkiem
   i dwukropkiem (czyli wyświetl komunikat "BŁĄD -?Dzielenie
   przez zero jest niewykonalne!" - wiersz nr 7).
   W innym przypadku wykonaj instrukcje umieszczone po słowie
   else:, tj. wykonaj dzielenie dwóch podanych liczb.
=
4. Wyświetlenie na ekranie komunikatu umieszczonego pomiędzy cudzysłowami.
   Ten komunikat będzie wyświetlony dopiero po spełnieniu warunku IF
   w wierszu nr 6.
=
5. Wyświetlenie na ekranie:
   5.1. Zawartości zmiennej liczbowej rzeczywistej "a".
   5.2. Znaku ukośnika (czyli /).
   5.3. Zawartości zmiennej liczbowej rzeczywistej "b".
   5.4. Znaku równania (czyli =).
   5.5. Wyniku dzielenie dwóch liczb.
=
6. Przeniesienie kursora tekstowego do kolejnego wiersza.
"""
