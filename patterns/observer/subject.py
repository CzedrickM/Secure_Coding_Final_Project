__author__ = "Czedrick Marcelino"
__version__ = "1.1.0"

from abc import ABC, abstractmethod
from patterns.observer.observer import Observer

class Subject(ABC):
    """
    This class maintains a list of its observers and notifying them 
    of state changes or events
    """

    def __init__(self) -> None:
        """
        Intiailizes a new instance of the Subject class.

        Returns:
            None
        """
        
        observers = []
        self._observers = observers

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        This method will attach the observer to the client
        so that they can notify the client if they need to.

        Args:
            observer(Observer): the observer that is observing
            the clients bank account.

        Returns:
            None
        """
        pass
    
    @abstractmethod
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
        pass

    @abstractmethod
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
        pass