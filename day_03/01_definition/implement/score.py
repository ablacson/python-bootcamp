class Score:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def __repr__(self):
        return f"Score: {self.value}"

    def _add__(self, other):
        return Score(self.value + other.value)

score1 = Score(20)
score2 = Score(10)
print(score1 + score2)
