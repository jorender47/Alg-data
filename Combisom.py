def combisom(lijst: list, x: int):
    for i in range(len(lijst)):
        for j in  range(i + 1, len(lijst)):
            if lijst[i] + lijst[j] == x:
               return True
    return False
