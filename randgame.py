import random as rd
a=rd.randint(0,10)
level=input("Do you want to easy or hard").lower() 
if level=='easy':
    life=10
elif level=='hard':
    life=5
else:
    print("wrong input")
while(life!=0):
    ch=int(input("guess your number"))
    if ch==a:
        print("you win!")
    else:
        print("try again!")
    life=life-1
    print("you have ",life," chances")