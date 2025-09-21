task = input("Enter your task for today: ")
priority = input("Enter the task's priority (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"Your task '{task}' is HIGH priority"
    case "medium":
        reminder = f"Your task '{task}' is MEDIUM priority"
    case "low":
        reminder = f"Your task '{task}' is LOW priority"
    case _:
        reminder = f"Your task '{task}' has an unspecified priority"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"

print(reminder)
