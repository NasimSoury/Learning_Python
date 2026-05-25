#از کاربر یک عدد بگیر و مشخص کن زوج هست یا فرد
while True:
    x=input("voeg een numer toe of voeg (stop) om te stoppen ")
    if x == "stop":
        print("dag!")
        break

    if x.isdigit():
        x=int(x)
        if x % 2==0 :
         print("het is een even numer! ")
        else:
         print("het is een oneven numer!")
    else:
        print("data is fout!je moet alleen een numer of stop typen!")