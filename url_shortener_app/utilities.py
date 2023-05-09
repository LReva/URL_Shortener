from random import randint, choice
import string


def generate_url():
    select_length = randint(4,8)
    characters = string.ascii_letters + string.digits
    random_string = "".join(choice(characters) for i in range(select_length))
    short_url = "http://short.est/" + random_string 
    return short_url