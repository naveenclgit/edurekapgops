price = 50
paid = 0
tpaid = 0
balance = price - tpaid

while paid < price:
    paid = int(input("Insert Coin: "))
    if paid in [5,10,25]:
        tpaid = tpaid + paid
        balance = price - tpaid
        if balance > 0:
            print (f"Amount Due: {balance}")
        else:
            balance = -(balance)
            print (f"Change Owed: {balance}")
            break
    else:
        print (f"Amount Due: {balance}")
