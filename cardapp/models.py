from django.db import models
class CustomerModel(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.CharField(max_length=40)
    address=models.TextField()

class CardTypesModel(models.Model):
    card_type_id = models.AutoField(primary_key=True)#card id
    name=models.CharField(max_length=30)
    limit = models.IntegerField()
    description=models.CharField(max_length=100)

class RequestModel(models.Model):
    id = models.AutoField(primary_key=True)
    card_type_id = models.IntegerField()
    customer_id = models.IntegerField()
    status=models.IntegerField()#
    remark=models.CharField(max_length=100)

class LimitIncreaseRequestModel(models.Model):
    id = models.AutoField(primary_key=True)
    card_type_id = models.IntegerField()
    final_limit = models.IntegerField()
    status=models.IntegerField()
    remark=models.CharField(max_length=100)

class CardDetailsModel(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    card_type_id = models.IntegerField()#card id
    card_number=models.IntegerField()
    card_limit=models.IntegerField()
    issued_date=models.DateField()
    expiration_date=models.DateField()
    is_blocked=models.BooleanField(default=False)
