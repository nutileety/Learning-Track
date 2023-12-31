alien={}
alien['color']="green"
alien['points']=20
# points=alien['points']
print(f"You have earned {alien['points']} points")
alien['x_pos']=0
alien['y_pos']=25
print(alien)

#deleting key and values
del alien['points']
print("After deleting ",alien)

alien['color']="yellow"
print(f"The alien color is now \"{alien['color']}\"")

alien_1={'x_pos': 0, 'y_pos': 25,'speed':'medium'}
print("Original position :",alien_1['x_pos'])
#speed is fast
alien_1['speed']='fast'

if alien_1['speed'] == 'slow':
    x_plus = 1
elif alien_1['speed'] == 'medium':
    x_plus = 2
else:
    x_plus = 3

alien_1['x_pos'] = alien_1['x_pos'] + x_plus
print("New position :",alien_1['x_pos'])




