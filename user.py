import sys,time,os,linecache
def user_logic():
    exit_app = False
    while not exit_app:
        get_login_token = input('Enter Your Login Token: ')
        get_pass = input('Enter Your Password: ')
        with open(f'data/{get_login_token}.txt','r') as f:
            username = linecache.getline(f"data/{get_login_token}.txt", 1)
        os.system('cls||clear')
        print('Welcome, '+username)
        print('')
        print('a. Check Balance')
        print('b. Send Someone')
        print('c. Your Payment Logs')
        print('d. Exit')
        print('')
        user_greet = input('Select B/W: ')
        if user_greet == 'a':
            get_login_token = input("Enter Login Token: ")
            with open(f'data/{get_login_token}.txt','r') as f:
                    balance_read = linecache.getline(f'data/{get_login_token}.txt', 4)
                    print(" Your Balance: "+balance_read)
        if user_greet == 'b':
            get_user_token = input("Enter The User's Token: ")
            send_funds = input('Send Funds? : ')
            with open(f'data/{get_login_token}.txt','r') as f:
                    balance_read = linecache.getline(f'data/{get_login_token}.txt', 4)
            if int(balance_read) < int(send_funds):
                print("Insufficient Funds ! Unable To Pay")
            if int(balance_read) > int(send_funds):
                input('Are You Sure ? : ')
                with open(f'data/{get_user_token}.txt','r+') as f:
                    lines = f.readlines()
                    lines[3] = send_funds
                    f.seek(0)
                    f.truncate()
                    f.writelines(lines)
                    f.truncate()
                get_login_token = input('Login Token For Payment: ')
                with open(f'data/{get_login_token}.txt','r+') as f:
                    balance_read = linecache.getline(f'data/{get_login_token}.txt', 4)
                    edited_balance = int(balance_read) - int(send_funds)
                    
                with open(f'data/{get_login_token}.txt','r+') as f:
                    lines = f.readlines()
                    lines[3] = str(edited_balance)
                    f.seek(0)
                    f.truncate()
                    f.writelines(lines)
                    f.truncate()
                    print('Payment Successful!')