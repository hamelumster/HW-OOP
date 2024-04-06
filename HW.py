class Student:
    """По заданию №2 (Атрибуты и взаимодействие классов) в классе создан метод выставления оценок лекторам rate_hw.
    По заданию №3 (Полиморфизм и магические методы) перегружен метод __str__.
    Также по заданию №3 в классе добавлен метод __lt__
    для возможности сравнения между собой студентов (в качестве параметра берется средний балл за домашние задания)
    """
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rate = 0

    #Метод выставления оценок лекторам
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Данный метод позволяет посчитать средний балл за домашние задания в рамках одного курса
    def average_grade_student(self):
        if len(self.grades) == 0:
            return 0
        else:
            sum_grades = 0
            count = 0
            for course, grades in self.grades.items():
                sum_grades += sum(grades)
                count += len(grades)
            return sum_grades / count

    # Перегруженный метод __str__ с учетом требуемого вывода информации
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        res += f'\nСредняя оценка за домашние задания: {self.average_grade_student():.2f}'
        res += f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
        res += f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    # Реализован метод __lt__ для возможности сравнения между собой студентов по среднему баллу за домашние задания
    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.average_grade_student() < other.average_grade_student()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """По заданию №1 (Наследование) Добавлен дочерний класс лекторов.
    По заданию №3 (Полиморфизм и магические методы) перегружен метод __str__.
    """
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Данный метод позволяет посчитать средний балл за выставленные оценки студентами;
    # метод идентичен методу average_grade_student в классе Student
    def average_grade_lecturer(self):
        if len(self.grades) == 0:
            return 0
        else:
            sum_grades = 0
            count = 0
            for course, grades in self.grades.items():
                sum_grades += sum(grades)
                count += len(grades)
            return sum_grades / count

    # Перегруженный метод __str__ с учетом требуемого вывода информации
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        res += f'\nСредняя оценка за лекции: {self.average_grade_lecturer():.2f}'
        return res

    # Реализован метод __lt__ для возможности сравнения между собой лекторов по среднему баллу,
    # который посчитан в рамках метода average_grade_lecturer
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.average_grade_lecturer() < other.average_grade_lecturer()


class Reviewer(Mentor):
    """Дочерний класс Mentor, создан по заданию №1 (Наследование)
    Согласно заданию только эксперты (Reviewer) могут выставлять оценки студентам - метод rate_hw указан в классе
    """
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Вывод информации
    # Перегруженный метод __str__ с учетом требуемого вывода информации
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

"""Задание № 4. Полевые испытания.
"""
 # Создаем студентов и определяем для них изучаемые и завершенные курсы
student_1 = Student('Sasuke', 'Uchiha', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Naruto', 'Uzumaki', 'male')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']


# Создаем экспертов и определяем курсы которые они проверяют
reviewer_1 = Reviewer('Hiruzen', 'Sarutobi')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Some', 'Kazekage')
reviewer_2.courses_attached += ['Git']


# Создаем лекторов и определяем курсы которые они ведут
lecturer_1 = Lecturer('Kakashi', 'Hatake')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Jiraya', 'a.k.a. Ero-sensei')
lecturer_2.courses_attached += ['Git']


# Добавляем оценки студентам
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 9)

reviewer_1.rate_hw(student_2, 'Python', 5)
reviewer_1.rate_hw(student_2, 'Python', 6)
reviewer_1.rate_hw(student_2, 'Python', 5)

reviewer_2.rate_hw(student_1, 'Git', 9)
reviewer_2.rate_hw(student_1, 'Git', 8)
reviewer_2.rate_hw(student_1, 'Git', 10)

reviewer_2.rate_hw(student_2, 'Git', 5)
reviewer_2.rate_hw(student_2, 'Git', 6)
reviewer_2.rate_hw(student_2, 'Git', 6)


# Добавляем оценки лекторам
student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 8)
student_1.rate_hw(lecturer_1, 'Python', 9)

student_1.rate_hw(lecturer_2, 'Git', 9)
student_1.rate_hw(lecturer_2, 'Git', 9)
student_1.rate_hw(lecturer_2, 'Git', 7)

student_2.rate_hw(lecturer_1, 'Python', 8)
student_2.rate_hw(lecturer_1, 'Python', 5)
student_2.rate_hw(lecturer_1, 'Python', 6)

student_2.rate_hw(lecturer_2, 'Git', 6)
student_2.rate_hw(lecturer_2, 'Git', 7)
student_2.rate_hw(lecturer_2, 'Git', 7)

print(f'Список студентов:\n'
      f'{student_1}\n'
      f'\n{student_2}\n'
      f'\nСписок лекторов:\n'
      f'{lecturer_1}\n'
      f'\n{lecturer_2}\n'
      f'\nСписок проверяющих:\n'
      f'{reviewer_1}\n'
      f'{reviewer_2}\n')

# Сравним между собой студентов
print(f'Студент {student_1.name} {student_1.surname} лучше, чем студент {student_2.name} {student_2.surname}')
print()

# Сравним между собой лекторов
print(f'Лектор {lecturer_1.name} {lecturer_1.surname} лучше, чем лектор {lecturer_2.name} {lecturer_2.surname}')
print()


"""Функция для подсчета средней оценки за домашние задания 
по всем студентам в рамках конкретного курса,
в качестве аргументов принимаем список студентов и название курса.

"""
def avg_grades_students(students, course):
    sum_grades = 0
    count = 0
    for student in students:
        if course in student.grades:
            sum_grades += sum(student.grades[course])
            count += len(student.grades[course])
    return sum_grades / count


# Выводим результат подсчета средней оценки по всем студентам для данного курса
print(f'Средняя оценка студентов по курсу Python: {avg_grades_students([student_1, student_2], "Python"):.2f}')
print(f'Средняя оценка студентов по курсу Git: {avg_grades_students([student_1, student_2], "Git"):.2f}')
print()


"""Функция для подсчета средней оценки за лекции 
всех лекторов в рамках курса,
в качестве аргумента принимаем список лекторов и название курса.

"""
def avg_grades_lecturers(lecturers, course):
    sum_grades = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            sum_grades += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return sum_grades / count


# Выводим результат подсчета средней оценки по всем лекторам для данного курса
print(f'Средняя оценка лекторов по курсу Python: {avg_grades_lecturers([lecturer_1, lecturer_2], "Python"):.2f}')
print(f'Средняя оценка лекторов по курсу Git: {avg_grades_lecturers([lecturer_1, lecturer_2], "Git"):.2f}')