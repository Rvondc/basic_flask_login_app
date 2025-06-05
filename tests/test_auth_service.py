import unittest
from app.services.auth_service import AuthService, TEMP_USERS # Assuming TEMP_USERS is accessible

class TestAuthService(unittest.TestCase):

    def setUp(self):
        """Set up for test methods."""
        self.auth_service = AuthService()
        # Keep a pristine copy of TEMP_USERS for each test
        self.original_temp_users = TEMP_USERS.copy() 
        # Ensure TEMP_USERS is reset for each test if it could be modified by the service
        # For this simple service, it's read-only, but this is good practice.
        TEMP_USERS.clear()
        TEMP_USERS.update({"user1": {"password": "password123"}, "user2": {"password": "anotherpassword"}})


    def tearDown(self):
        """Clean up after test methods by restoring original TEMP_USERS."""
        TEMP_USERS.clear()
        TEMP_USERS.update(self.original_temp_users)

    def test_verify_credentials_valid(self):
        """Test successful credential verification for a known user."""
        self.assertTrue(self.auth_service.verify_credentials("user1", "password123"))

    def test_verify_credentials_invalid_password(self):
        """Test credential verification with a correct username but invalid password."""
        self.assertFalse(self.auth_service.verify_credentials("user1", "wrongpassword"))

    def test_verify_credentials_invalid_username(self):
        """Test credential verification with a non-existent username."""
        self.assertFalse(self.auth_service.verify_credentials("nonexistentuser", "password123"))

    def test_verify_credentials_empty_username(self):
        """Test credential verification with an empty username string."""
        self.assertFalse(self.auth_service.verify_credentials("", "password123"))

    def test_verify_credentials_empty_password(self):
        """Test credential verification with an empty password string."""
        self.assertFalse(self.auth_service.verify_credentials("user1", ""))

    def test_verify_credentials_both_empty(self):
        """Test credential verification with both username and password empty."""
        self.assertFalse(self.auth_service.verify_credentials("", ""))

    def test_verify_credentials_case_sensitive_username(self):
        """Test that username verification is case-sensitive (if that's the design)."""
        # This depends on how TEMP_USERS keys are handled (dictionaries are case-sensitive)
        self.assertFalse(self.auth_service.verify_credentials("User1", "password123"))

if __name__ == '__main__':
    unittest.main()