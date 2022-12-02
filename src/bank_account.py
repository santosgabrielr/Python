class BankAccount:
    def __init__(self, number, owner):
        self.number = number
        self.owner = owner
        self._balance = 0

    @property
    def balance(self):
        return f'your balance is {self._balance}'

    def deposit(self, value):
        self._balance += value
        print(f'Successful deposit. Balance: $ {self._balance}')

    def withdraw(self, value):
        if value > self._balance:
            print(f'Withdrawl failed. Insufficient balance: $ {self._balance}')
            return 0
        self._balance -= value
        print(f'Successful withdrawl. Balance: $ {self._balance}')
        return value


class SavingsAccount(BankAccount):
    def __init__(self, number, owner):
        self.yields = 0.5
        super().__init__(number, owner)


class InvestmentAccount(SavingsAccount):
    def __init__(self, number, owner, account_manager):
        self.account_manager = account_manager
        super().__init__(number, owner)

    def withdraw(self, value):
        print('checking investment term...')
        print('calculating taxes and fees...')
        print('realizing withdrawl...')
        return super().withdraw(value)

    def invest(self, value):
        print('checking if this investment is possible...')
        self._balance += value
