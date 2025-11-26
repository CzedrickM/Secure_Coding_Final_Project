__author__ = "Czedrick Marcelino"
__version__ = "1.0.0"

from patterns.strategy.overdraft_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    The strategy that will be used to implement
    management fees on a bank account.
    """

    def __init__(self, date_created: date, management_fee: float):
        """
        Initializes a new instance of the ManagementFeeStrategy
        class.

        Args:
            date_created(date): the date the bank account
            was created.
            management_fee(float): the fee that will be 
            implemented on the clients bank account.
        """
        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

        self.__date_created = date_created

        self.__management_fee = management_fee
        

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        The method used to calculate the management fee.

        Args:
            account(BankAccount): the client's bank account.

        Returns:
            float: the management fee a bank account is receiving
            depending on certain conditions.
        """
        service_charge = 0
        self.account = account.balance

        if self.__date_created < self.TEN_YEARS_AGO:
            service_charge = self.BASE_SERVICE_CHARGE

        else:
            service_charge = (self.BASE_SERVICE_CHARGE + 
                              self.__management_fee)
        
        return service_charge
