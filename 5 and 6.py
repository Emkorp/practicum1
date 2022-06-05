revenue = int(input("What is revenue of your company? "))
prod_cost = int(input("What is production cost  of your company? "))
if revenue > prod_cost:
    print("Your company is profitable, because your revenue is more than production cost")
    profit = revenue / prod_cost
    profit = str(profit)
    print("Profit of your company is " + profit)
    staff = int(input("What is number of your staff? "))
    profit_per_person = str(revenue / staff)
    print("Profit per person of your company is " + profit_per_person)
if revenue < prod_cost:
    print("Your company is not profitable, because your revenue is less than production cost")
