class School(object):
    def __init__(self):
        self.dict_grades_students = {}

    def add_student(self, name, grade):
        if grade in self.dict_grades_students:
            self.dict_grades_students[grade].append(name)
        else:
            self.dict_grades_students[grade] = []
            self.dict_grades_students[grade].append(name)

    def roster(self):
        list_grades = list(self.dict_grades_students.keys())
        list_grades.sort()
        list_students = []
        for grade in list_grades:
            list_students_temp = []
            for student in self.dict_grades_students[grade]:
                list_students_temp.append(student)
            list_students_temp.sort()
            for student in list_students_temp:
                list_students.append(student)
        return list_students

    def grade(self, grade_number):
        if grade_number in self.dict_grades_students:
            list_students = self.dict_grades_students[grade_number]
            list_students.sort()
        else:
            list_students = []
        return list_students
