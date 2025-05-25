account_balance=1000
pin=7674  #using default pin
accountnumber=1234567891
def atm_services():
          print(" =====atm_services===== ")
          print("1.credit")
          print("2.withdraw")
          print("3.mini statement/balance enquary")
          print("4.pin change")
          print("5.exit")
        
def choice():
          choice=input("choose the options:")
          if choice in ['1','2','3','4','5']:
            return choice
          else:
              return 'choose correct opption'
def credit():
    global account_balance
    global pin
    password=int(input('enter the 4 digit pin:'))
    if password!=pin:
        print('enter the correct pin to credit')
    else:
        credit_amount=float(input('enter the credit_amount:'))
        if credit_amount<=0:
         print('enter the correct amount')
        else:
         account_balance+=credit_amount
         print(f'Rs{credit_amount} are credited to your account')
        
def withdraw():
    global account_balance
    global pin
    password=int(input('enter the password:'))
    if pin!=password:
        print("enter the correct pin to withdraw")
    else:
        debit_amount=float(input("enter the amount to withdraw:"))
        if debit_amount<=0 :
            print('enter the correct amount')
        else:
            if debit_amount>account_balance:
                print("you have insufficient balance in your bank")
            else:
                account_balance-=debit_amount
                print(f'Rs{debit_amount} is debited from your bank')
            
def mini_statement():
    password=int(input("enter 4 digit password for mini_starement:"))
    if password!=pin:
        print("enter correct password")
    else:
        print(f'Rs{account_balance} is available in your account')
        
def pinchange():
    global accountnumber
    global pin
    password=int(input('enter your 4 digit pin to change pin:'))
    if password != pin:
        print('enter the correct pin')
    else:
        account_number=int(input("enter the account number:"))
        if account_number == accountnumber:
            newpin=int(input("enter your new 4 digit pin:"))
            pin=newpin
            print(f"your pin has updated successfully")
        else:
            print("enter your correct account number")
        
print('-'*30)         
print("welcome to SBI atm services")
print("-"*30)
while True:
    atm_services()
    option=choice()
    if option=='1':
        credit()
    elif option == '2':
        withdraw()
    elif option == '3':
        mini_statement()
    elif option == '4':
        pinchange()
    elif option == '5':
        print("thank you for using SBI ATM services")
        print("have a good day")
        print('-'*30)
        break
