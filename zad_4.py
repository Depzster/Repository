def check_sum(num1, num2, num3):
    sum_of_first_two = num1 + num2
    return sum_of_first_two >= num3


num1 = int(input("Podaj pierwszą liczbę: "))
num2 = int(input("Podaj drugą liczbę: "))
num3 = int(input("Podaj trzecią liczbę: "))
result = check_sum(num1, num2, num3)

if result:
    print("Suma dwóch pierwszych liczb jest większa lub równa trzeciej.")
else:
    print("Suma dwóch pierwszych liczb jest mniejsza niż trzecia.")
