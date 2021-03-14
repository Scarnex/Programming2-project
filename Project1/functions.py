'''
The purpose of this module is to contain all the functions possible to make the main.py work.
If you run this module, it will test out all the functions.
Authors: Yousef Alshaibani and Abdelrahman Elsayed
Date: 14/3/2021
'''

import csv, os, random

#this allows the use of the csv and txt files on other computers. it reads from this folder instead of the directory
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
account_file = os.path.join(THIS_FOLDER, 'account_list.csv')
deposit_file = os.path.join(THIS_FOLDER, 'deposit.txt')
withdraw_file = os.path.join(THIS_FOLDER, 'withdraw.txt')
balance_file = os.path.join(THIS_FOLDER, 'balance.txt')
txt4_file = os.path.join(THIS_FOLDER, 'input4.txt')

balance = 0 #the balance you start with
def banner():
    welcome = 'Welcome to UBT Banking'
    print('* '*16)
    print(f'*{welcome:^29s}*')
    print('* '*16)

def login_screen():
    print('='*30)
    print('| 1. Login                   |')
    print('| 2. Create an account       |')
    print('| 3. Exit                    |')
    print('='*30)

#reads the csv file and if input is not found, it repeats the loop
def login(): 
    login = False
    while login == False:
        with open(account_file, 'r') as file:
            reader = csv.reader(file)
            username = input('Enter Username: ')
            pin = input('Enter PIN: ')
            next(reader) #skips the "header" line 

            for col in reader: #reads the username in the first column and the pin in the second column after the header from the csv file
                if username == col[0] and pin == col[1]:
                    print('Login successful!')
                    login = True
                    break
                else:
                    print('Try again')
                    break

#writes a row after the header in the csv file for future login
def create_account():
    print ('Here is an example of what your PIN should look like:', random.randint(111,999)) #prints random 3 digits as an example of a pin
    with open(account_file, 'w', newline = '') as file:
        header = ['Username', 'PIN']
        writer = csv.DictWriter(file, fieldnames = header)
        writer.writeheader()
        writer.writerow({'Username': input('Enter your new Username: '), 'PIN': int(input("Enter your new PIN: "))})     
        print('Account succesfully created!')

#what the user should see after a successful login screen
def options():
    with open(account_file, 'r') as file: #similar to the login function, it reads the first column of the csv file which is the username
        reader = csv.reader(file)
        next(reader)
        for col in reader:
            print(f'\nHello, {col[0].title()}. What would you like to do today?') #capitalizes the username for better aesthetics
            break
    print('='*30)
    print('| 1. Withdraw                |')
    print('| 2. Deposit                 |')
    print('| 3. Check balance           |')
    print('| 4. Transaction history     |')
    print('| 5. Exit                    |')
    print('='*30)

#takes the amount from the balance if there is any, otherwise print insufficient
def withdraw():
    global balance #allows the use of the balance variable from outside the function in line 11
    amount = float(input('Enter amount to withdraw: '))
    if amount > balance:
        print("You have insufficient funds.")
    else:
        balance -= amount 
        print(f'You withdrew {amount:.2f} SR from your account.')

        with open(withdraw_file, 'a', newline = '') as file: #writes the amount you withdrew to the txt file
            writer = csv.writer(file)
            writer.writerow([amount])

#adds amount to the balance
def deposit():
    global balance
    amount = float(input('Enter amount to deposit: '))
    balance += amount 
    print(f'You deposited {amount:.2f} SR into your account.')

    with open(deposit_file, 'a', newline = '') as file: #writes the amount you deposited to the txt file
        writer = csv.writer(file)
        writer.writerow([amount])

#prints current balance and writes it in the txt file               
def current_balance():
    with open(balance_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerow([balance])
        print(f'Your balance is {balance:.2f} SR.')

#prints all the amounts you withdrew and deposited throughout using the program
def transaction_history():
    with open(withdraw_file, 'r') as file: #reads and prints the withdraw.txt file
        print('-'*19)
        print('Withdrawal history:')
        print('-'*19)
        print(file.read())

    with open(deposit_file, 'r') as file: #reads and prints the deposit.txt file
        print('-'*16)
        print('Deposit History:')
        print('-'*16)
        print(file.read())

if __name__ == '__main__':
    print('Testing functions...\n')
    banner()
    login_screen()
    create_account()
    login()
    options()
    deposit()
    withdraw()
    current_balance()
    transaction_history()
    print('Test complete.')