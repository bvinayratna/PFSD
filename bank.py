#create a python script called bank.py with two variables and three functions balance, min-bal
#three functions are deposite, withdraw and enquery
#apply appropriate calls to the functios use local global scopes and also use functions with arguments and paramaters
balance = 100000
min_bal = 1000
print("Minimum amount to be deposited is", min_bal)
def deposite():
    money = int(input("Enter amount to deposit: "))
    if money>=min_bal:
        global balance
        balance=balance+money
    else:
        print("Deposite minimum amount of ",min_bal)
    

def withdraw():
    wmoney = int(input("Enter amount to withdraw: "))
    global balance
    balance=balance-wmoney
def enquery():
    print("HELP!!!");

deposite()
print(balance)
withdraw()
print(balance)
enquery()

