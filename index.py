import re
import math
from colorama import Fore, Style
import sys
from threading import Timer
import time
from datetime import datetime

print(Fore.GREEN + Style.BRIGHT + 'Welcome, time traveller. I can see that time travelling has got you lost here')
time.sleep(1.5)
taken_username = ['adam' , 'reaksmey' , 'michaellogy' , 'adamina' , 'melkita ulamun']

def takenusername():
    print(Fore.BLUE + 'You may begin by creating your username below')
    while True:
        newuser = input(Fore.RESET + 'Please create your username: ')
        if newuser in taken_username:
            print(Fore.RED + 'Username taken, Please try another one')
        else:
            print(Fore.GREEN + f'- Welcome, {newuser} -')
            time.sleep(1.5)
            break

takenusername()

def password():
    print(Fore.BLUE + 'For your next step, Please create a password')
    while True:
        password = input(Fore.RESET + 'Create your password: ')
        if len(password) < 8:
            print(Fore.RED + 'Make sure your password is 8 characters or longer')
        elif re.search('[0-9]' , password) is None:
            print(Fore.RED+ 'Make sure your password includes at least a number in it')
        elif re.search('[A-Z]' , password) is None:
            print(Fore.RED + 'Make sure your password includes at least a capital letter in it')
        else:
            break
    print(Fore.GREEN + 'Cool password')
    while True:
        conpass1 = input(Fore.RESET + 'Please confirm your password: ')
        if not conpass1 == password:
            print(Fore.RED + 'Oops, password did not match, Please try again')
        else:
            print(Fore.GREEN + 'New password confirmed')
            break
password()

def dob():
    print(Fore.BLUE + 'For your next step, Please enter your date of birth')
    date = int(input(Fore.RESET + 'Enter the day you were born: '))
    while True:
        if date > 31:
            print(Fore.RED + 'Invalid day, Please try again')
        else:
            break
        continue
    month = int(input(Fore.RESET + 'Enter the month you were born: '))
    while True:
        if month > 12:
            print(Fore.RED + 'Invalid month, Please try again: ')
        else:
            break
        continue
    year = int(input(Fore.RESET + 'Enter the year that you were born: '))
    while True:
        if year < 0:
            print(Fore.RED + 'Invalid year, Please try again: ')
        else:
            break
        break






dob()

























