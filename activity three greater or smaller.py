i=int(input("enter a number:"))
if(i<15):
    print("i is smaller than 15")
    print("i'm in if block")
else:
    if(i==15):
        print("i is equal than 15")
    else:
        print("i is bigger than 15")
    print("i'm in else block")
print("i'm not in if and not in else block")