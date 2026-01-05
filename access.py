"""
Access Control Module for Teach-In Blueprint

This module provides basic access control functionality for managing
user permissions and authentication.
"""

class AccessControl:
    """Manages user access and permissions."""
    
    def __init__(self):
        self.users = {}
        self.logged_in_users = set()
    
    def register_user(self, username, password, role="user"):
        """
        Register a new user with a username, password, and role.
        
        Args:
            username (str): The username for the new user
            password (str): The password for the new user
            role (str): The role of the user (default: "user")
        
        Returns:
            bool: True if registration successful, False if user already exists
        """
        if username in self.users:
            return False
        
        self.users[username] = {
            "password": password,
            "role": role
        }
        return True
    
    def login(self, username, password):
        """
        Authenticate a user with username and password.
        
        Args:
            username (str): The username
            password (str): The password
        
        Returns:
            bool: True if login successful, False otherwise
        """
        if username not in self.users:
            return False
        
        if self.users[username]["password"] == password:
            self.logged_in_users.add(username)
            return True
        
        return False
    
    def logout(self, username):
        """
        Log out a user.
        
        Args:
            username (str): The username to log out
        
        Returns:
            bool: True if logout successful, False if user wasn't logged in
        """
        if username in self.logged_in_users:
            self.logged_in_users.remove(username)
            return True
        return False
    
    def is_logged_in(self, username):
        """
        Check if a user is currently logged in.
        
        Args:
            username (str): The username to check
        
        Returns:
            bool: True if user is logged in, False otherwise
        """
        return username in self.logged_in_users
    
    def has_access(self, username, required_role=None):
        """
        Check if a user has access based on their login status and role.
        
        Args:
            username (str): The username to check
            required_role (str, optional): The required role for access
        
        Returns:
            bool: True if user has access, False otherwise
        """
        if not self.is_logged_in(username):
            return False
        
        if required_role is None:
            return True
        
        user_role = self.users[username]["role"]
        
        # Simple role hierarchy: admin > teacher > user
        role_hierarchy = {"admin": 3, "teacher": 2, "user": 1}
        
        user_level = role_hierarchy.get(user_role, 0)
        required_level = role_hierarchy.get(required_role, 0)
        
        return user_level >= required_level
    
    def get_user_role(self, username):
        """
        Get the role of a user.
        
        Args:
            username (str): The username
        
        Returns:
            str or None: The user's role, or None if user doesn't exist
        """
        if username in self.users:
            return self.users[username]["role"]
        return None


def main():
    """Example usage of the AccessControl class."""
    ac = AccessControl()
    
    # Register some users
    print("Registering users...")
    ac.register_user("alice", "password123", "admin")
    ac.register_user("bob", "password456", "teacher")
    ac.register_user("charlie", "password789", "user")
    
    # Test login
    print("\nTesting login...")
    print(f"Alice login: {ac.login('alice', 'password123')}")  # True
    print(f"Bob login with wrong password: {ac.login('bob', 'wrongpass')}")  # False
    print(f"Bob login: {ac.login('bob', 'password456')}")  # True
    
    # Test access
    print("\nTesting access...")
    print(f"Alice has access: {ac.has_access('alice')}")  # True
    print(f"Charlie has access (not logged in): {ac.has_access('charlie')}")  # False
    print(f"Alice has admin access: {ac.has_access('alice', 'admin')}")  # True
    print(f"Bob has admin access: {ac.has_access('bob', 'admin')}")  # False
    print(f"Bob has teacher access: {ac.has_access('bob', 'teacher')}")  # True
    
    # Test logout
    print("\nTesting logout...")
    print(f"Alice logout: {ac.logout('alice')}")  # True
    print(f"Alice has access after logout: {ac.has_access('alice')}")  # False
    
    print("\nAccess control demo complete!")


if __name__ == "__main__":
    main()
