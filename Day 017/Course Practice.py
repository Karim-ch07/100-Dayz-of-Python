# class User:
#     pass

# user_1 = User()
# user_1.id = "007"
# user_1.username = "agent"

# print(user_1.username)

# user_2 = User()
# user_2.id = "007"
# user_2.username = "agent too"

##################################################################################

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 #default value of the attribute "followers"

user_1 = User("007", "agent")

print(user_1.username)
