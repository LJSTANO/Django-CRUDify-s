
class BankAccount:
    def __init__(self, name="Joyce", balance=50):
        self.name = name # public attribute
        self.__balance = balance # private attribute
        print(f"My name: {self.name}, & balance: {self.__balance}")

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


defaultAccount = BankAccount()
print(defaultAccount.name)
print(defaultAccount.get_balance())
print("--------------------------------")
account = BankAccount("Ann", 70000)
account.deposit(45000)
print(f"After deposit, Balance: {account.get_balance()}")
account.withdraw(12000)
print(f"After withdraw, Balance: {account.get_balance()}")

# encapsulation - using private variables