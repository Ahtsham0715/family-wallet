





class Family_Wallet():
    def __init__(self):
        self.balance=0
        self.children_paid_amount = 0
        self.members = {
            'Mam' : {
                'amount_paid': 0,
                'amount_withdrawn': 0,
                'amount_deposited': 0,
                'requests':{},
                'transactions': {},
                'notifications' : '',
                'isblocked': False
                },
            'Dad' : {
                'amount_paid': 0,
                'amount_withdrawn': 0,
                'amount_deposited': 0,
                'requests':{},
                'transactions': {},
                'notifications' : '',
                },
            'Child1' : {
                'pending_requests':{},
                'transactions': {},
                'amount_paid': 0,
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                'isblocked': False
                },
            'Child2' : {
                'pending_requests':{},
                'transactions': {},
                'amount_paid': 0,
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                'isblocked': False
                },
            'Child3' : {
                'amount_paid': 0,
                'pending_requests':{},
                'transactions': {},
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                'isblocked': False
                },
            'Child4' : {
                'amount_paid': 0,
                'pending_requests':{},
                'transactions': {},
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                'isblocked': False
                },
            'Child5' : {
                'amount_paid': 0,
                'pending_requests':{},
                'transactions': {},
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                'isblocked': False
                },
            'Child6' : {
                'amount_paid': 0,
                'pending_requests':{},
                'transactions': {},
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                'isblocked': False
                },
            'Child7' : {
                'amount_paid': 0,
                'pending_requests':{},
                'transactions': {},
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                'isblocked': False
                },
            'Child8' : {
                'amount_paid': 0,
                'pending_requests':{},
                'transactions': {},
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                'isblocked': False
                },
        }
    
    def Deposit(self, amount, name):
        self.balance += amount
        
    def Withdraw(self, amount, name):
        self.balance -= amount
    
    def Pay(self, amount, name):
        if self.balance == 0:
            if name == 'Mam' or name == 'Dad':
                self.balance -= amount
                self.members[name]['amount_paid'] += amount
                print(f'{amount}$ has been paid\nyour remaining wallet balance is {self.balance}')
            else:
                if self.members['name']['paid_times'] == 0:
                    if amount <= 50:
                        self.balance -= amount
                        self.children_paid_amount += amount
                        self.members[name]['amount_paid'] += amount
                        print(f'{amount}$ has been paid\nyour daily remaining balance is {self.members[name]["daily_remaining_amount"]}')
                    else:
                        self.kid_input = input('you need permission from parents to pay more than 50$\nPress 1 to request to Mam or press any key to exit... ')
                        if self.kid_input == '1':
                            self.members['Mam']['requests'][name]['extra_money'] = f'{name} has requested to pay more than 50$\nPress 1 to accpet, Press 2 to reject or Press 3 to transfer to Dad... '

                else:
                    self.kid_input = input("You can't use wallet twice\nSend request to parents to use wallet again\nPress 1 to send request or press any key to exit... ")   
                    if self.kid_input == '1':
                        self.members['Mam']['requests'][name]['extra_usage'] = f'{name} has requested to use wallet second time\nPress 1 to accpet or Press 2 to reject... '
                        self.members['Dad']['requests'][name]['extra_usage'] = f'{name} has requested to use wallet second time\nPress 1 to accpet or Press 2 to reject... '
                    else:
                        pass        
        else:
            if name == 'Mam' or name == 'Dad':
                self.reponse = input('Insufficient balance\nPress 1 to deposit money or Press 2 to exit... ')
                if self.reponse == '1':
                    try:
                        self.amount = int(input('Enter amount you want to deposit... '))
                        self.balance += self.amount
                    except:
                        print('invalid amount')
                else:
                    pass  
            else:
                self.reponse = input('Insufficient balance\nPress 1 to request parents to deposit money or Press 2 to exit... ')
                if self.reponse == '1':
                        self.members['Mam']['requests'][name]['extra_usage'] = f'{name} has requested to deposit amount as account balance is not sufficient'
                else:
                    pass
