__author__ = "Czedrick Marcelino"
__version__ = "3.0.0"

from abc import ABC, abstractmethod
from datetime import date
from patterns.observer.subject import Subject
from patterns.observer.observer import Observer

class BankAccount(Subject, ABC):
    """
    Bank_Account class: Maintians bank account data.
    """
    def __init__(self, account_number: int, 
                 client_number: int, 
                 balance: float, date_created: date):
        """
        Initializes the Bank_Account class attributes with argument values.
        Now inherits from the Subject class so that it can notify the client
        of any changes happening in their bank account.

        Args:
            account_number(int): The client's account number.
            client_number(int): The number used to identify the client.
            balance(float): The balance a client's bank account has.
            date_created(date): The date represented by year, month
            and day, if it is not a date, it will be set to today's date.

        Raises:
            ValueError: When account number is not numeric,
            when client number is not numeric.
        """
        super().__init__()

        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account Number must be numeric.")
        
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client Number must be numeric.")
        
        if isinstance(balance, float):
            self.__balance = balance
        else:
            self.__balance = 0
        
        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()

        self.LARGE_TRANSACTION_THRESHOLD = float(9999.99)

        self.LOW_BALANCE_LEVEL = float(50.0)

    @property
    def account_number(self) -> int:
        """
        Accessor for the account number attribute.

        Returns:
            int: The account number of the client.
        """
        return self.__account_number
    
    @property
    def client_number(self) -> int:
        """
        Accessor for the client number attribute.

        Returns:
            int: The client's client number.
        """
        return self.__client_number
    
    @property
    def balance(self) -> float:
        """
        Accessor for the balance attribute.

        Returns:
            float: The balance of the client's bank account.        
        """
        return self.__balance
    
    def update_balance(self, amount: float) -> None:
        """
        Updates the balance of the bank account of the client.

        Args:
            amount(float): A float representing the 
            amount being added to the balance.
        
        Raises:
            ValueError: When amount is invalid balance is not updated.
        """
        if not isinstance(amount, (int, float)):
            self.__balance = self.__balance
        else: 
            self.__balance += amount

        
        if self.balance < self.LOW_BALANCE_LEVEL:
            message = (f"Low balance warning ${self.__balance:,.2f}: "
                   +f"on account {self.__account_number}")
            self.notify(message)

        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            message = (f"Large transaction ${amount:,.2f}:"
                       +f" on account {self.__account_number}")
            self.notify(message)
    
    def deposit(self, amount: float) -> None:
        """
        The money that is being put into the 
        bank account of the client.

        Args:
            amount(float): A float representing the 
            deposit amount being added to the balance.

        Raises:
            ValueError: deposit amount must be numeric, 
            deposit amount must be positive.
        """
        try:

            amount = float(amount)

        except:
            raise ValueError(f"Deposit amount: ${amount}" 
                                    + f" must be numeric.")

        formatted_amount = f"{float(amount):,.2f}"

        if amount < 0:
            raise ValueError(f"Deposit amount: "
                                + f"${formatted_amount} must be positive.")
        
        else:
            self.update_balance(amount)
    
    def withdraw(self, amount: float) -> None:
        """
        The money that is being taken out of the 
        client's bank account.

        Args:
            amount(float): A float representing the 
            withdrawn amount being subtracted from the balance.
        
        Raises:
            ValueError: withdraw amount must be numeric,
            withdrawal amount must be positive,
            withdrawal amount must not exceed the account balance.
        """
        try:
            amount = float(amount)
        
        except:
            raise ValueError(f"Withdraw amount: "
                            + f"${amount} must be numeric.")

        formatted_amount = f"{float(amount):,.2f}"
        formatted_balance = (f"{self.balance:,.2f}")

        if amount < 0:
            raise ValueError(f"Withdrawal amount: "
                            + f"${formatted_amount} must be positive.")
        
        if amount > self.balance:
            raise ValueError(f"Withdrawal amount: ${formatted_amount} "
                            +f"must not exceed the account balance: "
                            +f"${formatted_balance}")
        
        else:
            self.update_balance(-amount)

    def __str__(self) -> str:
        """
        Returns a string represenation of the class instance.

        Returns:
            str: the bank account instance formatted as a string.
        """
        return (f"Account Number: {self.__account_number} "
                + f"Balance: ${self.__balance:,.2f}\n")
    
    @abstractmethod
    def get_service_charges(self) -> float:
        """
        Gets the service charge to apply.

        Impleneted in subclass(es)
        """
        pass

    def attach(self, observer: Observer) -> None:
        """
        This method is used to add a new observer
        to the subject's list of observers

        Args:
            observer(Observer): the observer that is observing
            the clients bank account.

        Returns:
            None
        """
        self._observers.append(observer)
    
    def detach(self, observer: Observer) -> None:
        """
        This method detaches the observer from the client
        so that they can change to a different client if
        needed.

        Args:
            observer(Observer): the observer that is observing
            the clients bank account.

        Returns:
            None
        """
        self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """
        This method notifies the client so that
        the client knows what is happening.

        Args:
            message(str): the notification messaged
            to the client

        Return:
            None
        """
        for observer in self._observers:
            observer.update(message)

    db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123'
    }

    def get_user_input():
    user_input = input('Enter your name: ')
    return user_input