from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):

        if denom == 0:
            raise Exception("No division with 0!")

        self.numer = numer / self.calculate_gcd(numer, denom)
        self.denom = denom / self.calculate_gcd(numer, denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        num = (self.numer * other.denom) + (self.denom * other.numer)
        den = self.denom * other.denom
        return Rational(num, den)

    def __sub__(self, other):
        num = (self.numer * other.denom) - (self.denom * other.numer)
        den = self.denom * other.denom
        return Rational(num, den)

    def __mul__(self, other):
        num = self.numer * other.numer
        den = self.denom * other.denom
        return Rational(num, den)

    def __truediv__(self, other):
        num = self.numer * other.denom
        den = other.numer * self.denom
        return Rational(num, den)

    def __abs__(self):
        num = abs(self.numer)
        den = abs(self.denom)
        return Rational(num, den)

    def __pow__(self, power):
        abs_power = abs(power)
        num = self.numer ** abs_power
        den = self.denom ** abs_power
        return Rational(num, den)

    def __rpow__(self, base):
        return (abs(base) ** self.numer) ** (1 / self.denom)

    def calculate_gcd(self, a, b):
        if b == 0:
            return a
        return self.calculate_gcd(b, a % b)


