buyingcost=float(input("Give the price at which you bought the apple"))
sellingcost=float(input("Give the price at which you sold the apple"))
if (sellingcost>buyingcost):
    amount=float(sellingcost-buyingcost)
    print("Hurray! You made a profit of ",(amount))
else:
    print("No profit :(")
