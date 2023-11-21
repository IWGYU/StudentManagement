class StudentValidate:
    @staticmethod
    def checkCitizenIdentity(citizenIdentity: int):
        if (len(str(citizenIdentity)) > 12) | (len(str(citizenIdentity)) < 10):
            raise ValueError

    @staticmethod
    def checkCandidateNumber(candidateNumber: int):
        if (len(str(candidateNumber)) > 8) | (len(str(candidateNumber)) < 7):
            raise ValueError

    @staticmethod
    def checkName(name: str):
        if (len(name) < 5) | (len(name) > 255):
            raise ValueError

    @staticmethod
    def checkAddress(address: str):
        if (len(address) < 12) | (len(address) > 2048):
            raise ValueError

    @staticmethod
    def checkScore(score: float):
        if (score < 0.0) | (score > 10.0):
            raise ValueError
