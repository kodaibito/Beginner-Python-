from math import gcd

class RationalFraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()  # Başta sadeleştir

    def reduce(self):
        ortak_bolen = gcd(self.numerator, self.denominator)
        self.numerator //= ortak_bolen
        self.denominator //= ortak_bolen

    def to_float(self):
        return self.numerator / self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        return (self.numerator == other.numerator and
                self.denominator == other.denominator)

    def __add__(self, other):
        yeni_pay = self.numerator * other.denominator + other.numerator * self.denominator
        yeni_payda = self.denominator * other.denominator
        return RationalFraction(yeni_pay, yeni_payda)

    def __iadd__(self, other):
        self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        self.reduce()
        return self

    def __sub__(self, other):
        yeni_pay = self.numerator * other.denominator - other.numerator * self.denominator
        yeni_payda = self.denominator * other.denominator
        return RationalFraction(yeni_pay, yeni_payda)

    def __isub__(self, other):
        self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        self.reduce()
        return self

    def __mul__(self, other):
        yeni_pay = self.numerator * other.numerator
        yeni_payda = self.denominator * other.denominator
        return RationalFraction(yeni_pay, yeni_payda)

    def __imul__(self, other):
        self.numerator *= other.numerator
        self.denominator *= other.denominator
        self.reduce()
        return self

    def __truediv__(self, other):
        yeni_pay = self.numerator * other.denominator
        yeni_payda = self.denominator * other.numerator
        return RationalFraction(yeni_pay, yeni_payda)

    def __itruediv__(self, other):
        self.numerator *= other.denominator
        self.denominator *= other.numerator
        self.reduce()
        return self
    
    # Önce RationalFraction sınıfını yukarıda tanımladık.
# Şimdi örnekler ile çıktı alalım:

# 1. Sadeleştirme
a = RationalFraction(2, 4)   # 2/4 → 1/2
print("a:", a)               # Beklenen: 1/2

# 2. Eşitlik kontrolü
b = RationalFraction(3, 6)   # 3/6 → 1/2
print("a == b:", a == b)     # True

# 3. Toplama (__add__)
c = a + b                    # 1/2 + 1/2 = 1/1
print("a + b:", c)           # 1/1

# 4. Toplama (__iadd__)
a += b                       # a = a + b → 1/2 + 1/2 = 1/1
print("a += b:", a)          # 1/1

# 5. Çıkarma (__sub__)
d = RationalFraction(3, 4)
e = RationalFraction(1, 2)
print("d - e:", d - e)       # 3/4 - 1/2 = 1/4

# 6. Çıkarma (__isub__)
d -= e
print("d -= e:", d)          # 1/4

# 7. Çarpma (__mul__)
f = RationalFraction(2, 3)
g = RationalFraction(3, 5)
print("f * g:", f * g)       # 2/3 * 3/5 = 6/15 → 2/5

# 8. Çarpma (__imul__)
f *= g
print("f *= g:", f)          # 2/5

# 9. Bölme (__truediv__)
h = RationalFraction(4, 7)
i = RationalFraction(2, 3)
print("h / i:", h / i)       # 4/7 ÷ 2/3 = 12/14 → 6/7

# 10. Bölme (__itruediv__)
h /= i
print("h /= i:", h)          # 6/7

# 11. Float dönüşümü
print("h.to_float():", h.to_float())  # 0.857...