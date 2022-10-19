class Fraction:

    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):

        #d = a/b and a = 0 --> d = 0
        if self.numerator == 0:
            value = ' that gives you 0'

        #denominator cannot be 0
        elif self.denominator == 0:
            value = ' denominator cannot be 0'

        #d = a/b and a=b --> d = a
        elif self.numerator == self.denominator:
            value =" %d" % (self.numerator)
        else:
            value ="%d/%d" % (self.numerator, self.denominator)
        return value


    #add = (a*d + c*b)/b*d
    def __add__(self, num):
        if isinstance(num, int):
            num = Fraction(num)
        return Fraction(self.numerator * num.denominator +
                    self.denominator * num.numerator,
                    self.denominator * num.denominator)

    #sub = (a*b - c*b)/b*d
    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.numerator * other.denominator -
                        self.denominator * other.numerator,
                        self.denominator * other.denominator)

    #inverse = a/b --> b/a
    def inverse(self):
        return Fraction(self.denominator, self.numerator)