# 5a. Email Validation using RegEx
import re

# Open and read the file
with open("data.txt", "r") as file:
    text = file.read()

# Regular Expressions
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_pattern = r'\b\d{10}\b'
date_pattern = r'\b\d{2}[/-]\d{2}[/-]\d{4}\b'

# Extract data
emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)
dates = re.findall(date_pattern, text)

# Display results
print("Extracted Email IDs:")
for email in emails:
    print(email)

print("\nExtracted Phone Numbers:")
for phone in phones:
    print(phone)

print("\nExtracted Dates:")
for date in dates:
    print(date)

# 5b. Salary Calculation using Class Methods
class Employee:
    base_pay = 50000  # Class variable

    @classmethod
    def calculate_salary(cls, bonus):
        return cls.base_pay + bonus

total = Employee.calculate_salary(5000)
print(f"Total Salary: ${total}")








