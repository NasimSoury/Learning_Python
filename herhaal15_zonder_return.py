def total_price_with_return(prices):
    total = sum(prices)
    return total

# استفاده
x = total_price_with_return([12000, 8000, 5000])
print("x =", x)
print("با مالیات (9%):", x * 1.09)