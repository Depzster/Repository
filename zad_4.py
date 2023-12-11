def check_sum(num1, num2, num3):
    sum_of_first_two=num1+num2
    return sum_of_first_two>=num3
num1=int(input("Podaj 1 liczbę: "))
num2=int(input("Podaj 2 liczbę: "))
num3=int(input("Podaj 3 liczbę: "))
result=check_sum(num1, num2, num3)
if result:
    print("Suma dwóch pierwszych liczb jest większa lub równa trzeciej.")
else:
    print("Suma dwóch pierwszych liczb jest mniejsza niż trzecia.")
