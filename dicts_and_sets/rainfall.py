from collections import defaultdict


def get_rainfall():
    """exercise 15"""
    cities = defaultdict(int)
    while True:
        city = input('City: ')
        if not city:
            break
        rainfall = int(input('Rainfall: '))
        cities[city] += rainfall

    for city, rainfall in cities.items():
        print(f'{city}: {rainfall}')


if __name__ == '__main__':
    get_rainfall()
