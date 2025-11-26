__author__ = "Czedrick Marcelino"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    The strategy that a bank will use to implement
    fees if a certain bank account reaches a minimum balance threshold.
    """

    def __init__(self, minimum_balance: float):
        """
        Initializes a new instance of the MinimumBalanceStrategy
        class.

        Args:
            minimum_balance(float): the minimum balance
            an account can reach before a fee will be applied.
        """
        self.__minimum_balance = minimum_balance

        self.SERVICE_CHARGE_PREMIUM = float(2.0)
    
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        The method used to calculate the 
        minimum balance strategy fee

        Args:
        account(BankAccount): the client's bank account.

        Returns:
            float: the minimum balance fee a bank account is receiving
            depending on certain conditions.
        """
        service_charge = 0
        self.account = account.balance

        if self.account >= self.__minimum_balance:
            service_charge = self.BASE_SERVICE_CHARGE

        else:
            service_charge = (self.BASE_SERVICE_CHARGE 
                              * self.SERVICE_CHARGE_PREMIUM)
            
        return service_charge