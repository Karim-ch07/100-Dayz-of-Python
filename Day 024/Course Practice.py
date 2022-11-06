# file = open("external.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("external.txt") as file:
    contents = file.read()
    print(contents)
