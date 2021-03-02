import csv, os

#this allows the use of the csv and txt files on other computers. it reads from this folder instead of the directory
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(THIS_FOLDER, 'account_list.csv')
txt1_file = os.path.join(THIS_FOLDER, 'input1.txt')
txt2_file = os.path.join(THIS_FOLDER, 'input2.txt')
txt3_file = os.path.join(THIS_FOLDER, 'input3.txt')
txt4_file = os.path.join(THIS_FOLDER, 'input4.txt')

balance = 0 #the balance you start with
def banner():
    welcome = "Welcome to UBT Banking"
    print('* '*16)
    print(f'*{welcome:^29s}*')
    print('* '*16)

def login_screen():
    print('1. Login')
    print('2. Create an account')
    print('3. Exit')

#reads the csv file and if input is not found, it repeats the loop
def login(): 
    login = False
    while login == False:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            username = input('Enter user name: ')
            pin = input('Enter PIN: ')

            for row in reader: #reads the username in the first row and the pin in the second row of the csv file
                if username == row[0] and pin == row[1]:
                    print('Login successful!')
                    login = True
                    break
                else:
                    print('Try again')
                    break

#writes a row in the csv file for future login
def create_account():
    with open(csv_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerow([input('Enter your new user name: '), input('Enter your new PIN: ')])

#what the user should see after a successful login screen
def options():
    print()
    print('Please choose from the following options:')
    print('1. Withdraw')
    print('2. Deposit')
    print('3. Check balance')
    print('4. Previous transaction')
    print('5. Exit')

#takes the amount from the balance if there is any, otherwise print insufficient
def withdraw():
    global balance #allows the use of balance from outside the function in line 4
    amount = float(input('Enter amount to withdraw: '))

    if amount > balance:
        print("You have insufficient funds.")
    else:
        balance -= amount 
        print(f'You withdrew {amount:.2f} SR from your account.')

#adds amount to the balance
def deposit():
    global balance 
    amount = float(input('Enter amount to deposit: '))
    balance += amount 
    print(f'You deposited {amount:.2f} SR into your account.')

def current_balance():
    print(f'Your balance is {balance:.2f} SR.')

#def previous_transaction():  <--- work in progress

