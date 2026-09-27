def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def calculate_total(price, quantity):
    return price * quantity


def get_student_name(students, index):
    if 0 <= index < len(students):
        return students[index]
    return "Student not found"


numbers = [10, 20, 30, 40]
print("Average:", calculate_average(numbers))

price = 100
quantity = 2
print("Total:", calculate_total(price, quantity))

students = ["Aman", "Rahul", "Priya"]
print("Student:", get_student_name(students, 1))