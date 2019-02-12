
class Allergies(object):
    allergen_scores = {"eggs": 1, "peanuts": 2, "shellfish": 4, "strawberries": 8,
                       "tomatoes": 16, "chocolate": 32, "pollen": 64, "cats": 128}

    def __init__(self, score):
        self.score = score
        self.allergens = self.lst

    def is_allergic_to(self, item):
        return self.allergen_scores[item] & self.score != 0

    @property
    def lst(self):
        return [a for a in self.allergen_scores if self.is_allergic_to(a)]

