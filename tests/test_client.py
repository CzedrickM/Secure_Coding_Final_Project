"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""
__author__ = "ACE Faculty"
__version__ = "1.1.0"
__credits__ = "Czedrick Marcelino"


import unittest
from client.client import Client

class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client(1010, "Clark", "Susan", 
                             "susanclark@pixell-river.com")

    def test_init_valid_arguements_attributes_set(self):
        # Arrange & Act
        client = Client(1010, "Clark", "Susan", 
                        "susanclark@pixell-river.com")

        # Assert
        self.assertEqual(1010, client._Client__client_number)
        self.assertEqual("Clark", client._Client__first_name)
        self.assertEqual("Susan", client._Client__last_name)
        self.assertEqual("susanclark@pixell-river.com", 
                         client._Client__email_address)

    def test_init_non_numeric_client_number_raises_valueerror(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            client = Client("1010", "Clark", 
                            "Susan", "susanclark@pixell-river.com")

    def test_init_blank_first_name_raises_valueerror(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            client = Client(1010, "", "Susan", 
                            "susanclark@pixell-river.com")
    
    def test_init_blank_last_name_raises_valueerror(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            client = Client(1010, "Clark", "", 
                            "susanclark@pixell-river.com")
    
    def test_init_invalid_email_address_set_to_default_value(self):
        # Arrange, Act 
        client = Client(1010, "Clark", "Susan", "INVALID")
        
        # Assert
        self.assertEqual("email@pixell-river.com", 
                         client._Client__email_address)
    
    def test_valid_client_number_accessor_returned(self):
        # Arrange
        # I have done this in set up

        # Act and Assert
        self.assertEqual(1010, self.client.client_number)
    
    def test_valid_first_name_accessor_returned(self):
        # Arrange
        # I have done this in set up

        # Act and Assert
        self.assertEqual("Clark", self.client.first_name)

    def test_valid_last_name_accessor_returned(self):
        # Arrange
        # I have done this set up

        # Act and Assert
        self.assertEqual("Susan", self.client.last_name)

    def test_valid_email_address_accessor_returned(self):
        # Arrange
        # I have done this in set up

        # Act and Assert
        self.assertEqual("susanclark@pixell-river.com", 
                         self.client.email_address)
    
    def test_str_valid_inputs_returns_formatted_string(self):
        # Arrange
        expected = ("Susan, Clark [1010] - susanclark@pixell-river.com\n")

        # Act and Assert
        self.assertEqual(expected, str(self.client))