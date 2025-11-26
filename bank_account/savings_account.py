__author__ = "Czedrick Marcelino"
__version__ = "2.0.0"

from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    """
    SavingsAccount class that maintains SavingsAccount data.

    """
    
    def __init__(self, account_number: int, 
                 client_number: int, 
                 balance: float, date_created: date, 
                 minimum_balance: float):
        """
        
        Initializes the SavingsAccount class 
        attributes with arguement values.
        
        Args:
            account_number(int): The client's account number.
            client_number(int): The number used to identify the client.
            balance(float): The balance a client's bank account has.
            date_created(date): The date represented by year, month
            and day, if it is not a date, it will be set to today's date.
            minimum_balance(float): the minimum value a balance can be
            before further service charges are applied.

        Raises:
            ValueError: When account number is not numeric,
            when client number is not numeric.

            """
        
        super().__init__(account_number, 
                         client_number, balance, date_created)
        
        try:
            self.__minimum_balance = float(minimum_balance)
        except:
            self.__minimum_balance = 50
        
        self.__strategy = MinimumBalanceStrategy(self.__minimum_balance)

    def __str__(self) -> str:
        """
        Returns a string representation of the SavingsAccount object.

        Returns:
            str: the savings account instance formatted as a string.
        """
        message = super().__str__()
        message += (f"Minimum Balance: "
                    +f"${self.__minimum_balance:,.2f} "
                    +f"Account Type: Savings")
        return message
    
    def get_service_charges(self) -> float:
        """
        Calculates the service charge on client's bank 
        accounts based on conditions met.
        If clients balance is greater or equal to the minimum balance,
        service charge is set to BASE_SERVICE_CHARGE.
        If client's balance is less, then the service charge will be
        calculated using a specific formula.

        Returns:
            float: the calculated service charge.
        """
        service_charge = self.__strategy.calculate_service_charges(self)
        return service_charge
