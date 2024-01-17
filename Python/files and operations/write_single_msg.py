from pathlib import Path
contents = 'I love programming.'
contents += '\nI want to stay consistent in the coding.'
contents +=  '\nI want love my learning journey.'

path =  Path('programming.txt')
path.write_text(contents)
