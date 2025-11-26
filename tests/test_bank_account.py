"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
__author__ = "ACE Faculty"
__version__ = "1.1.1"
__credits__ = "Czedrick Marcelino"

import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.bank_account = BankAccount(2815, 1234, 10000.25)

    def test_init_valid_arguements_attributes_set(self):
        # Arrange & Act
        bank_account = BankAccount(2815, 1234, 10000.25)

        # Assert
        self.assertEqual(2815, bank_account._BankAccount__account_number)
        self.assertEqual(1234, bank_account._BankAccount__client_number)
        self.assertEqual(10000.25, bank_account._BankAccount__balance)

    def test_init_when_balance_argument_set_to_0_when_non_numeric_balance_is_inputted(self):
        # Arrange & Act
        bank_account = BankAccount(2815, 1234, "0")

        # Assert
        self.assertEqual(0, bank_account._BankAccount__balance)

    def test_init_when_non_numeric_account_number_raises_valueerror(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            bank_account = BankAccount("2815", 1234, 10000.25)

    def test_init_when_non_numeric_client_number_raises_valueerror(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            bank_account = BankAccount(2815, "1234", 10000.25)
    
    def test_account_number_accessor_valid_account_number_returned(self):
        # Arrange 
        # done in the set up

        # Act & Assert
        self.assertEqual(2815, 
                         self.bank_account.account_number)
    
    def test_client_number_accessor_valid_account_number_returned(self):
        # Arrange
        # done in the set up

        # Act & Assert
        self.assertEqual(1234, 
                         self.bank_account.client_number)

    def test_balance_accessor_valid_balance_returned(self):
        # Arrange
        # done in the set up

        # Act & Assert
        self.assertEqual(10000.25, 
                         self.bank_account.balance)
    
    def test_update_balance_correctly_when_positive_amount_is_recieved(self):
        # Arrange
        bank_account = BankAccount(2815, 1234, 10000.25)
        amount = 100.00
        expected = 10100.25

        # Act
        bank_account.update_balance(amount)
        actual = bank_account.balance

        #Assert
        self.assertEqual(actual, expected)
    
    def test_update_balance_correctly_when_negative_amount_is_recieved(self):
        # Arrange
        bank_account = BankAccount(2815, 1234, 10000.25)
        amount = -100.00
        expected = 9900.25

        # Act
        bank_account.update_balance(amount)
        actual = bank_account.balance
        
        # Assert
        self.assertEqual(actual, expected)
    
    def test_update_balance_remains_unchanged_when_amount_is_non_numeric_returns_balance(self):
        # Arrange
        bank_account = BankAccount(2815, 1234, 10000.25)
        amount = "INVALID"
        expected = 10000.25

        # Act
        bank_account.update_balance(amount)
        actual = bank_account.balance

        #Assert
        self.assertEqual(actual, expected)

    def test_deposit_balance_is_updated_correctly_when_valid_amount_is_provided(self):
        # Arrange
        bank_account = BankAccount(2815, 1234, 10000.25)
        amount = 200.00
        expected = 10200.25

        # Act
        bank_account.deposit(amount)
        actual = bank_account.balance

        # Assert
        self.assertEqual(actual, expected)
    
    def test_deposit_balance_when_negative_amount_is_recieved_raises_valueerror(self):
        # Arrange
        bank_account = BankAccount(2815, 1234, 10000.25)
        amount = -200.00

        # Act & Assert
        with self.assertRaises(ValueError):
            bank_account.deposit(amount)

    def test_withdraw_balance_when_valid_amount_provided(self):
        # Arrange
        bank_account = BankAccount(2815, 1234, 10000.25)
        amount = 150.00
        expected = 9850.25

        # Act
        bank_account.withdraw(amount)
        actual = bank_account.balance

        # Assert
        self.assertEqual(actual, expected)
    
    def test_withdraw_when_negative_amount_is_provided_raises_valueerror(self):
        # Arrange
        bank_account = BankAccount(2815, 1234, 10000.25)
        amount = -150.00

        # Act & Assert
        with self.assertRaises(ValueError):
            bank_account.withdraw(amount)
    
    def test_withdraw_when_amount_exceeds_balance_raises_valueerror(self):
        # Arrange
        bank_account = BankAccount(2815, 1234, 10000.25)
        amount = 20000.00

        # Act & Assert
        with self.assertRaises(ValueError):
            bank_account.withdraw(amount)
    
    def test_str_valid_inputs_returns_formatted_string(self):
        # Arrange
        expected = ("Account Number: 2815 Balance: $10,000.25\n")

        # Act & Assert
        self.assertEqual(expected, str(self.bank_account))
