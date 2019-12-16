class Player:
    def __init__(self, name):
        self.name = name

class Roll:
    def __init__(self, name):
        self.name = name

    def can_defeat(self, other):
        wins = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }
        if other.name == wins[self.name]:
            return True
        else: 
            return False
