my_food=['dosa','puri','idli','pulav']
friend_food=my_food[:]
my_food.append("ice-cream")
friend_food.append("desert")
print("my fav foods are :")
for my in my_food[:]:
    print(my.title())
print("\nmyfriend's food are :")
for friend in friend_food[:]:
    print(friend.title())