__author__ = "ACE Faculty"
__version__ = "2.0.0"
__credits__ = "Czedrick Marcelino"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    balance_updated_signal = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()
        try:
            if isinstance(account, BankAccount):
                self.__account = copy.deepcopy(account)
                self.account_number_label.setText(str(self.__account.account_number))
                self.balance_label.setText(str(f"${self.__account.balance:,.2f}"))

                self.deposit_button.clicked.connect(self.__on_apply_transaction)
                self.withdraw_button.clicked.connect(self.__on_apply_transaction)
                self.exit_button.clicked.connect(self.__on_exit)
        
        except ValueError:
            self.reject()



    @Slot()
    def __on_apply_transaction(self) -> None:
        """
        A method that attempts to perform
        a transaction using the amount entered 
        into the corresponding BankAccount.
        It will update balanceLabel if process is a success,
        otherwise, issues a QMessageBox if transaction is
        unsuccessful.
        """
        try:
            transaction_amount = float(self.transaction_amount_edit.text())
            try:
                if self.sender() == self.deposit_button:
                    transaction_type = "Deposit"
                    self.__account.deposit(transaction_amount)
                
                elif self.sender() == self.withdraw_button:
                    transaction_type = "Withdraw"
                    self.__account.withdraw(transaction_amount)

                self.balance_label.setText(f"${self.__account.balance:,.2f}")
                self.transaction_amount_edit.setText("")
                self.transaction_amount_edit.setFocus()

                self.balance_updated_signal.emit(self.__account)
            except ValueError as e:
                QMessageBox.information(self, f"{transaction_type} Failed", f"{e}")
        except:
            QMessageBox.information(self, "Invalid Data", 
                                    "Amount must be numeric.")
            self.transaction_amount_edit.setFocus()
            return
        

    @Slot()
    def __on_exit(self) -> None:
        """
        Exits out the window
        """
        self.close()