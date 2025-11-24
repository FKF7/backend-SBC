from django.core.exceptions import ValidationError
from core.constants import Constants

def isEmailValid(email) -> bool:
    with open(Constants.EMAILS_FILE_PATH, "r") as file:
        data = file.readlines()
        for line in data:
            if email == line.strip():
                return True
        return False