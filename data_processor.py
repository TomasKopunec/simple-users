"""
Contains the DataProcessor class which has methods for processing data 
and checking the validity of email addresses using the function from utils.py.
"""
from utils.utils import validate_email


class DataProcessor:
    def check_emails(self, emails):
        return [validate_email(email) for email in emails]