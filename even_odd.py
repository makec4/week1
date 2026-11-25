liczba = input("podaj liczbę całkowitą")
liczba1 = int(liczba)
liczba2 = liczba1 % 2
liczba3 = bool(liczba2)
if liczba3 == False:
	print("parzysta")
if liczba3 == True:
	print("nieparzysta")
