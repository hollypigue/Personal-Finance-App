import json

class UserData:
    @staticmethod
    def load_data():
        try:
            with open("users.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    @staticmethod
    def save_data(data):
        with open("users.json", "w") as f:
            json.dump(data, f)
