def welcome_message(name, surname):
    message = "Cześć " + name + " " + surname + "!"
    return message
name = input("Podaj imię: ")
surname = input("Podaj nazwisko: ")
result = welcome_message(name, surname)
print(result)

