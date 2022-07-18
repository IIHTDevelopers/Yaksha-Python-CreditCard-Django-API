from rest_framework.test import APITestCase
from cardapp.models import *
from cardapp.test.TestUtils import TestUtils
class CreditCardAppAPIExceptionalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.obj=CardDetailsModel.objects.create(customer_id=11,card_type_id=11,card_number=24680,card_limit=25000,issued_date="2021-11-01",expiration_date="2026-11-01",is_blocked="True")

    def test_apply_for_card_fail(self):
        url='http://127.0.0.1:8000/applyforcard/?customer_id=1&card_type_id=1'
        data={
        "card_type_id":1,
        "customer_id":1,
        "status":0,
        "remark":"None"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestApplyForCardFail", True, "exception")
            print("TestApplyForCardFail = Passed")
        else:
            test_obj.yakshaAssert("TestApplyForCardFail", False, "exception")
            print("TestApplyForCardFail = Failed")

    def test_accept_card_request_fail(self):
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
        if response.status_code==500:
            test_obj.yakshaAssert("TestAcceptCardRequestFail", True, "exception")
            print("TestAcceptCardRequestFail = Passed")
        else:
            test_obj.yakshaAssert("TestAcceptCardRequestFail", False, "exception")
            print("TestAcceptCardRequestFail = Failed")

    def test_request_for_increase_limit_fail(self):
        url='http://127.0.0.1:8000/applyforcard/?customer_id=1&card_type_id=1'
        data={
        "card_type_id":1,
        "customer_id":1,
        "status":0,
        "remark":"Please increase limit"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestRequestForIncreaseLimitFail", True, "exception")
            print("TestRequestForIncreaseLimitFail = Passed")
        else:
            test_obj.yakshaAssert("TestRequestForIncreaseLimitFail", False, "exception")
            print("TestRequestForIncreaseLimitFail = Failed")

    def test_get_status_of_card_fail(self):
        url='http://127.0.0.1:8000/getstatus/1234/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetStatusOfCardFail", True, "exception")
            print("TestGetStatusOfCardFail = Passed")
        else:
            test_obj.yakshaAssert("TestGetStatusOfCardFail", False, "exception")
            print("TestGetStatusOfCardFail = Failed")

    def test_block_card_fail(self):
        url='http://127.0.0.1:8000/blockcard/2/'
        data={
        "is_blocked":"True"
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestBlockCardFail", True, "exception")
            print("TestBlockCardFail = Passed")
        else:
            test_obj.yakshaAssert("TestBlockCardFail", False, "exception")
            print("TestBlockCardFail = Failed")

    def test_un_block_card_fail(self):
        url='http://127.0.0.1:8000/blockcard/2/'
        data={
        "is_blocked":"False"
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestUnBlockCardFail", True, "exception")
            print("TestUnBlockCardFail = Passed")
        else:
            test_obj.yakshaAssert("TestUnBlockCardFail", False, "exception")
            print("TestUnBlockCardFail = Failed")

    def test_reject_card_request_fail(self):
        url='http://127.0.0.1:8000/rejectcardrequest/1/'
        data={
        "remark":"Request for card is rejected"
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestRejectCardRequestFail", True, "exception")
            print("TestRejectCardRequestFail = Passed")
        else:
            test_obj.yakshaAssert("TestRejectCardRequestFail", False, "exception")
            print("TestRejectCardRequestFail = Failed")

    def test_accept_limit_increase_request_fail(self):
        url='http://127.0.0.1:8000/acceptincreasecardlimitrequest/2/'
        data={
        "card_limit":35000
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestAcceptLimitIncreaseRequestFail", True, "exception")
            print("TestAcceptLimitIncreaseRequestFail = Passed")
        else:
            test_obj.yakshaAssert("TestAcceptLimitIncreaseRequestFail", False, "exception")
            print("TestAcceptLimitIncreaseRequestFail = Failed")

    def test_reject_limit_increase_request_fail(self):
        url='http://127.0.0.1:8000/rejectincreasecardlimitrequest/2/'
        data={
        "remark":"Request is rejected"
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestRejectLimitIncreaseRequestFail", True, "exception")
            print("TestRejectLimitIncreaseRequestFail = Passed")

        else:
            test_obj.yakshaAssert("TestRejectLimitIncreaseRequestFail", False, "exception")
            print("TestRejectLimitIncreaseRequestFail = Failed")

    def test_request_for_increase_limit_of_blocked_card(self):
        url='http://127.0.0.1:8000/applyforcard/?customer_id=11&card_type_id=11'
        data={
        "card_type_id":1,
        "customer_id":1,
        "status":0,
        "remark":"Please increase limit"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if self.obj.is_blocked=="True":
            test_obj.yakshaAssert("TestRequestForIncreaseLimitOfBlockedCard", True, "exception")
            print("TestRequestForIncreaseLimitOfBlockedCard = Passed")
        else:
            test_obj.yakshaAssert("TestRequestForIncreaseLimitOfBlockedCard", False, "exception")
            print("TestRequestForIncreaseLimitOfBlockedCard = Failed")

    def test_apply_for_existing_card(self):
        url='http://127.0.0.1:8000/applyforcard/?customer_id=11&card_type_id=11'
        data={
        "card_type_id":11,
        "customer_id":11,
        "status":0,
        "remark":"None"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestApplyForExistingCard", True, "exception")
            print("TestApplyForExistingCard = Passed")
        else:
            test_obj.yakshaAssert("TestApplyForExistingCard", False, "exception")
            print("TestApplyForExistingCard = Failed")

    def test_apply_for_card_fourth_time(self):
        url='http://127.0.0.1:8000/applyforcard/?customer_id=11&card_type_id=44'
        data={
        "card_type_id":44,
        "customer_id":11,
        "status":0,
        "remark":"None"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestApplyForCardFourthTime", True, "exception")
            print("TestApplyForCardFourthTime = Passed")
        else:
            test_obj.yakshaAssert("TestApplyForCardFourthTime", False, "exception")
            print("TestApplyForCardFourthTime= Failed")
