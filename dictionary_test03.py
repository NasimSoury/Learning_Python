scores={
    "sami" : 16,
    "sara" : 18 ,
    "nona" : 19 ,
    "jadi" : 20 ,
    "jan" : 15 
}
print(f"list students : " , scores)

scores["sara"]= 4
del scores["jan"]
scores["monika"]= 15
print(scores)
for name , score in scores.items():
    if score <10 :
        print(f"{name} : you are failed")
    else:
        print(f"{name} : you are passed")
        