# Exploring the round() function

first_meal = 7.00
second_meal = 9.50
total = first_meal + second_meal
tax = total * 0.15

total_with_tax = round(total + tax)

print("Your first meal was: " + str(first_meal) + "\n")
print("Your second meal was: " + str(second_meal) + "\n")
print("Tax will be included as tip of 15% of your total meal(s) price")

print("The total for your meal today with tax/tip included is: " + str(total_with_tax))
