
"""
Created By Anandu S Nambiar


Title : Creating a word counter using Python (CUI)

The process is done through,
    1. store the whole document in a variable
    2. split the document using split()
    3. count the number of words in the variable without space
"""


doc = input("Enter document name/path : ")

file1 = open(doc,"r")

# flag for the count
f=0

# reading the data
for x in file1:
    data = x.split()

# counting no of words
for i in data:
    f = f+1

print("Number of Words in the document are ", f)

print("\n\n")
ext = input("Enter something to exit!")
