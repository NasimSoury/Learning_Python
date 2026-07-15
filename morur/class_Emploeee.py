class Employee():
    def __init__(self, name_input, family_input, age_input, salaris_input, position_input):
        self.name=name_input
        self.family=family_input
        self.age=age_input
        self.salaris=salaris_input
        self.position=position_input

    def show_info(self):
        print(f"employee {self.name} {self.family} is {self.age} jaar en heeft {self.salaris} salaris en is een {self.position}")

    def verhoogsalaris(self, procent):
        verhoog=self.salaris * procent/ 100
        self.salaris=verhoog+self.salaris
        print(f"de salaris van employee {self.name} {self.family} word tot {self.salaris} verhooger! ")

    def change_position(self, nieuw_position):
        old_position=self.position
        self.position=nieuw_position
        print(f"{old_position} is changed to {nieuw_position}")


employee1= Employee("sara", "Van Den Berg", 25, 500, "Hr")
employee2= Employee("jack", "Vos", 45, 800, "Junior Developer")

employee1.show_info()
employee1.verhoogsalaris(20)
employee1.change_position("manager")
employee1.show_info()