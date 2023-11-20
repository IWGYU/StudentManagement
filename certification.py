class Certification:
    #constructor
    def __init__(self, cerType: str, score: float):
        cerType = self.__parseCerType(cerType)
        self.__checkCerType(cerType)
        self.__checkScore(score)
        self.__cerType = cerType
        self.__score = self.__pasreScore(score)
    #getter & setter
    def setCerType(self, cerType: str):
        cerType = self.__parseCerType
        self.__checkCerType(cerType)
        self.__cerType = cerType
    def setScore(self, score: float):
        self.__checkScore(score)
        self.__score = self.__pasreScore(score)
    def getCerType(self) -> str:
        return self.__cerType
    def getScore(self) -> float:
        return self.__score
    #validator
    def __checkCerType(cerType: str):
        if (cerType != 'toeic') | (cerType != 'ielts'):
            raise ValueError
    def __checkScore(self, score: float):
        if ((self.__cerType == 'ielts') & ((score < 0.0) | (score > 9.0))) | ((self.__cerType == 'toeic') & ((score < 0.0) | (score > 990.0) | (score % 5 != 0))):
            raise ValueError
    #parser
    def __pasreScore(self, score: float) -> float:
        if self.__cerType == 'toeic':
            score = score / 100
        return score
    def __parseCerType(cerType: str) -> str:
        return cerType.strip().lower()