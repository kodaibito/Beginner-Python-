# 1. Lambda: bölünebilir mi 5'e?
div_by_5 = lambda x: x % 5 == 0

# 2. Recursion: n'den 1'e kadar yazdır
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

# 3. Recursion: üs alma
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

# 4. Fibonacci (n uzunlukta)
def fibonacci(n):
    seq = []
    a, b = 1, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

# 5. Listeyi düzleştir (recursion)
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# 6. Palindrome kontrolü (recursion)
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# 7. Liste ve index → hata varsa None
def safe_get(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None

# 8. Decorator: hata varsa tekrar dene
def retry_on_exception(exc_type, retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(retries):
                try:
                    return func(*args, **kwargs)
                except exc_type:
                    continue
            return None
        return wrapper
    return decorator

# 9. Lambda: rakamları topla
sum_digits = lambda x: sum(int(d) for d in str(x))


if __name__ == "__main__":
    print("1:", div_by_5(25))
    print("2:")
    countdown(5)
    print("3:", power(2, 4))
    print("4:", fibonacci(7))
    print("5:", flatten([1, [2, 3, [4]]]))
    print("6:", is_palindrome("racecar"))
    print("7:", safe_get(["a", "b", "c"], 5))
    
    @retry_on_exception(ValueError)
    def risky():
        raise ValueError("fail")
    print("8:", risky())  # None after retries

    print("9:", sum_digits(12345))