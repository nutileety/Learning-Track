# create variable of string
# create an empty list variable to words
# create empty string variable to build the currend_word
# iterate the string:
#   if there is not space:
    # add it to the current word of string
# else
    # add it to the list of word
    # reset the current word to restart fresh

# add the last word to the list

# create empty string result
# iterate thte list decrementally
    # add the list elements to the result string
# print the resersed variable

sentence = 'I Love Python'
words = []
current_word = ''
for char in sentence:
    if not char.isspace():
        current_word += char
    else:
        words.append(current_word)
        current_word = ''

words.append(current_word)

result = ''
for word in range(len(words)):
    result = words[word]+ ' ' + result
print(result)
    