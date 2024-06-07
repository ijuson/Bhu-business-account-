class StudentAccount(BankAccount):
    def __init__(self, account_number, account_holder):
        super().__init__(account_number, account_holder)
        self.__withdrawal_limit = 2000
        self.__deposit_limit = 50000

    def deposit(self, amount):
        if amount > self.__deposit_limit:
            print("Deposit limit exceeded!")
        else:
            super().deposit(amount)

    def withdraw(self, amount):
        if amount > self.__withdrawal_limit:
            print("Withdrawal limit exceeded!")
        else:
            super().withdraw(amount)

# Create accounts
savings_account = SavingsAccount("SAV123", "John kenedy")
current_account = CurrentAccount("CUR456", "Jane mathew")
children_account = ChildrenAccount("CHD789", "Baby last")
student_account = StudentAccount("STU901", "Student pascal")

# Perform transactions
savings_account.deposit(10000)
savings_account.withdraw(5000)

current_account.deposit(20000)
current_account.withdraw(15000)

children_account.deposit(5000)
children_account.check_balance()

student_account.deposit(40000)
student_account.withdraw(1500)