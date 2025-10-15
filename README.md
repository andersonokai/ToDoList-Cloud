# Overview

As a software engineer, I developed this To-Do List application to advance my expertise in **cloud database integration** and **user authentication**. The software enables secure task management using **Google Firestore** and **Firebase Authentication**, offering both a console-based interface (Python) for administrative tasks and a modern web interface (HTML/JavaScript) for user-friendly interaction.

The program integrates with Firestore to store tasks with fields: ID, name, description, status (Pending/Completed), and user ID. Users can create accounts, sign in, add tasks, view their tasks, update task status, and delete tasks. The console app, built with the Firebase Admin SDK, provides a robust backend with a menu-driven interface and interactive messages (e.g., welcome and goodbye prompts). The web app, using the Firebase Client SDK and **Tailwind CSS**, offers a responsive UI with real-time task updates and a sleek design.

**To use the program:**

* **Console App:** Run `python main.py` in the project directory with `todolist-andersonokai-firebase-adminsdk-fbsvc-16ffd9ebc8.json` present. Follow the menu to manage users and tasks.

* **Web App:** Open `index.html` in a browser, sign in or create an account, and use the interface to manage tasks.

My purpose was to build a scalable, secure task management system to showcase cloud database skills and prepare for fintech roles in Accra.

[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database

The application uses **Google Firestore**, a NoSQL cloud database, for storing user and task data.

## Database Structure:

* **`users` Collection:** Stores user information.

  * *Document ID:* `user_id` (unique user identifier).

  * *Fields:* `email` (string), `created_at` (timestamp).

* **`tasks` Collection:** Stores task information.

  * *Document ID:* Unique task ID (UUID).

  * *Fields:* `id` (string), `name` (string), `description` (string), `status` (string: Pending/Completed), `user_id` (string).

# Development Environment

## Tools:

* Visual Studio Code for coding and debugging.

* Firebase Console for managing Firestore and Authentication.

* Chrome Browser for testing the web UI.

* Git for version control.

## Programming Languages and Libraries:

* **Python 3.8+:** Console app with `firebase-admin` for backend operations.

* **HTML/JavaScript:** Web app with Firebase Client SDK (`firebase-app`, `firebase-auth`, `firebase-firestore`) for real-time access.

* **Tailwind CSS:** For responsive web UI styling.

* `uuid`: For generating unique task IDs in Python.

# Useful Websites

* [Firebase Documentation](https://firebase.google.com/docs)

* [Firestore Guide](https://firebase.google.com/docs/firestore)

* [Tailwind CSS](https://tailwindcss.com/docs)

* [JavaScript Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)

# Future Work

* Add task categories or priorities for enhanced organization.

* Implement task sorting and filtering in the web UI.

* Add password recovery for Firebase Authentication.
