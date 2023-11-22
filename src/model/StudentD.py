from model.Student import Student
from model.Certification import Certification


class StudentD(Student):
    # constructor
    def __init__(self, citizenIdentity: int, candidateNumber: int, name: str, address: str, mathScore: float,
                 literatureScore: float, englishScore: float, cert: Certification = None):
        super().__init__(citizenIdentity, candidateNumber, name, address, cert)
        self.__mathScore = mathScore
        self.__literatureScore = literatureScore
        self.__englishScore = englishScore

    # getter & setter
    def setMathScore(self, mathScore: float):
        self.__mathScore = mathScore

    def setLiteratureScore(self, literatureScore: float):
        self.__literatureScore = literatureScore

    def setEnglishScore(self, englishScore: float):
        self.__englishScore = englishScore

    def getMathScore(self) -> float:
        return self.__mathScore

    def getLiteratureScore(self) -> float:
        return self.__literatureScore

    def getEnglishScore(self) -> float:
        return self.__englishScore
    
    #subject dictionary
    subDict = dict([(0, 'toán'), (1, 'ngữ văn'), (2, 'tiếng Anh')])
