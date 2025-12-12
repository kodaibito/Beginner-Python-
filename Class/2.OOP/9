# Abstract sınıf: Fiyatlandırma stratejileri için şablon
class PricingStrategy:
    def calculate(self, order):
        raise NotImplementedError

# Standart fiyatlandırma
class StandardPricing(PricingStrategy):
    def calculate(self, order):
        return sum(item.price for item in order.items)

# Doğum günü bonusu (%10 indirim)
class BirthdayBonus(PricingStrategy):
    def calculate(self, order):
        total = sum(item.price for item in order.items)
        return total * 0.9

# Öğle vakti bonusu (5$ indirim, 20$ üstü siparişlerde)
class LunchTimeBonus(PricingStrategy):
    def calculate(self, order):
        total = sum(item.price for item in order.items)
        return total - 5 if total > 20 else total

# Menüdeki tek bir ürün
class MenuItem:
    def __init__(self, name, price):
        self.name = name        # Ürün adı
        self.price = price      # Ürün fiyatı

# Menü sınıfı: ürünleri tutar
class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_menu(self):
        for item in self.items:
            print(f"{item.name}: ${item.price}")

# Müşteri sınıfı
class Customer:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

# Garson sınıfı: sipariş alır
class Waiter:
    def __init__(self, name):
        self.name = name

    def take_order(self, customer, items):
        return Order(customer, items)

# Sipariş sınıfı
class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.pricing_strategy = StandardPricing()  # Varsayılan fiyatlandırma

    def set_pricing_strategy(self, strategy):
        self.pricing_strategy = strategy

    def calculate_total(self):
        return self.pricing_strategy.calculate(self)

# Fiş sınıfı: siparişin çıktısını verir
class Receipt:
    def __init__(self, order):
        self.order = order
        self.total = order.calculate_total()

    def print_receipt(self):
        print(f"Receipt for {self.order.customer.name}")
        for item in self.order.items:
            print(f"- {item.name}: ${item.price}")
        print(f"Total: ${self.total}")

# Restoran sınıfı: menü ve garsonları tutar
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.waiters = []

    def hire_waiter(self, waiter):
        self.waiters.append(waiter)
        # 1. Restoran oluştur
# 1. Restoran oluştur
r = Restaurant("Kral Sofrası")

# 2. Menüye ürün ekle
r.menu.add_item(MenuItem("Kebap", 20))
r.menu.add_item(MenuItem("Ayran", 5))
r.menu.add_item(MenuItem("Baklava", 10))

# 3. Menü göster
r.menu.show_menu()

# 4. Garson işe al
w = Waiter("Ali")
r.hire_waiter(w)

# 5. Müşteri oluştur
c = Customer("Alper", "12-12")

# 6. Sipariş ver
order = w.take_order(c, [r.menu.items[0], r.menu.items[2]])

# 7. Varsayılan fiyatlandırma ile hesapla
print("Standard total:", order.calculate_total())

# 8. Doğum günü bonusu uygula
order.set_pricing_strategy(BirthdayBonus())

# 9. Yeni fiyatı hesapla
print("Birthday bonus total:", order.calculate_total())

# 10. Lunch-time bonusu uygula
order.set_pricing_strategy(LunchTimeBonus())

# 11. Yeni fiyatı hesapla
print("Lunch bonus total:", order.calculate_total())

# 12. Fiş oluştur
receipt = Receipt(order)

# 13. Fişi yazdır
receipt.print_receipt()

# 14. Menüye yeni ürün ekle
r.menu.add_item(MenuItem("Çorba", 8))
