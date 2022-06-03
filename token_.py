import time
import requests

resp = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job").json()
sec = resp["seconds"]
tok = resp["token"]
resp = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": tok}).json()
assert resp["status"] == "Job is NOT ready"
time.sleep(sec)
resp = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": tok}).json()
assert resp["status"] == "Job is ready"
assert resp["result"] is not None