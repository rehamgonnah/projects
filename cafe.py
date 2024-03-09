# list of items sold in the cafe
menu = ["coffee", "croissant", "cake", "juice"]

# stock value for each item on the menu
stock = {"coffee": 50,
         "croissant": 30,
         "cake": 30,
         "juice": 30
         }

# price for each item on the menu
price = {"coffee": 3,
         "croissant": 4,
         "cake": 5,
         "juice": 3
         }

total_stock = 0 # initialising the variable to use inside the for loop

# for loop to loop through the menu items and multiply the stock values by the price values
for item in menu: 
    total_stock += stock[item] * price[item]
    
print("The total stock worth in the cafe = " + str(total_stock))
