class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder):
        super().__init__(account_number, account_holder)
        self.__interest_rate = 0.005
        self.__withdrawal_limit = 700000

    def deposit(self, amount):
        super().deposit(amount)
        interest = amount * self.__interest_rate
        super().deposit(interest)
        print("Interest added: ", interest)

    def withdraw(self, amount):
        if amount > self.__withdrawal_limit:
            print("Withdrawal limit exceeded!")
        else:
            super().withdraw(amount)

