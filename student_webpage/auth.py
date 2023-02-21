import json

logged_user = ""
def save_user(user):
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("data.json", "w") as file:
            json.dump(user, file, indent=4)
    else:
        data.update(user)
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)


def check_user(user, password):
    global logged_user
    with open("data.json", 'r') as file:
        data = json.load(file)
        user_dict = data[user]
        logged_user = user_dict['name']
        if user == user_dict['email'] and password == user_dict['password']:
            return True
        else:
            return False







# check_user("kslsls@hjnm", "890")


