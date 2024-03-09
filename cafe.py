# List of items sold in the cafe
menu = ["coffee", "croissant", "cake", "juice"]

# Stock value for each item on the menu
stock = {"coffee": 50,
         "croissant": 30,
         "cake": 30,
         "juice": 30
         }

# Price for each item on the menu
price = {"coffee": 3,
         "croissant": 4,
         "cake": 5,
         "juice": 3
         }

# Initialize variable for total stock worth
total_stock = 0

# Loop through the menu items and calculate the total stock worth
for item in menu: 
    total_stock += stock[item] * price[item]

# Display the total stock worth in the cafe
print("The total stock worth in the cafe = $" + str(total_stock))
