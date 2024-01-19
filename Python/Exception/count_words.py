from pathlib import Path

def count_words(path):
    try:
        content = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print("The file is not exists")
        pass

    else:
        words = content.split()  #split() helps to convert the text lines into list words by words.
        print(f"The file {path} contains {len(words)} words.")


files = ['guest_book.txt','learning_python.txt','siddharth.txt','programming.txt']
for file in files:
    path = Path(file)
    count_words(path)
