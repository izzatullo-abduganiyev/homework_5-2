def delete_task(index):
    with open("tasks.txt", "r", encoding="utf-8") as f:
        tasks = f.readlines()

    if 0 < index <= len(tasks):
        del tasks[index - 1]
        with open("tasks.txt", "w", encoding="utf-8") as f:
            f.writelines(tasks)
        print("Task o‘chirildi!")
    else:
        print("Noto‘g‘ri raqam!")
