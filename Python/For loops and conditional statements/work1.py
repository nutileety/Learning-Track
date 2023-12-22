"""2-3. Personal Message: Use a variable to represent a person’s name, and print a
message to that person. Your message should be simple, such as, “Hello Eric, would you
like to learn some Python today?” """

"""2-4. Name Cases: Use a variable to represent a person’s name, and then print that
person’s name in lowercase, uppercase, and title case."""

message="hello charlie, how is your learning experience in Python "
print(message)

message="chaRlie"
print(message.title())
print(message.upper())
print(message.lower())

""". Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s
 name using a variable called famous_person. Then compose your message and represent
 it with a new variable called message. Print your message."""

famous_person="charlie chaplin"
message="\"simplicity is difficult to achive\""

quote=f"{famous_person.title()} once said {message}"
print(quote)

"""2-7. Stripping Names: Use a variable to represent a person’s name, and include some
whitespace characters at the beginning and end of the name. Make sure you use each
character combination, "\t" and "\n", at least once.
"""

person_name=" names of persons: \n\t-John\n\t-Charlie\n\t-Tomy"
print(person_name.lstrip())