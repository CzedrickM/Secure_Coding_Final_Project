__author__ = "Czedrick Marcelino"
__version__ = "2.0.0"

from email_validator import validate_email, EmailNotValidError
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import datetime


class Client(Observer):
    """
    A class that is called Client that maintains client data.
    """

    def __init__(
        self,
        client_number: int,
        first_name: str,
        last_name: str,
        email_address: str,
    ):
        """
        Initiates client attributes with arguement values.

        Args:
            client_number (int): The client number to identify the
            client.
            first_name (str): the first name of the client.
            last_name (str): the last name of the client.
            email_address (str): the email address of the client.

        Raises:
            ValueError: when the client number is non numeric,
            when the first name is blank, when the last name is blank,
            when the email address is invalid
        """

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client Number must be numeric.")

        if len(first_name.strip()) > 0:
            self.__first_name = first_name
        else:
            raise ValueError("First name cannot be blank.")

        if len(last_name.strip()) > 0:
            self.__last_name = last_name
        else:
            raise ValueError("Last name cannot be blank.")

        try:
            validated_email = validate_email(
                email_address, check_deliverability=False
            )
            self.__email_address = validated_email.normalized
        except EmailNotValidError as e:
            self.__email_address = "email@pixell-river.com"

    @property
    def client_number(self) -> int:
        """
        Accessor for client number.

        Returns:
            int: The client number of the client
        """
        return self.__client_number

    @property
    def first_name(self) -> str:
        """
        Accessor for first name.

        Returns:
            str: The first name of the client.
        """
        return self.__first_name

    @property
    def last_name(self) -> str:
        """
        Accessor for last name.

        Returns:
            str: The last name of the client.
        """
        return self.__last_name

    @property
    def email_address(self) -> str:
        """
        Accessor for the email address.

        Returns:
            str: The email address of the client.
        """
        return self.__email_address

    def __str__(self) -> str:
        """
        Returns a string representation of the class instance.

        Returns:
            str: The client instance formatted as a string.
        """
        return (
            f"{self.__last_name}, "
            + f"{self.__first_name} "
            + f"[{self.__client_number}] - "
            + f"{self.__email_address}\n"
        )

    def update(self, message: str) -> None:
        """
        Updates the state of the client's bank account.

        Args:
            message(str): The state changes in a notification
             as a string.

        Returns:
            None
        """
        subject = f"ALERT: Unusual Activity: {datetime.now()}"
        message = (f"Notification for {self.__client_number}: "
                   +f"{self.__first_name} "
                    +f"{self.__last_name}: {message}")
        
        simulate_send_email(self.__email_address, 
                            subject, message)