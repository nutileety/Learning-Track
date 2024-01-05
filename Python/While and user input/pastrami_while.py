sandwich_order = ['grilled cheese','tomato cucumber','pastrami','paneer','curd'
                  ,'pastrami','pastrami']
finished_sandwich = []

#removing repeated pastrami from sandwich_order
while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')
print("Oops!, Deli had run out of pastrami sandwich!\n")

while sandwich_order:
    #printing and moving the prepared sandwich
    current_order = sandwich_order.pop()
    print(f" I had made a {current_order.title()} sandwich.")

    #adding the prepared sandwich to the finished list
    finished_sandwich.append(current_order)

print("\nThe list of finished sandwich are :")
for order in finished_sandwich:
    print(f"* {order.title()} sandwich.")