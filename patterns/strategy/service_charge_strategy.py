__author__ = "Czedrick Marcelino"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    Interface to be applied to subclasses.
    This will be used to apply service charges
    based on conditions met by each bank account.
    """
    BASE_SERVICE_CHARGE = float(0.50)

    @abstractmethod
    def calculate_service_charges(self, 
                                  account: BankAccount) -> float:
        """
        abstract method to be implemented in bank account depending on
        strategy being employed.

        Args:
            account(BankAccount): the account that will be charged
            by the service charge.

        Returns:
            float: the service charge amount.
        """
        pass