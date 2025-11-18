def isPalindroom(s):
    # Basisgevallen: lege string of 1 karakter is altijd palindroom
    if len(s) <= 1:
        return True
    # Vergelijk eerste en laatste karakter
    if s[0] != s[-1]:
        return False
    # Recursief controleren van het middelste deel
    return isPalindroom(s[1:-1])
