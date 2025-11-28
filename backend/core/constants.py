from django.db import models
from django.conf import settings

class Constants():
    EMAILS_FILE_PATH = f"{settings.BASE_DIR}/core/data/emails.txt"

class RequestStatus(models.IntegerChoices):
    PENDING = 1, "Pending"
    APPROVED = 2, "Approved"
    REJECTED = 3, "Rejected"
    EXPIRED = 4, "Expired"
    
class Roles(models.IntegerChoices):
    DIRECTORY_MEMBER = 1, "Membro da Diretoria"
    COUNCIL_MEMBER = 2, "Membro do Conselho"
    EDUCATION_COMMISSION = 3, "Comissão de Educação"
    REGIONAL_SECRETARY = 4, "Secretário Regional"
    SPECIAL_COMMISSION_COORDINATOR = 5, "Coordenador de Comissão Especial"
    OTHERS = 6, "Outros"