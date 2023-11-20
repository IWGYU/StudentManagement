from student import Student

class ManageStudent:
    def __init__(self):
        self.__lst = []
    def addStudent(self, student: Student):
        self.__lst.append(student)
    def getStudentsAsList(self) -> list:
        return self.__lst