import psycopg2


def create_tables(conn, cur):  # Функция, создающая структуру БД (таблицы)
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


def add_client_manual(conn, cur):  # Функция, позволяющая добавить нового клиента вручную
    entered_name = input("Введите имя: ")
    entered_surname = input("Введите фамилию: ")
    entered_email = input("Введите почту: ")
    cur.execute("""
            insert into clients(name, surname, email) values(%s, %s, %s) returning id;
            """, (entered_name, entered_surname, entered_email))
    print(f'Айди добавленной записи: {cur.fetchone()[0]}.')


def add_client(conn, cur, name, surname, email):  # Функция, позволяющая добавить нового клиента
    cur.execute("""
            insert into clients(name, surname, email) values(%s, %s, %s) returning id;
            """, (name, surname, email))
    print(f'Айди добавленной записи: {cur.fetchone()[0]}.')


def add_phone(conn, cur, client_id, phone):  # Функция, позволяющая добавить телефон для существующего клиента
    cur.execute("""
            insert into phones(client_id, number) values(%s, %s) returning client_id;
            """, (client_id, phone))
    print(f'Для клиента с айди {cur.fetchone()[0]} успешно добавлен номер {phone}.') #todo: сделать проверку на наличие искомого айди перед выполнением запроса


def change_client(conn, cur, client_id, name=None, surname=None, email=None, phones=None): #Функция, позволяющая изменить данные о клиенте
    cur.execute(f"""update clients set
                name = case when '{name}' = 'None' then name else '{name}' end,
                surname = case when '{surname}' = 'None' then surname else '{surname}' end,
                email = case when '{email}' = 'None' then email else '{email}' end
                where id={client_id} returning id;""")
    if phones != None:
        cur.execute(f"""update phones
        set number = {phones}
        where client_id={client_id} returning client_id;""")

    print(f'Запись клиента с айди {cur.fetchone()[0]} успешно изменена.')


def delete_phone(conn, cur, client_id, phone): #Функция, позволяющая удалить телефон для существующего клиента
    cur.execute("""
            delete from phones where client_id=%s and number=%s returning client_id;
            """, (client_id, phone))
    print(f'Телефон {phone} клиента с айди {cur.fetchone()[0]} успешно удалён.')


def delete_client(conn, cur, client_id): #Функция, позволяющая удалить существующего клиента
    cur.execute("""
            delete from clients where id=%s returning id;
            """, (client_id, ))
    print(f'Клиент с айди {cur.fetchone()[0]} успешно удалён.') #todo: придумать механизм удаления зависимостей перед удалением клиента

def find_client(conn, cur, name=None, surname=None, email=None, phone=None): #Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
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
        with conn.cursor() as cur:
            # create_tables(conn, cur)
            # add_client(conn, cur, 'name3', 'surname3', 'email3')
            # add_phone(conn, cur, '5', '12345678')
            change_client(conn, cur, client_id='5', name='name5', email='email@email.ru') #, phones='1231231'
            # delete_phone(conn, cur, '1', '12345678')
            # delete_client(conn, cur, '1')
            # find_client(conn, cur, phone='123123') #name='name3', surname='name1', email='name1', phone='12345'
    conn.close()