import random
import string


def generate_random_string(length):
    letters = string.ascii_uppercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

