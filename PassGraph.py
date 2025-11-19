class PassGraph:
    def __init__(self):
        self.players = []          # lijst van Player objects
        self.adj = {}              # dict: key = player.name, value = list of Pass

    # ---------------------------------------------------------
    # Hulpfunctie: naam van speler extracten
    # ---------------------------------------------------------
    def _get_name(self, player_or_name):
        if type(player_or_name) == str:
            return player_or_name
        return player_or_name.name   # Player object

    # ---------------------------------------------------------
    # 1) BASISOPERATIES
    # ---------------------------------------------------------

    def add_player(self, player):
        # voeg toe enkel als naam nog niet bestaat
        if not self.has_player(player):
            self.players.append(player)
            self.adj[player.name] = []

    def has_player(self, player_or_name):
        name = self._get_name(player_or_name)
        for p in self.players:
            if p.name == name:
                return True
        return False

    def get_player(self, name):
        for p in self.players:
            if p.name == name:
                return p
        return None

    def add_pass(self, sender, receiver, times=1):
        if times <= 0:
            raise ValueError("Pass count must be > 0")

        # spelers moeten bestaan
        if not self.has_player(sender) or not self.has_player(receiver):
            return  # of raise error

        sender_name = sender.name
        receiver_name = receiver.name

        # bestond de pass al?
        for p in self.adj[sender_name]:
            if p.sender == sender and p.receiver == receiver:
                p.nr_of_times += times
                return

        # anders nieuwe pass
        new_p = Pass(sender, receiver, times)
        self.adj[sender_name].append(new_p)

    def get_pass(self, sender_name, receiver_name):
        if sender_name not in self.adj:
            return None

        for p in self.adj[sender_name]:
            if p.sender.name == sender_name and p.receiver.name == receiver_name:
                return p
        return None

    def neighbors(self, sender_name):
        if sender_name not in self.adj:
            return []
        return self.adj[sender_name]

    # ---------------------------------------------------------
    # 2) ANALYSEFUNCTIES
    # ---------------------------------------------------------

    def total_weight(self, subset=None):
        if subset is None:
            subset = [p.name for p in self.players]

        total = 0
        subset_set = set(subset)   # sneller

        for sender_name in subset_set:
            if sender_name not in self.adj:
                continue

            for p in self.adj[sender_name]:
                if p.receiver.name in subset_set:  # beide in subset
                    total += p.nr_of_times

        return total

    def pass_intensity(self, subset=None):
        if subset is None:
            subset = [p.name for p in self.players]

        n = len(subset)
        if n < 2:        # speciaal geval
            return 0.0

        numerator = self.total_weight(subset)
        denominator = n * (n - 1)

        return numerator / denominator

    def top_pairs(self, k=5):
        all_passes = []

        for sender_name in self.adj:
            for p in self.adj[sender_name]:
                all_passes.append(p)

        # sorteer op gewicht, dalend
        all_passes.sort(key=lambda p: p.nr_of_times, reverse=True)

        return all_passes[:k]

    def distribution_from(self, sender_name):
        if sender_name not in self.adj:
            return []

        result = []
        for p in self.adj[sender_name]:
            result.append((p.receiver.name, p.nr_of_times))

        # sorteer op nr_of_times (dalend)
        result.sort(key=lambda x: x[1], reverse=True)
        return result

    # ---------------------------------------------------------
    # Nieuw: lijst van spelers en passes
    # ---------------------------------------------------------
    def players_list(self):
        return self.players.copy()

    def passes_list(self):
        all_passes = []
        for sender_name in self.adj:
            all_passes.extend(self.adj[sender_name])
        return all_passes

    # ---------------------------------------------------------
    # Bestand inlezen
    # ---------------------------------------------------------
    def _load_from_txt(self, path):
        section = None
        try:
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if line.startswith("[") and line.endswith("]"):
                        section = line.upper()
                        if section not in ["[PLAYERS]", "[PASSES]"]:
                            raise ValueError(f"Unknown section: {section}")
                        continue

                    if section == "[PLAYERS]":
                        parts = line.split(";")
                        if len(parts) != 2:
                            raise ValueError(f"Invalid player line: {line}")
                        name, number = parts[0].strip(), parts[1].strip()
                        try:
                            number = int(number)
                        except:
                            raise ValueError(f"Invalid number for player: {line}")
                        self.add_player(Player(name, number))

                    elif section == "[PASSES]":
                        if "->" not in line or ":" not in line:
                            raise ValueError(f"Invalid pass line: {line}")
                        left, right = line.split(":")
                        sender_name, receiver_name = left.split("->")
                        sender_name = sender_name.strip()
                        receiver_name = receiver_name.strip()
                        try:
                            times = int(right.strip())
                        except:
                            raise ValueError(f"Invalid pass count: {line}")
                        if not self.has_player(sender_name) or not self.has_player(receiver_name):
                            raise ValueError(f"Pass references unknown player: {line}")
                        sender = self.get_player(sender_name)
                        receiver = self.get_player(receiver_name)
                        self.add_pass(sender, receiver, times)
                    else:
                        raise ValueError("No section defined yet")
        except FileNotFoundError:
            raise ValueError(f"File not found: {path}")

    # ---------------------------------------------------------
    # Bestand opslaan
    # ---------------------------------------------------------
    def save_to_txt(self, path):
        with open(path, "w", encoding="utf-8") as f:
            f.write("[PLAYERS]\n")
            for p in sorted(self.players, key=lambda x: x.name):
                f.write(f"{p.name};{p.number}\n")

            f.write("[PASSES]\n")
            for sender_name in sorted(self.adj.keys()):
                for p in self.adj[sender_name]:
                    f.write(f"{p.sender.name} -> {p.receiver.name} : {p.nr_of_times}\n")