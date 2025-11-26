__author__ = "ACE Faculty"
__version__ = "3.0.0"
__credits__ = "Czedrick Marcelino"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount
from pprint import pprint

class ClientLookupWindow(LookupWindow):
    """
    A window that will find clients based on their number. 
    Inherited from LookupWindow which provides the GUI design.
    """

    def __init__(self):
        """
        Initializes the window.
        """
        super().__init__()

        self.__client_listing, self.__accounts = load_data()


        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)
        self.filter_button.clicked.connect(self.__on_filter_clicked)

    @Slot()
    def __on_lookup_client(self) -> None:
        """
        Acts as a slot for the lookup_button clicked signal.
        Obtains the Client object from the client 
        dictionary based on the
        client number entered.

        Returns:
            None
        """
        client_number_input = self.client_number_edit.text()
        try:
            client_number = int(client_number_input)
            
            self.reset_display()
        
            if client_number in self.__client_listing.keys():
                client = self.__client_listing[client_number]
                self.client_info_label.setText(f"Client Name: "
                                               +f"{client.first_name} "
                                               +f"{client.last_name}")

            if client_number not in self.__client_listing.keys():
                QMessageBox.information(self, "Not Found", 
                                        f"Client Number: "
                                        +f"{client_number} "
                                        +f"not found.")
                self.reset_display()

            for account in self.__accounts.values():
                if account.client_number == client_number:
                    account_item = \
                        QTableWidgetItem(str(account.account_number))
                    balance_item = \
                        QTableWidgetItem(f"${account.balance:,.2f}")
                    date_created_item = \
                        QTableWidgetItem(str(account._date_created))
                    account_type_item = \
                        QTableWidgetItem(account.__class__.__name__)
                    
                    account_item.setTextAlignment(Qt.AlignCenter)
                    balance_item.setTextAlignment(Qt.AlignRight 
                                                  | Qt.AlignVCenter)
                    date_created_item.setTextAlignment(Qt.AlignCenter)
                    account_type_item.setTextAlignment(Qt.AlignCenter)
                    
                    row = self.account_table.rowCount()
                    self.account_table.insertRow(row)

                    self.account_table.setItem(row, 0, account_item)
                    self.account_table.setItem(row, 1, balance_item)
                    self.account_table.setItem(row, 2, date_created_item)
                    self.account_table.setItem(row, 3, account_type_item)
                    
            self.account_table.resizeColumnsToContents()

            self.__toggle_filter(False)

        except ValueError:
            QMessageBox.information(self, "Input Error", 
                                    "The client number "
                                    "must be a numeric value.")
    
    @Slot()
    def __on_text_changed(self) -> None:
        """
        This method clears all bank account records
        from the account_table.

        Returns:
            None.
        """
        self.account_table.setRowCount(0)

    @Slot(int, int)
    def __on_select_account(self, row: int, column: int) -> None:
        """
        Identifies the account selected
        and transfer control to the Account Details window
        based on the selected account.

        Args:
            row(int): Row that has been clicked on.
            column(int): Column that has been clicked on.

        Returns:
            None.
        """
        try:
            account_number_cell = self.account_table.item(row, 0).text()
            account_number = int(account_number_cell)

            if account_number in self.__accounts:
                account = self.__accounts[account_number]
                account_details = AccountDetailsWindow(account)
                account_details.balance_updated_signal.connect(self.__update_data)
                account_details.exec_()

            else:
                QMessageBox.information(self, "No Bank Account", 
                                        "Bank Account "
                                        "selected does not exist.")
        except:
            QMessageBox.information(self, "Invalid Selection", 
                                    "Please select a valid record.")
    
    @Slot(BankAccount)
    def __update_data(self, account:BankAccount) -> None:
        """
        Updates client data in the account
        and client dictionary.

        Args:
            account(BankAccount): The client's account 
            that will be updated.
        
        Returns:
            None.
        """
        for i in range(self.account_table.rowCount()):
            if str(account.account_number) == \
                self.account_table.item(i, 0).text():
                balance_item = \
                    QTableWidgetItem(f"${account.balance:,.2f}")
                balance_item.setTextAlignment(Qt.AlignRight 
                                                  | Qt.AlignVCenter)
                self.account_table.setItem(i, 1, (balance_item))
                for updated_account in self.__accounts:
                    if updated_account == str(account.account_number):
                        account.balance = float(balance_item)
                        account = self.__accounts[account.balance]
        update_data(account)
    @Slot()
    def __on_filter_clicked(self) -> None:
        """
        Will obtain user-defined filter criteria from the filter
        combo box and the filter edit widgets based on that
        criteria. Will filter records currently displayed in the
        account table widget.

        Returns:
            None
        """
        if self.filter_button.text() == "Apply Filter":
            filter_input = self.filter_combo_box.currentIndex()
            filter_edit_input = self.filter_edit.text()
            

            for row in range(self.account_table.rowCount()):
                filter_item = self.account_table.item(row, filter_input)

                if filter_edit_input in filter_item.text():
                    self.account_table.setRowHidden(row, False)
                else:
                    self.account_table.setRowHidden(row, True)

            self.__toggle_filter(True)
        
        else:
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)
            
            self.__toggle_filter(False)
    
    def __toggle_filter(self, filter_on: bool) -> None:
        """
        Displays the filter widgets to indicate to the user
        whether or not filtering is happening.

        Args:
            filter_on(bool): When true, the filter button text will display
            'reset' to indicate that the filtering is happening
            and the user can press the reset button to 
            redisplay all records. When false, the text will become
            'Apply Filter' to tell the user that filtering is not taking
            place.
        
        Returns:
            None
        """
        self.filter_button.setEnabled(True)

        if filter_on == True:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is currently Filtered")

        else:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)

            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

            self.filter_label.setText("Data is Not Currently Filtered")