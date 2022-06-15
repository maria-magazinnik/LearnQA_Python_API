import requests

class TestAPI:
    need_cookie = {'HomeWork': 'hw_value'}
    need_status_code = 200

    def test_cookies(self):
        resp = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        assert resp.status_code == self.need_status_code
        cookies = dict(resp.cookies)
        print(cookies)
        assert cookies == self.need_cookie