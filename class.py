class Student:
    def __init__(self, name, major, id):
        self.name = name
        self.major = major
        self.id = id
    
    def study(self):
        print(f'{self.name} is studying')

    def set_major(self, major):
        self.major = major

    def get_major(self):
        return self.major

student = Student('Jiseok', 'Computer Science', '1234')
student.study()

class ForeignStudent(Student):
    def __init__(self, name, major, id, lang):
        super().__init__(name, major, id)
        self.lang = lang
        