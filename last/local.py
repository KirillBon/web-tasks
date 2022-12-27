import requests
from pprint import pprint
r = requests.get('http://127.0.0.1:5000/users')
print(r.status_code, r.headers, type(r.text), r.json())
# r = requests.post('http://127.0.0.1:5000/users', json={
#     "id": 2,
#     "name": "Kirill",
#     "surname": "Bobarev"
#     })
# pprint(r.json())

# r = requests.post('http://127.0.0.1:5000/users', json={
#     "user_name": "Boba",
#     "user_surname": "Drake"
#     })


# r = requests.put('http://127.0.0.1:5000/users', json={
#     "user_id": 4,
#     "user_name": "Shen",
#     "user_surname": "Xe"
#     })
# pprint(r.json())
r = requests.delete('http://127.0.0.1:5000/users', json={
    "user_id": 4,
    })
# pprint(r.text)