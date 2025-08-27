import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="homework",
        user="postgres",
        password="izzatullo001.ab",
        host="localhost",
        port="5432"
    )

def show_tasks():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("select id, task from taasks")
            res = cur.fetchall()
            if not res:
                print("hali hech qanday task yo‘q.")
            else:
                for task_id, task in res:
                    print(f"{task_id}. {task}")

def del_task():
    task_id = int(input('ochiradigan task id si: '))
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("delete from taasks where id = %s", (task_id,))
        conn.commit()
    print("task o'chirildi!")

def update_task():
    task_id = int(input("o'zgartirmoqchi bo'lgan task id si: "))
    new_task = input("yangi taskni kiriting: ")
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("update taasks set task = %s where id = %s", (new_task, task_id))
        conn.commit()
    print("task yangilandi!")

def start():
    while True:
        command = input("""
        1. task qo'shish
        2. tasklarni ko'rish
        3. taskni o'chirish
        4. taskni o'zgartirish
        5. chiqish
        kiriting: """)

        if command == '1':
            task = input("vazifani kiriting: ")
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("insert into taasks(task) values (%s)", (task,))
                conn.commit()
            print("task qo'shildi!")

        elif command == '2':
            show_tasks()

        elif command == '3':
            show_tasks()
            del_task()

        elif command == '4':
            show_tasks()
            update_task()

        elif command == '5':
            print('yakunlandi')
            break

        else:
            print("noto'g'ri buyruq!")

start()
