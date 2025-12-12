class BankAccount:
    def __init__(self, name, balance, account_number):
        self.name = name                    # Her yerden erişilebilir (public)
        self._balance = balance             # Sadece sınıf içinden ve alt sınıflardan erişilebilir (protected)
        self.__account_number = account_number  # Sadece bu sınıf içinde erişilebilir (private)

    def deposit(self, amount):
        self._balance += amount             # Para yatırma

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount         # Para çekme
        else:
            print("Yetersiz bakiye.")

    def get_balance(self):
        return self._balance                # Bakiyeyi döndürür

    def display_info(self):
        print(f"İsim: {self.name}")
        print(f"Bakiye: {self._balance}")
        print(f"Hesap No: {self.__account_number}")

    
    def __init__(self, name, balance, account_number, interest_rate):
        super().__init__(name, balance, account_number)
        self.interest_rate = interest_rate  # Faiz oranı

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest           # Faizi bakiyeye ekler
        acc = SavingAccount("Yiğit", 1000, "TR123456789", 0.05)