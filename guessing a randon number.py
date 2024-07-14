import random
randNum= random.randint(1, 100)
while True:
     num=int(input(" enter the number or quit(Q) :"))
     if(num== "Q"):
         break

     num = int(num)   
     if(num==randNum):
         print("find it.",randNum)
         break
     elif(num<randNum):
         print("your given num ia too small.")
     else:
         print("your given num is too big.")   

print("-------GAME OVER---------")    