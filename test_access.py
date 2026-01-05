"""
Tests for the Access Control Module
"""

import unittest
from access import AccessControl


class TestAccessControl(unittest.TestCase):
    """Test cases for AccessControl class."""
    
    def setUp(self):
        """Set up a fresh AccessControl instance for each test."""
        self.ac = AccessControl()
    
    def test_register_user(self):
        """Test user registration."""
        result = self.ac.register_user("testuser", "testpass", "user")
        self.assertTrue(result)
        
        # Try to register the same user again
        result = self.ac.register_user("testuser", "testpass", "user")
        self.assertFalse(result)
    
    def test_login_success(self):
        """Test successful login."""
        self.ac.register_user("alice", "password123", "user")
        result = self.ac.login("alice", "password123")
        self.assertTrue(result)
        self.assertTrue(self.ac.is_logged_in("alice"))
    
    def test_login_wrong_password(self):
        """Test login with wrong password."""
        self.ac.register_user("alice", "password123", "user")
        result = self.ac.login("alice", "wrongpassword")
        self.assertFalse(result)
        self.assertFalse(self.ac.is_logged_in("alice"))
    
    def test_login_nonexistent_user(self):
        """Test login with nonexistent user."""
        result = self.ac.login("nonexistent", "password")
        self.assertFalse(result)
    
    def test_logout(self):
        """Test logout functionality."""
        self.ac.register_user("alice", "password123", "user")
        self.ac.login("alice", "password123")
        self.assertTrue(self.ac.is_logged_in("alice"))
        
        result = self.ac.logout("alice")
        self.assertTrue(result)
        self.assertFalse(self.ac.is_logged_in("alice"))
    
    def test_logout_not_logged_in(self):
        """Test logout when user is not logged in."""
        self.ac.register_user("alice", "password123", "user")
        result = self.ac.logout("alice")
        self.assertFalse(result)
    
    def test_has_access_logged_in(self):
        """Test access for logged in user."""
        self.ac.register_user("alice", "password123", "user")
        self.ac.login("alice", "password123")
        self.assertTrue(self.ac.has_access("alice"))
    
    def test_has_access_not_logged_in(self):
        """Test access for user not logged in."""
        self.ac.register_user("alice", "password123", "user")
        self.assertFalse(self.ac.has_access("alice"))
    
    def test_role_hierarchy_admin(self):
        """Test that admin has access to all roles."""
        self.ac.register_user("admin", "password", "admin")
        self.ac.login("admin", "password")
        
        self.assertTrue(self.ac.has_access("admin", "user"))
        self.assertTrue(self.ac.has_access("admin", "teacher"))
        self.assertTrue(self.ac.has_access("admin", "admin"))
    
    def test_role_hierarchy_teacher(self):
        """Test that teacher has limited access."""
        self.ac.register_user("teacher", "password", "teacher")
        self.ac.login("teacher", "password")
        
        self.assertTrue(self.ac.has_access("teacher", "user"))
        self.assertTrue(self.ac.has_access("teacher", "teacher"))
        self.assertFalse(self.ac.has_access("teacher", "admin"))
    
    def test_role_hierarchy_user(self):
        """Test that regular user has minimal access."""
        self.ac.register_user("user", "password", "user")
        self.ac.login("user", "password")
        
        self.assertTrue(self.ac.has_access("user", "user"))
        self.assertFalse(self.ac.has_access("user", "teacher"))
        self.assertFalse(self.ac.has_access("user", "admin"))
    
    def test_get_user_role(self):
        """Test getting user role."""
        self.ac.register_user("alice", "password", "teacher")
        
        role = self.ac.get_user_role("alice")
        self.assertEqual(role, "teacher")
        
        # Test nonexistent user
        role = self.ac.get_user_role("nonexistent")
        self.assertIsNone(role)


if __name__ == "__main__":
    unittest.main()
