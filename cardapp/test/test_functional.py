from rest_framework.test import APITestCase
from cardapp.models import *
from cardapp.test.TestUtils import TestUtils
class CreditCardAppAPIFunctionalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        CustomerModel.objects.create(name="Venu",phone=9951849651,email="venu.gopal@iiht.com",address="Hyderabad")
        CardTypesModel.objects.create(name="Amazon",limit=20000,description="This is amazon card")
        RequestModel.objects.create(card_type_id=1,customer_id=1,status=0,remark="None")
        CardDetailsModel.objects.create(customer_id=2,card_type_id=2,card_number=67890,card_limit=25000,issued_date="2021-11-01",expiration_date="2026-11-01",is_blocked="False")
        LimitIncreaseRequestModel.objects.create(card_type_id=1,final_limit=35000,status=0,remark="Please increase the limit of my card")
        LimitIncreaseRequestModel.objects.create(card_type_id=2,final_limit=35000,status=0,remark="Please increase the limit of my card")

    def test_add_cards(self):
        url='http://127.0.0.1:8000/addcardtypes/'
        data=   {
        "name":"Flipkart",
        "limit":15000,
        "description": "This is flipkart card"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("TestAddCards", True, "functional")
            print("TestAddCards = Passed")
        else:
            test_obj.yakshaAssert("TestAddCards", False, "functional")
            print("TestAddCards = Failed")

    def test_list_all_card_types(self):
        url='http://127.0.0.1:8000/listallcardtypes/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestListAllCardTypes", True, "functional")
            print("TestListAllCardTypes = Passed")
        else:
            test_obj.yakshaAssert("TestListAllCardTypes", False, "functional")
            print("TestListAllCardTypes = Failed")

    def test_customer_registration(self):
        url='http://127.0.0.1:8000/customerregistration/'
        data=      {
        "name":"Venu",
        "phone":9951849651,
        "email": "venu.gopal@iiht.com",
        "address": "Hyderabad"
    }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("TestCustomerRegistration", True, "functional")
            print("TestCustomerRegistration = Passed")
        else:
            test_obj.yakshaAssert("TestCustomerRegistration", False, "functional")
            print("TestCustomerRegistration = Failed")

    def test_apply_for_card(self):
        url='http://127.0.0.1:8000/applyforcard/?customer_id=1&card_type_id=1'
        data=         {
        "card_type_id":1,
        "customer_id":1,
        "status":0,
        "remark":"None"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("TestApplyForCard", True, "functional")
            print("TestApplyForCard = Passed")
        else:
            test_obj.yakshaAssert("TestApplyForCard", False, "functional")
            print("TestApplyForCard = Failed")

    def test_accept_card_request(self):
        url='http://127.0.0.1:8000/acceptcardrequest/1/'
        data= {
        "customer_id":1,
        "card_type_id":1,
        "card_number":12345,
        "card_limit":15000,
        "issued_date":"2021-11-01",
        "expiration_date":"2026-11-01",
        "is_blocked":"False"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("TestAcceptCardRequest", True, "functional")
            print("TestAcceptCardRequest = Passed")
        else:
            test_obj.yakshaAssert("TestAcceptCardRequest", False, "functional")
            print("TestAcceptCardRequest = Failed")

    def test_list_all_card_requests(self):
        url='http://127.0.0.1:8000/listallcardrequests/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestListAllCardRequests", True, "functional")
            print("TestListAllCardRequests = Passed")
        else:
            test_obj.yakshaAssert("TestListAllCardRequests", False, "functional")
            print("TestListAllCardRequests = Failed")

    def test_list_blocked_cards(self):
        url='http://127.0.0.1:8000/listallblockedcards/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestListBlockedCards", True, "functional")
            print("TestListBlockedCards = Passed")
        else:
            test_obj.yakshaAssert("TestListBlockedCards", False, "functional")
            print("TestListBlockedCards = Failed")

    def test_request_for_increase_limit(self):
        url='http://127.0.0.1:8000/applyforcard/?customer_id=1&card_type_id=1'
        data=         {
        "card_type_id":1,
        "customer_id":1,
        "status":0,
        "remark":"Please increase limit"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("TestRequestForIncreaseLimit", True, "functional")
            print("TestRequestForIncreaseLimit = Passed")
        else:
            test_obj.yakshaAssert("TestRequestForIncreaseLimit", False, "functional")
            print("TestRequestForIncreaseLimit = Failed")

    def test_list_all_limit_increase_requests(self):
        url='http://127.0.0.1:8000/listlimitincreaserequests/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestListAllLimitIncreaseRequests", True, "functional")
            print("TestListAllLimitIncreaseRequests = Passed")
        else:
            test_obj.yakshaAssert("TestListAllLimitIncreaseRequests", False, "functional")
            print("TestListAllLimitIncreaseRequests = Failed")

    def test_get_status_of_card(self):
        url='http://127.0.0.1:8000/getstatus/1/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetStatusOfCard", True, "functional")
            print("TestGetStatusOfCard = Passed")
        else:
            test_obj.yakshaAssert("TestGetStatusOfCard", False, "functional")
            print("TestGetStatusOfCard = Failed")

    def test_block_card(self):
        url='http://127.0.0.1:8000/blockcard/2/'
        data={
        "is_blocked":"True"
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestBlockCard", True, "functional")
            print("TestBlockCard = Passed")
        else:
            test_obj.yakshaAssert("TestBlockCard", False, "functional")
            print("TestBlockCard = Failed")

    def test_un_block_card(self):
        url='http://127.0.0.1:8000/blockcard/2/'
        data={
        "is_blocked":"False"
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestUnBlockCard", True, "functional")
            print("TestUnBlockCard = Passed")
        else:
            test_obj.yakshaAssert("TestUnBlockCard", False, "functional")
            print("TestUnBlockCard = Failed")

    def test_reject_card_request(self):
        url='http://127.0.0.1:8000/rejectcardrequest/1/'
        data={
        "remark":"Reuest for card is rejected"
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestRejectCardRequest", True, "functional")
            print("TestRejectCardRequest = Passed")
        else:
            test_obj.yakshaAssert("TestRejectCardRequest", False, "functional")
            print("TestRejectCardRequest = Failed")

    def test_accept_limit_increase_request(self):
        url='http://127.0.0.1:8000/acceptincreasecardlimitrequest/2/'
        data={
        "card_limit":35000
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestAcceptLimitIncreaseRequest", True, "functional")
            print("TestAcceptLimitIncreaseRequest = Passed")
        else:
            test_obj.yakshaAssert("TestAcceptLimitIncreaseRequest", False, "functional")
            print("TestAcceptLimitIncreaseRequest= Failed")

    def test_reject_limit_increase_request(self):
        url='http://127.0.0.1:8000/rejectincreasecardlimitrequest/2/'
        data={
        "remark":"Request is rejected"
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestRejectLimitIncreaseRequest", True, "functional")
            print("TestRejectLimitIncreaseRequest = Passed")
        else:
            test_obj.yakshaAssert("TestRejectLimitIncreaseRequest", False, "functional")
            print("TestRejectLimitIncreaseRequest = Failed")
