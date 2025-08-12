from writer import Writer
from datetime import date

class Account():
    def __init__(self):
        self.writer = Writer('data.csv')
        bal = self.writer.get_balance()
        
        if not isinstance(bal, int):
            raise ValueError("<class Account> method __init__() self.__balance must be int but got", bal)
        
        self.__balance: int = bal
    
    @property
    def balance(self):
        return self.__balance
    
    def add_income(self, amount: int, comment: str, date = date.today()):
        self.__balance += amount
        
        self.writer.add_row(
            type='income',
            amount=amount,
            date=date,
            balance=self.balance,
            comment=comment
        )
        
    def add_expense(self, amount: int, comment: str, date = date.today()):
        self.__balance -= amount
        
        self.writer.add_row(
            type='expense',
            amount=amount,
            date=date,
            balance=self.balance,
            comment=comment
        )


# account = Account()

# print(account.balance)

# account.add_income(200, "sold remote")

# print(account.balance)