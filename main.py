import time
print("Welcome to the Grocery Store!")
time.sleep(1)
print("Aisle 1 is the produce aisle, Aisle 2 is the snack aisle, Aisle 3 is the drinks aisle, Aisle 4 is the canned food aisle, Aisle 5 is the bread / cereal aisle, Aisle 6 is the meat / poultry aisle, Aisle 7 is the dairy aisle, and Aisle 8 is the frozen food aisle.")
time.sleep(14)
doneShopping = False
cart = []
subtotal = 0
total = 0
aislesDictionary = {"Aisle 1": ["1: Apples ($3.00 per pound)", "2: Oranges ($2.90 per pound)", "3: Bananas ($3.20 per pound)", "4: Avocados ($4.10 per pound)", "5: Tomatoes ($3.70 per pound)", "6: Spinach ($4.00 per pound)", "7: Broccoli ($3.80 per pound)", "8: Potatoes ($2.80 per pound)"],
                    "Aisle 2": ["1: Mini Chocolate Chip Cookies ($5.80 per container)", "2: Party-Size Lays Salt And Vinegar Chips ($3.40 per bag)", "3: Party-Size Lays Barbecue Chips ($3.50 per bag)", "4: Party-Size Lays Sour Cream and Onion Chips ($3.50 per bag)", "5: Double Stuffed Oreos ($3.20 per container)", "6: Haribo Gummy Bears ($2.90 per bag)", "7: Hershey's Chocolate Bars ($1.30 per bar)", "8: Snickers Bars ($1.40 per bar)"],
                    "Aisle 3": ["1: Coca-Cola ($1.80 per bottle)", "2: Diet Coca-Cola ($1.60 per bottle)", "3: Pepsi ($1.75 per bottle)", "4: Diet Pepsi ($1.60 per bottle)", "5: Orange Fanta ($2.00 per bottle)", "6: Dr. Pepper ($2.05 per bottle)", "7: Lemonade ($2.25 per bottle)", "8: Purified Water ($2.00 per bottle)"],
                    "Aisle 4": ["1: Canned Beans ($1.05 per can)", "2: Canned Peas ($1.10 per can)", "3: Canned Tomatoes ($1.15 per can)", "4: Canned Mixed Vegetables ($1.40 per can)", "5: Canned Chilies ($1.25 per can)", "6: Canned Artichoke Hearts ($1.35 per can)", "7: Canned Jalapeños ($1.40 per can)", "8: Canned Pineapple ($1.25 per can)"],
                    "Aisle 5": ["1: White Bread ($2.80 per loaf)", "2: Multigrain Bread ($3.20 per loaf)", "3: Rye Bread ($2.90 per loaf)", "4: Plain Bagels ($2.90 per bag)", "5: Sesame Bagels ($3.00 per bag)", "6: Rice Krispies Cereal ($2.70 per box)", "7: Cocoa Puffs Cereal ($2.85 per box)", "8: Honey Bunches of Oats Cereal ($3.00 per box)"],
                    "Aisle 6": ["1: Chicken Thigh ($2.20 per pound)", "2: Chicken Breast ($2.30 per pound)", "3: Salmon Filet ($2.10 per poud)", "4: Albacore Tuna Filet ($2.00 per pound)", "5: Bacon ($3.80 per pound)", "6: Pork Shoulder ($4.00 per pound)", "7: Rib-Eye Steak ($5.20 per pound)", "8: Ground Beef ($5.00 per pound)"],
                    "Aisle 7": ["1: Whole Milk ($3.20 per gallon)", "2: Reduced-Fat Milk (3.00 per gallon)", "3: Fat-Free Milk ($2.90 per gallon)", "4: Soy Milk ($2.90 per gallon)", "5: Heavy Cream ($2.00 per container)", "6: Unsalted Butter ($1.15 per stick)", "7: Cheddar Cheese Slices ($2.30 per package)", "8: Mozzarella Cheese Slices ($2.40 per pound)"],
                    "Aisle 8": ["1: Frozen Green Beans ($2.30 per bag)", "2: Frozen Corn ($2.25 per bag)", "3: Frozen Peas ($2.10 per bag)", "4: Frozen Mixed Vegetables ($2.60 per bag)", "5: Strawberry Popsicles ($3.20 per box)", "6: Orange Popsicle ($3.10 per box)", "7: Vanilla Ice Cream ($3.50 per container)", "8: Chocolate Ice Cream ($3.55 per container)"]}
aisle = input("Which aisle would you like to go to?")
for i in aislesDictionary[aisle]:
    print(i)
    time.sleep(1)
while doneShopping == False:
    items = input("Enter the item you would like to buy. Only enter ONE item here (you can add others later). If you are done shopping in this aisle, enter 's'. If you would like to proceed to checkout, enter 'd'. ")
    while items != "s" and items != "d":
        myAisle = aislesDictionary[aisle]
        # Adds the item entered to the cart
        cart.append(myAisle[int(items) - 1])
        print(myAisle[int(items) - 1])
        # Give the program another action so that it doesn't get stuck on the print statement
        items = input("Enter the item you would like to buy. Only enter ONE item here (you can add others later). If you are done shopping in this aisle, enter 's'. If you would like to proceed to checkout, enter 'd'. ")

    if items == "s":
        aisle = input("Which aisle would you like to go to?")
        myAisle = aislesDictionary[aisle]

        for i in aislesDictionary[aisle]:
            print(i)
            time.sleep(1)
        items = input("Enter the item you would like to buy. Only enter ONE item here (you can add others later). If you are done shopping in this aisle, enter 's'. If you would like to proceed to checkout, enter 'd'. ")
        cart.append(myAisle[int(items) - 1])
        print(myAisle[int(items) - 1])
    if items == "d":
        doneShopping = True
print("You have entered the checkout area. ")
time.sleep(1)
print("Your cart: \n")
for i in cart:
    print(i)
    time.sleep(0.5)
for i in cart:
    index = i.find("$")
    subtotal += float(i[index + 1:index + 5])
print("Your subtotal is: $", subtotal)
total = 1.07 * subtotal
time.sleep(1)
print("Your total is: $", round(total, 2))
time.sleep(1)
print("Thank you for shopping here! Please come again!")