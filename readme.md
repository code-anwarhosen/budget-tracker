# **Simple Budget Tracker [CLI]**

* Simple budget tracker CLI application built using `python`. 

* Used `csv` as storage


## Requirements

* Make sure `python` installed
* That's it, You're good to go.


## Installation

1. **Clone the repository.**
```bash
git clone https://github.com/code-anwarhosen/budget-tracker.git
```

2. **Move to project directory**
```bash
cd budget-tracker
```

## Usages

* Initialization
```bash
python cli.py init --amount # --amount is your initial balance
```

* Add Income
```bash
python cli.py in/income -a 5000 -c Incentive # this command add 5000 to your balance with `Incentive` as comment.
```

* Add Expense
```bash
python cli.py ex/expense -a 1200 -c Food # this command remove 1200 from your balance with `Food` as comment.
```

* See Summary
```bash
python cli.py su/summary # Shows last 5 entries with your balance
```


***and you can always use `python cli.py -h` for details help.***

[Github: code-anwarhosen](https://github.com/code-anwarhosen/)

