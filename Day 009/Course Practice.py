programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again",
}

#retrieving items from dictionary.
print(programming_dictionary["Bug"])

#Adding new items to dictionary.
programming_dictionary["Test"] = "Sample info"
print(programming_dictionary)

#Create an empty dictionary
empty_dict = {}

#Wipe an exsisting dictionary.
programming_dictionary = {}
print(programming_dictionary)

#Edit an item in a disctionary.
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary["Bug"])

#Loop through a dictionary.
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])
