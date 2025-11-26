"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.1.0"
__credits__ = "Czedrick Marcelino"

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime

from bank_account import *

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.

try:
    chequing_1 = ChequingAccount(2815, 2000, 5000.00,
                                        date(2001, 9, 28),
                                        100000.00, 0.12)
except ValueError as e:
    print(e)

# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.

print(chequing_1)
print(f"Service Charge: ${chequing_1.get_service_charges()}\n")


# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
try:
    chequing_1.deposit(100000.00)
    print(chequing_1)
    print(f"Service Charge: ${chequing_1.get_service_charges()}\n")

except ValueError as e:
    print(e)

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.

try:
    savings_1 = SavingsAccount(2815, 2000, 5000.00, 
                             date(2001, 9, 28), 100.00)

except ValueError as e:
    print(e)

# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.

print(savings_1)
print(f"Service Charge: ${savings_1.get_service_charges()}\n")


# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.

try:
    savings_1.withdraw(4950.00)
    print(savings_1)
    print(f"Service Charge: ${savings_1.get_service_charges()}\n")

except ValueError as e:
    print(e)

print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.

try:
    investment_1 = InvestmentAccount(2815, 2000, 5000.00, 
                                   date(2001, 9, 28), 1.25)

except ValueError as e:
    print(e)

# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.

print(investment_1)
print(f"Service Charge: ${investment_1.get_service_charges()}\n")

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.

try:
    investment_2 = InvestmentAccount(2815, 2000, 5000.00, 
                                   date(2020, 9, 28), 1.25)

except ValueError as e:
    print(e)

# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.

print(investment_2)
print(f"Service Charge: ${investment_2.get_service_charges()}\n")

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
try:
    chequing_1.withdraw(chequing_1.get_service_charges())
    savings_1.withdraw(savings_1.get_service_charges())
    investment_1.withdraw(investment_1.get_service_charges())
    investment_2.withdraw(investment_2.get_service_charges())

except ValueError as e:
    print(e)

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.

print(f"{chequing_1}\n")
print(f"{savings_1}\n")
print(f"{investment_1}\n")
print(f"{investment_2}\n")