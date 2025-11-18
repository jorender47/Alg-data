def hanoi(n):
    stappen = hanoihelper(n, "A", "C", "B", 0)
    print(f"{stappen} stappen gedaan")
def hanoihelper(n, start, eind, helper, stappen):
    if n == 1:
        print(f"Schijf {n} van {start} naar {eind}")
        stappen += 1
        return stappen
    else:
        stappen = hanoihelper(n-1, start, helper, eind, stappen)
        print(f"Schijf {n} van {start} naar {eind}")
        stappen += 1
        stappen = hanoihelper(n-1, helper, eind, start, stappen)
        return stappen