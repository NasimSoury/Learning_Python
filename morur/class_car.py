class car():
    def __init__(self, color_input , speed_input):
        self.color=color_input
        self.speed=speed_input

    def show_info(self):
        print(f"this car is {self.color} and has {self.speed} km/h speed!")
              

my_car=car("red" , 120)
my_car.show_info()
