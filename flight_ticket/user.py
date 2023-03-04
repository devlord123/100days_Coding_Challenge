import requests
message = """Hello, Welcome to HB_Traveling Agent. 
We email you available cheap flights in Nigeria.
"""

def register():
    print(message)
    Fname = input("Whats your first name: ")
    Lname = input("Whats your last name: ")
    Email = input("Whats your email address: ")

    params = {
        'user': {
            'firstName': Fname,
            'lastName': Lname,
            'emails': Email,
        }
    }

    response = requests.post(url=f"https://api.sheety.co/f31713ee5ec8d8d97a39f5d301cdc14d/flightDeals/users",
                             json=params)

    print(response.text)

def get_user_mails():
    users_mail = []
    response = requests.get(url="https://api.sheety.co/f31713ee5ec8d8d97a39f5d301cdc14d/flightDeals/users")
    data = response.json()['users']
    for dt in data:
        users_mail.append(dt['emails'])

    return users_mail

