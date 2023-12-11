from datetime import datetime


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city, self.street, self.zip_code = city, street, zip_code
        self.open_hours, self.phone = open_hours, phone

    def __str__(self):
        return f"Library: {self.city}, {self.street}, {self.zip_code}, {self.open_hours}, {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name, self.last_name = first_name, last_name
        self.hire_date, self.birth_date = datetime.strptime(hire_date, "%Y-%m-%d"), datetime.strptime(birth_date, "%Y-%m-%d")
        self.city, self.street, self.zip_code, self.phone = city, street, zip_code, phone

    def __str__(self):
        return (
            f"Employee: {self.first_name} {self.last_name}, "
            f"Hire Date: {self.hire_date.strftime('%Y-%m-%d')}, "
            f"Birth Date: {self.birth_date.strftime('%Y-%m-%d')}, "
            f"{self.city}, {self.street}, {self.zip_code}, {self.phone}"
        )


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library, self.publication_date = library, datetime.strptime(publication_date, "%Y-%m-%d")
        self.author_name, self.author_surname, self.number_of_pages = author_name, author_surname, number_of_pages

    def __str__(self):
        return (
            f"Book: {self.author_name} {self.author_surname}, "
            f"Publication Date: {self.publication_date.strftime('%Y-%m-%d')}, "
            f"{self.number_of_pages} pages\n{self.library}"
        )


class Order:
    def __init__(self, employee, student_name, books, order_date):
        self.employee, self.student_name, self.books = employee, student_name, books
        self.order_date = datetime.strptime(order_date, "%Y-%m-%d")

    def __str__(self):
        book_list = "\n".join([str(book) for book in self.books])
        return (
            f"Order Date: {self.order_date.strftime('%Y-%m-%d')}\n"
            f"{self.employee}\nStudent Name: {self.student_name}\nBooks:\n{book_list}"
        )


library1 = Library("City1", "Street1", "11111", "9:00 AM - 5:00 PM", "111-222-333")
library2 = Library("City2", "Street2", "22222", "10:00 AM - 6:00 PM", "444-555-666")

employee1 = Employee("John", "Doe", "2023-01-01", "1990-01-01", "City1", "Street1", "11111", "987-654-321")
employee2 = Employee("Jane", "Smith", "2023-02-01", "1985-05-10", "City1", "Street1", "11111", "123-456-789")
employee3 = Employee("Bob", "Johnson", "2023-03-01", "1988-08-15", "City2", "Street2", "22222", "111-222-333")

book1 = Book(library1, "2022-01-01", "Author1", "Surname1", 200)
book2 = Book(library1, "2022-02-01", "Author2", "Surname2", 150)
book3 = Book(library2, "2022-03-01", "Author3", "Surname3", 180)
book4 = Book(library2, "2022-04-01", "Author4", "Surname4", 220)
book5 = Book(library2, "2022-05-01", "Author5", "Surname5", 250)

order1 = Order(employee1, "Student1", [book1, book2, book3], "2023-04-10")
order2 = Order(employee2, "Student2", [book4, book5], "2023-04-15")

print(order1)
print("\n----------------\n")
print(order2)
