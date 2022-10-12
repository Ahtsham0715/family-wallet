





class Family_Wallet():
    def __init__(self):
        self.balance=0
        self.members = {
            'Mam' : {
                'amount_paid': 0,
                'amount_withdrawn': 0,
                'amount_deposited': 0,
                'requests':{},
                'notifications' : '',
                },
            'Dad' : {
                'amount_paid': 0,
                'amount_withdrawn': 0,
                'amount_deposited': 0,
                'requests':{},
                'notifications' : '',
                },
            'Child1' : {
                'amount_paid': 0,
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                },
            'Child2' : {
                'amount_paid': 0,
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                },
            'Child3' : {
                'amount_paid': 0,
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                },
            'Child4' : {
                'amount_paid': 0,
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                },
            'Child5' : {
                'amount_paid': 0,
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                },
            'Child6' : {
                'amount_paid': 0,
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                },
            'Child7' : {
                'amount_paid': 0,
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                },
            'Child8' : {
                'amount_paid': 0,
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                },
        }
    
    def Deposit(self, amount, name):
        self.balance += amount
        
    def Withdraw(self, amount, name):
        self.balance -= amount
    
    def Pay(self, amount, name):
        if name == 'Mam' or name == 'Dad':
            self.balance -= amount
            self.members[name]['amount_paid'] += amount
            print(f'{amount}$ has been paid\nyour remaining wallet balance is {self.balance}')
        else:
            if self.members['name']['paid_times'] == 0:
                self.balance -= amount
                self.members[name]['amount_paid'] += amount
                print(f'{amount}$ has been paid\nyour daily remaining balance is {self.members[name]["daily_remaining_amount"]}')
                
