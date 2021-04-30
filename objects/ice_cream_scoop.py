from typing import List


class Scoop:
    def __init__(self, flavor: str):
        self.flavor = flavor

    def __repr__(self):
        return f'Scoop({self.flavor})'


def create_scoops(flavors: List[str]) -> List[Scoop]:
    return [Scoop(f) for f in flavors]
