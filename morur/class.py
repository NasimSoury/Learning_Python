class student:
    def __init__(self, name_input, grade_input):
        self.name= name_input
        self.grade= grade_input

    def show_info(self):
        print(self.name, "has" , self.grade , "grade")

student1= student("nasim" , 2)
student1.show_info()
