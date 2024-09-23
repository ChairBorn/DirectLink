import unittest
from datetime import timedelta, datetime, timezone
from jose import jwt
import os
from DirectLink.auth import create_access_token, SECRET_KEY, ALGORITHM

# Ensure the SECRET_KEY is set for testing
os.environ["SECRET_KEY"] = "test_secret_key"


class TestCreateAccessToken(unittest.TestCase):

    def test_create_access_token_default_expiry(self):
        data = {"sub": "testuser"}
        token = create_access_token(data)
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        self.assertEqual(decoded_token["sub"], "testuser")
        self.assertIn("exp", decoded_token)
        self.assertTrue(decoded_token["exp"] > datetime.now(timezone.utc).timestamp())

    def test_create_access_token_custom_expiry(self):
        data = {"sub": "testuser"}
        expires_delta = timedelta(minutes=10)
        token = create_access_token(data, expires_delta)
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        self.assertEqual(decoded_token["sub"], "testuser")
        self.assertIn("exp", decoded_token)
        expected_expiry = (datetime.now(timezone.utc) + expires_delta).timestamp()
        self.assertAlmostEqual(decoded_token["exp"], expected_expiry, delta=1)

if __name__ == "__main__":
    unittest.main()