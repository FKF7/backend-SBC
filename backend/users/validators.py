from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from core.constants.constants import Constants

def isEmailValid(email) -> bool:
    print(Constants.EMAILS_FILE_PATH)
    with open(Constants.EMAILS_FILE_PATH, "r") as file:
        emails = [line.strip().lower() for line in file if line.strip()]
        return email in emails