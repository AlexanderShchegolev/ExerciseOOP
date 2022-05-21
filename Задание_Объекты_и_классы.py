class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'    

    def _avr_rating(self):
        sum_ = 0
        keys = self.grades.keys()
        for grade in self.grades.values():
            sum_ += (sum(grade) / len(grade)) / len(keys)   
        return round(sum_, 2)        

    def __lt__(self, other):
        if not isinstance(self, Student) or not isinstance(other, Student):
            print('Обьект не является представителем класса!')
            return
        if self._avr_rating() > other._avr_rating():
            print(f'Средний бал студента {self.name} выше')
        else:
            print(f'Средний бал студента {other.name} выше')        


    def __str__(self):
        res = f'''
Имя: {self.name} 
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self._avr_rating()}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses)}'''
        return res           
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}     

    def _avr_rating(self):
        sum_ = 0
        keys = self.grades.keys()
        for grade in self.grades.values():
            sum_ += (sum(grade) / len(grade)) / len(keys)   
        return round(sum_, 2)        


    def __lt__(self, other):
        if not isinstance(self, Lecturer) or not isinstance(other, Lecturer):
            print('Обьект не является представителем класса!')
            return
        if self._avr_rating() > other._avr_rating():
            print(f'Средний бал лектора {self.name} выше')
        else:
            print(f'Средний бал лектора {other.name} выше')           
       
       
    def __str__(self):
        res = f'''
Имя: {self.name} 
Фамилия: {self.surname} 
Средняя оценка за лекции: {self._avr_rating()}'''
        return res              

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'''
Имя: {self.name} 
Фамилия: {self.surname} '''
        return res        

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Lara', 'Croft')
cool_reviewer.courses_attached += ['Python', 'Git']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(best_student, 'Git', 10)

print(best_student)

some_student = Student('Paul', 'Shark', 'man')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

some_reviewer = Reviewer('Anna', 'Kim')
some_reviewer.courses_attached += ['Python', 'Git']
 
some_reviewer.rate_hw(some_student, 'Python', 8)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 8)
some_reviewer.rate_hw(some_student, 'Git', 9)
some_reviewer.rate_hw(some_student, 'Git', 9)
some_reviewer.rate_hw(some_student, 'Git', 10)

print(some_student)

print(cool_reviewer)
print(some_reviewer)


cool_lecturer = Lecturer('Peter', 'O\'Neal')
cool_lecturer.courses_attached += ['Python', 'Git']

some_student.rate_hw(cool_lecturer, 'Python', 10) 
some_student.rate_hw(cool_lecturer, 'Python', 10) 
some_student.rate_hw(cool_lecturer, 'Python', 9) 
some_student.rate_hw(cool_lecturer, 'Git', 10) 
some_student.rate_hw(cool_lecturer, 'Git', 10) 
some_student.rate_hw(cool_lecturer, 'Git', 9) 

print(cool_lecturer) 

some_lecturer = Lecturer('James', 'Jones')
some_lecturer.courses_attached += ['Python', 'Git']

best_student.rate_hw(some_lecturer, 'Python', 10) 
best_student.rate_hw(some_lecturer, 'Python', 9) 
best_student.rate_hw(some_lecturer, 'Python', 9) 
best_student.rate_hw(some_lecturer, 'Git', 10) 
best_student.rate_hw(some_lecturer, 'Git', 9) 
best_student.rate_hw(some_lecturer, 'Git', 10) 

print(some_lecturer) 

best_student.__lt__(some_student)
# some_student.__lt__(best_student)

cool_lecturer.__lt__(some_lecturer)
# some_lecturer.__lt__(cool_lecturer)

students_list = [some_student, best_student]


def get_avg_hw_grade(students, course):
    sum_ = 0
    for student in students:
        for key, value in student.grades.items():
            if key == course:
                sum_ += (sum(value) / len(value)) / len(students_list)
       
    return round(sum_, 2) 

print(get_avg_hw_grade(students_list, 'Python'))  
print(get_avg_hw_grade(students_list, 'Git'))  

print(some_student.grades)
print(best_student.grades)


lecturer_list = [cool_lecturer, some_lecturer]


def get_avg_hw_grade(lecturers, course):
    sum_ = 0
    for lecturer in lecturers:
        for key, value in lecturer.grades.items():
            if key == course:
                sum_ += (sum(value) / len(value)) / len(lecturer_list)
       
    return round(sum_, 2) 

print(get_avg_hw_grade(lecturer_list, 'Python'))  
print(get_avg_hw_grade(lecturer_list, 'Git'))  

print(some_lecturer.grades)
print(cool_lecturer.grades)