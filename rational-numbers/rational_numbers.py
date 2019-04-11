def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

def reduce(rational):
    greatest_common_divisor = gcd(rational.numer, rational.denom)
    numer = rational.numer/abs(greatest_common_divisor)
    denom = rational.denom/abs(greatest_common_divisor)
    return Rational(int(numer), int(denom))

def calc_neg(rational):
    numer = rational.numer
    denom = rational.denom
    if denom < 0:
        numer *= -1
        denom *= -1
    return Rational(int(numer), int(denom))

class Rational(object):
    def __init__(self, numer, denom):
        greatest_common_divisor = gcd(numer, denom)
        numer = numer/abs(greatest_common_divisor)
        denom = denom/abs(greatest_common_divisor)
        if denom < 0:
            numer *= -1
            denom *= -1
        self.numer = int(numer)
        self.denom = int(denom)

    def __eq__(self, other):
        if isinstance(other,float):
            return self.numer/self.denom == other
        else:
            return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return reduce(calc_neg(Rational(self.numer*other.denom + self.denom*other.numer, abs(other.numer*other.denom))))

    def __sub__(self, other):
        return reduce(calc_neg(Rational(self.numer*other.denom - self.denom*other.numer, abs(other.numer * other.denom))))

    def __mul__(self, other):
        numer = self.numer*other.numer
        denom = self.denom*other.denom
        rational_temp = Rational(numer, denom)
        return reduce(rational_temp)

    def __truediv__(self, other):
        numer = self.numer*other.denom
        denom = self.denom*other.numer
        rational_temp = Rational(numer, denom)
        return reduce(calc_neg(rational_temp))

    def __abs__(self):
        return reduce(Rational(abs(self.numer),abs(self.denom)))

    def __pow__(self, power):
        if power > 0:
            return reduce(calc_neg(Rational(self.numer**power, self.denom**power)))
        else:
            return reduce(calc_neg(Rational(self.denom**abs(power), self.numer**abs(power))))

    def __rpow__(self, base):
        return float(base**(self.numer/self.denom))
