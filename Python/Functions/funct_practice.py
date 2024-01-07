def funct(names):
    while names:
        print(f"Hello! {names}")
        if names == None:
            break

output = ['john','max','tom']
funct(output)