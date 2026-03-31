from datetime import datetime
from task_manager.validation import validate_due_date, validate_task_description, validate_task_title

tasks = [
    {
        "title": "Groceries",
        "description": "Shop at Market Basket for food",
        "due_date": "2024-06-26",
        "completed": True
    }
]

def add_task(title, description, due_date):
    try:
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)
    except ValueError as e:
        print(f"Validation error: {e}")
        return

    if len(tasks) > 0:
        for task in tasks:
            if (task["title"] == title and
                task["description"] == description and
                task["due_date"] == due_date):
                print("Task already exists. Please try again.")
                return

    tasks.append({
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    })
    print("Task added successfully!")

def mark_task_as_complete(index, tasks=tasks):
    try:
        index = int(index)
        if index < 0 or index >= len(tasks):
            print("Invalid task index. Please try again.")
            return
        tasks[index]['completed'] = True
        print("Task marked as complete!")
    except ValueError:
        print("Invalid input. Please enter a number.")

def view_pending_tasks(tasks=tasks):
    has_pending = False
    print("Pending Tasks:")
    for i, task in enumerate(tasks):
        if not task['completed']:
            print(f"{i}. {task['title']} - Due: {task['due_date']}")
            has_pending = True
    if not has_pending:
        print("No pending tasks found.")

def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0
    completed_tasks = sum(1 for task in tasks if task['completed'])
    progress = (completed_tasks / len(tasks)) * 100
    return progress