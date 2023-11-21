from Certification import Certification
from validate.StudentValidate import StudentValidate


class Student:

    def __init__(self, citizenIdentity: int, candidateNumber: int, name: str, address: str,
                 cert: Certification = None):
        StudentValidate.checkCitizenIdentity(citizenIdentity)
        StudentValidate.checkCandidateNumber(candidateNumber)
        StudentValidate.checkName(name)
        StudentValidate.checkAddress(address)
        self.__citizenIdentity = citizenIdentity
        self.__candidateNumber = candidateNumber
        self.__name = name
        self.__address = address
        self.__cert = cert

    def setCitizenIdentity(self, citizenIdentity: int):
        StudentValidate.checkCitizenIdentity(citizenIdentity)
        self.__citizenIdentity = citizenIdentity

    def setCandidateNumber(self, candidateNumber: int):
        StudentValidate.checkCandidateNumber(candidateNumber)
        self.__candidateNumber = candidateNumber

    def setName(self, name: str):
        StudentValidate.checkName(name)
        self.__name = name

    def setAddress(self, address: str):
        StudentValidate.checkAddress(address)
        self.__address = address

    def setCert(self, cert: Certification):
        self.__cert = cert

    def getCitizenIdentity(self) -> int:
        return self.__citizenIdentity

    def getCandidateNumber(self) -> int:
        return self.__candidateNumber

    def getName(self) -> str:
        return self.__name

    def getAddress(self) -> str:
        return self.__address

    def getCert(self) -> Certification:
        return self.__cert
