from pathlib import Path

filenames = ['cats.txt','dogs.txt']
for filename in filenames:
    try:
        path = Path(filename)
        content = path.read_text()
    except FileNotFoundError:
        pass # pass or silient the exception if file is misssing.
        # print("The file is missing which you are looking for!")
    else:
        print(content,"\n")
