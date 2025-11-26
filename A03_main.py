"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Czedrick Marcelino"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client

from bank_account import *
from datetime import date
from client.client import Client


# 2. Create a Client object with data of your choice.

try:
    client1 = Client(2815, "Czedrick", 
           "Marcelino", "czedrick@pixell-river.com")
    
except ValueError as e:
    print(e)


# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.

try:
    chequing_account1 = ChequingAccount(2001, 2815, 100.00, 
                    date(2020, 9, 28), 1000.00, 0.12)
    
except ValueError as e:
    print(e)


try:
    savings_account1 = SavingsAccount(1001, 2815, 100.00, date(2020, 9, 28), 10.00)

except ValueError as e:
    print(e)

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).

chequing_account1.attach(client1)
savings_account1.attach(client1)



# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.

date_2 = date(1999, 9, 28)

try:
    client2 = Client(2000, "Mickey", 
           "Marcelino", "mickey@pixell-river.com")

except ValueError as e:
    print(e)

try:
    savings_account2 = SavingsAccount(1002, 2000, 150.00, date_2, 50.00)

except ValueError as e:
    print(e)


# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

try:
    chequing_account1.deposit(10000.00)
except ValueError as e:
    print(e)

try:
    chequing_account1.withdraw(10075.00)
except ValueError as e:
    print(e)

try:
    chequing_account1.deposit(200.00)
except ValueError as e:
    print(e)

try:
    savings_account1.deposit(10000.00)
except ValueError as e:
    print(e)

try:
    savings_account1.withdraw(10075.00)
except ValueError as e:
    print(e)

try:
    savings_account1.deposit(50.00)
except ValueError as e:
    print(e)

try:
    savings_account2.deposit(10000.00)
except ValueError as e:
    print(e)

try:
    savings_account2.withdraw(10125.00)
except ValueError as e:
    print(e)

try:
    savings_account2.deposit(100.00)
except ValueError as e:
    print(e)