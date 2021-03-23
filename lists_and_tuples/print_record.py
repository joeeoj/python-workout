from typing import List, Tuple


def format_sort_records(people: List[Tuple]) -> None:
    """exercise 13"""
    for person in people:
        print(f'{person[1]:<10} {person[0]:<10} {person[2]:>5.2f}')
