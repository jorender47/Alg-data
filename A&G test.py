def zoek(gesorteerd: list, x: int):
    eerste = 0
    laatste = len(gesorteerd) - 1
    while laatste >= eerste:
        midden = (eerste + laatste) // 2
        if x == gesorteerd[midden]:
            return midden
        elif x > gesorteerd[midden]:
            eerste = midden + 1
        else:
            laatste = midden - 1
    return None

print(zoek([0, 2, 4, 6, 8, 10, 12, 14], 4))

