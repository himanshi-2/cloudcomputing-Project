bal=2000
PIN=1235
chance = 5
print('*******WELCOME********')
while chance>=0:
    x=int(input('Enter PIN Number: '))
    if x==PIN:
        print('*Login Sucessful*')
        x = int(input('Press 1 to continue: '))
        if x == 1:
            print('1. Check Balance')
            print('2. Withdraw Amount')
            d=int(input('Enter Your Choice: '))
            if d==1:
                print('Your Balance is: ')
                print(bal)
            elif d==2:
                wd=int(input('Enter amount to withdraw:'))
                if wd<bal:
                    print('withdraw successful')
                    bal=bal-wd
                else:
                    print('insufficient funds')
        else:
            print('Successfully Logged Out')
    else:
        print('Invalid Password')
        chance-=1
        if chance==0:
            print('******Account Blocked******')
            break