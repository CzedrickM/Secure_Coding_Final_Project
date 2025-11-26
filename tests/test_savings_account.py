__author__ = "Czedrick Marcelino"
__version__ = "1.0.0"

from bank_account.savings_account import SavingsAccount
import unittest
from datetime import date

class TestSavingsAccount(unittest.TestCase):
    def setUp(self):
        self.savings = SavingsAccount(2815, 2000, 
                                        5000.00,
                                        date(2001, 9, 28),
                                        100.00)
    def test_init_valid_arguements_attributes_set(self):
        savings = SavingsAccount(2815, 2000, 
                                        5000.00,
                                        date(2001, 9, 28),
                                        100.00)
    
    
    # verify bankaccount attributes
        self.assertEqual(2815, savings._BankAccount__account_number)
        self.assertEqual(2000, savings._BankAccount__client_number)
        self.assertEqual(5000.00, savings._BankAccount__balance)

    # verify protected attributes
        self.assertEqual(date(2001, 9, 28), savings._date_created)

    # verify private attributes
        self.assertEqual(100.00, savings._SavingsAccount__minimum_balance)
    
    def test_init_when_minimum_balance_has_invalid_type(self):
        savings = SavingsAccount(2815, 2000, 
                                        5000.00,
                                        date(2001, 9, 28),
                                        "string")
        self.assertEqual(50.00, savings._SavingsAccount__minimum_balance)
    
    def test_get_service_charges_when_balance_greater_than_minimum_balance(self):
        expected = 0.50

        actual = self.savings.get_service_charges()

        self.assertEqual(expected, actual)
    
    def test_get_service_charges_when_balance_equal_minimum_balance(self):
        savings = SavingsAccount(2815, 2000, 
                                        100.00,
                                        date(2001, 9, 28),
                                        100.00)
        
        expected = 0.50
        
        actual = savings.get_service_charges()

        self.assertEqual(expected, actual)
    
    def test_get_service_charges_when_balance_less_than_minimum_balance(self):
        savings = SavingsAccount(2815, 2000, 
                                        50.00,
                                        date(2001, 9, 28),
                                        100.00)
        
        expected = 1.00

        actual = savings.get_service_charges()

        self.assertEqual(expected, actual)
    
    def test_str_valid_inputs_returns_formatted_string(self):
        expected = (f"Account Number: 2815 Balance: $5,000.00\n"
                +f"Minimum Balance: $100.00 Account Type: Savings")
        actual = str(self.savings)

        self.assertEqual(expected, actual)