
from fuctions.Add_task import add_task
from fuctions.Show_tasks import show_tasks
from fuctions.Del_task import delete_task


def start():
    command = input("""
        1. Task qo`shish.
        2. Tasklarni ko`rish.
        3. Task o`chirish.
        4. Chiqish.
        Kiriting: """)
    return command


while True:
    com = start()
    if com == '1':
        task = input("Vazifangizni kiriting: ")
        add_task(task)

    elif com == '2':
        show_tasks()

    elif com == '3':
        show_tasks()
        index = int(input("Ochirmoqhi bolgan task raqami: "))
        delete_task(index)

