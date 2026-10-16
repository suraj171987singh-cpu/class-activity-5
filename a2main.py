costprice = float(input("Enter the cost price: "))
sellingprice = float(input("Enter the selling price: "))


if (sellingprice > costprice):
    Profit = sellingprice - costprice 

    print("Profit of the product is ", Profit)
else: 
    print("No profit")