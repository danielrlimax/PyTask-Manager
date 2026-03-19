# 📝 PyTask Manager

A simple and efficient **command-line task manager** built in Python.
This project allows you to create, manage, and track tasks with different statuses using a persistent JSON storage system.

---

## 🚀 Features

* ✅ Create new tasks
* 📋 List all tasks
* ❌ Remove tasks by index
* 🔄 Update task status (To Do / Doing / Done)
* ✏️ Edit task details (name, description, status)
* 🔍 Filter tasks by status
* 💾 Automatic save/load using `tasks.json`

---

## 📁 Project Structure

```
PyTask Manager/
│
├── App.py        # Main application (CLI interface)
├── Manager.py    # Task manager logic (CRUD operations)
├── Task.py       # Task model
├── Status.py     # Enum for task status
└── tasks.json    # Persistent storage (auto-generated)
```

---

## ⚙️ How It Works

### 🧠 Core Components

* **Task**

  * Represents a task with:

    * Name
    * Description
    * Status
    * Creation date

* **Status (Enum)**

  * `To Do`
  * `Doing`
  * `Done`

* **Manager**

  * Handles all task operations:

    * Add
    * Remove
    * Update
    * Edit
    * Filter
    * Save/Load from JSON

* **App (CLI)**

  * Interactive menu system for user input

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pytask-manager.git
cd pytask-manager
```

### 2. Run the application

```bash
python App.py
```

---

## 🖥️ Usage

When you run the app, you’ll see a menu like this:

```
==== TO-DO LIST ====
1 - Create Task
2 - List Tasks
3 - Remove Task
4 - Update Status
5 - Edit Task
6 - Filter by Status
0 - Exit
```

### Example Flow:

* Create a task → option `1`
* View tasks → option `2`
* Update status → option `4`
* Filter tasks → option `6`

---

## 💾 Data Persistence

* All tasks are stored in a file called:

```
tasks.json
```

* This file is automatically:

  * Created if it doesn't exist
  * Updated after every change

---

## 🛠️ Technologies Used

* Python 3
* Built-in libraries:

  * `json`
  * `datetime`
  * `enum`
  * `os`

---

## 📌 Future Improvements

- Add task priorities
- Add deadlines and reminders
- GUI version (Tkinter / Web)
- Search tasks by keyword
- Export tasks (CSV / PDF)
- Integrate a real database (e.g., PostgreSQL, MySQL)
- Add user-based task separation (multi-user support)

---

## 🤝 Contributing

Feel free to fork this project and improve it!
Pull requests are welcome.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Developed by **Lima**

---
