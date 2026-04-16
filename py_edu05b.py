#--== Python ==--
#Ćwiczenie: Instrukcja warunkowa IF - łączenie warunków.
#
liczba = int(input("Podaj liczbę od 1 do 9: ")) #1
if((liczba > 0) and (liczba < 10)):             #2
 print("Podana liczba to:", liczba)             #3
else:                                           #2
 print("BŁĄD -?Podana liczba jest błędna!")     #4
print("")                                       #5
"""
Legenda:
1. Zadeklarowanie zmiennej "liczba" i przypisanie do niej wartości
   liczbowej, podanej przez użytkownika za pomocą klawiatury.
   Przed przypisaniem do zmiennej "liczba" liczby podanej przez
   użytkownika, następuje konwersja tej liczby do typu integer
   (czyli do typu całkowitego).
=
2. Za pomocą instrukcji warunkowej IF następuje sprawdzenie
   równocześnie dwóch warunków.
   Sprawdzenie polega na zweryfikowaniu, czy zawartość
   zmiennej "liczba" jest większa od 0 i również mniejsza od 10.
   Jeżeli warunki są spełnione, to wykonaj instrukcje umieszczone zaraz
   za warunkiem i dwukropkiem (czyli wyświetl na ekranie tekst umieszczony
   pomiędzy cudzysłowami oraz zawartość zmiennej "liczba" - wiersz nr 6).
   W innym przypadku wykonaj instrukcje umieszczone zaraz za słowem
   else i dwukropkiem (czyli wyświetl na ekranie komunikat
   "BŁĄD -?Podana liczba jest błędna!" - wiersz nr 8).
=
3. Wyświetlenie na ekranie tekstu umieszczonego pomiędzy cudzysłowami
   oraz zawartości zmiennej "liczba". Wyświetlenie to nastąpi dopiero
   po spełnieniu warunków w wierszu nr 5.
=
4. Wyświetlenie na ekranie komunikatu informującego o błędnie wprowadzonej
   liczbie. Ten komunikat jest wyświetlony w momencie, gdy warunek IF
   (wiersz nr 5), nie został spełniony.
=
5. Przeniesienie kursora tekstowego do kolejnego wiersza.
"""