class Product():
    def __init__(self, name_input, price_input, stock_input):
        self.name=name_input
        self.price=price_input
        self.stock=stock_input

    def show_info(self):
        print(f" There are {self.stock} {self.name}s in stock. ")

    def change_price(self, nieuw_price):
        if nieuw_price <=0:
            print(f"Error! {nieuw_price} must be greater dan zero!")
        else:
            
            old_price=self.price
            self.price=nieuw_price   # علامت== درست نیست یه مساوی درسته
            print(f"{old_price}€ has been changed to {nieuw_price}€!")

    def increase_stock(self, nieuw_stock):
        if nieuw_stock<=0:
            print(f"{nieuw_stock} must be greater dan zero!")
        else:
            self.stock+=nieuw_stock
            print(f"stock has been increase to {self.stock}.")

    def buy_quantity(self, number):
         
         
         if number<=0:
              print(f"Error! {number} must be greaterdan zero!")
         elif number> self.stock:
              print(f"Error! We don't have enough stock. Available stock: {self.stock}!")
         else :
              self.stock-=number
              print(f"{number} {self.name} have been sold successfully.")

    




    
Product1=Product("Laptop" , 1500 , 15)
Product1.show_info()
Product1.increase_stock(3)
Product1.show_info()
Product1.change_price(1700)
Product1.buy_quantity(2)
Product1.show_info()

Product2=Product("mouse", 50, 8)
Product2.show_info()
Product2.buy_quantity(1)
Product2.show_info()
Product1.show_info()
Product1.buy_quantity(17)
Product1.show_info()
Product1.change_price(1800)