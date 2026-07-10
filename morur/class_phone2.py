class phone():
    def __init__(self,input_name,input_prijs):
        self.name=input_name
        self.prijs=input_prijs

    def print_prijs_toman(self):
        t=self.prijs *200000
        print(t)


ph1=phone("apple" , 1000)
ph2=phone("samsung" , 500)
ph1.print_prijs_toman()

ph2.print_prijs_toman()

#print(f" {ph1.name} has {ph1.prijs} price ")
#print(f" {ph2.name} has {ph2.prijs} price ")