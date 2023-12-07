import streamlit as st
import yaml
from typing import Dict
import hashlib

class User:
    def __init__(self, username, password, email=None):
        self.username = username
        self.password_hash = self._hash_password(password)
        self.email = email

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        return self.password_hash == self._hash_password(password)

class Authenticate:
    def __init__(self, users):
        self._users_as_dict: Dict[str, User] = {}
        user_data = users.get('usernames', {})  # Access 'usernames' from the loaded data
        for username, user_info in user_data.items():
            if isinstance(user_info, dict) and "password" in user_info:
                self._users_as_dict[username] = User(username, user_info["password"], user_info.get("email"))

    def login(self, username, password):
        user = self._users_as_dict.get(username)
        if user and user.verify_password(password):
            return True
        return False

def login_page(authenticator):
    global authentication_status, username
    st.title("Login into your account on MindfulMelodies")
    username_input = st.text_input("Username:")
    password_input = st.text_input("Password:", type="password")
    if authenticator.login(username_input, password_input):
            authentication_status = True
            username = username_input
            st.success(f'Welcome {username} . How are you feeling today?')
    else:
            authentication_status = False
            st.error('Username/password is incorrect')

def main():
    st.set_page_config(page_title="MindfulMelodies",
    page_icon=":notes:",  
    layout="wide")

    try:
        with open('credentials.txt') as file:
            config = yaml.load(file, Loader=yaml.SafeLoader)

        authenticator = Authenticate(config['credentials'])
   

    except Exception as e:
        st.exception(f"Error loading data: {e}")

    login_page(authenticator)

if __name__ == "__main__":
    main()
