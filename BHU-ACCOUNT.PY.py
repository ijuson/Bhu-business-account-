class BankAccount:
    def _init_(self, account_number, account_holder):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount
        print("Deposit successful. Your new balance is: ", self.__balance)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print("Withdrawal successful. Your new balance is: ", self.__balance)

    def check_balance(self):
        print("Your current balance is: ", self.__balance)