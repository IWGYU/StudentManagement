from certification import Certification

class Student:
    #constructor
    
    #ssn: social security number
    #idn: identification number
    #name: full name
    #adr: address
    #cerr: certification
    def __init__(self, ssn: int, idn: int, name: str, adr: str, cerr : Certification = None):
        self.__checkSSN(ssn)
        self.__checkIDN(idn)
        self.__checkName(name)
        self.__checkAdr(adr)
        self.__ssn = ssn
        self.__idn = idn
        self.__name = name
        self.__adr = adr
        self.__cerr = cerr
    #getter & setter
    def setSSN(self, ssn: int):
        self.__checkSSN(ssn)
        self.__ssn = ssn
    def setIDN(self, idn: int):
        self.__checkIDN(idn)
        self.__idn = idn
    def setName(self, name: str):
        self.__checkName(name)
        self.__name = name
    def setAdr(self, adr: str):
        self.__checkAdr(adr)
        self.__adr = adr
    def setCerr(self, cerr: Certification):
        self.__cerr = cerr
    def getSSN(self) -> int:
        return self.__ssn
    def getIDN(self) -> int:
        return self.__idn
    def getName(self) -> str:
        return self.__name
    def getAdr(self) -> str:
        return self.__adr
    def getCerr(self) -> Certification:
        return self.__cerr
    #validator
    def __checkSSN(ssn: int):
        strSSN = str(ssn)
        if (len(strSSN) > 12) | (len(strSSN) < 10):
            raise ValueError
    def __checkIDN(idn: int):
        strIDN = str(idn)
        if (len(strIDN) > 8) | (len(strIDN) < 7):
            raise ValueError
    def __checkName(name: str):
        if (len(name) < 5) | (len(name) > 255):
            raise ValueError
    def __checkAdr(adr: str):
        if (len(adr) < 12) | (len(adr) > 2048):
            raise ValueError

def checkScore(score: float):
    if (score < 0.0) | (score > 10.0):
        raise ValueError

#############################################

class StudentC(Student):
    #constructor
    
    #litScr = literature score
    #histScr = history score
    #geoScr = geography score
    def __init__(self, ssn: int, idn: int, name: str, adr: str, litScr: float, histScr: float, geoScr: float, cerr : Certification = None):
        checkScore(litScr)
        checkScore(histScr)
        checkScore(geoScr)
        super().__init__(ssn, idn, name, adr, cerr)
        self.__litScr = litScr
        self.__histScr = histScr
        self.__geoScr = geoScr
    #getter & setter
    def setLitScr(self, litScr: float):
        checkScore(litScr)
        self.__litScr = litScr
    def setHistScr(self, histScr: float):
        checkScore(histScr)
        self.__histScr = histScr
    def setGeoScr(self, geoScr: float):
        checkScore(geoScr)
        self.__geoScr = geoScr
    def getLitSrc(self) -> float:
        return self.__litScr
    def getHistSrc(self) -> float:
        return self.__histScr
    def getGeoSrc(self) -> float:
        return self.__geoScr

#############################################

class StudentD(Student):
    #constructor
    
    #mathScr = math score
    #litScr = literature score
    #engScr = english score
    def __init__(self, ssn: int, idn: int, name: str, adr: str, mathScr: float, litScr: float, engScr: float, cerr : Certification = None):
        checkScore(mathScr)
        checkScore(litScr)
        checkScore(engScr)
        super().__init__(ssn, idn, name, adr, cerr)
        self.__mathScr = mathScr
        self.__litScr = litScr
        self.__engScr = engScr
    #getter & setter
    def setMathScr(self, mathScr: float):
        checkScore(mathScr)
        self.__mathScr = mathScr
    def setLitScr(self, litScr: float):
        checkScore(litScr)
        self.__litScr = litScr
    def setEngScr(self, engScr: float):
        checkScore(engScr)
        self.__engScr = engScr
    def getMathSrc(self) -> float:
        return self.__mathScr
    def getLitSrc(self) -> float:
        return self.__litScr
    def getEngScr(self) -> float:
        return self.__engScr
