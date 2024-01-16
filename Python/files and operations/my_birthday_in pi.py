from pathlib import Path 

path = Path("pi_million_digits.txt")
contents = path.read_text()
lines = contents.splitlines()
pi_digits = ''
for line in lines:
    pi_digits += line.strip()
birth_date = input("Enter your DOB (dd/mm/yy): ")
if birth_date in pi_digits:
    print("Your DOB is in first million pi digits.")
else:
    print("Your DOB is not in first million pi digits.")    