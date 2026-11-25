początek notatek

#task.1.1
1.Aby podać typ wartości używamy funkcji type, a przykładowe użycie
wygląda tak: type(false).
2.Aby sprawdzić typ wartości a następnie go wyświetlić korzystamy z 
funkcji print a przykład to: print(type(false)). W ten sposób możemy 
wyświetlić wszyskie typy wartości.
3.Aby określić wartość wyniku np. 10/2 używamy funkcji type(działanie),
przykładowo type(2**3).
4.Python na początku przyjmuje wszystkie wpisane inputy jako tekst,
czyli <class>str (string), lecz możemy to zmienić.
5.Aby od razu mieć wybrany typ wartości w inpucie, trzeba przed samym
inputem zrobić odpowiednią niewiadomą np: wiek = int(input("podaj wiek"))
W wyżej ukazanym przypadku zależało nam na typie wartości jako liczby
całkowitej, więc użyliśmy int przed nawiasem z inputem. Jeżeli chciałbym
mieć float, to w miejsce int wpisałbym float.
6.W momencie, w którym chciałbym sprawdzić typ wartości tej niewiadomej
w funkcji type(....) w nawiasie zamiast liczby wpisuje nazwę niewiadomej.
np:tpye(age)
<class>int
7.W razie potrzeby sprawdzenia typu wartości działania, możemy to wykonać
za pomocą funkcji type(działanie) np: type(10//2).

#task1.2
1.Aby zmienić typ wartości z str na int, trzeba wpisać int przed nawias z
wartością string w ten sposób: tekst = "22" liczba = int(tekst). Działa
to tylko wtedy, kiedy w stringu jest liczba całkowita w nawiasie i kiedy
wykorzystamy do tego nieiwadome.
2.Aby zmienić tyo wartości ze string na float to wykorzystujemy dwie 
niewiadome, podobnie jak punkt wyżej tylko zamiast int jest float, a 
wymagania to liczba całkowita, lub zmiennoprzecinkowa w nawiasie.
3.Przed liczbą typu float (zmiennoprzecinkową) wpisujemy int, po czym 
liczbę dajemy w nawias: height=185.7 float(height)
4.W przypadku zmiany typu wartości z int na float robimy to samo co 
powyżej, tylko wpisując na odwrót funkcje: age = 16 float(age).
5.Liczba całkowita wpisana w pythonie ma wartość int, do momentu kiedy 
jest w nawiasie. Wtedy jest to str: type(99)
<class>int
type("99")
<class>str
Natomiast, żeby zmienić tą wartość z int na str należy wpisać:
age = 34
wiek = str(age)
Wtedy wyświetli się <class>str, co znaczy, że opercja przeszła pomyślnie.
6.Aby zmienić wartość ze str na bool, należy użyć funkcji bool:
bool("jajko")
True -oznacza, że wartość ma oczekiwany przez nas typ i w tym przypadku 
wynosi prawdę (ma wartość).
7.Sytuacja ze zmianą liczby (str) na prawdę/fałsz (bool) wygląda 
podobnie do powyższej. Piszem więc:
bool(586)
True
bool(0)
False
8.Przykładowa niemożliwa zamiana to ze str na int:
age = 89
str(89)
w tym miejscu byłby błąd oznajmujący nam, iż ta operacja jest
niemożliwa ze względów logicznych.
9.Zamiany, które tracą informacje to np:
age = 20
str(age)
"20"
type(age)
<class>int
w momencie wpisania type(age), spodziewamy się typu str, bo wygląda 
jakby został zmieniony, a tak jednak w momencie wpisania type(age)
uzyskujemy typ wartości int, czyli ten pierwotny.
10.Porównując int(3.75) z round(3.75), możemy zauważyć, że int bierze 
pełną liczbę, kiedy round zaokrągla ją , tak, jakbyśmy się tego 
spodziewali:
 int(3.75)
3
round(3,75)
4 

#task1.3
Podczas tworzenia krótkiego programu wyswietlił mi się błąd : 
ValueError: invalid literal for int() with base 10: '2.5'
Mimo, że widzimy liczbę zmiennoprzecinkową, to python wyczytuje ją jako string przez to, że jest w cudzysłowie. 
Właśnie dlatego nie możemy zmienić typu wartości z domniemanego floata (który był stringiem) na inta.
 
-question to investigate:
1.Kiedy użyjemy int(fraction) zaokrągli nam w dół do pełnej całości, a round(fraction) zaokrągli nam w sposób właściwy (matematycznie).
2.float(text_decimal) działa, bo musi przenieść wartość z str na float, a int musiałby przenieść wartość dwukrotnie: z str na float i z float na int 
3.str(whole) to wartość 'pisemna' a whole jest zmienną z wpisaną wartością matematyczną.
4.bool("0") jest wartością prawdziwą (True), ponieważ zero jest w nawiasie, co zmienia wartość z matematycznej na 'pisemną' .
5.
Zmiana typu wartości zmienia typ wartości, nie tworzy nowej, dlatego nie można zmienić np. str na int (oprócz cyfr w cudzysłowie).
6.Przykład odwracalnej przemiany wartości to ze string na bool,int na float.
7.round() zaokrągla lczbę, a int() bierze tylko całość np:
round(3.77)
4
int(3.77)
3
8.Nic niespodziewanego się nie stanie, po prostu zostaną odrzucone białe znaki (spacje) pomiędzy cudzysłowiem, a liczbą.


#task1.4
Zrobione, działa prawidłowo.

#task2.1

1.Operator == sprawdza, czy dwie wartości są równe.
np.5 == 5 True  ,  4 == 5 False 
2.Operator != sprawdza, czy dwie wartości są różne.
np.4 != 5 True  ,  5 != 5 False
3.Operator > sprwadza, czy liczba (z lewej strony znaku) jest większa od drugiej (tej z prawej)
np.4>3 True  , 4>5  False
4.Operator < sprwadza, czy liczba (z lewej strony znaku) jest mniejsza od drugiej (z prawej strony znaku)
np. 4<6 True  ,  4<3 False
5.Operator >= sprawdza, czy liczba (z lewej strony znaku) jest większa lub równa od drugiej liczby (z prawej storny znaku)
np. 4 >= 4  ,  True 4>=3 False
6.Operator <= sprawdza czy liczba (z lewej strony znaku) jest mniejsza lub równa od drugiej (z prawej strony znaku)
np. 4<=5 True  ,  4<=2  False 

#task2.2 
Experiment
Questionos to investigate:
1.Różnica wychodzi z własności znaku w pythonie: = służy do przypisania zmiennej, a == porównuje ze sobą dwie liczby.
2.Można porównać ze sobą dwa stringi. np. "jajko" == "kura" False
3.Można bezproblemowo porównać ze sobą dwa różne typy liczb (całkowitą i zmiennoprzecikową) np. -3 == -3.0 True

#task3.1
1.and-jeśli lewa storna ma wartość fałszywą to "wygrywa" i and przyjmuje jej wartość, a jeśli jest prawdziwa (True), to bierze tą drugą>
2.or-jeśli lewa jest prwadziwa, to bierze lewą (działa odwrotnie do and), a jeśli lewa jest fałszywa, to bierze prawą.
3.not-zwraca True/False, lecz odwraca prawdziwość, czyli: not 5  False (5 jest prawdziwe) , not 0 True (0 jest fałszywe). (not zmienia wynik na bool).

#task3.2
W programie logic.py:
And dawał True wtedy, gdy oby dwa warunki zostały spełnione.
Or dawał True wtedy, kiedy chociaż jeden warunek zostawał spełniony.
Not zmienia wartość bool-ową na przeciwną (np. not 5 = False-5 normalnie ma wartość)

#task4.1
muszę dokończyć, bo nie dzxiała na razie idę dalej

#task4.2
 
 
