import json


def load_user_data():

    with open("test_data/user_data.json", "r") as file:
        return json.load(file)