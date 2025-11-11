from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from core.constants.constants import Constants

def isEmailValid(email) -> bool:
    with open(Constants.EMAILS_FILE_PATH, "r") as file:
        data = file.readlines()
        for line in data:
            if email == line.strip():
                return True
        return False