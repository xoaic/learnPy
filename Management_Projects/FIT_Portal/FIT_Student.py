import pickle

class FIT_Student:
    def __init__(self, StudentName, StudentClass):
        self.sId = 1900
        self.sName = StudentName
        self.sClass = StudentClass

    def getStudentID(self):
        self.sId += 1

class Course(FIT_Student):
    def __init__(self, Subject, StudentName, StudentClass, InternalScore, FinalScore):
        super().__init__(StudentName, StudentClass)
        self.Subj = Subject
        self.iScore = InternalScore
        self.fScore = FinalScore
        self.fGrade

    def calculateFinalGrade(self):
        aveMark = self.iScore * 0.4 + self.fScore * 0.6
        if aveMark < 5:
            self.fGrade = 'F'
        elif aveMark > 8:
            self.fGrade = 'E'
        else:
            self.fGrade = 'G'

    def main(self):
        record = Course('SS1', 'Khanh', '2c11', 9, 9)
        with open('record.dat', 'wb') as fh:
            pickle.dump(record, fh)