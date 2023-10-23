class Student:
    def __init__(self, name, id_number, grades):
        self.name = name
        self.id_number = id_number
        self.grades = grades

    def calculate_average(self):
        """Calculates the student's average grade."""
        total_points = 0
        for grade in self.grades:
            total_points += grade
        return total_points / len(self.grades)

    def get_total_points(self):
        """Calculates the student's total points."""
        total_points = 0
        for grade in self.grades:
            total_points += grade
        return total_points

    def __str__(self):
        return f"Student: {self.name}, ID: {self.id_number}, Average: {self.calculate_average():.2f}"


class Teacher:
    def __init__(self, name, id_number, students):
        self.name = name
        self.id_number = id_number
        self.students = students

    def calculate_class_average(self):
        """Calculates the average grade of all students in the teacher's class."""
        total_points = 0
        for student in self.students:
            total_points += student.get_total_points()
        return total_points / len(self.students)

    def get_best_student(self):
        """Returns the student with the highest average grade in the teacher's class."""
        best_student = None
        highest_average = 0
        for student in self.students:
            average = student.calculate_average()
            if average > highest_average:
                best_student = student
                highest_average = average
        return best_student

    def __str__(self):
        return f"Teacher: {self.name}, ID: {self.id_number}, Class Average: {self.calculate_class_average():.2f}"


# Example usage:

students = [
    Student("Alice", 1, [90, 85, 95]),
    Student("Bob", 2, [80, 75, 90]),
    Student("Carol", 3, [70, 80, 85]),
]

teacher = Teacher("Mr. Smith", 4, students)

class_average = teacher.calculate_class_average()
print(f"Class average: {class_average:.2f}")

best_student = teacher.get_best_student()
print(f"Best student: {best_student}")