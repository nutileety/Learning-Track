from pathlib import Path
#importing Path class to read the file

path = Path('pi_million_digits.txt')
contents  = path.read_text()
lines = contents.splitlines()

pi_string = ''
for line in lines:
    # print(line)
    pi_string += line.strip()
print(f"{pi_string[:52]}....")
print(len(pi_string))