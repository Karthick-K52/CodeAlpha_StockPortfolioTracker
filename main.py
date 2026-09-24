def main():
    stock_price={'AAPL':180,'TSLA':250,'GOOG':150,'MSFT':400,'AMZN':200}
    print ()
    print("Available Stocks")
    for i in stock_price:
        print(i)

    while True:
        try:
            stock_count=int(input("Out of 5 Stocks.How many different stocks do you want to buy?:"))
            if stock_count<=0 or stock_count>5:
                print("Please Enter The valid Amount Of number...")
                print()
            else:
                break
        except ValueError:
            print("Please Enter the different stock count in number...")
            print()

    stock_list=[]
    quantity_list=[]

    for i in range(stock_count):
        stock_valid=False
        quantity_valid=False

        while not stock_valid:
            print()
            stock=input(f"Enter the name of stock {i+1}:").upper().strip()
            if stock in stock_price:
                stock_valid=True
            else:
                print("Please select the listed stock...")

        while not quantity_valid:
            try:
                quantity=int(input("Enter the stock quantity: "))
                if quantity>0:
                    quantity_valid=True
                    stock_list.append(stock)
                    quantity_list.append(quantity)
                else:
                    print("Please Enter the valid quantity...")
            except ValueError:
                print("Enter the quantity in numbers... ") 
                print()  
    print()
    total_amount=0
    for i in range (stock_count):
        stock_name=stock_list[i]
        print("Stock Name:",stock_name)
        investment_amount=quantity_list[i]*stock_price[stock_name]
        print("Quantity:",quantity_list[i])
        print("Investment:",investment_amount)
        total_amount+=investment_amount

    print("Total Amount:",total_amount)
main()