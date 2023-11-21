from validate.CertValidate import CertValidate


class Certification:

    def __init__(self, certType: str, score: float):
        cert = CertValidate.parseCertType(certType)
        CertValidate.checkCertType(cert)
        CertValidate.checkScore(cert, score)
        self.__certType = cert
        self.__score = CertValidate.parseScore(cert, score)

    def setCerType(self, certType: str):
        cert = CertValidate.parseCertType(certType)
        CertValidate.checkCertType(cert)
        self.__certType = cert

    def setScore(self, certType: str, score: float):
        CertValidate.checkScore(certType, score)
        self.__score = CertValidate.parseScore(certType, score)

    def getCerType(self) -> str:
        return self.__certType

    def getScore(self) -> float:
        return self.__score
    # validator
