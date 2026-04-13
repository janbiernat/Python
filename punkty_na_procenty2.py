#Punkty na procenty.
#(c) by Jan T. Biernat
#
#Napisz program, który obliczy
#jaki procent stanowi dany punkt
#względem maksymalnej liczby punktów.
#Np.: mamy 5 punktów, które
#     stanowią 50% względem
#     maksymalnej ilości punktów
#     (tj. 10 punktów).
#
punkty_t = input("Maksymalna ilość punktów: ")                  #1
punkty = int(punkty_t)                                          #2
if(punkty > 0):                                                 #3
    print("")                                                   #4
    print(" Punkty | % ")                                       #5
    linia = "-" * 16                                            #6
    print(linia)                                                #7
    for i in range(punkty):                                     #8
        w = i+1                                                 #9
        procent = round((w*100)/punkty, 2)                      #10
        print(f"{(w):7}", "|", f"{(procent):5}")                #11
else:                                                           #3
    print("BŁĄD -?Podana ilość punktów musi być większa od 0!") #12
print("")                                                       #4
input("Naciśnij ENTER ...")
"""
Legenda:
1. Wiersz 12.
   Pobranie danych z klawiatury i przypisanie tych
   danych do zmiennej tekstowej o nazwie "punkty_t".
   Do pobrania danych z klawiatury służy
   instrukcja INPUT, która posiada jeden
   parametr. W tym parametrze umieszcza się treść,
   który jest wyświetlany na ekranie przed
   wprowadzeniem danych.
=
2. Wiersz 13.
   Konwersja zawartości zmiennej tekstowej "punkty_t" na typ integer
   i przypisanie tych wartości liczbowych całkowitych do zmiennej
   o nazwie "punkty".
=
3. Wiersz 14.
   Sprawdzenie za pomocą instrukcji warunkowej IF, czy zawartość
   zmiennej liczbowej całkowitej "punkty" jest większa od wartości
   zerowej. Jeżeli warunek jest spełniony (tzn. zawartość zmiennej
   "punkty" > 0), to wykonaj instrukcje od linii 15 do 22 włącznie.
   W innym przypadku wyświetl komunikat o błędnie wprowadzonej
   wartości - linia 24 (komentarz nr 12). Komunikat znajduje się
   za wyrazem "else:".
=
4. Wiersz 15. Przeniesienie kursora tekstowego do kolejnego wiersza.
=
5. Wiersz 16. Wyświetlenie na ekranie tekstu umieszczonego pomiędzy cudzysłowami.
=
6. Wiersz 17. Przypisanie do zmiennej tekstowej "linia" szesnastu znaków minus (tj. -).
   Zapis "-"*16 oznacza zwielokrotnienie znaku "-" do 16 powtórzeń,
                następnie następuje przypisanie tych znaków do zmiennej
                tekstowej "linia".
=
7. Wiersz 18. Wyświetlenie na ekranie 16 znaków minus.
=
8. Wiersz 19. Za pomocą pętli FOR następuje powtórzenie z góry
   określoną ilość razy instrukcji umieszczonych w liniach
   od 20 do 22 włącznie.
   Instrukcje te są umieszczone w kolejnych liniach, które
   są przesunięte względem pętli FOR minimum o jeden znak
   spacji w prawą stronę.
   Ilość powtórzeń jest określona przez wartość przechowywaną
   w zmiennej liczbowej całkowitej "punkty".
=
9. Wiersz 20. Zapis w = i+1 powoduje przypisanie do zmiennej
   liczbowej całkowitej "w" wartości przechowywanej w zmiennej
   liczbowej całkowitej "i", zwiększonej o wartość 1.
   Do zmiennej liczbowej całkowitej "i" przypisywana jest
   wartość liczbowa nadawana przez pętli FOR.
   W powtórzeniu 1 pętli do zmiennej "i" wpisana jest wartości 0.
   W powtórzeniu 2 pętli do zmiennej "i" wpisana jest wartość 1.
   W powtórzeniu N pętli do zmiennej "i" wpisana jest wartość N
   i po tym powtórzeniu następuje zakończenie wykonania pętli.
=
10. Wiersz 21. Oblicz ile procent stanowi dany punkt
    względem maksymalnej liczby punktów.
    Obliczenia wykonane są na podstawie wzoru:
       procent = ((punkt*100)/maksymalna_ilosc_punktow).
    Do zaokrąglenia wyniku obliczeń do 2 miejsc po przecinku
    służy instrukcja round. Instrukcja round(p1, p2) posiada
    dwa parametry.
    Parametr 1 (p1) - to jest liczba, która podlega zaokrągleniu.
    Parametr 2 (p2) - umożliwia określenie za pomocą liczby ilości
                      miejsc po przecinku.
=
11. Wiersz 22. Wyświetlenie na ekranie obliczonych procentów
    dla wybranych punktów.
    Zapis f"{(w):7}":
      a) f - oznacza informację, że liczba będzie formatowana.
      b) {(w):7} - zawartość zmiennej liczbowej całkowitej "w"
                   będzie wyświetlana na ekranie z wiodącymi
                   znakami pustymi (tj. znakami spacji) przed
                   wyświetlaną liczbą.
                   Np.: jest liczba 5, to przed tą liczbą
                        umieszczone zostaną 6 znaków pustych
                        Znaki puste i liczba 5 stanowi 7 znaków,
                        tj. liczbę umieszczoną po znaku dwukropka.
                   Takie formatowania umożliwia wyświetlanie liczba
                   w konfiguracji: jednostki pod jednostkami,
                                   dziesiątki pod dziesiątkami,
                                   setki pod setkami i tak dalej.
=
12. Wiersz 24. Wyświetlenie na ekranie komunikatu o błędnie
    wprowadzonej wartości przez użytkownika.
"""
