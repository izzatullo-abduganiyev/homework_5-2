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
            cur.execute("""
                SELECT id, task FROM tasks
                """)
            res = cur.fetchall()
            if not res:
                print("Hali hech qanday task yo‘q.")

            else:
                for task_id, task in res:
                    print(f"{task_id}. {task}")

while True:
    command = input("""
    1. Task qo'shish
    2. Tasklarni ko'rish
    3. Task ni o`chirish
    4. Chiqish
    Kiriting: """)


    if command == '1':
        task = input("Vazifani kiriting: ")
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    insert into tasks(task)
                    values (%s)
                """, (task,))
            conn.commit()
        print("Task qo'shildi!")


    elif command == '2':
        show_tasks()

    elif command == '3':
        show_tasks()
        task_id = int(input(''))

