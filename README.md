# Matatu Sacco Manager CLI

A Beginner-Friendly Python OOP Course Project

The Matatu Sacco Manager is a simple command-line application written in Python. It allows users to register accounts, log in, manage vehicle fleets, assign routes, and record passenger fare transactions.
The project is intentionally small. Its main purpose is to demonstrate the Python concepts required in the assignment without adding unnecessary frameworks, databases, or advanced patterns.
The application demonstrates:
- Classes and objects
- Inheritance
- Encapsulation
- Multiple interacting classes
- Modular Python files
- JSON file persistence
- Registration and login
- Password hashing
- User, Manager, and Driver roles
- Decorators
- Input validation
- Error handling
- Interactive CLI menus


### Project title
Matatu Sacco Manager CLI

### Problem
A Matatu Sacco, fleet operator, or small transport group may want a simple way to track vehicle fleets, driver assignments, and passenger fare revenue without using a complex web application or database system.
The Matatu Sacco Manager provides a command-line solution where users can register, log in, register vehicles, assign drivers to routes, record daily trip transactions, and view financial logs. Sacco Administrators have extra permissions: they can void invalid transactions and edit vehicle statuses.
The project focuses on learning Python programming and Object-Oriented Programming rather than building a large production system.

### Target users
The target users are:
- Matatu Sacco Administrators
- Fleet Managers
- Matatu Drivers
- Transport Coordinators
- Beginner Python programmers learning OOP

### Core features
The application supports:
- User registration
- User login
- Password hashing
- Admin, Manager, and Driver roles
- Vehicle registration and status tracking
- Route creation and assignment
- Fare transaction logging and payout calculation
- Transaction voiding for Admin users
- Saving users, vehicles, and transactions in JSON files

### Main entities
The main entities are:
- User
- Admin
- Vehicle
- FleetManager
- AuthManager
The two main data entities are User and Vehicle.

## Storage Plan
The project uses JSON files rather than a database.

data/
├── users.json
├── vehicles.json
└── transactions.json

## Authentication Strategy
The authentication system follows this simple flow:
Plaintext
Registration
    |
    v
Validate input
    |
    v
Hash password
    |
    v
Save user to users.json

## Git Workflow Plan
A simple Git workflow is enough for this project.
Start the repository:

Bash
git init
git add .
git commit -m "Initial project setup"

## Project Folder Structure
Plaintext
matatu_sacco_manager/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── vehicle.py
│   ├── route.py
│   └── transaction.py
│
├── utils/
│   ├── __init__.py
│   ├── auth.py
│   ├── decorators.py
│   ├── storage.py
│   └── validators.py
│
├── data/
│   ├── users.json
│   ├── vehicles.json
│   └── transactions.json
│
└── tests/
    ├── __init__.py
    ├── test_auth.py
    ├── test_models.py
    ├── test_cli.py
    └── test_decorators.py

## How to Run the Application
Requirement
Install Python 3.
Check Python:

Bash
python --version

## Limitations and Possible Future Improvements

The project intentionally avoids advanced features.
Possible future improvements include:
Use bcrypt or Argon2 for production-grade password hashing.
Prevent public users from choosing the Admin role during registration.
Give every vehicle, route, and transaction a unique ID.
Allow users to edit vehicle details and maintenance schedules.
Track driver shifts and assign specific vehicles to individual drivers.
Add automated fare collection and MPESA API payment integration.
Replace JSON files with PostgreSQL or SQLite database.
Add a web or graphical interface.
These improvements are not required for the current project. The current version is deliberately small so that the main Python and OOP concepts remain easy to understand.

## Final Summary

The Matatu Sacco Manager demonstrates how a relatively small Python project can combine several important programming ideas.
The main flow is:
User starts CLI
|
v
Register / Login
|
v
User or Admin object
|
v
Fleet & Route menu
|
v
FleetManager
|
v
JSON storage

The key OOP ideas are:
Classes       -> User, Vehicle, FleetManager, AuthManager, MatatuCLI
Inheritance   -> Admin inherits from User
Encapsulation -> private password hash
Interaction   -> MatatuCLI uses AuthManager and FleetManager


