from pathlib import Path

def count_words(filename,word):
    path = Path(filename)
    content = path.read_text()
    the_words = content.lower().count(word)
    print(f"The number of 'the ' words in {filename} file are {the_words}")

count_words('gutenburg_raw.txt','the ')