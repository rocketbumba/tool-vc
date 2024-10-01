from enum import Enum
import xml.etree.ElementTree as ET

from modules.create_account import Account

#APPLCORED100064206

while True:
    print('Welcome!')
    print('1. Create new account')
    print('0. Exit')
    choice = input()
    if choice == '1':
        try:
            account = Account()
            account.create_account()
            print('Account created')
        except Exception as e:
            print(e)
            print('Try again')
    elif choice == '0':
        break
    else:
        print('Invalid choice')

