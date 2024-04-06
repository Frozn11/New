class Student:
    name = ""
    age = 0
    course = ""
    school = ""
    finished_corse = []
    def name_(self):
        print("name:", self.name)

    def age_(self):
        print("age:", self.age)

    def info_(self):
        print("age", self.age,",name:",self.name,",school:",self.school)

    def finish_corse(self):
        print("Congratulations, the course is finished")
        self.finished_corse.append(self.course)
student = Student()
student.name = "Карим"
student.course = "python lvl3"
student.age = 16
student.school = "Kodland"
student.info_()
