from collections import defaultdict
from itertools import groupby
from math import factorial

# 1. Max & Min in List
def max_min(lst):
    return max(lst), min(lst)

# 2. String içindeki özel harfler
def unique_letters(s):
    return set(s)

# 3. Reverse List (no built-in)
def reverse_list(lst):
    return [lst[i] for i in range(len(lst)-1, -1, -1)]

# 4. Revert Dict (key ↔ value)
def revert_dict(d):
    return {v: k for k, v in d.items()}

# 5. Custom dict.update
def custom_update(d1, d2):
    for k, v in d2.items():
        d1[k] = v
    return d1

# 6. 5 Harften uzun özel stringler
def filter_strings(lst):
    return [s for s in set(lst) if len(s) > 5]

# 7. En çok kullanılan harf
def most_frequent_letter(text):
    freq = defaultdict(int)
    for ch in text:
        if ch.isalpha():
            freq[ch.lower()] += 1
    return max(freq, key=freq.get)

# 8. Anagram grupları
def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return list(groups.values())

# 9. Faktoriyel toplamı
memo = {}
def memo_fact(n):
    if n in memo:
        return memo[n]
    memo[n] = factorial(n)
    return memo[n]

def sum_factorials(n):
    return sum(memo_fact(i) for i in range(1, n+1))

# 10. Kelime checkliyoruz
def vowel_column_check(matrix):
    vowels = set("aeiouAEIOU")
    cols = zip(*matrix)
    for col in cols:
        count = sum(1 for word in col if word and word[0] in vowels)
        if count > 2:
            return False
    return True

if __name__ == "__main__":
    print("1:", max_min([3, 7, 1, 9]))
    print("2:", unique_letters("hello world"))
    print("3:", reverse_list([1, 2, 3, 4]))
    print("4:", revert_dict({"a": "1", "b": "2"}))
    print("5:", custom_update({"x": 1}, {"y": 2}))
    print("6:", filter_strings(["apple", "banana", "kiwi", "banana", "strawberry"]))
    print("7:", most_frequent_letter("hello world, how are you?"))
    print("8:", group_anagrams(["bat", "tab", "cat", "act", "tac"]))
    print("9:", sum_factorials(5))  # 1! + 2! + 3! + 4! + 5!
    print("10:", vowel_column_check([
        ["apple", "banana", "orange"],
        ["ice", "grape", "umbrella"],
        ["owl", "melon", "egg"]
    ]))
