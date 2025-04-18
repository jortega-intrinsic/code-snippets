from browser import timer
from random import choice
COUNTRIES = [
    {"country": "Albania", "url": "https://i.scdn.co/image/ab67616d0000b27390fa357b5ac6ce651add3a70"},
    {"country": "Australia", "url": "https://www.worldometers.info/img/flags/small/tn_as-flag.gif"},
    {"country": "Brazil", "url": "https://www.worldometers.info/img/flags/small/tn_br-flag.gif"},
    {"country": "Canada", "url": "https://www.worldometers.info/img/flags/small/tn_ca-flag.gif"},
    {"country": "Russia", "url": "https://www.worldometers.info/img/flags/small/tn_rs-flag.gif"},
    ]

IMAGE_WIDTH = 400
IMAGE_HEIGHT = 300

def get_random_option():
    random_option = choice(COUNTRIES)
    return random_option

def display_flag(url):
    image = Image(url)
    image.set_size(IMAGE_WIDTH, IMAGE_HEIGHT)
    add(image)

def check_user_answer(option, guess):
    if guess.lower() == option["country"].lower():
        return True
    else:
        return False


async def play():
    print("You have 3 plays, guess the country based on the flag!")
    for i in range(3):
        option = get_random_option()
        display_flag(option["url"])
        guess = await async_input("What country has this flag? ")
        isCorrect = check_user_answer(option, guess)
        if isCorrect:
            print("You got it!")
        else:
            print("Better luck next time!")


aio.run(play())