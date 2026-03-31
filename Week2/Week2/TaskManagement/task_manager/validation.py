from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str):
        raise ValueError("Task title must be a string.")
    if len(title) == 0:
        raise ValueError("Task title cannot be empty.")
    if len(title) > 100:
        raise ValueError("Task title is too long.")
    return True

def validate_task_description(description):
    if not isinstance(description, str):
        raise ValueError("Task description must be a string.")
    if len(description) == 0:
        raise ValueError("Task description cannot be empty.")
    if len(description) > 500:
        raise ValueError("Task description is too long.")
    return True

def validate_due_date(due_date):
    if not isinstance(due_date, str):
        raise ValueError("Due date must be a string.")
    if len(due_date) == 0:
        raise ValueError("Due date cannot be empty.")
    if len(due_date) != 10:
        raise ValueError("Due date must be in YYYY-MM-DD format.")
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Invalid due date format. Please use YYYY-MM-DD.")