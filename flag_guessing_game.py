# Must use Python Graphics!
from browser import timer
from random import choice

COUNTRIES = [
    {"name": "Albania", "url": "https://i.scdn.co/image/ab67616d0000b27390fa357b5ac6ce651add3a70"},
    {"name": "Australia", "url": "https://www.worldometers.info/img/flags/small/tn_as-flag.gif"},
    {"name": "Brazil", "url": "https://www.worldometers.info/img/flags/small/tn_br-flag.gif"},
    {"name": "Canada", "url": "https://www.worldometers.info/img/flags/small/tn_ca-flag.gif"},
    {"name": "Russia", "url": "https://www.worldometers.info/img/flags/small/tn_rs-flag.gif"},
    ]

IMAGE_WIDTH = 400
IMAGE_HEIGHT = 300

def display_flag(country):
    url = country["url"]
    image = Image(url)
    image.set_size(IMAGE_WIDTH, IMAGE_HEIGHT)
    add(image)

def check_user_answer(country, guess):
    if guess.strip().lower() == country["name"].lower():
        return True
    else:
        return False


async def play():
    print("You have 3 plays, guess the country based on the flag!")
    for i in range(3):
        random_country = choice(COUNTRIES)
        display_flag(random_country)
        guess = await async_input("What country has this flag? ")
        isCorrect = check_user_answer(random_country, guess)
        if isCorrect:
            print("You got it!")
        else:
            print("Better luck next time!")

aio.run(play())
