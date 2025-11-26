__author__ = "Czedrick Marcelino"
__version__ = "2.0.0"

from bank_account.bank_account import BankAccount
from datetime import date, timedelta
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):
    """
    InvestmentAccount class: maintains the InvestmentAccount data.
    """

    def __init__(self, account_number: int, 
                 client_number: int, 
                 balance: float, date_created: date, 
                 management_fee: float):
        """
        Initializes the InvestmentAccount class attributes with 
        arguement values.

        Args:
            account_number(int): The client's account number.
            client_number(int): The number used to identify the client.
            balance(float): The balance a client's bank account has.
            date_created(date): The date represented by year, month
            and day, if it is not a date, it will be set to today's date.
            management_fee(float): a float that stores a flat-rate fee
            the bank charges for managing an investment account.
            If management_fee is a float, it will return as the given
            amount. Otherwise, it will be set to 2.55

        Raises:
            ValueError: When account number is not numeric,
            when client number is not numeric.
        """
        super().__init__(account_number, 
                         client_number, balance, date_created)
        
        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

        try:
            self.__management_fee = float(management_fee)
        except:
            self.__management_fee = 2.55

        self.__strategy = ManagementFeeStrategy(self._date_created,
                                                 self.__management_fee)
        
    def __str__(self) -> str:
        """
        Returns a string representation of a InvestmentAccount object

        Returns:
            investment_account as a string.
        """
        message = super().__str__()

        if self._date_created > self.TEN_YEARS_AGO:
            message += (f"Date Created: {self._date_created} "
                        + f"Management Fee: ${self.__management_fee:,.2f} "
                        + f"Account Type: Investment")
        else:
            message += (f"Date Created: {self._date_created} "
                        +f"Management Fee: Waived "
                        +f"Account Type: Investment")
        return message
    
    def get_service_charges(self) -> float:
        """
        Calculates the service charges on the clients bank account based
        on certain conditions.
        If date created of the InvestmentAccoutn instance 
        is a date more than 10 years ago,
        the service charge is equal to BASE_SERVICE_CHARGE.
        If this is not the case, service charge is equal to 
        BASE_SERVICE_CHARGE + management fee.
        Uses the management fee strategy to call the method.

        Returns:
            float: the calculated service 
            charge based on the condition met.
        """
        service_charge = self.__strategy.calculate_service_charges(self)
        return service_charge