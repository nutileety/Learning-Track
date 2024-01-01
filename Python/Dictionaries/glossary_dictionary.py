glossary={
    'string':'collections of characters',
    'variable':'lable to the value',
    'array':'homogeneous collections of string',
    'datatypes':'collections of possible values',
    'algorithm':'steps helps to perform a specified problems',
    'flowchart':'The daigramatical representation of the problem',
    'float':'it is a datatype used for decimals',
    'integers':'it is a datatype used for whole numbers',
    'boolean':'it is also a datatype used for true or false statements',
    'looping':'repeating the set of statements until the condition is flase'
    }
print(f"string:\n{glossary['string']}\n")
print(f"variable:\n{glossary['variable']}\n")
print(f"array:\n{glossary['array']}\n")
print(f"datatype:\n{glossary['datatypes']}\n")
print(f"algorithm:\n{glossary['algorithm']}\n")

for word,meaning in glossary.items(): 
    print(f"{word.title()} : {meaning.title()}.")