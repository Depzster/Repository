def pomnoz_przez_dwa_for(lista):
    wynik=[]
    for liczba in lista:
        wynik.append(liczba*2)
    return wynik
lista=[1, 2, 3, 4, 5]
wynik_for=pomnoz_przez_dwa_for(lista)
print(wynik_for)
