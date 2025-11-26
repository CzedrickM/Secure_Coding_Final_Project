__author__ = "Czedrick Marcelino"
__version__ = "2.0.0"

from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.overdraft_strategy import OverdraftStrategy


class ChequingAccount(BankAccount):
    """
    ChequingAccount class: Maintains the ChequingAccount data.
    """

    def __init__(self, account_number: int, 
                 client_number: int, 
                 balance: float, date_created: date, 
                 overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the Bank_Account class attributes with argument values.

        Args:
            account_number(int): The client's account number.
            client_number(int): The number used to identify the client.
            balance(float): The balance a client's bank account has.
            date_created(date): The date represented by year, month
            and day.
            overdraft_limit(float): The maximum amount a balance 
            be overdrawn.
            overdraft_rate(float): The rate to which 
            overdraft fees will be applied.

        Raises:
            ValueError: When account number is not numeric,
            when client number is not numeric.
        """
        super().__init__(account_number, client_number, balance,
                         date_created)
        
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except:
            self.__overdraft_limit = -100
        
        try:
            self.__overdraft_rate = float(overdraft_rate)
        except:
            self.__overdraft_rate = 0.05

        self.__strategy = OverdraftStrategy(self.__overdraft_limit, 
                                            self.__overdraft_rate)
    
    def __str__(self) -> str:
        """
        Returns a string represenation of the class instance.

        Returns:
            str: the chequing account instance formatted as a string.
        """
        message = super().__str__()
        message += (f"Overdraft Limit: ${self.__overdraft_limit:,.2f} "
                    +f"Overdraft Rate: {self.__overdraft_rate * 100:,.2f}% "
                    +f"Account Type: Chequing")
        return message
    
    def get_service_charges(self) -> float:
        """
        Calculates the service charges on the clients bank account based
        on certain conditions.
        It will return the calculated service charge that a bank account
        will incur. This will be handled using the OverdraftStrategy.

        Returns:
            float: the calculated bank account after the service charge 
            based on the condition met.
        """
        service_charge = self.__strategy.calculate_service_charges(self)
        return service_charge
    