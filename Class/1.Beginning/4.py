# 1. Max of Three Numbers
def max_of_three(a, b, c):
    return max(a, b, c)

# 2. Sum of Digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# 3. Multiplication Table
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# 4. Valid Time Format (HH:MM:SS)
def is_valid_time(s):
    try:
        h, m, sec = map(int, s.split(":"))
        return 0 <= h < 24 and 0 <= m < 60 and 0 <= sec < 60
    except:
        return False

# 5. Dot Inside Circle
def is_inside_circle(radius, dot_x, dot_y, center_x=0, center_y=0):
    distance = ((dot_x - center_x)**2 + (dot_y - center_y)**2)**0.5
    return distance <= radius

# 6. Binary to Decimal
def binary_to_decimal(binary_str):
    return int(binary_str, 2)

# 7. Decimal to Binary
def decimal_to_binary(n):
    return bin(n)[2:]

# 8. Expanded Form
def expanded_form(n):
    digits = str(n)
    length = len(digits)
    parts = [str(int(digits[i]) * 10**(length - i - 1)) for i in range(length) if digits[i] != '0']
    return ' + '.join(parts)

# 9. Levenshtein Distance
def levenshtein(a, b):
    dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[-1][-1]


# ---------------- DEMO ----------------
if __name__ == "__main__":
    print("1. Max of three:", max_of_three(5, 9, 3))
    print("2. Sum of digits:", sum_of_digits(12345))
    print("3. Multiplication table:")
    multiplication_table(7)
    print("4. Valid time:", is_valid_time("23:59:59"))
    print("5. Dot inside circle:", is_inside_circle(5, 2, 3))
    print("6. Binary to decimal:", binary_to_decimal("1011"))
    print("7. Decimal to binary:", decimal_to_binary(11))
    print("8. Expanded form:", expanded_form(70304))
    print("9. Levenshtein distance:", levenshtein("otospu cocu", "orospu çocuğu"))