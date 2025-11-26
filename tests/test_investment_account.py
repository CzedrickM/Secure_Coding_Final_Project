__author__ = "Czedrick Marcelino"
__version__ = "1.0.0"


import unittest
from bank_account.investment_account import InvestmentAccount
from datetime import date, timedelta


class TestInvestmentAccount(unittest.TestCase):
    def setUp(self):
        self.investment_account = InvestmentAccount(2815, 2000, 
                                        5000.00,
                                        date(2001, 9, 28), 1.25)
        self.exactly_ten = date.today() - timedelta(days = 10 * 365.25)
        self.new_date = date.today() - timedelta(days = 5 * 365.25)
    
    def test_init_valid_arguements_attributes_set(self):
        investment_account = InvestmentAccount(2815, 2000, 5000.00,
                                        date(2001, 9, 28), 1.25)
        
        # verify private attributes in BankAccount
        self.assertEqual(2815, 
                investment_account._BankAccount__account_number)
        self.assertEqual(2000, 
                investment_account._BankAccount__client_number)
        self.assertEqual(5000.00, 
                investment_account._BankAccount__balance)

        # verify protected attributes in BankAccount
        self.assertEqual(date(2001, 9, 28), investment_account._date_created)

        # verify superclass private attributes
        self.assertEqual(1.25, 
                investment_account._InvestmentAccount__management_fee)

    def test_when_management_fee_has_invalid_type(self):
        investment_account = InvestmentAccount(2815, 2000, 5000.00,
                                        date(2001, 9, 28), "string")
        
        self.assertEqual(2.55, 
                         investment_account._InvestmentAccount__management_fee)
    
    def test_when_date_created_more_than_10_years_ago(self):
        expected = 0.5
        actual = self.investment_account.get_service_charges()

        self.assertEqual(expected, actual)

    def test_when_date_created_exactly_10_years_ago(self):
        investment_account = InvestmentAccount(2815, 2000, 5000.00,
                                        self.exactly_ten, 1.25)
   
        expected = 1.75
        actual = investment_account.get_service_charges()
        
        self.assertEqual(expected, actual)

    def test_when_date_created_within_last_10_years(self):
        investment_account = InvestmentAccount(2815, 2000, 5000.00,
                                        self.new_date, 1.25)
        expected = 1.75
        actual = investment_account.get_service_charges()

        self.assertEqual(expected, actual)
    
    def test_str_dispalys_waived_management_fee_when_date_created_more_than_10_years_ago(self):
        expected_management_fee = 1.25

        self._investment_account__management_fee = 1.25

        expected_message = ("Account Number: 2815 Balance: $5,000.00\n"
                    +"Date Created: 2001-09-28 Management Fee: Waived "
                    +"Account Type: Investment")
        
        actual_message = self.investment_account.__str__()
        actual_management_fee = self.investment_account._InvestmentAccount__management_fee
        
        self.assertEqual(expected_message, actual_message)
        self.assertEqual(expected_management_fee, actual_management_fee)

    def test_str_displays_when_date_created_within_last_10_years(self):
        investment_account = InvestmentAccount(2815, 2000, 5000.00,
                                        self.new_date, 1.25)

        expected_message = (f"Account Number: 2815 Balance: $5,000.00\n"
                            +f"Date Created: {self.new_date} Management Fee: $1.25 "
                            +f"Account Type: Investment")
        
        actual_message = str(investment_account)

        self.assertEqual(expected_message, actual_message)
    