import os
import requests
from dotenv import load_dotenv

load_dotenv()

database = {
    1: "Slowerzz",
    2: "Headorteil"
}


def get_user(user_id):
    return database.get(user_id)


def get_user_from_db():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code != 200:
        raise requests.HTTPError
    return response.json()


print(os.getenv('TOKEN'))
