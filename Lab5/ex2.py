class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited ", amount, ". New balance: ", self.balance)

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrew ", amount, ". New balance: ",self.balance)
        else:
            print("Insufficient funds. Withdrawal not allowed.")

    def calculate_interest(self):
        pass


class SavingsAccount(Account):
    def calculate_interest(self):
        interest_rate = 0.03
        interest = self.balance * interest_rate
        self.balance += interest
        print(f"Interest of ", interest, " added. New balance: ", self.balance)


class CheckingAccount(Account):
    def calculate_interest(self):
        interest_rate = 0.01
        interest = self.balance * interest_rate
        self.balance += interest
        print("Interest of ", interest, " added. New balance: ", self.balance)


savings_account = SavingsAccount("001", "John Doe", 1000)
savings_account.deposit(500)
savings_account.calculate_interest()
savings_account.withdraw(300)
savings_account.calculate_interest()
print("\n")

checking_account = CheckingAccount("002", "Jane Smith", 1500)
checking_account.deposit(200)
checking_account.calculate_interest()
checking_account.withdraw(100)
checking_account.calculate_interest()
