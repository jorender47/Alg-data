def overzicht(codes):
    lands = {"Engelstalige landen": 0, "Franstalige landen": 0, "Duitstalige landen": 0, "Japan": 0, "Russischtalige landen": 0, "China": 0, "Overige landen": 0, "Fouten" : 0}
    for code in codes:
        if (code[0:3] == '978' or code[0:3] == '979') and controlegetal(code):
                lands = landen(code, lands)
        else:
            lands["Fouten"] += 1

    for land in lands:
        print(f"{land}: {lands[land]}")

def controlegetal(code):
    o = int(code[0]) + int(code[2]) + int(code[4]) + int(code[6]) + int(code[8]) + int(code[10])
    e = int(code[1]) + int(code[3]) + int(code[5]) + int(code[7]) + int(code[9]) + int(code[11])
    resultaat = (10 -(o+3*e) % 10) % 10
    return resultaat == int(code[12])

def landen(code, land):
    if code[3] == "0" or code[3] == "1":
        land["Engelstalige landen"] += 1
    if code[3] == "2":
        land["Franstalige landen"] += 1
    if code[3] == "3":
        land["Duitstalige landen"] += 1
    if code[3] == "4":
        land["Japan"] += 1
    if code[3] == "5":
        land["Russischtalige landen"] += 1
    if code[3] == "7":
        land["China"] += 1
    if code[3] == "6" or code[3] == "9" or code[3] == "8":
        land["Overige landen"] += 1

    return land