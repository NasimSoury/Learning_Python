def final_price(price, discont):
    amount_discount= (price * discont) / 100
    total= price - amount_discount
    return total


print(final_price(100, 30))