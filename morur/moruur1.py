print("hello,world!")

naam="Ali"
leeftijd=20
print(naam, "is", leeftijd, "yaar! ")
#of beter :
print(f"{naam} is {leeftijd} yaar!")


#گرفتن ورودی از کاربر=invoer van de gebruiker
naam=input("invoer je naam : ")
print(f" hallo {naam} ")

#if= voorwaarde

leeftijd= int(input("invoer je leeftijd: "))
if leeftijd>= 18:
    print(f" je bent een volwassen! ")
else:
    print(f" je bent een kind!")