from setup import setuplogic
from admin import adminlogic
from user import user_logic
import time , os , sys

#setuplogic()

def bankingapp():
    exit_app = False
    while not exit_app:
        print("Welcome To Last's Banking App")
        time.sleep(2)
        os.system('cls||clear')
        print("a. Login As Admin")
        print("b. Login As User")        
        print("c. Exit")
        print('')
        greet = input('Select B/W: ')
        if greet == 'a':
            adminlogic()
        if greet == 'b':
            user_logic()
        if greet == 'c':
            exit()
        
bankingapp()