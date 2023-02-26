from validator_collection import validators, checkers, errors

user_email = input("What is your email address? ")
try:
    email_address = validators.email(user_email)
    if email_address:
        print("Valid")
except ValueError:
    print("Invalid")

