from bank import NewBank


bank = NewBank("Alice", 25, 500, "1234")


bank.name = "Bob"
bank.age = 30
bank.money = 1000
bank.key = "5678"


print(bank.name)
print(bank.age)
print(bank.money)
print(bank.key)
