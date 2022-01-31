class bank:
 balance=0
 def __init__(self,accountno,name,accounttype,balance):
  self.accountno=accountno
  self.name=name
  self.accounttype=accounttype
  self.balance=balance

 def accountinformation(self):
  print("\n --ACCOUNT INFORMATION--\n")
  print("Account Number:",self.accountno)
  print("Account Name:",self.name)
  print("Account Type:",self.accounttype)
  print("Account Balance:",self.balance,".00")
  print("------------------------")

 def deposit(self):
  deposit=int(input("\n Enter the Amount to Deposit: "))
  print("Rs.",deposit,"Deposited Successfully...")
  print("------------------------")
  self.balance=self.balance+deposit

 def withdraw(self):
   withdraw=int(input("\n Enter the Amount to Withdraw: "))
   if withdraw > self.balance:
     print("Your Account has Insufficient Balance...")
     print("------------------------")
   else:
     self.balance=self.balance-withdraw
     print("Rs.",withdraw,"Withdrawn Successfully...")
     print("------------------------")
    
     
print("   Enter the Details of your Bank Account")
acc_no=int(input("Enter the Account Number:"))
acc_name=input("Enter the Name:")
acc_type=input("Enter the Account type-(Savings/Current):")
balance=int(input("Enter the Initial Balance:"))

obj=bank(acc_no,acc_name,acc_type,balance)

while(1):
    print("\n --WELCOME TO PYTHON BANK--")
    print("\n1.Account Information\n2.Deposit\n3.Withdraw\n4.Exit\n")
    opt=int(input("Select your option:"))
    if opt == 1:
        obj.accountinformation()
    elif opt == 2:
        obj.deposit()
    elif opt == 3:
        obj.withdraw()
    elif opt == 4:
        print("Exited")
        print("     Thank You Visit Again....\n")
        print("------------------------")
        break
    else:
        print("Invalid Option")
        print("------------------------")
