





class Family_Wallet():
    def __init__(self):
        self.balance=0
        self.children_paid_amount = 0
        self.family_transaction_details = []
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
    
    def check_transactions(self):
        mydetails = ''
        for i in range(self.family_transaction_details):
            mydetails += f'{i}- {self.family_transaction_details[i]}\n\n'
        print(mydetails)
    
    
    def Deposit(self, amount, name):
        self.balance += amount
        self.family_transaction_details.append(f'{name} has deposited {amount}')
        
        
    def Withdraw(self, amount, name):
        self.balance -= amount
        self.family_transaction_details.append(f'{name} has withdrawn {amount}')    
    def Pay(self, amount, name, transaction_details):
        if self.balance != 0:
            if name == 'Mam' or name == 'Dad':
                self.balance -= amount
                self.members[name]['amount_paid'] += amount
                print(f'{amount}$ has been paid\nyour remaining wallet balance is {self.balance}')
                self.family_transaction_details.append(f'{name} has paid {amount} to purchase {transaction_details["item_name"]} from {transaction_details["shop_name"]}')
            else:
                if self.members['name']['paid_times'] == 0:
                    if amount <= 50:
                        self.balance -= amount
                        self.children_paid_amount += amount
                        self.members[name]['amount_paid'] += amount
                        print(f'{amount}$ has been paid\nyour daily remaining balance is {self.members[name]["daily_remaining_amount"]}')
                        self.family_transaction_details.append(f'{name} has paid {amount} to purchase {transaction_details["item_name"]} from {transaction_details["shop_name"]}')
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


def main():
    family_wallet = Family_Wallet()
    print('Welcome to Family Wallet...!!!\n\n')
    name = input('Enter your name... ')
    if name in family_wallet.members.keys() and name != 'Dad' and name != 'Mam':
        if family_wallet.members[name]['isblocked']:
            print('Sorry You are blocked by the dad.')
        else:
            reponse = input('Press 1 to pay or press 2 to exit... ')
            if reponse == '1':
                try:
                    amount = int(input('Enter amount you want to pay... '))
                    item_name = input('Enter item name you are going to purchase... ')
                    shop_name = input('Enter shop name from where you are going to purchase this item... ')
                    
                    family_wallet.Pay(amount=amount, name=name, transaction_details={
                        'item_name' : item_name,
                        'shop_name' : shop_name,
                    })
                except:
                    amount = int(input('Invalid amount! Again Enter the amount... '))
                    item_name = input('Enter item name you are going to purchase... ')
                    shop_name = input('Enter shop name from where you are going to purchase this item... ')
                    family_wallet.Pay(amount=amount, name=name, transaction_details={
                        'item_name' : item_name,
                        'shop_name' : shop_name,
                    })
    elif name in family_wallet.members.keys():
        if name == 'Mam':
            if family_wallet.members[name]['isblocked']:
                print('Sorry You are blocked by the dad.')
            else:
                if family_wallet.balance < 100:
                    print('\n\nYour wallet balance is low please deposit some amount.\n\n')
                print('Press 1 to Pay\nPress 2 to deposit money\nPress 3 to withdraw money\nPress 4 to check requests\nPress 5 to check family transactions\nPress 6 to check balance')
                response = input()
                if reponse == '1':
                    try:
                        amount = int(input('Enter amount you want to pay... '))
                        item_name = input('Enter item name you are going to purchase... ')
                        shop_name = input('Enter shop name from where you are going to purchase this item... ')
                        
                        family_wallet.Pay(amount=amount, name=name, transaction_details={
                            'item_name' : item_name,
                            'shop_name' : shop_name,
                        })
                    except:
                        amount = int(input('Invalid amount! Again Enter the amount... '))
                        item_name = input('Enter item name you are going to purchase... ')
                        shop_name = input('Enter shop name from where you are going to purchase this item... ')
                        family_wallet.Pay(amount=amount, name=name, transaction_details={
                            'item_name' : item_name,
                            'shop_name' : shop_name,
                        })
                elif response == '2':
                    amount = int(input('Enter amount you want to deposit... '))
                    family_wallet.Deposit(amount=amount, name=name)
                elif response == '3':
                    amount = int(input('Enter amount you want to withdraw... '))
                    family_wallet.Withdraw(amount=amount, name=name)
                elif response == '4':
                    print(family_wallet.members[name]['requests'].values())
                elif response == '5':
                    family_wallet.check_transactions()
                elif response == '6':
                    print(f'your remaining balance is {family_wallet.balance}$.')
                else:
                    print('Invalid Choice')
        elif name == 'Dad':
            if family_wallet.balance < 100:
                print('\n\nYour wallet balance is low please deposit some amount.\n\n')
            print('Press 1 to Pay\nPress 2 to deposit money\nPress 3 to withdraw money\nPress 4 to check requests\nPress 5 to check family transactions\nPress 6 to check balance\nPress 7 to block a family member.... ')
            response = input()
            if reponse == '1':
                try:
                    amount = int(input('Enter amount you want to pay... '))
                    item_name = input('Enter item name you are going to purchase... ')
                    shop_name = input('Enter shop name from where you are going to purchase this item... ')
                    
                    family_wallet.Pay(amount=amount, name=name, transaction_details={
                        'item_name' : item_name,
                        'shop_name' : shop_name,
                    })
                except:
                    amount = int(input('Invalid amount! Again Enter the amount... '))
                    item_name = input('Enter item name you are going to purchase... ')
                    shop_name = input('Enter shop name from where you are going to purchase this item... ')
                    family_wallet.Pay(amount=amount, name=name, transaction_details={
                        'item_name' : item_name,
                        'shop_name' : shop_name,
                    })
            elif response == '2':
                amount = int(input('Enter amount you want to deposit... '))
                family_wallet.Deposit(amount=amount, name=name)
            elif response == '3':
                amount = int(input('Enter amount you want to withdraw... '))
                family_wallet.Withdraw(amount=amount, name=name)
            elif response == '4':
                print(family_wallet.members[name]['requests'].values())
            elif response == '5':
                family_wallet.check_transactions()
            elif response == '6':
                print(f'your remaining balance is {family_wallet.balance}$.')
            elif reponse == '7':
                member_name = input('Enter the name of family member you want to block... ')
                if family_wallet.members[member_name] in family_wallet.members.keys():
                    family_wallet.members[member_name]['isblocked'] = True
                    print(f'{member_name} has been blocked')
                else:
                    print('family member not found')
            else:
                print('Invalid Choice')
        else:
            print('Invalid Input')    
    else:
        print('Family Member not found!!')     