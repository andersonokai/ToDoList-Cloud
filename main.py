# main.py
# To-Do List Application for CSE 310 Module #3
# Author: Anderson Okai, Ghana
# Date: October 15, 2025
# Purpose: Manage tasks in Firestore with Firebase Authentication for user-specific access
# Requirements: Create Firestore database, implement user authentication, full CRUD operations

import firebase_admin
from firebase_admin import credentials, firestore, auth
import os
import uuid
from getpass import getpass

def initialize_firebase():
    """
    Initialize Firebase Admin SDK with Service Account JSON and connect to Firestore.
    Returns Firestore client for database operations.
    """
    try:
        # Path to Service Account JSON file (keep secret, not in GitHub)
        cred_path = os.path.join(os.path.dirname(__file__), 'todolist-andersonokai-firebase-adminsdk-fbsvc-16ffd9ebc8.json')
        
        # Initialize Firebase app with credentials
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
        
        # Get Firestore client
        db = firestore.client()
        print("Successfully connected to Firestore!")
        return db
    except Exception as e:
        print(f"Error initializing Firebase: {e}")
        return None

def create_user(db):
    """
    Create a new user with email and password using Firebase Authentication.
    Returns user_id if successful, None otherwise.
    """
    try:
        email = input("Enter email: ")
        password = getpass("Enter password (minimum 6 characters): ")
        
        # Create user in Firebase Authentication
        user = auth.create_user(
            email=email,
            password=password
        )
        print(f"User created successfully with ID: {user.uid}")
        
        # Store user info in Firestore
        db.collection('users').document(user.uid).set({
            'email': email,
            'created_at': firestore.SERVER_TIMESTAMP
        })
        return user.uid
    except Exception as e:
        print(f"Error creating user: {e}")
        return None

def sign_in_user():
    """
    Sign in a user with email and password using Firebase Authentication.
    Returns user_id if successful, None otherwise.
    Note: Admin SDK simulates sign-in by fetching user; use Client SDK for production.
    """
    try:
        email = input("Enter email: ")
        password = getpass("Enter password: ")
        
        # Verify user by email (simulating sign-in)
        user = auth.get_user_by_email(email)
        print(f"User signed in successfully with ID: {user.uid}")
        return user.uid
    except Exception as e:
        print(f"Error signing in: {e}")
        return None

def add_task(db, user_id):
    """
    Add a new task to the Firestore 'tasks' collection for the authenticated user.
    Prompts for name and description, sets status to Pending.
    Returns True if successful, False otherwise.
    """
    try:
        # Generate unique task ID
        task_id = str(uuid.uuid4())
        
        # Get task details from user
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        
        # Validate inputs
        if not name.strip() or not description.strip():
            print("Task name and description cannot be empty.")
            return False
        
        # Create task document
        task_data = {
            'id': task_id,
            'name': name,
            'description': description,
            'status': 'Pending',
            'user_id': user_id
        }
        
        # Add to Firestore
        db.collection('tasks').document(task_id).set(task_data)
        print(f"Task '{name}' added successfully with ID: {task_id}")
        return True
    except Exception as e:
        print(f"Error adding task: {e}")
        return False

def list_tasks(db, user_id):
    """
    Retrieve and display all tasks for the authenticated user from Firestore.
    Prints task details (ID, name, description, status).
    Returns True if successful, False otherwise.
    """
    try:
        # Query tasks where user_id matches
        tasks = db.collection('tasks').where('user_id', '==', user_id).stream()
        
        print("\nYour Tasks:")
        found = False
        for task in tasks:
            task_data = task.to_dict()
            print(f"ID: {task_data['id']}")
            print(f"Name: {task_data['name']}")
            print(f"Description: {task_data['description']}")
            print(f"Status: {task_data['status']}")
            print("-" * 30)
            found = True
        
        if not found:
            print("No tasks found for this user.")
        return True
    except Exception as e:
        print(f"Error retrieving tasks: {e}")
        return False

def modify_task(db, user_id):
    """
    Modify a task's status or description in the Firestore 'tasks' collection.
    Prompts for task ID and fields to update, ensures user_id matches.
    Returns True if successful, False otherwise.
    """
    try:
        task_id = input("Enter task ID to modify: ")
        
        # Verify task exists and belongs to user
        task_ref = db.collection('tasks').document(task_id)
        task = task_ref.get()
        if not task.exists or task.to_dict()['user_id'] != user_id:
            print("Task not found or you don't have permission.")
            return False
        
        print("1. Update Status (Pending/Completed)")
        print("2. Update Description")
        choice = input("Enter choice (1-2): ")
        
        updates = {}
        if choice == '1':
            status = input("Enter new status (Pending/Completed): ")
            if status not in ['Pending', 'Completed']:
                print("Invalid status. Use 'Pending' or 'Completed'.")
                return False
            updates['status'] = status
        elif choice == '2':
            description = input("Enter new description: ")
            updates['description'] = description
        else:
            print("Invalid choice.")
            return False
        
        # Update task in Firestore
        task_ref.update(updates)
        print(f"Task {task_id} updated successfully.")
        return True
    except Exception as e:
        print(f"Error modifying task: {e}")
        return False

def delete_task(db, user_id):
    """
    Delete a task from the Firestore 'tasks' collection.
    Prompts for task ID, ensures user_id matches.
    Returns True if successful, False otherwise.
    """
    try:
        task_id = input("Enter task ID to delete: ")
        
        # Verify task exists and belongs to user
        task_ref = db.collection('tasks').document(task_id)
        task = task_ref.get()
        if not task.exists or task.to_dict()['user_id'] != user_id:
            print("Task not found or you don't have permission.")
            return False
        
        # Delete task from Firestore
        task_ref.delete()
        print(f"Task {task_id} deleted successfully.")
        return True
    except Exception as e:
        print(f"Error deleting task: {e}")
        return False

def main():
    """
    Main function to initialize Firestore and provide a menu for user actions.
    Manages authentication state and allows full CRUD operations for signed-in users.
    """
    # Initialize Firestore
    db = initialize_firebase()
    
    if not db:
        print("Setup failed. Exiting.")
        return

    current_user_id = None
    
    while True:
        if current_user_id:
            print(f"\nTo-Do List Application (Logged in as user {current_user_id})")
            print("1. Add Task")
            print("2. List Tasks")
            print("3. Modify Task")
            print("4. Delete Task")
            print("5. Sign Out")
        else:
            print("\nTo-Do List Application")
            print("1. Create User")
            print("2. Sign In")
            print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if not current_user_id:
            if choice == '1':
                user_id = create_user(db)
                if user_id:
                    print(f"Welcome, user {user_id}! Please sign in to manage tasks.")
            elif choice == '2':
                user_id = sign_in_user()
                if user_id:
                    current_user_id = user_id
                    print(f"Logged in as user {user_id}. Ready to manage tasks.")
            elif choice == '3':
                print("Exiting application.")
                break
            else:
                print("Invalid choice. Try again.")
        else:
            if choice == '1':
                add_task(db, current_user_id)
            elif choice == '2':
                list_tasks(db, current_user_id)
            elif choice == '3':
                modify_task(db, current_user_id)
            elif choice == '4':
                delete_task(db, current_user_id)
            elif choice == '5':
                print(f"User {current_user_id} signed out.")
                current_user_id = None
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()