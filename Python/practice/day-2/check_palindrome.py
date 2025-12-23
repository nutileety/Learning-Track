word = 'madam'
reversed_word = ''
for i in word:
    reversed_word = i + reversed_word
if (word == reversed_word):
    print(True)
else:
    print(False)