from model.Student import Student


class StudentController:
    def __init__(self):
        self.__lst = []

    def addStudent(self, student: Student):
        self.__lst.append(student)

    def getStudentsAsList(self) -> list:
        return self.__lst
