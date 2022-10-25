# Быковский Сергей Сергеевич ИДБ-21-11
# Вариант 4
# 4) Напишите классы для предметной области университета. Возможные классы: студент и преподаватель. 
# В 4-м и 5-м пунктах хранение объектов одного класса реализовать в формате JSON, другого − в формате XML.

class Person():
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

    def GetName(self):
        return self.fullName

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
    def __init__(self, fullName, age, faculty, email = ""):
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

class Professor(Person):
    def __init__(self, fullName, age, statusInScience, officeNumber = "", email = ""):
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
            

def main():
    proffessor = Professor("Loi Mafas", 30, "P.H.D in Physics", 4, "prof@gmail.com")
    person = Student("Mike Vazovski", 19, "Applied Informatic", "sergei.bykovskiy2003@gmail.com")
    
main()
