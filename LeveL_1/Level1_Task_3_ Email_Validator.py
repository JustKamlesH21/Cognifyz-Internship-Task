#Email Validator

def is_valid_email(email):
    a= email.split('@')
    if len(a) != 2:
        return False
    username, domain = a
    if not username or not domain:
        return False
    if '.' not in domain:
        return False
    if domain not in ['gmail.com', 'yahoo.com', 'hotmail.com','outlook.com',]:
        return False
    return True

email = input("Enter an email address: ")
if is_valid_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")
    print("Enter a valid email id")