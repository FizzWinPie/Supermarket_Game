"""
This Python program simulates a user's shopping experience in a supermarket. 
It allows the user to purchase items such as a lottery ticket, apples, cans of beans, and sodas. 
The program guides the user through the shopping process.
"""

import random
winnings = random.randint(2, 10)    # use "winnings = random.randint(2, 10)" to generate a random int from $2 - $10 
probability_of_winning = random.randint(1,3)    # 33% chance of winning

# unit price of items
constant_lottery_unit_price = 2
constant_apple_unit_price = .99
constant_canned_beans_unit_price = 1.58
constant_soda_unit_price = 1.23

lottery_amount, apple_amount, canned_beans_amount, soda_amount = 0, 0, 0, 0

money = 0 # the initial amount of money the user has for shopping
money_spent = 0

#Welcome message and prices
print("\n\n--------------------------------------------")
print("\nHello and Welcome to the supermarket!\n")
print("We have a variety of item to choose from:")
print( "1) lottery tickets: ${}".format(constant_lottery_unit_price))
print( "2) apple: ${}".format(constant_apple_unit_price))
print( "3) canned beans: ${}".format(constant_canned_beans_unit_price))
print( "4) soda: ${}".format(constant_soda_unit_price))


try:
    money = int(input("\nHow much money do you want to spend for shopping? "))
except ValueError:
    print("Please type a valid int")


#Lottery ticket
if money >= 2:
    answer = input("\nYou have ${} available. Would you like to purchase a lottery ticket for $2? (Press y/n) ".format(money))
    if answer == "y" or answer == "Y":
        money_spent += 2
        money -= 2
        lottery_amount += 1
        if probability_of_winning == 1: # probability of winning is 1/3 or 33%
            print("Congrats! You won ${} :)".format(winnings))
            money += winnings
        else:
            winnings = 0
            print("Sorry! You are a loser :(")
        print("\nYou purchased a lottery ticket and you now have ${} available".format(round(money)))
    elif answer == "n" or answer == "N":
        print("No lottery ticket was purchased. Money left: ${}".format(money))
        winnings = 0
else:
    print("You do not have enough money for a lottery ticket.")


#Apples
answer = input("\nWould you like to purchase apples? (Type y/n) ")
try:
    if answer == "y" or answer == "Y":
        apple_amount = int(input("How many? "))
        total_apples_cost = apple_amount * constant_apple_unit_price
        if total_apples_cost <= money:
            money -= total_apples_cost
            money_spent += total_apples_cost
            print("You want to buy {} apples which will cost ${}".format(apple_amount, round(total_apples_cost, 2)))
        else:
            print("You want to buy {} apples which will cost ${}. However, you don't have enough money".format(apple_amount, round(total_apples_cost, 2)))
            apple_amount = 0
    elif answer == "n" or answer == "N":
        print("No apples were purchased")
    else:
        print("Error! Type a valid response (y/n).\nNo purchase was made.\n")
except ValueError:
    print("Error. Type a valid number!\n No apples were purchased")

print("Total money spent: ${}".format(round(money_spent, 2)))
print("Money left: ${}".format(round(money, 2)))


#Beans
answer = input("\nWould you like to purchase cans of beans? (Type y/n) ")
try:
    if answer == "y" or answer == "Y":
        canned_beans_amount = int(input("How many? "))
        total_beans_cost = canned_beans_amount * constant_canned_beans_unit_price
        if total_beans_cost <= money:
            money -= total_beans_cost
            money_spent += total_beans_cost
            print("You want to buy {} cans of beans which will cost ${}".format(canned_beans_amount, round(total_beans_cost, 2)))
        else:
            print("You want to buy {} cans of beans which will cost ${}. However, you don't have enough money".format(canned_beans_amount, round(total_beans_cost, 2)))
            canned_beans_amount = 0
    elif answer == "n" or answer == "N":
        print("No cans of beans were purchased")
    else:
        print("Error! Type a valid response (y/n).\nNo purchase was made.\n")
except ValueError:
    print("Error. Type a valid number!\n No beans were purchased")

print("Total money spent: ${}".format(round(money_spent, 2)))
print("Money left: ${}".format(round(money, 2)))


#Soda
answer = input("\nWould you like to purchase soda? (Type y/n) ")
try:
    if answer == "y" or answer == "Y":
        soda_amount = int(input("How many? "))
        total_soda_cost = soda_amount * constant_soda_unit_price
        if total_soda_cost <= money:
            money -= total_soda_cost
            money_spent += total_soda_cost
            print("You want to buy {} soda which will cost ${}".format(soda_amount, round(total_soda_cost, 2)))
        else:
            print("You want to buy {} soda which will cost ${}. \nHowever, you don't have enough money.".format(soda_amount, round(total_soda_cost, 2)))
            soda_amount = 0
    elif answer == "n" or answer == "N":
        print("No sodas were purchased")
    else:
        print("Error! Type a valid response (y/n).\nNo purchase was made.\n")
except ValueError:
    print("Error. Type a valid number!\n No sodas were purchased")

print("Total money spent: ${}".format(round(money_spent, 2)))
print("Money left: ${}".format(round(money, 2)))


#Ending
print("\n\n->>> This is your closing statement <<<-")
print("\nMoney left: ${}".format(round(money, 2)))
print("Money spent: ${}".format(round(money_spent, 2)))
print("Nr of lottery tickets purchased: {}".format(lottery_amount))
print("Amount of lottery winnings: ${}".format(round(winnings)))
print("Nr of apples: {}".format(apple_amount))
print("Nr of cans of beans: {}".format(canned_beans_amount))
print("Nr of sodas: {}".format(soda_amount))
print("--------------------------------------------")
