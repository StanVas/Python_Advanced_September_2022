from advanced.error_handling.custom_exceptions import NameTooShort, MustContainAtSymbolError, InvalidDomainError
from advanced.error_handling.helpers import VALID_DOMAINS


def valid_email(email):
    try:
        name, domain = email.split('@')
    except ValueError:
        raise MustContainAtSymbolError("Email must contain @")

    try:
        name, extension = domain.split('.')
    except ValueError:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if extension not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if len(name) < 4:
        raise NameTooShort("Name must be more than 4 characters")
    return True


email = input()

while not email == 'End':
    if valid_email(email):
        print('Email is valid')
    email = input()
