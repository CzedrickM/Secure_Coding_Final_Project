__author__ = "Czedrick Marcelino"
__version__ = "1.0.1"

from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    The strategy used for overdraft limits being 
    exceeded on bank accounts.
    """

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes a new instance of the OverdraftStrategy
        class.

        Args:
            overdraft_limit(float): the limit a bank account
            can withdraw.

            overdraft_rate(float): the rate or fee that the 
            bank will charge the bank account.
        """

        self.__overdraft_limit = overdraft_limit
    
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        The method used to calculate service charges on the 
        bank account of the client.

        Args:
            account(BankAccount): the client's bank account that is
            being charged by the service fees.

        Returns:
            float: the service charge a bank account is receiving
            depending on certain conditions.
        """
        service_charge = 0
        self.account = account.balance

        if self.account >= self.__overdraft_limit:
            service_charge = self.BASE_SERVICE_CHARGE
        
        if self.account < self.__overdraft_limit:
            service_charge = (self.BASE_SERVICE_CHARGE + 
                              (self.__overdraft_limit - self.account) * 
                              self.__overdraft_rate)
            
        return service_charge