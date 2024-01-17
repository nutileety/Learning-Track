from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()
print("1st time:")
print(content)

print(f"\n{content.replace('Python','Java')}")

print("\n2nd time:")
for line in  content.splitlines():
    print(line)