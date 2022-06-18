print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $$$"))

tmp = input(
    "What percentage of the tip whold you like to give? *just the number:")
tip_p = int(tmp)
tip = tip_p / 100 * bill
total_fee = bill + tip
tmp = input("How many people split the bill?")
split = int(tmp)
split_fee = round(total_fee / split, 2)
print(f"each of you spend {split_fee} each")
