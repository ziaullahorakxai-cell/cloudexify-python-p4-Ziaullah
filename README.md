# CloudExify Python Internship — Project 4

## Student Information

**Name:** Ziaullah Orakzai  
**Registration Number:** CX-INT-2026-PY-0441  
**Internship:** CloudExify Python Internship — Month 2  
**Project:** Project 4 — To-Do List Manager


# To-Do List Manager

**CloudExify Python Internship — Month 2, Project 4 (Final Project)**

A command-line to-do list application built in Python. Tasks are stored
persistently in a `tasks.json` file, so your list survives between runs.

## Features

- **Add tasks** with a title, priority (High/Medium/Low), category
  (Work/Study/Personal), and an optional due date
- **View tasks** — all tasks, pending only, or filtered by High priority
  (always sorted with High priority first)
- **Mark tasks as done**
- **Delete tasks** (with a yes/no confirmation)
- **Edit a task's** title or priority
- **Statistics** — total, completed, pending, high-priority-pending counts,
  and completion percentage
- **Persistent storage** using the `json` module — tasks are saved to
  `tasks.json` after every change and reloaded automatically on startup
- **Timestamps** using the `datetime` module — every task records when
  it was created

### Bonus features included

- Show overdue tasks (past due date, still pending)
- Show tasks due today
- Search tasks by keyword in the title
- Edit task title or priority
- Task categories (Work / Study / Personal)

## How to Run

1. Make sure you have Python 3 installed.
2. Run the script from a terminal:

   ```bash
   python3 todo_manager.py
   ```

3. Use the numbered menu to add, view, complete, edit, or delete tasks.
4. Your tasks are automatically saved to `tasks.json` in the same folder,
   so closing and reopening the program keeps your list intact.

## Files

| File              | Purpose                                    |
|-------------------|---------------------------------------------|
| `todo_manager.py` | Main program                               |
| `tasks.json`      | Auto-created on first run to store tasks   |
| `README.md`       | This file                                  |

## Concepts Used

- `json` module — saving/loading task data
- `datetime` module — recording creation timestamps and checking due dates
- List of dictionaries — storing all tasks in memory
- List comprehensions — filtering by status, priority, category, keyword
- `sorted()` with a `key` function — sorting tasks by priority
- `enumerate()` — locating tasks by index for deletion
- f-strings — formatted table output
- Functions — one function per feature, called from a main menu loop

## GitHub Projects

- [Project 1](https://github.com/ziaullahorakzai-cell/CloudExify-Project-1)
- [Project 2](https://github.com/ziaullahorakzai-cell/CloudExify-Project-2)
- [Project 3](https://github.com/ziaullahorakzai-cell/cloudexify-python-p3-Ziaullah)
- [Project 4 – To-Do List Manager](https://github.com/ziaullahorakxai-cell/cloudexify-python-p4-Ziaullah)
- [GitHub] (https://github.com/ziaullahorakxai-cell)

---

*Built as part of the CloudExify Summer Internship 2026.*