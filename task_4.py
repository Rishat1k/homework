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


student_1 = Student('Andrey', 'Ivanov', 'm')
student_2 = Student('Elena', 'Petrova', 'w')

reviewer_1 = Reviewer('Maxim', 'Ivanov')
reviewer_2 = Reviewer('Maxim', 'Sapogov')

lecturer_1 = Lecturer('Anton', 'Kotov')
lecturer_2 = Lecturer('Anna', 'Stepanova')

student_1.courses_in_progress.append('Python')
student_1.finished_courses.append('Основы программирования')

student_2.courses_in_progress.append('Python')
student_2.courses_in_progress.append('Java')
student_2.finished_courses.append('Основы программирования')

lecturer_1.courses_attached.append('Python')
lecturer_2.courses_attached.append('Java')

reviewer_1.courses_attached.append('Python')
reviewer_2.courses_attached.append('Java')

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Java', 10)
reviewer_2.rate_hw(student_2, 'Java', 8)

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_2.rate_lecturer(lecturer_1, 'Python', 7)
student_2.rate_lecturer(lecturer_1, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Java', 7)
student_2.rate_lecturer(lecturer_2, 'Java', 10)

print(student_1)
print(student_2)
print(student_1 < student_2)
print(lecturer_1)
print(lecturer_2)
print(lecturer_1 < lecturer_2)
print(reviewer_1)
print(reviewer_2)

def average_grade(students, course):
    result = 0
    for student in students:
        if isinstance(student, Student):
            if course not in student.courses_in_progress:
                return f'{student.name} не обучается на курсе {course}'
            result += sum(student.grades[course])/len(student.grades[course])
        else:
            return f'{student.name} не является студентом!'
    return result/len(students)

def lecturer_grade(lecturers, course):
    result = 0
    for lecture in lecturers:
        if isinstance(lecture, Lecturer):
            if course not in lecture.courses_attached:
                return f'{lecture.name} не ведет курс {course}'
            result += sum(lecture.lecturer_grades[course])/len(lecture.lecturer_grades[course])
        else:
            return f'{lecture.name} не является лектором!'
    return result/len(lecturers)

