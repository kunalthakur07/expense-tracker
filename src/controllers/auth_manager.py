# Very simple username-only login
from src.utils.filehandler import FileHandler
import os
USERS_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'data', 'users.csv')

class AuthManager:
    @staticmethod
    def register(username):
        if not os.path.exists(USERS_FILE):
            with open(USERS_FILE, 'w') as f:
                f.write("username\n")
        # check exists
        with open(USERS_FILE, 'r') as f:
            if username + '\n' in f.readlines():
                return False
        with open(USERS_FILE, 'a') as f:
            f.write(username + '\n')
        return True

    @staticmethod
    def login(username):
        if not os.path.exists(USERS_FILE):
            return False
        with open(USERS_FILE, 'r') as f:
            return username + '\n' in f.readlines()
