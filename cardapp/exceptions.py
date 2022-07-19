
from rest_framework.exceptions import APIException
class InvalidId(APIException):
    default_detail = 'Customer id or card type id is Invalid'

class IdDoesNotExist(APIException):
    default_detail = 'Customer request id does not exist'

class CardBlocked(APIException):
    default_detail = 'Card has blocked'

class AlreadyApplied(APIException):
    default_detail = 'This type of card already applied. You can not apply same card more than once'

class CanNotApply(APIException):
    default_detail = 'Sorry! You can not apply more than 3 cards'

class CardIdDoesNotExist(APIException):
    default_detail = 'Specified card id does not exist'
