import psycopg2


def create_tables(conn):  # Функция, создающая структуру БД (таблицы)
    with conn.cursor() as cur:
        cur.execute("""
                create table if not exists clients(
                id serial primary key,
                name varchar(50) not null,
                surname varchar(50) not null,
                email varchar(50) not null
                );

                create table if not exists phones(
                number integer not null unique,
                client_id integer references Clients(id)
                );
                """)
        conn.commit()


def add_client_manual(conn):  # Функция, позволяющая добавить нового клиента
    entered_name = input("Введите имя: ")
    entered_surname = input("Введите фамилию: ")
    entered_email = input("Введите почту: ")
    with conn.cursor() as cur:
        cur.execute("""
                insert into clients(name, surname, email) values(%s, %s, %s) returning id;
                """, (entered_name, entered_surname, entered_email))
        print(f'Айди добавленной записи: {cur.fetchone()[0]}.')


def add_client(conn, name, surname, email):  # Функция, позволяющая добавить нового клиента
    with conn.cursor() as cur:
        cur.execute("""
                insert into clients(name, surname, email) values(%s, %s, %s) returning id;
                """, (name, surname, email))
        print(f'Айди добавленной записи: {cur.fetchone()[0]}.')


def add_phone(conn, client_id, phone):  # Функция, позволяющая добавить телефон для существующего клиента
    with conn.cursor() as cur:
        cur.execute("""
                insert into phones(client_id, number) values(%s, %s) returning client_id;
                """, (client_id, phone))
        print(f'Для клиента с айди {cur.fetchone()[0]} успешно добавлен номер {phone}.') #todo: сделать проверку на наличие искомого айди перед выполнением запроса


def change_client(conn, client_id, name=None, surname=None, email=None, phones=None): #Функция, позволяющая изменить данные о клиенте
    with conn.cursor() as cur:
        cur.execute("""
                update clients set name=%s where id=%s returning id;
                """, (name, client_id)) #меняем имя
        print(f'Запись клиента с айди {cur.fetchone()[0]} успешно изменена.')#todo: сделать уточнение, что именно нужно менять, и в зависимости от этого, меняем запрос к базе


def delete_phone(conn, client_id, phone): #Функция, позволяющая удалить телефон для существующего клиента
    with conn.cursor() as cur:
        cur.execute("""
                delete from phones where client_id=%s and number=%s returning client_id;
                """, (client_id, phone))
        print(f'Телефон {phone} клиента с айди {cur.fetchone()[0]} успешно удалён.')


def delete_client(conn, client_id): #Функция, позволяющая удалить существующего клиента
    with conn.cursor() as cur:
        cur.execute("""
                delete from clients where id=%s returning id;
                """, (client_id, ))
        print(f'Клиент с айди {cur.fetchone()[0]} успешно удалён.') #todo: придумать механизм удаления зависимостей перед удалением клиента

def find_client(conn, name=None, surname=None, email=None, phone=None): #Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
    with conn.cursor() as cur:
        cur.execute("""
                SELECT * FROM clients c
                full JOIN Phones p ON c.id = p.client_id
                WHERE name=%s or surname=%s or email=%s or number=%s;
                """, (name, surname, email, phone))
        result = cur.fetchall()
        if result == []:
            print('Ничего не найдено...')
        else:
            print(f'Клиент успешно найден: {result}')


if __name__ == '__main__':
    with psycopg2.connect(database='clients_base', user='postgres',
                          password='postgres') as conn:  # todo: убрать реквизиты в отдельный файл
        # create_tables(conn)
        # add_client(conn, 'name3', 'surname3', 'email3')
        # add_phone(conn, '5', '12345678')
        # change_client(conn, '1', 'name3')
        # delete_phone(conn, '1', '12345678')
        # delete_client(conn, '1')
        find_client(conn, phone='123123') #name='name3', surname='name1', email='name1', phone='12345'
    conn.close()