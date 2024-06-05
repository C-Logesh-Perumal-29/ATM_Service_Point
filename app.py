from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []

    def check_balance(self):
        self.transactions.append(f"Checked balance: ₹{self.balance}")
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: ₹{amount}")
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew: ₹{amount}")
            return True
        elif amount > self.balance:
            return "Insufficient balance"
        else:
            return False

    def get_transactions(self):
        return self.transactions

atm = ATM()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/balance')
def balance():
    balance = atm.check_balance()
    return render_template('balance.html', balance=balance)

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        success = atm.deposit(amount)
        if success:
            message = f"₹{amount} deposited successfully."
        else:
            message = "Invalid deposit amount."
        return render_template('result.html', message=message)
    return render_template('deposit.html')

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        result = atm.withdraw(amount)
        if result == True:
            message = f"₹{amount} withdrawn successfully."
        elif result == "Insufficient balance":
            message = result
        else:
            message = "Invalid withdrawal amount."
        return render_template('result.html', message=message)
    return render_template('withdraw.html')

@app.route('/transactions')
def transactions():
    transactions = atm.get_transactions()
    return render_template('transactions.html', transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)
