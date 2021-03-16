import random


def guessing_game():
    """exercise 1"""
    ans = random.randint(1, 100)

    while True:
        user_input = int(input('Guess a number between 1 - 100: '))

        if user_input == ans:
            print('Just right')
            break
        if user_input > ans:
            print('Too high')
        if user_input < ans:
            print('Too low')


if __name__ == '__main__':
    guessing_game()
