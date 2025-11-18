def samenvoegen(lijst1: list, lijst2: list):
    lijst3 = []
    kortste = min(len(lijst1), len(lijst2))
    for i in range(kortste):
        lijst3.append(lijst1[i])
        lijst3.append(lijst2[i])
    return lijst3


def weven(lijst1: list, lijst2: list):
    lijst3 = []
    len1 = len(lijst1)
    len2 = len(lijst2)
    langste = max(len(lijst1), len(lijst2))
    for i in range(langste):
        lijst3.append(lijst1[i % len1])
        lijst3.append(lijst2[i % len2])
    return lijst3

def ritsen(lijst1: list, lijst2: list):
    lijst3 = []
    len1 = len(lijst1)
    len2 = len(lijst2)
    kortste = min(len(lijst1), len(lijst2))
    for i in range(kortste):
        lijst3.append(lijst1[i])
        lijst3.append(lijst2[i])
    if len1 > len2:
        lijst3.extend(lijst1[kortste:])
    else:
        lijst3.extend(lijst2[kortste:])
    return lijst3

