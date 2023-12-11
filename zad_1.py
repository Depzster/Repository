class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50


student1 = Student("Jan Kowalski", [60, 75, 80, 90])
student2 = Student("Anna Nowak", [40, 35, 50, 45])

result1 = student1.is_passed()
result2 = student2.is_passed()

print(f"Czy {student1.name} zdał/a? {result1}")
print(f"Czy {student2.name} zdał/a? {result2}")
