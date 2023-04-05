import sqlite3
import random as r


conn = sqlite3.connect("bank.db")
cur = conn.cursor()


def NewUser(name, pin, amount):
    cur.execute("""CREATE TABLE IF NOT EXISTS bank(
        name TEXT,
        pin INT,
        amount INT
    )""")
    cur.execute("INSERT INTO bank VALUES(?, ?, ?)", (name, pin, amount))
    #cur.execute("DROP TABLE bank")
    #conn.commit()
    cur.execute("SELECT * FROM bank")
    print(f"Your account's name: {name}\nYour account's pin: {pin}\nYour account's amount: {amount}")
    conn.commit()



def CheckUsers():
    owner = input("Are you my owner? (y/n): ").lower()
    if owner ==  'y':
        password = int(input("Then tell me the password: "))
        if password == 1275:
            choose = input("Hey owner what do you want to do today?\nCheck accounts\n: ").lower()
            if choose == 'check accounts':
                cur.execute("SELECT * FROM bank")
                infos = cur.fetchall()
                print("Name " + "\t\tPin " + "\t\tAmount")
                print("-----------" + "\t----------" + "\t-----------")
                for info in infos:
                    print(info[0] + "\t\t" + str(info[1]) + "\t\t" + str(info[2]))
            else:
                print("Bye sir have a great day!")
        else:
            print("Wrong password please continue as a normal user")
    else:
        pass



def Deposit(pin, amount):
    check = True
    for a, b, c in cur.execute("SELECT * FROM bank"):
        if b == pin:
            check = False
            val = int(c)
            dep = val + amount
            cur.execute(f"UPDATE bank SET amount = {dep} WHERE pin = {pin}")
            print(f"{amount} deposited to your account successfully\nbalance available in bank {dep}")
            conn.commit()
    if check:
        print("Invalid pin")
def Withdraw(pin, amount):
    check = True
    for a, b, c in cur.execute("SELECT * FROM bank"):
        if b == pin:
            check = False
            val = int(c)
            wit = val - amount
            cur.execute(f"UPDATE bank SET amount = {wit} WHERE pin = {pin}")
            print(f"{amount} withdrawed from your account successfully\nremaining balance in account {wit}")
            conn.commit()
    if check:
        print("Invalid pin")


def CheckBalance(pin):
    check = True
    for a, b, c in cur.execute("SELECT * FROM bank"):
        if b == pin:
            check = False
            val = int(c)
            print(f"Your account's balance: {val}")
    if check:
        print("Invalid pin")

def ForgotPin(name):
    check = True
    for a, b, c in cur.execute("SELECT * FROM bank"):
        if a == name:
            check =  False
            print(f"Hey {name} your pin is {b} please don't forget it!")
    if check:
        print("There is no account with that name!")

def running():
    CheckUsers()
    a = input("Hey, welcome to my bank\nDo you have account? (y/n): ").lower()
    if a == "y":
        b = input("Nice, so what do you want to do?\nDeposit\nWithdraw\nCheck amount\nForgot pin?\n: ").lower()
        if b == "deposit":
            pin = int(input("Okay, so tell me your pin: "))
            amount = int(input("And how much money do you want to deposit?: "))
            Deposit(pin, amount)
        elif b == "withdraw":
            pin = int(input("Please enter your pin: "))
            amount = int(input("Enter amount to withdraw: "))
            Withdraw(pin, amount)
        elif b == "check amount":
            pin = int(input("Enter your pin: "))
            CheckBalance(pin)
        elif b == "forgot pin":
            name = input("Oh, do you want to recover your account? (y/n): ").lower()
            if name == "y":
                nam = input("Okay, so please enter your account's name: ")
                ForgotPin(nam)
            else:
                print("K bye then :)")
        else:
            print("Choose a valid option!")
    elif a == "n":
        c = input("Do you want to open an account? (y/n): ").lower()
        if c == "y":
            name = input("Okay, please tell me your name: ")
            pin = r.randint(100000, 9999999)
            amount = 0
            NewUser(name, pin, amount)
        elif c == "n":
            print("okay, bye have a great day :)")
        else:
            print("Plase choose a valid option (y means yes, n means no)")
    ask = input("Do you want to do something more? (y/n)").lower()
    if ask == "y":
        running()
    elif ask == "n":
        print("Okay bye have a great day!")
    else:
        print("Please choose a valid option!")
running()