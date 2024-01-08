# unfinished_model = ['mobile case','zip','rubiks']
# completed_model = []
# while unfinished_model:
#     printing_model = unfinished_model.pop()
#     print("printing:",printing_model)
#     completed_model.append(printing_model)

# print("\nThe completed models are: ")
# for complete in completed_model:
    # print(complete)

def printing_model(unfinished_model,completed_model):
    while unfinished_model:
        printing = unfinished_model.pop()
        print("Printing:",printing)
        completed_model.append(printing)

def completing(completed_model):
    print("\nThe completed models are:")
    for complete in completed_model:
        print(complete)

unfinished= ['mobile case','zip','rubiks']
completed = []
printing_model(unfinished[:],completed)
completing(completed)
print(unfinished)