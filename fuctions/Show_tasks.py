def show_tasks():
    with open("tasks.txt", "r", encoding="utf-8") as f:
        tasks = f.readlines()
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task.strip()}")
