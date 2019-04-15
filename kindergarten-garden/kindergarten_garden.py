class Garden(object):
    def __init__(self, diagram, students=None):

        diagrams = diagram.split('\n')

        self.list_diagrams = []

        counter = 0
        while counter < len(diagrams[0]):
            list_temp = []
            list_temp.append(diagrams[0][counter])
            list_temp.append(diagrams[0][counter+1])
            counter += 2
            self.list_diagrams.append(list_temp)

        counter = 0
        for i in self.list_diagrams:
            i.append(diagrams[1][counter])
            i.append(diagrams[1][counter+1])
            counter += 2

        self.plants_chars = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}

        if students == None:
            self.students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
            self.students.sort()
        else:
            self.students = students
            self.students.sort()

        self.dict_plants_students = {}

        for index, list in enumerate(self.list_diagrams):
            self.dict_plants_students[self.students[index]] = list

    def plants(self, student):
        list_plants = []
        for plant in self.dict_plants_students[student]:
            list_plants.append(self.plants_chars[plant])
        return list_plants
