__author__ = "Czedrick Marcelino"
__version__ = "1.0.1"

import unittest
from bank_account.chequing_account import ChequingAccount
from datetime import date

class TestChequingAccount(unittest.TestCase):
    def setUp(self):
        self.chequing = ChequingAccount(2815, 2000, 5000.00,
                                        date(2001, 9, 28),
                                        -50.00, 0.12)
    
    def test_init_valid_arguments_attributes_set(self):
        chequing_account = ChequingAccount(2815, 2000, 5000.00,
                                        date(2001, 9, 28),
                                        -50.00, 0.12)
        
        # verify super class private attributes
        self.assertEqual(-50.00, chequing_account._ChequingAccount__overdraft_limit)
        self.assertEqual(0.12, chequing_account._ChequingAccount__overdraft_rate)

        # verify protected attributes
        self.assertEqual(date(2001, 9, 28), chequing_account._date_created)
        
        # verify private attributes in BankAccount
        self.assertEqual(2815, chequing_account._BankAccount__account_number)
        self.assertEqual(2000, chequing_account._BankAccount__client_number)
        self.assertEqual(5000.00, chequing_account._BankAccount__balance)

    def test_init_when_overdraft_limit_has_invalid_type(self):
        chequing_account = ChequingAccount(2815, 2000, 5000.00,
                                        date(2001, 9, 28),
                                        "string", 0.12)
        self.assertEqual(-100, chequing_account._ChequingAccount__overdraft_limit)

    def test_init_when_overdraft_rate_has_invalid_type(self):
        chequing_account = ChequingAccount(2815, 2000, 5000.00,
                                        date(2001, 9, 28),
                                        -50.00, "string")
        self.assertEqual(0.05, chequing_account._ChequingAccount__overdraft_rate)
    
    # Ask question about date("") if it has to be there to recognzie we are passing it through the function
    def test_init_when_date_created_has_invalid_type(self):
        chequing_account = ChequingAccount(2815, 2000, 5000.00,
                                        "2001, 9, 28",
                                        -50.00, 0.12)
        self.assertEqual(date.today(), chequing_account._date_created)
    
    def test_get_service_charges_when_balance_greater_than_overdraft_limit(self):
        expected = 0.50
        actual = self.chequing.get_service_charges()

        self.assertEqual(expected, actual)

    def test_get_service_charges_when_balance_less_than_overdraft_limit(self):
        chequing_account = ChequingAccount(2815, 2000, 5000.00,
                                        date(2001, 9, 28),
                                        100000.00, 0.12)
        expected = 11400.5
        actual = chequing_account.get_service_charges()

        self.assertEqual(expected, actual)
    
    def test_get_service_charges_when_balance_equals_overdraft_limit(self):
        chequing_account = ChequingAccount(2815, 2000, 5000.00,
                                        date(2001, 9, 28),
                                        5000.00, 0.12)
        
        expected = 0.50
        actual = chequing_account.get_service_charges()

        self.assertEqual(expected, actual)
    
    def test_str_returns_appropriate_value_based_on_attribute_values(self):
        expected = ("Account Number: 2815 Balance: $5,000.00\n"
                    +"Overdraft Limit: $-50.00 Overdraft Rate: "
                    +"12.00% Account Type: Chequing")
        
        self.assertEqual(expected, str(self.chequing))