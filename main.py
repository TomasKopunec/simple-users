# main.py
"""
The main script that creates a User instance and processes some data using the DataProcessor class.
"""
from user import User
from data_processor import DataProcessor

def main():
    user = User("John Doe", "john.doe@example.com")
    print(user)
    
    processor = DataProcessor()
    emails = ['invalid', 'bob@company', 'alice@gmail.com', 'tomino123@yahoo.com']
    result = processor.check_emails(emails)
    print(f"Email validation output: {result}")

if __name__ == "__main__":
    main()
