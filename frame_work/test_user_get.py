from lib.MyRequests import MyRequests
from lib.BaseCase import BaseCase
from lib.Assertions import Assertions

class TestUserWithAnotherId(BaseCase):
    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': 1234
        }
        response1 =MyRequests.post('/user/login', data=data)
        auth_sid = self.get_cookie(response1, 'auth_sid')
        token = self.get_header(response1,'x-csrf-token')

        response2 = MyRequests.get(f'/user/1',
                                 headers={'x-csrf-token': token},
                                 cookies={'auth_sid': auth_sid})
        Assertions.assert_json_has_key(response2, 'username')
        Assertions.assert_json_has_not_key(response2, 'email')
        Assertions.assert_json_has_not_key(response2, 'firstname')
        Assertions.assert_json_has_not_key(response2, 'lastname')