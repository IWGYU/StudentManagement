from modelt.Student import Student
from modelt.Certification import Certification
from validatet.StudentValidate import StudentValidate

class StudentD(Student):
    # constructor
    def __init__(self, citizenIdentity: int, candidateNumber: int, name: str, address: str, mathScore: float,
                 literatureScore: float, englishScore: float, cert: Certification = None):
        StudentValidate.checkScore(mathScore)
        StudentValidate.checkScore(literatureScore)
        StudentValidate.checkScore(englishScore)
        super().__init__(citizenIdentity, candidateNumber, name, address, cert)
        self.__mathScore = mathScore
        self.__literatureScore = literatureScore
        self.__englishScore = englishScore

        self.__satScore = StudentValidate.CalculatorSATScore(literatureScore, mathScore, englishScore, cert)
    # getter & setter
    def setMathScore(self, mathScore: float):
        StudentValidate.checkScore(mathScore)
        self.__mathScore = mathScore

    def setLiteratureScore(self, literatureScore: float):
        StudentValidate.checkScore(literatureScore)
        self.__literatureScore = literatureScore

    def setEnglishScore(self, englishScore: float):
        StudentValidate.checkScore(englishScore)
        self.__englishScore = englishScore
    def setSATScore(self, SATScore: float):
        self.__satScore = SATScore

    def getMathScore(self) -> float:
        return self.__mathScore

    def getLiteratureScore(self) -> float:
        return self.__literatureScore

    def getEnglishScore(self) -> float:
        return self.__englishScore

    def getSATScore(self) -> float:
        return self.__satScore
    #subject dictionary
    subDict = dict([(0, 'toán'), (1, 'ngữ văn'), (2, 'tiếng Anh')])