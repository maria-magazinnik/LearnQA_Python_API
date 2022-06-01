import requests

# 1

for i in ["GET", "POST", "PUT", "DELETE"]:
    if i == "GET":
        res = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
        print(res.text)
    elif i == "POST":
        res = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
        print(res.text)
    elif i == "PUT":
        res = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type")
        print(res.text)
    elif i == "DELETE":
        res = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type")
        print(res.text)

# 2

res = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(res)

# 3
for i in ["GET", "POST", "PUT", "DELETE"]:
    if i == "GET":
        res = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": i})
        print(res.text)
    elif i == "POST":
        res = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": i})
        print(res.text)
    elif i == "PUT":
        res = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": i})
        print(res.text)
    elif i == "DELETE":
        res = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": i})
        print(res.text)

# 4
for i in ["GET", "POST", "PUT", "DELETE"]:
    for j in ["GET", "POST", "PUT", "DELETE"]:
        if i == "GET":
            res = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": j})
            print("GET with method {}".format(j), res.text)
        elif i == "POST":
            res = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": j})
            print("POST with method {}".format(j), res.text)
        elif i == "PUT":
            res = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": j})
            print("PUT with method {}".format(j), res.text)
        elif i == "DELETE":
            res = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": j})
            print("DELETE with method {}".format(j), res.text)