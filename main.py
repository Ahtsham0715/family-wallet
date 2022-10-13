


import datetime


class Family_Wallet():
    def __init__(self):
        with open('bank_balance.txt', 'r') as f:
            self.bank_balance = int(f.read())
        with open('wallet_balance.txt', 'r') as f:
            self.balance= int(f.read())
        self.children_paid_amount = 0
        self.family_transaction_details = []
        self.family_blocked_details = {}
        self.items_data = [
            {
                'item_name' : 'bag',
                'shop_name' : 'walmat'
                },
            {
                'item_name' : 'sneakers',
                'shop_name' : 'walmat'
                },
            {
                'item_name' : 'mouse',
                'shop_name' : 'walmat'
                },
            {
                'item_name' : 'laptop',
                'shop_name' : 'amazon'
                },
            {
                'item_name' : 'milk',
                'shop_name' : 'amazon'
                },
            {
                'item_name' : 'chocolates',
                'shop_name' : 'amazon'
                },
        ]
        with open('blocked.txt', 'r') as f:
            for data in f.readlines():
                self.family_blocked_details[str(data).split(',')[0]] = str(data).split(',')[1]
            
        self.members = {
            'Mam' : {
                'amount_paid': 0,
                'amount_withdrawn': 0,
                'amount_deposited': 0,
                'requests':{},
                'transactions': {},
                'notifications' : '',
                'isblocked': self.family_blocked_details['Mam']
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
                'isblocked': self.family_blocked_details['Child1']
                },
            'Child2' : {
                'pending_requests':{},
                'transactions': {},
                'amount_paid': 0,
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                'isblocked': self.family_blocked_details['Child2']
                },
            'Child3' : {
                'amount_paid': 0,
                'pending_requests':{},
                'transactions': {},
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                'isblocked': self.family_blocked_details['Child3']
                },
            'Child4' : {
                'amount_paid': 0,
                'pending_requests':{},
                'transactions': {},
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                'isblocked': self.family_blocked_details['Child4']
                },
            'Child5' : {
                'amount_paid': 0,
                'pending_requests':{},
                'transactions': {},
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                'isblocked': self.family_blocked_details['Child5']
                },
            'Child6' : {
                'amount_paid': 0,
                'pending_requests':{},
                'transactions': {},
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                'isblocked': self.family_blocked_details['Child6']
                },
            'Child7' : {
                'amount_paid': 0,
                'pending_requests':{},
                'transactions': {},
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                'isblocked': self.family_blocked_details['Child7']
                },
            'Child8' : {
                'amount_paid': 0,
                'pending_requests':{},
                'transactions': {},
                'amount_withdrawn': 0,
                'daily_remaining_amount': 0,
                'paid_times': 0,
                'isblocked': self.family_blocked_details['Child8']
                },
        }
    
    def check_transactions(self):
        # mydetails = ''
        # for i in range(self.family_transaction_details):
        #     mydetails += f'{i}- {self.family_transaction_details[i]}\n\n'
        # print(mydetails)
        print('\n\nFamily Transactions details\n\n')
        with open('family_transanctions.txt', 'r') as f:
            for data in f.readlines():
                print(data)

    
    def Deposit(self, amount, name):
        if int(self.bank_balance) >= int(amount):
            self.balance += amount
            with open('wallet_balance.txt', 'w') as f:
                f.write(str(self.balance))
                
            with open('bank_balance.txt', 'w') as f:
                f.write(str(int(self.bank_balance) - int(amount)))
            
            with open('family_transanctions.txt', 'a') as f:
                f.write(f'{name} has deposited {amount}\n')
            self.family_transaction_details.append(f'{name} has deposited {amount} at {datetime.datetime.now()}')
            print(f'\n\n{amount}$ has been deposited from your bank account.\nYour new wallet balance is {self.balance}\n')
        else:
            print('Unable to Deposit this amount as your bank balance is low.')
        
        
    def Withdraw(self, amount, name):
        self.balance -= amount
        with open('wallet_balance.txt', 'w') as f:
            f.write(str(self.balance))
        with open('family_transanctions.txt', 'a') as f:
            f.write(f'{name} has withdrawn {amount} at {datetime.datetime.now()}\n')
        self.family_transaction_details.append(f'{name} has withdrawn {amount}')  
        print(f'{amount} has been withdrawn successfully')  
        
    def Pay(self, amount, name, transaction_details):
        if self.balance != 0:
            if name == 'Mam' or name == 'Dad':
                self.balance -= amount
                with open('wallet_balance.txt', 'w') as f:
                    f.write(str(self.balance))
                self.members[name]['amount_paid'] += amount
                print(f'{amount}$ has been paid\nyour remaining wallet balance is {self.balance}')
                self.family_transaction_details.append(f'{name} has paid {amount} to purchase {transaction_details["item_name"]} from {transaction_details["shop_name"]}')
                with open('family_transanctions.txt', 'a') as f:
                    f.write(f'{name} has paid {amount} to purchase {transaction_details["item_name"]} from {transaction_details["shop_name"]} at {datetime.datetime.now()}\n')
            else:
                if self.members[name]['paid_times'] == 0:
                    if amount <= 50:
                        self.balance -= amount
                        with open('wallet_balance.txt', 'w') as f:
                            f.write(str(self.balance))
                        self.children_paid_amount += amount
                        self.members[name]['amount_paid'] += amount
                        print(f'{amount}$ has been paid\nyour daily remaining balance is {self.members[name]["daily_remaining_amount"]}')
                        self.family_transaction_details.append(f'{name} has paid {amount} to purchase {transaction_details["item_name"]} from {transaction_details["shop_name"]}')
                        with open('family_transanctions.txt', 'a') as f:
                            f.write(f'{name} has paid {amount} to purchase {transaction_details["item_name"]} from {transaction_details["shop_name"]} at {datetime.datetime.now()}\n')
                    else:
                        self.kid_input = input('you need permission from parents to pay more than 50$\nPress 1 to request to Mam or press any key to exit... ')
                        if self.kid_input == '1':
                            self.members['Mam']['requests'][name]['extra_money'] = f'{name} has requested to pay more than 50$\nPress 1 to accpet, Press 2 to reject or Press 3 to transfer to Dad... '

                else:
                    self.kid_input = input("You can't use wallet twice\nSend request to parents to use wallet again\nPress 1 to send request or press any key to exit... ")   
                    if self.kid_input == '1':
                        with open('requests.txt', 'a') as f:
                            f.write(f'{name} has requested to use wallet second time\n')
                        # self.members['Mam']['requests'][name]['extra_usage'] = f'{name} has requested to use wallet second time\nPress 1 to accpet or Press 2 to reject... '
                        # self.members['Dad']['requests'][name]['extra_usage'] = f'{name} has requested to use wallet second time\nPress 1 to accpet or Press 2 to reject... '
                    else:
                        pass        
        
        else:
            if name == 'Mam' or name == 'Dad':
                self.reponse = input('Insufficient balance\nPress 1 to deposit money or Press 2 to exit... ')
                if self.reponse == '1':
                    try:
                        self.amount = int(input('Enter amount you want to deposit... '))
                        self.balance += self.amount
                        with open('wallet_balance.txt', 'w') as f:
                            f.write(str(self.balance))
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
    family_info = {}
    with open('blocked.txt', 'r') as f:
        # data = f.readlines()
        for data in f.readlines():
            family_info[str(data).split(',')[0]] = str(data).split(',')[1]
        print(family_info)
    family_wallet = Family_Wallet()
    print('Welcome to Family Wallet...!!!\n\n')
    name = input('Enter your name... ')
    if name in family_wallet.members.keys() and name != 'Dad' and name != 'Mam':
        if family_info[name] == 'True\n':
            print('Sorry You are blocked by the dad.')
        else:
            print('Items List\n\n')
            print('Item Name\t\tShop Name\n\n')
            for item in family_wallet.items_data:
                print(f'{item["item_name"]}\t\t{item["shop_name"]}')
            response = input('Press 1 to pay or press 2 to exit... ')
            if response == '1':
               
                try:
                    amount = int(input('Enter amount you want to pay... '))
                   
                except:
                    amount = int(input('Invalid amount! Again Enter the amount... '))
                item_name = input('Enter item name you are going to purchase... ')
                shop_name = input('Enter shop name from where you are going to purchase this item... ')
                    
                family_wallet.Pay(amount=amount, name=name, transaction_details={
                        'item_name' : item_name,
                        'shop_name' : shop_name,
                    })
    elif str(name) in family_wallet.members.keys():
        if name == 'Mam':
            if family_info[name] == 'True\n':
                print('Sorry You are blocked by the dad.')
            else:
                print('Items List\n\n')
                print('Item Name\t\tShop Name\n\n')
                for item in family_wallet.items_data:
                    print(f'{item["item_name"]}\t\t{item["shop_name"]}')
                if family_wallet.balance < 100:
                    print('\n\n*** Your wallet balance is low please deposit some amount!!! ***\n\n')
                # print('Press 1 to Pay\nPress 2 to deposit money\nPress 3 to withdraw money\nPress 4 to check requests\nPress 5 to check family transactions\nPress 6 to check balance')
                res = input('Press 1 to Pay\nPress 2 to deposit money\nPress 3 to withdraw money\nPress 4 to check requests\nPress 5 to check family transactions\nPress 6 to check balance... ')
                print(res)
                # print(type(res))
                if res == '1':
                    print('Items List\n\n')
                    print('Item Name\t\tShop Name\n\n')
                    for item in family_wallet.items_data:
                        print(f'{item["item_name"]}\n\n{item["shop_name"]}')
                    try:
                        amount = int(input('Enter amount you want to pay... '))
                       
                    except:
                        amount = int(input('Invalid amount! Again Enter the amount... '))
                    item_name = input('Enter item name you are going to purchase... ')
                    shop_name = input('Enter shop name from where you are going to purchase this item... ')
                    family_wallet.Pay(amount=amount, name=name, transaction_details={
                        'item_name' : item_name,
                        'shop_name' : shop_name,
                    })
                elif res == '2':
                    print(f'your bank balance is {family_wallet.bank_balance}$')
                    amount = int(input('Enter amount you want to deposit... '))
                    family_wallet.Deposit(amount=amount, name=name)
                elif res == '3':
                    amount = int(input('Enter amount you want to withdraw... '))
                    family_wallet.Withdraw(amount=amount, name=name)
                elif res == '4':
                    with open('requests.txt', 'r') as f:
                        requests = f.readlines()
                    for request in requests:
                        print(request)
                    # print(family_wallet.members[name]['requests'].values())
                elif res == '5':
                    family_wallet.check_transactions()
                elif res == '6':
                    print(f'your remaining balance is {family_wallet.balance}$.')
                else:
                    print('Invalid Choice')
        elif name == 'Dad':
            if family_wallet.balance < 100:
                print('\n\n*** Your wallet balance is low please deposit some amount!!! ***\n\n')
            print('Press 1 to Pay\nPress 2 to deposit money\nPress 3 to withdraw money\nPress 4 to check requests\nPress 5 to check family transactions\nPress 6 to check balance\nPress 7 to block a family member\nPress 8 to unblock a family person.... ')
            res = input()
            if res == '1':
                print('Items List\n\n')
                print('Item Name\t\tShop Name\n\n')
                for item in family_wallet.items_data:
                    print(f'{item["item_name"]}\n\n{item["shop_name"]}')
                try:
                    amount = int(input('Enter amount you want to pay... '))
                   
                except:
                    amount = int(input('Invalid amount! Again Enter the amount... '))
                item_name = input('Enter item name you are going to purchase... ')
                shop_name = input('Enter shop name from where you are going to purchase this item... ')
                family_wallet.Pay(amount=amount, name=name, transaction_details={
                    'item_name' : item_name,
                    'shop_name' : shop_name,
                })
            elif res == '2':
                print(f'your bank balance is {family_wallet.bank_balance}$')
                amount = int(input('Enter amount you want to deposit... '))
                family_wallet.Deposit(amount=amount, name=name)
            elif res == '3':
                amount = int(input('Enter amount you want to withdraw... '))
                family_wallet.Withdraw(amount=amount, name=name)
            elif res == '4':
                print(family_wallet.members[name]['requests'].values())
            elif res == '5':
                family_wallet.check_transactions()
            elif res == '6':
                print(f'your remaining balance is {family_wallet.balance}$.')
            elif res == '7':
                print('\n\n*** UnBlocked Persons List ***\n\n')
                for key,value in family_info.items():
                    if value == 'False\n':
                        print(f'{key}\n')
                member_name = input('Enter the name of family member you want to block... ')
                if member_name in family_wallet.members.keys():
                    # family_wallet.members[member_name]['isblocked'] = True
                    family_info[member_name] = 'True\n'
                    with open('blocked.txt', 'w') as f:
                        for key, value in family_info.items():
                            f.write(f'{key},{value}')
                    print(f'{member_name} has been blocked')
                else:
                    print('family member not found')
            elif res == '8':
                print('\n\n*** Blocked Persons List ***\n\n')
                for key,value in family_info.items():
                    if value == 'True\n':
                        print(f'{key}\n')
                member_name = input('Enter the name of family member you want to unblock... ')
                if member_name in family_wallet.members.keys():
                    # family_wallet.members[member_name]['isblocked'] = True
                    if family_info[member_name] == 'True\n':
                        family_info[member_name] = 'False\n'
                        with open('blocked.txt', 'w') as f:
                            for key, value in family_info.items():
                                f.write(f'{key},{value}')
                        print(f'{member_name} has been unblocked')
                    else:
                        print(f'\n*** {member_name} not found in blocked list.')
                else:
                    print('family member not found')
            else:
                print('Invalid Choice')
        else:
            print('Invalid Input')    
    else:
        print('Family Member not found!!')     
        
main()