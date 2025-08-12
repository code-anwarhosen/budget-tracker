import csv, os
from datetime import date
from typing import List, Dict

class Writer():
    __fieldnames = ['income', 'expense', 'date', 'comment', 'balance']
    
    def __init__(self, filename: str):
        self.filename = filename
    
    def is_first_run(self) -> bool:
        if os.path.exists(self.filename) and self.get_balance():
            return False
        return True
    
    def initialize(self, init_bal: int = 0) -> None:
        if not self.is_first_run():
            return None
        
        with open(self.filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=Writer.__fieldnames)
            
            print('Initializing csv file header with: ', Writer.__fieldnames)
            writer.writeheader()
            
            print('Creating budget file with initial balance:', init_bal)
            writer.writerow({
                'date': date.today(),
                'balance': init_bal,
                'comment': 'initial'
            })
            print('Done, Success!')
    
    def load_from_csv(self) -> List[Dict]:
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
        
    def get_balance(self) -> int | None:
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                
                last_row = None
                for row in reader:
                    last_row = row
                
                if last_row:
                    return int(last_row['balance'])
                
        except FileNotFoundError:
            print(f'Error: \'{self.filename}\' does not exists.\n')
            
        except Exception as error:
            print(f'Error: {error}.')
            
        return None
        
        
    def add_row(self, type, amount, date, balance, comment='N/A'):
        if type not in ['income', 'expense']:
            raise ValueError('type must be income or expense')
        
        try:
            with open(self.filename, 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=Writer.__fieldnames)
                
                writer.writerow({
                    type : amount,
                    'date' : date,
                    'balance': balance,
                    'comment': comment
                })
            return True
        
        except Exception:
            return False
        
    def reset(self) -> None:
        with open(self.filename, 'w') as file:
            file.write('')
            
        
# writer = Writer('data.csv')

# if writer.is_first_run():
    # writer.initialize(2000)

# writer.add_row('income', 1200, date.today(), 1200, 'tv set')
# writer.add_row('expense', 500, date.today(), 700, 'got food')

# data = writer.load_from_csv()
# for row in data:
#     print(row)
    
# print(writer.get_balance())
