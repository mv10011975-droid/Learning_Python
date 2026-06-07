expences={
    "Housing":25000 ,
    "Foods":15000,
    "Jym Subscription":5000,
    "Fuel":3400,
    "Transport":2500,  
}
print("Your current expences are")
for key,value in expences.items():
    print(key,":",value)
while True:
    while True:   
        try :
            n=int(input("1.Add expence\n2.Show expence\n3.show total spending\n4.Show category wise spending\n5.Delete Expense Category\n6.Exit\nSelect option you want to continue with"))
            if n<1 or n>6 :
                raise ValueError
            break
        except ValueError :
            print("Select between given 6 option")

    if n ==1 :
        while True:
            try:
                u=int(input("How many expences:"))
                break
            except ValueError:
                print("Integers value only")
        for i in range(u):
            while True:
                x=input("Type of expence:")
                if x in expences:
                    print(f"{x} already exist.\nType what to do further\n1.Add in expence\n2.Update expence of {x} ")
                    while True:
                        try:
                            w=int(input())
                            if w<1 or w>2 :
                                raise ValueError 
                            break
                        except ValueError :
                            print("Type appropriate option")
                    
                    break
                else:break
            while True:
                try:
                    t=float(input("Amount:"))
                    if t<0:
                        raise ValueError
                    break
                except ValueError:print("Numerical value only")
            if x in expences:
                if w==1:
                    expences[x]+=t
                else : expences[x]=t
            else:expences[x]=t
        print(f"Updated expences are: {expences}")
    
    elif n==2:
        print(f"Your expence is {expences}")

    elif n==3:
        r=sum(expences.values())
        print(f"Your total spending is:{r}")
    elif n==4:
        for key,value in expences.items():
            print(key,":",value)
    elif n==5:
        for key,values in expences.items():
            print(key,":",values)
        try:
            h=input("Type expence you wanat to remove:")
            del expences[h]
        except KeyError:
            print("Write whatever expence is present also check spelling mistakes")
        
        print("Updated expences is")
        for key,values in expences.items():
            print(key,":",values)
    elif n==6:
        print("Thankyou")
        break
