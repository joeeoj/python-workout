from . ice_cream_scoop import Scoop


class Bowl:
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *args: Scoop):
        for s in args:
            self.scoops.append(s)

    def __repr__(self):
        return f'Bowl({",".join([s.flavor for s in self.scoops])})'
