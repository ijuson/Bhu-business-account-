class ChildrenAccount(BankAccount):
    def _init_(self, account_number, account_holder):
        super()._init_(account_number, account_holder)
        self.__interest_rate = 0.007

    def deposit(self, amount):
        super().deposit(amount)
        interest = amount * self.__interest_rate
        super().deposit(interest)
        print("Interest added: ", interest)