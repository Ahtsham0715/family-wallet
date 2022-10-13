class bank_account():
    def __init__(self):
        with open('bank_balance.txt', 'r') as f:
            self.bank_balance = int(f.read())
    