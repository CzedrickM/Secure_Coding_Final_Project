""""
Description: A client program written to verify correctness of 
the BankAccount and Client classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.2.0"
__credits__ = "Czedrick Marcelino"

from bank_account.bank_account import BankAccount
from client.client import Client

def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Client classes.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates a valid instance of the Client class.
    # Use your own unique valid values for the inputs to the class.

    try:
        client_account = \
            Client(1010, "Clark", "Susan", 
                   "susanclark@pixell-river.com")

    except ValueError as e:
        print(e)

    # 2. Declare a BankAccount object with an initial value of None.

    bank_client = None

    # 3. Using the bank_account object declared in step 2, code a statement 
    # to instantiate the BankAccount object.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use a floating point value for the balance. 
    
    try:
        bank_client = \
            BankAccount(2815, 1010, 10000.25)

    except ValueError as e:
        print(e)

    # 4. Code a statement which creates an instance of the BankAccount class.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use an INVALID value (non-float) for the balance. 

    try: 
        bank_account = \
            BankAccount(2815, 1010, "INVALID")
    
    except ValueError as e:
        print(e)

    # 5. Code a statement which prints the Client instance created in step 1. 
    # Code a statement which prints the BankAccount instance created in step 3.

    try:
        print(client_account)
    
    except ValueError as e:
        print(e)
    
    try: 
        print(bank_client)
    
    except ValueError as e:
        print(e)
    
    # 6. Attempt to deposit a non-numeric value into the BankAccount create in step 3. 
    try:
        amount = "INVALID"
        bank_client.deposit(amount)

    except ValueError as e:
        print(e)

    # 7. Attempt to deposit a negative value into the BankAccount create in step 3. 
    
    try:
        amount = -100.00
        bank_client.deposit(amount)
    
    except ValueError as e:
        print(e)

    # 8. Attempt to withdraw a valid amount of your choice from the BankAccount create in step 3. 

    try:
        amount = 150.00
        bank_client.withdraw(amount)

    except ValueError as e:
        print(e)

    # 9. Attempt to withdraw a non-numeric value from the BankAccount create in step 3. 

    try:
        amount = "INVALID"
        bank_client.withdraw(amount)

    except ValueError as e:
        print(e)

    # 10. Attempt to withdraw a negative value from the BankAccount create in step 3. 

    try:
        amount = -150.00
        bank_client.withdraw(amount)
    
    except ValueError as e:
        print(e)

    # 11. Attempt to withdraw a value from the BankAccount create in step 3 which 
    # exceeds the current balance of the account. 

    try:
        amount = 20000.00
        bank_client.withdraw(amount)
    except ValueError as e:
        print(e)

    # 12. Code a statement which prints the BankAccount instance created in step 3. 

    try:
        print(bank_client)
    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()