
class Student:
    
    def __init__(self, name, studentId, grade):
        self.__name = name
        self.__studentId = studentId
        self.__grade = grade
   
    def getName(self):
        return self.__name

    def getStudentId(self):
        return self.__studentId

    def getGrade(self):
        return self.__grade

    
    def setGrade(self, grade):
        self.__grade = grade

    
    def displayInfo(self):
        print(f"Name: {self.__name} | ID: {self.__studentId} | Grade: {self.__grade}")

if __name__ == "__main__":
   
    student1 = Student("Lila Mae Cruz", "2026-010", 89)
    student2 = Student("James Ethan Reyes", "2026-012", 90)
  
    student1.setGrade(88)
   
    student1.displayInfo()
    student2.displayInfo()
    