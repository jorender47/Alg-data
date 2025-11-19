class Pass:
    def __init__(self, sender: str, receiver: str, nr_of_times: int):
        self.sender = sender
        self.receiver = receiver
        self.nr_of_times = nr_of_times

    def get_weight(self):
        return self.nr_of_times

    def get_start(self):
        return self.sender

    def get_end(self):
        return self.receiver

    def __eq__(self, other):
        if type(other) == Pass:
            return (self.sender == other.sender and
                    self.receiver == other.receiver)
        return False

    def __str__(self):
        return f"Pass from {self.sender} to {self.receiver}"
