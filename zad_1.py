def welcome_message(name, surname):
    message = f"Czesc {name} {surname}!"
    return message


name = input("Podaj imie: ")
surname = input("Podaj nazwisko: ")

result = welcome_message(name, surname)
print(result)
