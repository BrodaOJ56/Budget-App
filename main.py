import budget

food = budget.Category("Food")
food.deposit(5000, "Initial deposit")
food.withdraw(150, "Groceries")
food.withdraw(200, "Restuarant purchase")
print (food.get_balance())
clothing = budget.Category("Clothing")
food.transfer (300, clothing)
clothing.withdraw(50, "Shopping")
clothing.withdraw(150,"Shopping")
entertainment = budget.Category("Entertainment")
entertainment.deposit(20000,"Initial deposit" )
entertainment.withdraw(100,"Birthday")
entertainment.withdraw(15000,"Wedding")

print(food)
print(clothing)
print(entertainment)
