def total_price_no_return(prices):
    total = sum(prices)
    print("جمع خرید:", total)

# استفاده
total_price_no_return([12000, 8000, 5000])   # چاپ میکنه
x = total_price_no_return([12000, 8000, 5000])  # تلاش ناموفق برای ذخیره
print("x =", x) #اما نمیتونه ایکس رو پیدا کنه و None برمیگردونه