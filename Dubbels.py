def dubbel(lijst: list):
    gezien = set()
    for x in lijst:
        if x in gezien:
            return x
        gezien.add(x)
    return None


def dubbels(lijst: list):
    enkel = set()
    meermaals = set()

    for x in lijst:
        if x in enkel:
            enkel.remove(x)
            meermaals.add(x)
        elif x not in meermaals:
            enkel.add(x)

    return enkel, meermaals
