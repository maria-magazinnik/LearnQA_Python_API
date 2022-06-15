import requests

class TestAPIHeaders:
    need_status_code = 200
    need_header = "Some secret value"

    def test_headers(self):
        resp = requests.get("https://playground.learnqa.ru/api/homework_header")
        assert resp.status_code == self.need_status_code
        print(resp.headers)
        header = resp.headers["x-secret-homework-header"]
        assert header == self.need_header, "Wrong headers"