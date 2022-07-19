

from rest_framework.serializers import ModelSerializer
from cardapp.models import CustomerModel,CardTypesModel,RequestModel,LimitIncreaseRequestModel,CardDetailsModel
class CustomerSerializer(ModelSerializer):
    class Meta:
        model=CustomerModel
        fields='__all__'

class CardTypesSerializer(ModelSerializer):
    #student=StudentSerializer(read_only=True,many=True)
    class Meta:
        model=CardTypesModel
        fields='__all__'

class RequestSerializer(ModelSerializer):
    class Meta:
        model=RequestModel
        fields='__all__'

class LimitIncreaseRequestSerializer(ModelSerializer):
    class Meta:
        model=LimitIncreaseRequestModel
        fields='__all__'

class CardDetailsSerializer(ModelSerializer):
    class Meta:
        model=CardDetailsModel
        fields='__all__'
