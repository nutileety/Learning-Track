def print_function(**models):
    print("I like some of the car models are:")
    for name,model in models.items():
        print(f"{name.title()} : {model.title()}")

