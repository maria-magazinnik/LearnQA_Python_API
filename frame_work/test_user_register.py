import pytest

from lib.my_requests import MyRequests
from lib.BaseCase import BaseCase
from lib.Assertions import Assertions
from datetime import datetime


class TestUserRegister(BaseCase):

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content{response.content}"

    def test_create_user_with_incorrect_email(self):
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Invalid email format", f"Unexpected response content{response.content}"

    exclude_params = {
        'username',
        'firstName',
        'lastName',
        'email',
        'password'
    }

    @pytest.mark.parametrize("missing_params", exclude_params)
    def test_create_user_with_missing_params(self, missing_params):
        data = self.prepare_registration_data()
        data.pop(missing_params, None)
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The following required params are missed: {missing_params}", \
            f"Unexpected response content: {response.content}"

    names = {"i"}
    @pytest.mark.parametrize("name", names)
    def test_create_user_with_short_name(self, name):
        data = self.prepare_registration_data(username=name)
        response = MyRequests.post("/user", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too short", \
            f"Unexpected response content: {response.content}"

    names = {"uhirurtg ugh ghiurhg     ugihtiugwihg  uhgiuhgiuhg  hgihgiuhgiprgjg  g iuhgs HIHGIUSRHG  IUGHIHG IU HIUHGIUHGORHGOS  UIRHGIUOHGIRHGHGIHGIUHGISH  UIHGIHGHIiuhiug   ihgiu74t3498yr  uhuhgehihfugugufhuigugugugyeuisgyuguguguhudyg uguguefuoego ugougoguo  YFHFVS7775BN HFH"}
    @pytest.mark.parametrize("name", names)
    def test_create_user_with_very_long_name(self, name):
        data = self.prepare_registration_data(username=name)
        response = MyRequests.post("/user", data=data)
        Assertions.assert_code_status(response, 400)
        assert_text = "long" if len(name) > 250 else "short"
        assert response.content.decode("utf-8") == f"The value of 'username' field is too {assert_text}", \
            f"Unexpected response content: {response.content}"