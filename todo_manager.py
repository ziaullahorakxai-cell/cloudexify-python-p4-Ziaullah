# To-Do List Manager


# **Name:** Ziaullah Orakzai  
# **Registration Number:** CX-INT-2026-PY-0441  
# **Internship:** CloudExify Internship Program — Month 2  
# **Project:** Project 4

"""
todo_manager.py
CloudExify Python Internship — Month 2, Project 4: To-Do List Manager

A command-line to-do list application that stores tasks persistently
in a JSON file. Demonstrates:
    - the json module (saving/loading structured data)
    - the datetime module (timestamping task creation)
    - list comprehensions for filtering
    - sorted() with a key function for custom ordering
    - f-strings for formatted table output
"""

import json
import os
from datetime import datetime, date

FILE = "tasks.json"
next_id = 1


# ---------------------------------------------------------------------
# File I/O
# ---------------------------------------------------------------------

def load_tasks():
    """Load tasks from the JSON file. Returns an empty list if no file
    exists yet. Also updates the global next_id counter so new tasks
    never reuse an old id."""
    global next_id

    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        try:
            tasks = json.load(f)
        except json.JSONDecodeError:
            # File exists but is empty/corrupted -- start fresh safely
            return []

    if tasks:
        next_id = max(t["id"] for t in tasks) + 1

    return tasks


def save_tasks(tasks):
    """Write the current list of tasks to the JSON file."""
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


# ---------------------------------------------------------------------
# Core features
# ---------------------------------------------------------------------

def add_task(tasks):
    """Prompt the user for task details and append a new task."""
    global next_id
    print("\n--- ADD NEW TASK ---")

    title = input("Task title: ").strip()
    if not title:
        print("Title cannot be empty!")
        return

    # Priority selection
    print("Priority: 1) High  2) Medium  3) Low")
    while True:
        choice = input("Select (1-3): ").strip()
        if choice == "1":
            priority = "High"
            break
        elif choice == "2":
            priority = "Medium"
            break
        elif choice == "3":
            priority = "Low"
            break
        else:
            print("Enter 1, 2, or 3!")

    # Category (bonus feature)
    print("Category: 1) Work  2) Study  3) Personal")
    cat_choice = input("Select (1-3, or skip): ").strip()
    category_map = {"1": "Work", "2": "Study", "3": "Personal"}
    category = category_map.get(cat_choice, "General")

    due_date = input("Due date (YYYY-MM-DD) or skip: ").strip()
    if not due_date:
        due_date = "No due date"
    else:
        # Basic validation so bad input doesn't silently break sorting
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format, saving as 'No due date' instead.")
            due_date = "No due date"

    task = {
        "id": next_id,
        "title": title,
        "priority": priority,
        "category": category,
        "due_date": due_date,
        "status": "Pending",
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }

    tasks.append(task)
    next_id += 1
    save_tasks(tasks)
    print(f"Task added! ID: {task['id']}")


def view_tasks(tasks, filter_status=None, filter_priority=None,
               filter_category=None, keyword=None):
    """Display tasks, optionally filtered by status, priority, category,
    or a keyword found in the title. High priority tasks are always
    shown first."""
    display = tasks

    if filter_status:
        display = [t for t in display if t["status"] == filter_status]
    if filter_priority:
        display = [t for t in display if t["priority"] == filter_priority]
    if filter_category:
        display = [t for t in display if t.get("category") == filter_category]
    if keyword:
        display = [t for t in display if keyword.lower() in t["title"].lower()]

    if not display:
        print("\nNo tasks found!")
        return

    # Sort: High priority first
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    display = sorted(display, key=lambda t: priority_order.get(t["priority"], 4))

    print(f"\n{'ID':<5} {'Title':<25} {'Priority':<10} "
          f"{'Status':<10} {'Category':<10} {'Due Date'}")
    print("-" * 80)

    for t in display:
        status_mark = "DONE" if t["status"] == "Done" else "..."
        print(f"{t['id']:<5} {t['title']:<25} "
              f"{t['priority']:<10} {status_mark:<10} "
              f"{t.get('category', 'General'):<10} {t['due_date']}")


def mark_done(tasks):
    """Mark a pending task as done, chosen by id."""
    view_tasks(tasks, filter_status="Pending")

    try:
        task_id = int(input("\nEnter task ID to mark done: "))
    except ValueError:
        print("Please enter a number!")
        return

    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "Done":
                print("Task is already done!")
            else:
                task["status"] = "Done"
                save_tasks(tasks)
                print(f"Task '{task['title']}' marked as done!")
            return

    print(f"No task found with ID {task_id}")


def delete_task(tasks):
    """Delete a task (with confirmation), chosen by id."""
    view_tasks(tasks)

    try:
        task_id = int(input("\nEnter task ID to delete: "))
    except ValueError:
        print("Please enter a number!")
        return

    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            confirm = input(f"Delete '{task['title']}'? (yes/no): ").lower()
            if confirm in ["yes", "y"]:
                tasks.pop(i)
                save_tasks(tasks)
                print("Task deleted!")
            return

    print(f"No task found with ID {task_id}")


def edit_task(tasks):
    """Bonus: edit a task's title or priority."""
    view_tasks(tasks)

    try:
        task_id = int(input("\nEnter task ID to edit: "))
    except ValueError:
        print("Please enter a number!")
        return

    for task in tasks:
        if task["id"] == task_id:
            print("1. Edit title  2. Edit priority  3. Cancel")
            choice = input("Select (1-3): ").strip()

            if choice == "1":
                new_title = input("New title: ").strip()
                if new_title:
                    task["title"] = new_title
                    save_tasks(tasks)
                    print("Title updated!")
                else:
                    print("Title cannot be empty!")
            elif choice == "2":
                print("Priority: 1) High  2) Medium  3) Low")
                p_choice = input("Select (1-3): ").strip()
                mapping = {"1": "High", "2": "Medium", "3": "Low"}
                if p_choice in mapping:
                    task["priority"] = mapping[p_choice]
                    save_tasks(tasks)
                    print("Priority updated!")
                else:
                    print("Invalid choice!")
            else:
                print("Cancelled.")
            return

    print(f"No task found with ID {task_id}")


def show_overdue(tasks):
    """Bonus: show tasks whose due date has passed and are still pending."""
    today = date.today()
    overdue = []

    for t in tasks:
        if t["status"] == "Pending" and t["due_date"] != "No due date":
            try:
                due = datetime.strptime(t["due_date"], "%Y-%m-%d").date()
                if due < today:
                    overdue.append(t)
            except ValueError:
                continue

    if not overdue:
        print("\nNo overdue tasks. Nice work!")
        return

    print(f"\n{'ID':<5} {'Title':<25} {'Priority':<10} {'Due Date'}")
    print("-" * 60)
    for t in overdue:
        print(f"{t['id']:<5} {t['title']:<25} {t['priority']:<10} {t['due_date']}")


def show_due_today(tasks):
    """Bonus: show tasks due today."""
    today_str = date.today().strftime("%Y-%m-%d")
    due_today = [t for t in tasks if t["due_date"] == today_str
                 and t["status"] == "Pending"]

    if not due_today:
        print("\nNo tasks due today.")
        return

    print(f"\n{'ID':<5} {'Title':<25} {'Priority':<10}")
    print("-" * 45)
    for t in due_today:
        print(f"{t['id']:<5} {t['title']:<25} {t['priority']:<10}")


def show_stats(tasks):
    """Print summary statistics about the task list."""
    total = len(tasks)
    done = sum(1 for t in tasks if t["status"] == "Done")
    pending = total - done
    high = sum(1 for t in tasks if t["priority"] == "High"
               and t["status"] == "Pending")

    print("\n=== TASK STATISTICS ===")
    print(f"Total Tasks   : {total}")
    print(f"Completed     : {done}")
    print(f"Pending       : {pending}")
    print(f"High Priority : {high} pending")
    if total > 0:
        pct = (done / total) * 100
        print(f"Completion    : {pct:.0f}%")


# ---------------------------------------------------------------------
# Main menu
# ---------------------------------------------------------------------

def main():
    tasks = load_tasks()
    print(f"Loaded {len(tasks)} tasks.")

    while True:
        print("\n=== TO-DO LIST MANAGER ===")
        print("1. Add task")
        print("2. View all tasks")
        print("3. View pending tasks")
        print("4. View high priority")
        print("5. Mark task as done")
        print("6. Delete task")
        print("7. Show statistics")
        print("8. Edit task")
        print("9. Show overdue tasks")
        print("10. Show tasks due today")
        print("11. Search tasks by keyword")
        print("12. Exit")

        choice = input("Choose (1-12): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks, filter_status="Pending")
        elif choice == "4":
            view_tasks(tasks, filter_priority="High")
        elif choice == "5":
            mark_done(tasks)
        elif choice == "6":
            delete_task(tasks)
        elif choice == "7":
            show_stats(tasks)
        elif choice == "8":
            edit_task(tasks)
        elif choice == "9":
            show_overdue(tasks)
        elif choice == "10":
            show_due_today(tasks)
        elif choice == "11":
            kw = input("Enter keyword to search: ").strip()
            view_tasks(tasks, keyword=kw)
        elif choice == "12":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()