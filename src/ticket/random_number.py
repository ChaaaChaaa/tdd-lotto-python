import random


def generate_random_numbers():
    random_numbers = random.sample(range(1, 46), 6)
    return sorted(random_numbers)
