# import requests

# response = requests.get("https://api.github.com")

# data = response.json()

# print(data)

# # if response.status_code == 200:
# #     print("Request successful")
# # else:
# #     print("Request failed")

# import requests

# try:
#     response = requests.get(
#         "https://jsonplaceholder.typicode.com/todos/1",
#         timeout=5
#     )

#     response.raise_for_status()

#     data = response.json()

#     print(data)

# except requests.RequestException as e:
#     print("Error:", e)

# import requests

# response = requests.get("https://api.github.com")

# print(response.text)

# import requests

# url = "https://api.github.com"

# response = requests.get(url)

# if response.status_code == 200:

#     data = response.json()

#     print(data)

# else:
#     print("Request failed")

import requests

url = "https://api.github.com"

try:
    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        print("Request successful!")

        data = response.json()

        print("GitHub Name:", data["current_user_url"])
        print("Repository URL:", data["repository_url"])

    else:
        print("Request failed")
        print("Status Code:", response.status_code)

except requests.RequestException as e:
    print("Error:", e)