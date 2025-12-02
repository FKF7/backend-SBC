from django.db import models
from django.conf import settings

class Constants():
    EMAILS_FILE_PATH = f"{settings.BASE_DIR}/core/data/emails.txt"

class RequestStatus(models.IntegerChoices):
    PENDING = 1, "Pending"
    AWAITING_PAYMENT = 2, "Aguardando Pagamento"
    APPROVED = 3, "Approved"
    REJECTED = 4, "Rejected"
    EXPIRED = 5, "Expired"

class Roles(models.IntegerChoices):
    DIRECTORY_MEMBER = 1, "Membro da Diretoria"
    COUNCIL_MEMBER = 2, "Membro do Conselho"
    EDUCATION_COMMISSION = 3, "Comissão de Educação"
    REGIONAL_SECRETARY = 4, "Secretário Regional"
    SPECIAL_COMMISSION_COORDINATOR = 5, "Coordenador de Comissão Especial"
    OTHERS = 6, "Outros"
    
class TravelTime(models.IntegerChoices):
    MORNING = 1, "Manhã"
    AFTERNOON = 2, "Tarde"
    EVENING = 3, "Noite"
    NIGHT = 4, "Madrugada"

class RoomType(models.IntegerChoices):
    SINGLE = 1, "Individual"
    DOUBLE = 2, "Duplo"
    GUEST = 3, "Com Convidado"