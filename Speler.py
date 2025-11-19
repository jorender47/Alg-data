class Player:
    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number

    def __eq__(self, other):
        try:
            return self.name == other.name
        except AttributeError:
            return False

    def __lt__(self, other):
        try:
            return self.number < other.number
        except AttributeError:
            return NotImplemented

    def __str__(self):
        return f"{self.name} ({self.number})"

# Maak spelerobjecten
p1 = Player("Eden Hazard", 10)
p2 = Player("Moussa Dembele", 19)
p3 = Player("Jan Vertonghen", 5)

# Plaats ze in een lijst
players = [p1, p2, p3]

# Print één object
print("Print één speler:")
print(p1)

# Test eq
print("\nTest eq:")
print("p1 == Player('Eden Hazard', 99)? →", p1 == Player("Eden Hazard", 99))
print("p1 == p2? →", p1 == p2)

# Test lt + sorting
print("\nGesorteerde spelers op rugnummer:")
sorted_players = sorted(players)
for p in sorted_players:
    print(p)