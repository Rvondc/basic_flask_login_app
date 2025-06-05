# For a very basic example, hardcode users.
TEMP_USERS = {
    "admin": {"password": "1234"},
    "user1": {"password": "password123"},
    "user2": {"password": "anotherpassword"}
}

class AuthService:
    def verify_credentials(self, username, password):
        user = TEMP_USERS.get(username)
        if user and user["password"] == password:
            return True
        return False