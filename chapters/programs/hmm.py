A for loop looks like this

for x in range(0,11):
    print(x)

A baker has three customers. He asks them each how many cakes they want
so he knows how many he must bake. He writes this program.

total = 0
print("Customer", 1, "how many cakes do you want?")
cakes = int(input())
total = total + cakes

print("I will bake", total, "cakes!")

Rewrite this program using a for loop so it is only 6 (or fewer) lines. 

total=0
for x in range(1, 4):
    print("Customer", x, "how many cakes do you want?")
    cakes = int(input())
    total = total + cakes

print

The baker gets a fourth customer. Change the program so it works for 4 customers.

The baker has a different number of customers every day. Change the program so it
asks how many customers there are. Store the number typed by the user in a variable
called c. change the loop so it works for c customers.

If a customer orders 12 cakes, he gets an extra cake for free. Use an if statement to check cakes>12. If true, add one more cake.


Rather than the user typing in data, your program might be supplied with data in an array.
here is an array of prices on a shopping list. note we dont use a currency symbol except when we print the price. (also this is bad way to store prices, why? can you think of a better way?)

prices = [3.49, 9.99, 2.50, 20.00]
for price in prices:
    print("item costs £", price)

any item that costs more than 10 will be discounted by 20 percent. use an if statememt to check if the proces is more than 10. if it is, multiply the price by 0.8 to reduce it before you add it to the total.



Sometimes you won't know at the start of the loop how many times you need to iterate.
One solution to this is loop forever with while True. your users probably won't want your prpgram to run forefer however, so you should insert a break statement to end the loop when some condition is met.
