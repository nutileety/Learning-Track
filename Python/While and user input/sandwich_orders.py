sandwich_order = ['grilled cheese','tomato cucumber','paneer','curd']
finished_sandwich = []
while sandwich_order:
    current_order = sandwich_order.pop()
    print(f" I had made a {current_order.title()} sandwich.")
    finished_sandwich.append(current_order)

print("\nThe list of finished sandwich are :")
for order in finished_sandwich:
    print(f"* {order.title()} sandwich.")