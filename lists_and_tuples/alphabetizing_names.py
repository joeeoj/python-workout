from operator import itemgetter
from typing import List


def alphabetize_names(people: List[dict]) -> List[dict]:
    return sorted(people, key=itemgetter('last', 'first'))
