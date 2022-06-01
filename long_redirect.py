import requests

resp = requests.get("https://playground.learnqa.ru/api/long_redirect")
print(len(resp.history))
last_url = ""
for i in resp.history:
    last_url = i.url

print(last_url)