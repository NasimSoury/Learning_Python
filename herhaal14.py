def average(scores):
    total=sum(scores) / len(scores)
    
    print(total)

    if total <10:
        print("failed")
    elif total<15:
        print("normal")  
    else:
        print("passed")





average([12,18,19,20])

