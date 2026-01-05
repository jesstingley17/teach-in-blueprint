# teach-in-blueprint

A simple access control system for educational platforms, providing user authentication and role-based access management.

## Features

- User registration and authentication
- Role-based access control (admin, teacher, user)
- Simple permission hierarchy
- Easy-to-use API

## Installation

No external dependencies required. This project uses only Python standard library.

## Usage

### Basic Example

```python
from access import AccessControl

# Create an access control instance
ac = AccessControl()

# Register users with different roles
ac.register_user("alice", "password123", "admin")
ac.register_user("bob", "password456", "teacher")
ac.register_user("charlie", "password789", "user")

# Login a user
if ac.login("alice", "password123"):
    print("Login successful!")

# Check if user has access
if ac.has_access("alice"):
    print("Alice has access!")

# Check role-specific access
if ac.has_access("alice", "admin"):
    print("Alice has admin access!")

# Logout
ac.logout("alice")
```

### Running the Demo

```bash
python access.py
```

### Running Tests

```bash
python test_access.py
```

## Role Hierarchy

The system implements a simple role hierarchy:
- **admin**: Full access to all features
- **teacher**: Access to teacher and user level features
- **user**: Basic access only

## API Reference

### `AccessControl()`

Main class for managing access control.

#### Methods

- `register_user(username, password, role="user")`: Register a new user
- `login(username, password)`: Authenticate a user
- `logout(username)`: Log out a user
- `is_logged_in(username)`: Check if a user is logged in
- `has_access(username, required_role=None)`: Check if user has access
- `get_user_role(username)`: Get the role of a user

## License

This is a demonstration project for educational purposes.