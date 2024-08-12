list=["rahul",'ramesh','amrita','kritika','khushi','shweta','kunal','schine','shweta','ayush','dhruv']
labour=[]
today=5
while today>=0:
    def func(name):
        if name in list:
            print("present",name)
            labour.append(name)
        elif name not in list:
            names=input("Do you want the labour in the list(yes/no): ")
            if names=="yes":
                labour.append(name)
                print(name ,"is add today")
            else:
                print(name,"we don't add you today")
        else:
            list.remove(name)
            print(name,"is not present so it removed from the list")
            
    func(input("enter the name: "))
    today-=1
print("updated list of labours: ",labour)
print("they are present for full time so each person ruppes:200")
pi=len(labour)
print(pi ,"num of labour so total is: ",pi*200)
    