# 1. Завдання: Система управління банком
# Створіть клас Банк, який буде представляти банк та мати наступні методи:
# ● __init__: Конструктор класу, в якому створюється пустий список клієнтів банку.
# ● додати_клієнта(ім'я): Метод для додавання нового клієнта до банку. Клієнт - це
# об'єкт класу Клієнт.
# ● знайти_клієнта(ім'я): Метод, який приймає ім'я клієнта і повертає відповідний
# об'єкт класу Клієнт, якщо такий клієнт існує в банку, або повертає None, якщо
# клієнта немає.
# ● зберегти_дані_в_файл(файл_назва): Метод, який зберігає інформацію про всіх
# клієнтів банку у текстовий файл. Кожен рядок файлу має містити ім'я клієнта та
# іншу важливу інформацію, якщо це потрібно.
# ● завантажити_дані_з_файлу(файл_назва): Метод, який завантажує дані про
# клієнтів з текстового файлу і створює відповідні об'єкти класу Клієнт.
# Створіть також клас Клієнт, який буде представляти клієнта банку. У класі Клієнт
# повинні бути наступні атрибути:
# ● ім'я: Ім'я клієнта.
# ● баланс: Поточний баланс клієнта.
# ● Додайте метод __str__, який повертає рядок з інформацією про клієнта у
# зручному форматі.
# Правила:
# ● Під час створення об'єкта класу Банк, створіть порожній список клієнтів.
# ● Під час додавання нового клієнта до банку створюйте об'єкт класу Клієнт та
# додавайте його до списку клієнтів банку.
# ● При спробі зберегти або завантажити дані з файлу, використовуйте винятки
# (наприклад, FileNotFoundError або IOError), щоб обробити можливі помилки.
# ● Додайте обробку помилок для випадків, коли клієнт не знайдений або файл не
# знайдено.
# ● Реалізуйте інші методи та функціональність за бажанням.

# class KlientKontrol:
#     def __get__(self, instance, owner):
#         return instance.__dict__['name']
#     def __set__(self, instance, value):
#         if isinstance(value, int) or value <= 0:
#             raise Exception('Unknown name')
#         instance.__dict__['name'] = value
#
#     def __delete__(self, instance):
#         del instance.__dict__['name']
#
# class Klient:
#     name = KlientKontrol()
#     def __init__(self, klient, balance):
#         self.klient = klient
#         self.balance = balance
#
#     def __str__(self):
#         print(f"that klient: {self.klient} has {self.balance}")
#
# class Bank(Klient):
#     name = KlientKontrol()
#     def __init__(self, klient):
#         super().__init__(klient)
#         self.list_of_clients = []
#     def add(self, name):
#         self.list_of_clients = name
#     def found(self, name):
#         for person in self.list_of_clients:
#             if name == person:
#                 print(f'founded is {name}')
#             else:
#                 print('None')
#     def save(self, info):
#         with open('info.txt', 'w') as i:
#             i.writelines(info)
#
#     def show_info(self, name):
#         try:
#             with open('info.txt', 'r') as i:
#                 for row in i.readlines():
#                     if name in row:
#                         print(row)
#                         Klient(row)
#         except:
#             print('"Oops!  That was no valid name.  Try again..."')

class DollarValue:
    def __get__(self, instance, owner):
        return instance.__dict__['DollarValue']
    def __set__(self, instance, value):
        if isinstance(value, str) or value <= 0:
            raise Exception('Unknown DollarValue')
        instance.__dict__['DollarValue'] = value

    def __delete__(self, instance):
        del instance.__dict__['DollarValue']

class Catalog:
    kotirovky = DollarValue()

    def __init__(self, investor):
        self.investor = investor
        self.kripta = {}
        self.kotirovky = {}

    def add(self, name, amount):
        self.kripta = {name: amount}
    def delete(self, kriptoval):
        self.kripta.pop(kriptoval)

    def Value(self):
        DollarValue(self.kotirovky)

    def show(self):
        print(f'name of kriptovaluta and her amount: {self.kripta}, {self.kotirovky}')








