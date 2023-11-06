def jezeli(number):
    return number % 2==0
num=int(input("Podaj liczbę: "))
result=jezeli(num)
if result:
    print("parzysta")
else:
    print("nieparzysta")
