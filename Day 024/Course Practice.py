# file = open("external.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("external.txt") as file:
#     contents = file.read()
#     print(contents)

# #the write method will overwrite the existing file with the new string
# #Also, it is important to remember that files are opened on read only by default. It can not write without setting the right mode
# with open("external.txt", mode="w") as file:
#     file.write("Next text.")

# #if a file does not exist, it is going to be created
# with open("New.txt", mode="w") as file:
#     file.write("Next text.")

#when the file is not in the work directory, we should indicate its absolute path
with open("/Users/_/OneDrive/Bureau/external.txt") as file:
    contents = file.read()
    print(contents)

#or a relative file path (relative to the work directory)
with open("../../OneDrive/Bureau/external.txt") as file:
    contents = file.read()
    print(contents)
