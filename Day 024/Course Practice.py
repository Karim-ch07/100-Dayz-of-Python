# file = open("external.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("external.txt") as file:
#     contents = file.read()
#     print(contents)

with open("external.txt", mode="w") as file:
    file.write("Next text.")
