import time, random
realIngQ = ["10 6-inch tortillas", "2 cups Monterey Jack cheese", "1 2-ounce can sliced black olives", "5 tablespoons neutral oil", "5 tablespoons hot sauce"]
fakeIngQ = ["1 teaspoon baking soda", "1 cup chocolate chips", "3 large eggs", "2 cups kale", "4 tablespoons orange juice"]
realIngS = ["8 ounces spaghetti noodles", "4 cups tomato sauce", "8 teaspoons salt", "2 cups grated parmesan cheese", "4 tablespoons olive oil"]
fakeIngS = ["2 cups cocoa powder", "4 slices white bread", "1 teaspoon apple cider vinegar", "4 pounds spinach", "1 whole lemon"]
realIngC = ["8 ounces softened cream cheese", "1 14-ounce can condensed milk", "2 teaspoons vanilla extract", "18 - 20 graham crackers", "2 tablespoons unsalted butter"]
fakeIngC = ["1 cup freeze-dried blueberries", "1 whole bell pepper, diced", "1 tablespoon black pepper", "2 chicken thighs", "3 bags green tea"]
numberItemsGuessedRight = 0
totalIngQ = realIngQ + fakeIngQ
random.shuffle(totalIngQ)
totalIngS = realIngS + fakeIngS
random.shuffle(totalIngS)
totalIngC = realIngC + fakeIngC
random.shuffle(totalIngC)
print("Welcome to the Cooking Game!")
time.sleep(1)
print("There are two parts to the game. In the first part, you will have to identify the five ingredients that are present in the recipe and the five fake ones. In the second part, you will have to rearrange the steps of the recipe so that they are in the right order.")
time.sleep(10)
level = input("Choose a level by typing 1, 2, or 3. ")
print("PART 1\n")
time.sleep(1)
if level == "1":
    print("Below are a list of 10 ingredients. You will have to identify which five are part of the recipe (quesadillas), and which five are fake.\n")
    time.sleep(2)
    for i in totalIngQ:
        print(i)
        time.sleep(1.5)
    while numberItemsGuessedRight < 5:
        itemGuessed = input("Enter ONE of the items you believe are actually in the recipe. Enter the item and the amount (e.g. 1/2 tablespoon salt): ")
        time.sleep(0.5)
        if itemGuessed in realIngQ:
            print("Correct! That is one of the real ingredients. \n")
            numberItemsGuessedRight += 1
            realIngQ.remove(itemGuessed)
            time.sleep(1)
        elif itemGuessed in fakeIngQ:
            print("Incorrect! That is one of the fake ingredients. \n")
            time.sleep(1)
        else:
            print("Please enter a valid input.")
        print("There are / is", 5 - numberItemsGuessedRight, "correct item(s) remaining. ")
        time.sleep(1)
    print("PART 2\n")
    time.sleep(1)
    print("For the next part, you will have to rearrange the steps of the recipe so that they are in the correct order.")
    time.sleep(2)
    steps = ["Add 1 tablespoon oil to a large frying pan or griddle and heat over medium heat.", "Place one tortilla flat on the frying pan, cook for 1 minute, and flip the tortilla over.", "Sprinkle a little more than 1/4 cup cheese on top of tortilla, followed by your desired amount of olives and hot sauce.", "Lay another tortilla on top to make a sandwich and cover with a lid. Cook for 1 minute, then flip the quesadilla.", "Once the cheese has melted, transfer the quesadilla to a plate. Cut and serve."]
    shuffledSteps = ["Add 1 tablespoon oil to a large frying pan or griddle and heat over medium heat.", "Place one tortilla flat on the frying pan, cook for 1 minute, and flip the tortilla over.", "Sprinkle a little more than 1/4 cup cheese on top of tortilla, followed by your desired amount of olives and hot sauce.", "Lay another tortilla on top to make a sandwich and cover with a lid. Cook for 1 minute, then flip the quesadilla.", "Once the cheese has melted, transfer the quesadilla to a plate. Cut and serve."]
    random.shuffle(shuffledSteps)
    print("Here are the steps:\n")
    time.sleep(1)
    for i in shuffledSteps:
        print(i)
        time.sleep(5)
    numberStepsGuessedRight = 0
    while numberStepsGuessedRight < 5:
        stepGuessed = input("Enter the FIRST WORD of Step " + str(numberStepsGuessedRight + 1) + ": ")
        splitSteps = steps[numberStepsGuessedRight].split()
        if stepGuessed == splitSteps[0]:
            print("Correct! That is the right step.\n")
            numberStepsGuessedRight += 1
            time.sleep(1)
        elif stepGuessed != splitSteps[0]:
            print("Incorrect! That is not the right step.\n")
            time.sleep(1)
        else:
            print("Please enter a valid input.")
    if numberStepsGuessedRight == 5:
        print("Congratulations! You have completed the stage!")
elif level == "2":
    print("Below are a list of 10 ingredients. You will have to identify which five are part of the recipe (spaghetti), and which five are fake.\n")
    time.sleep(2)
    for i in totalIngS:
        print(i)
        time.sleep(1.5)
    while numberItemsGuessedRight < 5:
        itemGuessed = input("Enter ONE of the items you believe are actually in the recipe. Enter the item and the amount (e.g. 1/2 tablespoon salt): ")
        time.sleep(0.5)
        if itemGuessed in realIngS:
            print("Correct! That is one of the real ingredients. \n")
            numberItemsGuessedRight += 1
            realIngS.remove(itemGuessed)
            time.sleep(1)
        elif itemGuessed in fakeIngS:
            print("Incorrect! That is one of the fake ingredients. \n")
            time.sleep(1)
        else:
            print("Please enter a valid input.")
        print("There are / is", 5 - numberItemsGuessedRight, "correct item(s) remaining. ")
        time.sleep(1)
    print("PART 2\n")
    time.sleep(1)
    print("For the next part, you will have to rearrange the steps of the recipe so that they are in the correct order.")
    time.sleep(2)
    steps = ["Bring 4-6 quarts of water to a boil",  "Once boiling, add 2 ounces of spaghetti and cook for 9 minutes. Drain off the hot water and rinse with cold water for 5 seconds.", "In a separate heated pot, add a cup of tomato sauce, a tablespoon of olive oil, and 2 teaspoons of salt. Mix until combined.", "Add the cooked pasta to the sauce pot and saute for 2 - 3 minutes.", "Remove pasta and sauce from pot, plate, add 1/2 cup of parmesan cheese on top, and serve."]
    shuffledSteps = ["Bring 4-6 quarts of water to a boil",  "Once boiling, add 2 ounces of spaghetti and cook for 9 minutes. Drain off the hot water and rinse with cold water for 5 seconds.", "In a separate heated pot, add a cup of tomato sauce, a tablespoon of olive oil, and 2 teaspoons of salt. Mix until combined.", "Add the cooked pasta to the sauce pot and saute for 2 - 3 minutes.", "Remove pasta and sauce from pot, plate, add 1/2 cup of parmesan cheese on top, and serve."]
    random.shuffle(shuffledSteps)
    print("Here are the steps:\n")
    time.sleep(1)
    for i in shuffledSteps:
        print(i)
        time.sleep(6)
    numberStepsGuessedRight = 0
    while numberStepsGuessedRight < 5:
        stepGuessed = input("Enter the FIRST WORD of Step " + str(numberStepsGuessedRight + 1) + ": ")
        splitSteps = steps[numberStepsGuessedRight].split()
        if stepGuessed == splitSteps[0]:
            print("Correct! That is the right step.\n")
            numberStepsGuessedRight += 1
            time.sleep(1)
        elif stepGuessed != splitSteps[0]:
            print("Incorrect! That is not the right step.\n")
            time.sleep(1)
        else:
            print("Please enter a valid input.")
    if numberStepsGuessedRight == 5:
        print("Congratulations! You have completed the stage!")
elif level == "3":
    print("Below are a list of 10 ingredients. You will have to identify which five are part of the recipe (cheesecake), and which five are fake.\n")
    time.sleep(2)
    for i in totalIngC:
        print(i)
        time.sleep(1.5)
    while numberItemsGuessedRight < 5:
        itemGuessed = input("Enter ONE of the items you believe are actually in the recipe. Enter the item and the amount (e.g. 1/2 tablespoon salt): ")
        time.sleep(0.5)
        if itemGuessed in realIngC:
            print("Correct! That is one of the real ingredients. \n")
            numberItemsGuessedRight += 1
            realIngC.remove(itemGuessed)
            time.sleep(1)
        elif itemGuessed in fakeIngC:
            print("Incorrect! That is one of the fake ingredients. \n")
            time.sleep(1)
        else:
            print("Please enter a valid input.")
        print("There are / is", 5 - numberItemsGuessedRight, "correct item(s) remaining. ")
        time.sleep(1)
    print("PART 2\n")
    time.sleep(1)
    print("For the next part, you will have to rearrange the steps of the recipe so that they are in the correct order.")
    time.sleep(2)
    steps = ["Melt the butter. Then, in a food processor or by hand, crush the graham crackers and mix with the melted butter.", "Add the graham cracker mixture to a 9-inch springform cake pan, and set in the fridge for an hour.", "In a large mixing bowl, add the cream cheese and beat until fluffy. Gradually stir in the condensed milk and vanilla extract until fully combined.", "Spoon the filling into the set crust and smooth the top with an offset spatula. Refrigerate for 4 hours.", "Remove the cheesecake from the pan by running a knife along the side of the pan. Cut and serve."]
    shuffledSteps = ["Melt the butter. Then, in a food processor or by hand, crush the graham crackers and mix with the melted butter.", "Add the graham cracker mixture to a 9-inch springform cake pan, and set in the fridge for an hour.", "In a large mixing bowl, add the cream cheese and beat until fluffy. Gradually stir in the condensed milk and vanilla extract until fully combined.", "Spoon the filling into the set crust and smooth the top with an offset spatula. Refrigerate for 4 hours.", "Remove the cheesecake from the pan by running a knife along the side of the pan. Cut and serve."]
    random.shuffle(shuffledSteps)
    print("Here are the steps:\n")
    time.sleep(1)
    for i in shuffledSteps:
        print(i)
        time.sleep(6)
    numberStepsGuessedRight = 0
    while numberStepsGuessedRight < 5:
        stepGuessed = input("Enter the FIRST WORD of Step " + str(numberStepsGuessedRight + 1) + ": ")
        splitSteps = steps[numberStepsGuessedRight].split()
        if stepGuessed == splitSteps[0]:
            print("Correct! That is the right step.\n")
            numberStepsGuessedRight += 1
            time.sleep(1)
        elif stepGuessed != splitSteps[0]:
            print("Incorrect! That is not the right step.\n")
            time.sleep(1)
        else:
            print("Please enter a valid input.")
    if numberStepsGuessedRight == 5:
        print("Congratulations! You have completed the stage!")