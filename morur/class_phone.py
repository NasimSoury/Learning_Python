class phone :
    def __init__(self, name_brand, value_storage):
        self.nb=name_brand
        self.vs=value_storage
    def show_info(self):
        print(f" {self.nb} has {self.vs} storage!")
ph1=phone("nokia", 128)
ph2=phone("apple" , 512)

ph1.show_info()
ph2.show_info()