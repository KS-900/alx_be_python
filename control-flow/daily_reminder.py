task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = task + " is a high priority task"
    case "medium":
        reminder = task + " is a medium priority task"
    case "low":
        reminder = task + " is a low priority task"
if time_bound == "yes":
    print(f"Reminder: '{reminder}' that requires immediate attention today!")
else:
    print(f"Note: + '{reminder}'. + Consider completing it when you have free time.")
