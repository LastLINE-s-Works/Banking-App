import sys,time,os,linecache
exit_app = False
def adminlogic():
    while not exit_app:
        getpass = input('Admin Password: ')
        with open('adminpass','r') as f:
            checkpass = f.read()
        if getpass != checkpass:
            print('Wrong Password')
        elif getpass == checkpass:
            print('Logged In As Admin')
            os.system('cls||clear')
            print("Last's Banking App Admin Dashboard")
            print('')
            print('a. Add User')
            print('b. Check User Balance')
            print('c. Edit Funds')
            print('d. Delete User')
            print('e. Exit')
            print('')
            admin_greet = input('Select B/W: ')
            if admin_greet == 'a':
                username = input('Username Will Be: ')
                login_token = input('Login Token: ')
                password = input('Password Will Be: ')
                balance = input('Balance Will Be: ')
                with open(f'data/{login_token}.txt','w') as f:
                    f.write(username+'\n')
                    f.write(password+'\n')
                    f.write(login_token+'\n')
                    f.write(balance+'\n')
                    f.write("Transactions: ")
                with open(f'data/{login_token}-pass.txt','w') as f:
                    f.write(password)
                time.sleep(2)
                print('User Added Succesfully !')
            if admin_greet == 'b':
                get_login_token = input("Enter User's Login Token: ")
                with open(f'data/{get_login_token}.txt','r') as f:
                    balance_read = linecache.getline(f'data/{get_login_token}.txt', 4)
                    print("Balance: "+balance_read)
            if admin_greet =='c':
                get_login_token = input("Enter User's Login Token: ")
                edit_funds = input('Funds: ')
                with open(f'data/{get_login_token}.txt','r+') as f:
                    lines = f.readlines()
                    lines[3] = edit_funds
                    f.seek(0)
                    f.truncate()
                    f.writelines(lines)
                    f.truncate()
                    print('Funds Edited')
            if admin_greet == 'd':
                get_login_token = input("Enter User's Login Token: ")
                with open(f'data/{get_login_token}.txt','w') as f:
                    os.remove(f.name)
                    f.close()
                    print("User Deleted Successfully !")
            if admin_greet == 'e':
                exit()