from itertools import combinations
from datetime import datetime

# Görev 1: Zincirleme iterator
class ChainSequences:
    def __init__(self, *sequences):
        self.sequences = sequences
        self.seq_index = 0
        self.item_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.seq_index < len(self.sequences):
            current_seq = self.sequences[self.seq_index]
            if self.item_index < len(current_seq):
                item = current_seq[self.item_index]
                self.item_index += 1
                return item
            else:
                self.seq_index += 1
                self.item_index = 0
        raise StopIteration

# Görev 2: Zip iterator
class ZipSequences:
    def __init__(self, *sequences):
        self.sequences = sequences
        self.index = 0
        self.min_len = min(len(seq) for seq in sequences)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.min_len:
            result = [seq[self.index] for seq in self.sequences]
            self.index += 1
            return result
        else:
            raise StopIteration

# Görev 3: Asal sayı generator
def generate_primes(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    for num in range(1, n):
        if is_prime(num):
            yield num

# Görev 4: Kombinasyon generator
def generate_combinations(sequence, k):
    for combo in combinations(sequence, k):
        yield combo

# Görev 5: Çok boyutlu listeyi düzleştirme
def flatten_iterate(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten_iterate(item)
        else:
            yield item

# Menü
def main():
    print("\n📦 Python Iterator & Generator Görevleri")
    print("1 - Zincirleme diziler (chain_sequences)")
    print("2 - Zip diziler (zip_sequences)")
    print("3 - Asal sayı üret (generate_primes)")
    print("4 - Kombinasyon üret (generate_combinations)")
    print("5 - Listeyi düzleştir (flatten_iterate)")
    choice = input("(1-5): ")

    if choice == "1":
        result = ChainSequences([1, 2, 3], [4], [5])
        for item in result:
            print(item)

    elif choice == "2":
        result = ZipSequences([1, 2], [3, 4], [5, 6])
        for item in result:
            print(item)

    elif choice == "3":
        n = int(input("How many numbers do you wnat?: "))
        for p in generate_primes(n):
            print(p)

    elif choice == "4":
        seq = [1, 2, 3]
        k = 2
        for c in generate_combinations(seq, k):
            print(c)

    elif choice == "5":
        nested = [1, 2, [3, [4], 5]]
        for x in flatten_iterate(nested):
            print(x)

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()