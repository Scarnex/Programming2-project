'''
This is a banking app that lets you perform banking services similar to the conventional banking apps
If you run this module, you'll be able to use our banking services
Authors: Yousef Alshaibani and Abdelrahman Elsayed
Date: 14/3/2021
'''

from functions import banner, login_screen, login, create_account, options, withdraw, deposit, current_balance, transaction_history
import sys

while True:
    banner()
    login_screen()
    login_choice = int(input('Option: '))

    if login_choice == 1:
        login()
        break
    elif login_choice == 2:
        create_account()
        break
    elif login_choice == 3:
        sys.exit('Thank you for using UBT banking. Have a good day!')
    else:
        print('Invalid option')
        continue
        
while True:
    options()
    choice = int(input('Option: '))

    if choice == 1:
        withdraw()
    elif choice == 2:
        deposit()
    elif choice == 3:
        current_balance()
    elif choice == 4:
        transaction_history()
    elif choice == 5:
        sys.exit('Thank you for using UBT banking. Have a good day!')
    else:
         print('Invalid option.')
         continue

    answer = input('\nWould you like to do another transaction? (y/n): ')
    if answer.lower() == 'y':
        continue
    else:
        sys.exit('Thank you for using UBT banking. Have a good day!')