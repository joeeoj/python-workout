from objects.ice_cream_scoop import create_scoops


def test_a_few():
    flavors = ['chocolate', 'vanilla', 'cookies and cream']
    scoops = create_scoops(flavors)

    for s, f in zip(scoops, flavors):
        assert repr(s) == f'Scoop({f})'
