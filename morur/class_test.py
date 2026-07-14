class Employee():
    def __init__(self, name_input, falily_input, age_input, salaris_input, position_input):
        self.name=name_input
        self.family=falily_input
        self.age=age_input
        self.salaris=salaris_input
        self.position=position_input

    def showinfo_employee(self):
        print(f"{self.name} {self.family} is {self.age} and has {self.salaris} salaris and is a {self.position}")

    def salarisverhoging(self, perocent):
        verhoog= self.salaris *perocent / 100
        self.salaris=self.salaris+verhoog
      
        print(f"de salaris van {self.name} word verhoog tot {self.salaris}")


employee1=Employee("Ali", "Ahmadi" , 23 , 500 , "Hr")
employee2=Employee("sara", "hosseini" , 47, 700 , "accountant")

employee1.showinfo_employee()
employee2.showinfo_employee()

employee1.salarisverhoging(10)
employee2.salarisverhoging(20)