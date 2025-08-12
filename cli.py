import sys, argparse
from tracker import Account
from writer import Writer


def main() -> None:
    parser = get_argparser()
    args = parser.parse_args()
    action = args.action

    writer = Writer('data.csv')
    
    if action == 'init':
        balance = args.amount
        
        if not balance:
            print('-a/--amount required: int \n')
            
        try:
            balance = int(balance)
        except Exception as error:
            parser.error("Balance must be int.")
            sys.exit(1)
            
        writer.initialize(balance)

    
    if writer.is_first_run():
        print("Data storage not initialized!")
        print(f"run \'python {sys.argv[0]} init -a/--amount [balance amount e.g. 500 or 0]\' to initialize")
        sys.exit(1)
    
    account = Account()
    
    if action in ["in", "income", "ex", "expense"]:
        amount, comment = args.amount, args.comment
        if None in [amount, comment]:
            parser.error("the following arguments are required: -a/--amount, -c/--comment")
        
        if action in ["in", "income"]:
            print("added income: ")
            account.add_income(amount=amount, comment=comment)
            
        if action in ["ex", "expense"]:
            print("added expense: ")
            account.add_expense(amount=amount, comment=comment)
            
        
    elif action in ["su", "summary"]:
        month, year = args.month, args.year
        
        print('###Summary###')
        print(f'Balance is: {account.balance} tk\n')
        
        print("""
            income  |  expense  |  date  |  balance  |  comment
            ---------------------------------------------------
            """,
            end=''
        )
        data = writer.load_from_csv()
        for row in data[-5:]:
            income = row['income'] if row['income'] else '    '
            expense = row['expense'] if row['expense'] else '    '
            
            string = f"""
            {income}  | {expense}  | {row['date']}  |  {row['balance']}  |  {row['comment']}
            """
            print(string, end='')
        
    elif action == 'reset':
        inp = input('All data will be lost. \nAre you sure you want to delete? \n\nType yes|no: ')
        if inp != 'yes':
            print('\nAborting')
            sys.exit(1)
            
        writer.reset()
        print('###Data Reseted###')
        print('Make a fresh start.')
        
        

def get_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Simple Budget Tracker CLI Application\n\nExamples:\n  python cli.py in -a 500 -c Salary\n  python cli.py su",
        formatter_class=argparse.RawTextHelpFormatter
    )

    # Exit the program if no argument provided
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    actions = ["init", "in", "income", "ex", "expense", "su", "summary", "reset"]
    
    parser.add_argument(
            "action", choices=actions, 
            help="Actions: add income, add expense, get summary"
    )

    parser.add_argument("-a", "--amount", type=int, help="Amount Value")
    parser.add_argument("-c", "--comment", help="Comment of the entry")

    # Only for getting summary
    parser.add_argument("-m", "--month", type=int, help="Month number (1-12)")
    parser.add_argument("-y", "--year", type=int, help="Year (e.g., 2025)")
    
    return parser



if __name__ == '__main__':
    main()
