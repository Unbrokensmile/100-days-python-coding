print ("Welcome to the tip calculator ")
money = input("What was the total bill? $$$")
money = float(money)
tip_p = input("What precentage of the tip whold you like to give? *just the number")
tip_p = int(tip_p)
tip_p2 = tip_p / 100 * money
money2 = money + tip_p2
split1 = input("How many people split the bill?")
split1 = int(split1)
money2 = round(money2 / split1, 2)
print(f"each of you spend{money2} each")
