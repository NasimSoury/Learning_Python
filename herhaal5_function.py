#def welcome ():
 #   name=input("what is your name?")
  #  print("welcome" , name)


#welcome ()



#اول تابع را تعریف میکنیم یا میسازیم
def calculate(scores):  #اسکورز ینی یه اسم که شامل داده است و بعدا این اطلاعات را میدهیم اگه خالی بزاریمش فقط کدهایی که اولین بار زیر تابع نوشته شده بود را برمیگرداند
    total=sum(scores)
    avrage= total/len(scores)
    return total, avrage

#اینجا ما اسکورز رو میسازیم 

grades1=[18,22,6,19]
grades2=[14,12,6,20]

print(calculate(grades1))
print(calculate(grades2))


#
def find_bigest (numbers):
    return max(numbers)

numbers=[2,6,83,65,15,42,67,96]

print(find_bigest(numbers))