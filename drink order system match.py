drink = input("Choose from coffee, tea, water and juice ")

match drink.lower():
    case "coffee":
        price = 2.50
    case "tea":
        price = 1.80
    case "water":
        price = 0
    case "juice":
        price = 3.38

print (drink, " and the price is £", price)