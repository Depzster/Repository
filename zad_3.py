def is_even(number):
    return number % 2 == 0


num = int(input("Podaj liczbę: "))
result = is_even(num)

if result:
    print("Liczba jest parzysta.")
else:
    print("Liczba jest nieparzysta.")
