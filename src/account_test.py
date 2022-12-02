from bank_account import SavingsAccount, InvestmentAccount

savings_account = SavingsAccount('001', 'Gabriel')
investment_account = InvestmentAccount('001', 'Gabriel', 'Valmir')

print('\n----savings account operations----')
savings_account.deposit(1000)
withdraw_1 = savings_account.withdraw(100)
withdraw_2 = savings_account.withdraw(3000)

print(f'first savings account withdrawl: $ {withdraw_1}')
print(f'second savings account withdrawl: $ {withdraw_2}')

print('\n----investiment account operations----')
investment_account.deposit(500)
withdraw_3 = investment_account.withdraw(300)
withdraw_4 = investment_account.withdraw(300)

print(f'first investment account withdraw: $ {withdraw_3}')
print(f'second investment account withdraw: $ {withdraw_4}')
