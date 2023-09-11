class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return "Ошибка"

    def average_grade(self):
        average_grade = 0
        count = 0
        if len(self.grades) >= 1:
            for course in self.grades:
                average_grade += sum(self.grades[course])
                count += len(self.grades[course])
            average_grade /= count
            return average_grade
        else:
            return 'У данного студента нет оценок'

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}'
                f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        if not isinstance(other, Student):
            return f'{other} не является студентом'
        if len(self.grades) > 0 and len(other.grades) > 0:
            return self.average_grade() < other.average_grade()
        else:
            return 'У одного из студентов нет оценок'


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.lecturer_grades = {}

    def average_grade(self):
        average_grade = 0
        count = 0
        if len(self.lecturer_grades) >= 1:
            for course in self.lecturer_grades:
                average_grade += sum(self.lecturer_grades[course])
                count += len(self.lecturer_grades[course])
            average_grade /= count
            return average_grade
        else:
            return 'У данного лектора нет оценок'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return f'{other} не является лектором'
        if len(self.lecturer_grades) > 0 and len(other.lecturer_grades) > 0:
            return self.average_grade() < other.average_grade()
        else:
            return 'У одного из лекторов нет оценок'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


