def add_tasks(tasks):
    with open('tasks.txt', "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(f"{task['id']} {task['task']}\n")
