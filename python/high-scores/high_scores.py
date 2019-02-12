class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top(self):
        return sorted(self.scores, reverse=True)[:3]

    def report(self):
        diff_from_best = self.personal_best() - self.latest()
        if diff_from_best == 0:
            return f"Your latest score was {self.latest()}. That's your personal best!"
        else:
            return f"Your latest score was {self.latest()}. That's {diff_from_best} short of your personal best!"
