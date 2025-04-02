# Luke Murdock, Financial Calculator

def main(): # Lets user pick what they want to do with the financial calculator
    while True:
        try:
            choice = int(input("\nFinancial Calculator:\nBudget Allocator(1) Tip(2) Sale Price(3) Compoud Interest(4) Savings Goal(5) Done(6)\n"))        
        except:
            print("Invalid Input")
            continue
        if choice <= 0 or choice > 6:
            print("Invalid Input")
            continue
        break

    if choice == 1:
        budget()
    elif choice == 2:
        tip()
    elif choice == 3:
        sale()
    elif choice == 4:
        comp()
    elif choice == 5:
        goal()
    elif choice == 6:
        print("Come back soon!")
        return
    
def budget(): # Allocates a persons money into savings, bills, food, and fun
    while True:
        try:
            ans = float(input("How much money do you have?: "))
        except:
            print("Invalid Input")
            continue
        break

    # Formats and calculates how much money should be spent in each category
    print(f"\nSavings: ${round(ans*0.2, 2):,.2f} | Bills: ${round(ans*0.5, 2):,.2f} | Food: ${round(ans*0.2, 2):,.2f} | Fun: ${round(ans*0.1, 2):,.2f}")
    main()

def tip(): # Calculates how much a tip will cost and the total cost
    while True:
        try:
            cost = float(input("How much are you spending?: "))
            tip = float(input("What percentage is your tip in decimal form?: "))
        except:
            print("Invalid Input")
            continue
        break

    print(f"\nTip Cost: ${round(cost*tip, 2):,.2f} | Total Cost: ${round(cost*tip+cost, 2):,.2f}")
    main()

def sale(): # Calculates how much money is saved with a discount and what is the final cost
    while True:
        try:
            cost = float(input("How much are you spending?: "))
            disc = float(input("What percentage is your discount in decimal form?: "))
        except:
            print("Invalid Input")
            continue
        break

    print(f"\nMoney Saved: ${round(cost*disc, 2):,.2f} | Final Cost: ${round(cost-cost*disc, 2):,.2f}")
    main()

def comp(): # Calculates how much money you will get
    while True:
        try:
            start_money = money = float(input("How much money is in the account?: "))
            interest = float(input("How much interest in decimal form?: "))
            time = float(input("How many times will interest occur before you take out your money?: "))
        except:
            print("Invalid Input")
            continue
        break
    i = 1
    while i <= time:
        money = money*interest + money
        i += 1
    print(f"\nMoney Gained: ${round(money-start_money, 2):,.2f} | Final Money: ${round(money, 2):,.2f}")
    main()

def goal(): # Tells the user how long it will take to complete their savings goal
    while True:
        try:
            occur = int(input("How often are you depositing? Weekly(1) Monthly(2)\n"))
            deposit = float(input("How much money are you depositing each time?: "))
            goal = float(input("How much money do you want saved?: "))
        except:
            print("Invalid Input")
            continue
        if occur <= 0 or occur > 2:
            continue
        break

    time = round(goal/deposit)
    print(f"\nTo reach this goal, it will take you about {time} {'week' if occur == 1 else 'month'}{'s' if time > 1 else ''}.")
    main()

if __name__ == "__main__":
    main()