__author__ = "Czedrick Marcelino"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    This class will be used to define the interface
    for all concrete observers that need to be notified of
    changes in the subject.
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """
        This method will be used to implement in the conrete classes
        to notify observers when there are changes to the subject.

        Args:
            message(str): the message in a string that will
            display when there has been an update

        Returns:
            None
        """
        pass