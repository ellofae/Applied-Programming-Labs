# Быковский Сергей Сергеевич ИДБ-21-11
# Вариант 4
# 4) Напишите классы для предметной области университета. Возможные классы: студент и преподаватель. 
# В 4-м и 5-м пунктах хранение объектов одного класса реализовать в формате JSON, другого − в формате XML.

import json
from xml.etree import ElementTree

from abc import ABC
from abc import abstractmethod

class Person(ABC):
    def __init__(self, fullName, age, email = ""):
        self.fullName = fullName
        self.email = email
        try:
            if(age <= 100 and age >= 0):
                self.age = age
            else:
                self.age = 0
                print("Incorrect range of age")
        except ValueError:
            print("Incorrect Value Error has been detected")
        except TypeError:
            print("Incorrect Type Error has been detected")

    @abstractmethod
    def GetName(self):
        return self.fullName
    
    @abstractmethod
    def GetEmail(self):
        return self.email

    def ChangeName(self):
        while(True):
            new_name = input("Type in a new name: ")
            if len(new_name) != 0:
                self.fullName = new_name
                break

    def ChangeEmail(self):
        while(True):
            new_email = input("type in a new email: ")
            if len(new_email) != 0:
                self.email = new_email
                break

class Student(Person):
    def __init__(self, fullName, age, faculty="", email = ""):
        self.faculty = faculty
        Person.__init__(self, fullName, age, email)

    def ChangeFaculty(self):
        while(True):
            new_faculty = input("Type in a new faculty name: ")
            if len(new_faculty) != 0 and not any(char.isdigit() for char in new_faculty):
                self.faculty = new_faculty
                break

    def InfoOnStudent(self):
        print(f"Student's name: {self.fullName}, faculty: {self.faculty}, age: {self.age}, email: {self.email} ")

    # Overriding abstract methods
    def GetName(self):
        return "Mr. " + self.fullName
    
    def GetEmail(self):
        return self.email

class Professor(Person):
    def __init__(self, fullName, age, statusInScience, officeNumber, email = ""):
        Person.__init__(self, fullName, age, email)
        self.statusInScience = statusInScience
        try:
            if(officeNumber <= 500 and officeNumber >= 0):
                self.officeNumber = officeNumber
            else:
                print("Not existing office number")
                self.officeNumber = None
        except ValueError:
            print("Incorrect Value Error has been detected")
        except TypeError:
            print("Incorrect Type Error has been detected")

    def ChangeOfficeNumber(self):
        while(True):
            new_office = input("Type in a new ofiice number: ")
            if any(char.isdigit() for char in new_office):
                self.officeNumber = new_office
                break                

    def InfoOnProfessor(self):
        print(f"Professor's name: {self.fullName}, status in science: {self.statusInScience}, office number: {self.officeNumber}, age: {self.age}, email: {self.email} ")

    # Overriding abstract methods
    def GetName(self):
        return "Proffessor " + self.fullName
    
    def GetEmail(self):
        return self.email

def main():
    ## JSON file plugging into array of data
    print("\n")
    stud = []

    with open("students.json") as f:
        data = json.load(f)
    for piece in data['students']:
        stud.append(piece)

    print("Amount of students: ", len(stud))
    print("Student list: ")
    for i in range(len(stud)):
        stud1 = Student(stud[i]['fullName'], stud[i]['age'], stud[i]['faculty'], stud[i]['email'])
        stud1.InfoOnStudent()

    # JSON file transfering CHANGED data to another json file
    for student in data['students']:
        del student['age']
        student['courseNumber'] = None

    with open('new_students.json', 'w') as f:
        json.dump(data, f, indent = 2)


    ## XML file parsing 
    proffesorsCount = 0
    proffesorsDividedList = []
    tree = ElementTree.parse("proffesors.xml")
    root = tree.getroot()
    
    for i in root:
        proffesorsCount += 1

    count = 0
    proffesorsList = []
    temp_list = []
    for element in root:
        for child in element:
            if count < 4:
                temp_list.append(child.text)
                count += 1
            else:
                temp_list.append(child.text)   
                proffesorsList.append(temp_list)
                count = 0
                temp_list = []
    
    print("\nAmount of proffesors: ", len(proffesorsList))
    print("Proffesors list: ")
    for i in range(proffesorsCount):
        prof1 = Professor(proffesorsList[i][0], int(proffesorsList[i][1]), proffesorsList[i][2], int(proffesorsList[i][3]), proffesorsList[i][4])
        prof1.InfoOnProfessor()
        
    # Extracting XML file

    greg = root[0]
    description = ElementTree.Element("description")
    description.text = "Showed excellent skills during sciecific work"
    greg.append(description)

    greg = root[1]
    description.text = "Showed excellent skills during sciecific work"
    greg.append(description)

    tree.write("new_proffesors.xml")
    print("\n")
    ## XML file parsing

main()
