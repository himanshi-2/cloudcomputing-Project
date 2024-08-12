chances=4
sum=0
print("****Welcome in HIMANSHI restaurant****")
while chances>0:

    print("\n","what do you want to order")
    print("\n","1.pizza","\n","2.Drink","\n","3.add cheeze")
    option=int(input("enter your choice:"))
    if option==1:
        print("\n","   you want to ordered pizza   ","\n","4. veg","\n","5. NON veg")
        op=int(input("enter your choice: "))
        if op==4:
            print("\n","6. MARGHERITA                    price:199","\n","7. DOUBLEE CHEESE MARGHERITA     price:249","\n","8. FARM HOUSE                    price:299","\n","9. PEPPY PANEER                  price:265")
            mood=int(input("enter your choice: "))
            if mood==6:
                print("********order is confirmed MARGHERITA PIZZA********")
                price=199
                sum+=price
            elif mood==7:
                print("********order is confirmed DOUBLEE CHEESE MARGHERITA******** ")   
                price=249
                sum+=price
            elif mood==8:
                print("********order is confirmed FARM HOUSE********")
                price=299  
                sum+=price   
            elif mood==9:
                print("********order is confirmed PEPPY PANEER********")    
                price=265
                sum+=price
        elif op==5:
            print("\n","10. CHICKEN GOLDEN        price:249","\n","11. CHICKEN DOMINATOR     price:349","\n","12. CHICKEN SAUSAGE       price:299","\n","13. KEEMA DOO PYAZA       price:189")
            choose=int(input("enter your choice: "))
            if choose==10:
                print("******order is confirmed CHICKEN GOLDEN********")
                price=249
                sum+=price
            elif choose==11:
                print("********order is confirmed CHICKEN DOMINATOR********")
                price=349
                sum+=price
            elif choose==12:
                print("********order is confirmed CHICKEN SAUSAGE********")
                price=299
                sum+=price
            elif choose==13:
                print("********order is confirmed KEEMA DOO PYAZA********")
                price=189
                sum+=price
    elif option==2:
        print("\n","what do you want to drink","\n","14. pepsi         price:49","\n","15. tea           price:49","\n","16. coffee        price:89","\n","17. cold coffee   price:69")
        dr=int(input("enter your choice: "))
        if dr==14:
            print("********order is confirmed pepsi********")
            price=49
            sum+=price
        elif dr==15:
            print("********order is confirmed tea********")
            price=49
            sum+=price
        elif dr==16:
            print("********order is confirmed coffee********")
            price=89
            sum+=price
        elif dr==17:
            print("********order is confirmed cold coffee********")
            price=69
            sum+=price   
    elif option==3:
        print("ADD CHEESE ")
        print("*****************only 3 slices you can ADD******************")
        ch=int(input("enter the amount: ")) 
        if ch==1:
            print("1 slice added   price:20")
            price=20
            sum+=price
        elif ch==2:
            print("\n","2 slices added  price:40")
            price=40
            sum+=price
        else:
            print("\n","3 slices added  price:60")     
            price=60 
            sum+=price  
    chances-=1
    if chances==1:
        print("THANK YOU FOR ORDERING COME AGAIN")
        print("Your total= ",sum)
        break






            



    