import csv, os, getpass

#this allows the use of the csv and txt files on other computers. it reads from this folder instead of the directory
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
account_file = os.path.join(THIS_FOLDER, 'account_list.csv')
deposit_file = os.path.join(THIS_FOLDER, 'deposit.txt')
withdraw_file = os.path.join(THIS_FOLDER, 'withdraw.txt')
balance_file = os.path.join(THIS_FOLDER, 'balance.txt')
txt4_file = os.path.join(THIS_FOLDER, 'input4.txt')

balance = 0 #the balance you start with
def banner():
    welcome = "Welcome to UBT Banking"
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

            for col in reader: #reads the username in the first column and the pin in the second column of the csv file
                if username == col[0] and pin == col[1]:
                    print('Login successful!')
                    login = True
                    break
                else:
                    print('Try again')
                    break

#writes a row in the csv file for future login
def create_account():
    with open(account_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerow([input('Enter your new Username: '), input('Enter your new PIN: ')])
        print('Account succesfully created!')

#what the user should see after a successful login screen
def options():
    with open(account_file, 'r') as file: #similar to the login function, it reads the first column of the csv file which is the username
        reader = csv.reader(file)
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
                 
def current_balance():
    with open(balance_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerow([balance])
        print(f'Your balance is {balance:.2f} SR.')

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
