chance=3
import random 
words =["python","c","c++","java","js","sql"]
target_word=random.choice(words)
while chance>0:
    user_word=input("\nenter your word or quit(Q)")
    if user_word=="Q":
        break
    if user_word==target_word:
        print("\nfind it : ",target_word)  
        break 
    elif user_word not in words:
        print("\nInvalid input ! enter a valid word or (Q) for quit")
        chance-=1
        if chance==0:
            print("\nChances are over due to Invalid input")
    else:
        print("Wrong guess try again") 
             
        
print("\n******** GAME OVER *********")       
    
    