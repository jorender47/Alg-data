def zigzag_traag(lijst: list):
    lijst.sort()
    for i in range(0, len(lijst) - 1, 2):
        lijst[i], lijst[i + 1] = lijst[i + 1], lijst[i]
def iszigzag(lijst: list):
    for i in range(len(lijst) -1):
        if i % 2 == 0:
            if lijst[i] < lijst[i + 1]:
                return False
        else:
            if lijst[i] > lijst[i + 1]:
                return False

    return True

def zigzag_snel(lijst: list):
    for i in range(0, len(lijst), 2):
        if i > 0 and lijst[i] < lijst[i - 1]:
            lijst[i], lijst[i - 1] = lijst[i - 1], lijst[i]

        if i + 1 < len(lijst) and lijst[i] < lijst[i + 1]:
            lijst[i], lijst[i + 1] = lijst[i + 1], lijst[i]



