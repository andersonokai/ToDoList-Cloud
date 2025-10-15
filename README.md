# Overview

As a software engineer, I developed this To-Do List application to advance my expertise in cloud database integration and user authentication. The software enables secure task management using Google Firestore and Firebase Authentication via a console-based interface built with Python.

The program integrates with Firestore to store tasks with fields: ID, name, description, status (Pending/Completed), and user ID. Users can create accounts, sign in, add tasks, view tasks, update status or description, and delete tasks. The console app, using the Firebase Admin SDK, provides a robust backend with interactive messages like welcome and goodbye prompts, making it user-friendly and efficient.

To use the program, run `python main.py` in the project directory with `todolist-andersonokai-firebase-adminsdk-fbsvc-16ffd9ebc8.json` present. Follow the menu to manage users and tasks.

My purpose was to build a scalable, secure task management system to showcase cloud database skills for fintech roles in Accra.

[Software Demo Video](https://youtu.be/xyz) 

# Cloud Database

The application uses **Google Firestore**, a NoSQL cloud database, for storing user and task data.

**Database Structure**:
- **users Collection**: Stores user information.
  - Document ID: `user_id` (unique user identifier).
  - Fields: `email` (string), `created_at` (timestamp).
- **tasks Collection**: Stores task information.
  - Document ID: Unique task ID (UUID).
  - Fields: `id` (string), `name` (string), `description` (string), `status` (string: Pending/Completed), `user_id` (string).

# Development Environment

**Tools**:
- Visual Studio Code for coding and debugging.
- Firebase Console for managing Firestore and Authentication.
- Git for version control.

**Programming Languages and Libraries**:
- **Python 3.8+**: Console app with `firebase-admin` for backend operations.
- **uuid**: For generating unique task IDs.

# Useful Websites

- [Firebase Documentation](https://firebase.google.com/docs)
- [Firestore Guide](https://firebase.google.com/docs/firestore)
- [Python Documentation](https://docs.python.org/3/)

# Future Work

- Add task categories or priorities for enhanced organization.
- Implement task sorting and filtering.
- Add password recovery for Firebase Authentication.
