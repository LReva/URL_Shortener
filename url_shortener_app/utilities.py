from random import randint, choice
import string
import json
from .models import URL


def generate_url():
    select_length = randint(4,8)
    characters = string.ascii_letters + string.digits
    random_string = "".join(choice(characters) for i in range(select_length))
    short_url = "http://short.est/" + random_string 
    return short_url

def terminal_print_long_short_url(long_url, short_url):
    json_data = json.dumps({"long_url": long_url, "short_url": short_url})
    print(json_data)

def save_new_url(long_url, short_url):
    new_url = URL(long_url = long_url, short_url = short_url)
    new_url.save()

def generate_until_unique(long_url):
    while True:
        short_url = generate_url()
        try: 
            URL.objects.get(short_url = short_url)
        except URL.DoesNotExist:
            save_new_url(long_url, short_url)
            terminal_print_long_short_url(long_url, short_url)
            return short_url