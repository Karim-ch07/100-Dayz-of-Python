from src.schemas.user import User
from mongoengine.errors import NotUniqueError


def getUsers():
    return User.object().all()

def getVolunteers():
    pass

def getHelpMe():
    pass

def getSpecificUsers(keyword):
    pass

def postUser():
    try:
        User.first_name = 'Paris'
        User.last_name = 'Nakita Kejser'
        User.phone = '234567890'
        User.location = (323.232, 232.232)
    except NotUniqueError as e:
        print('User exists already!')

def putUser():

