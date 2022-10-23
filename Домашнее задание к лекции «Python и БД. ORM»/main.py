import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale


sql_type = 'postgresql'
sql_username = 'postgres'
sql_password = ''
database_name = 'bookshop_db'


DSN = f'{sql_type}://{sql_username}:{sql_password}@localhost:5432/{database_name}'
engine = sqlalchemy.create_engine(DSN)

# create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# session.add_all([])

requested_publisher_name = input('Введите название издателя: ')

q = session.query(Shop).join(Stock).join(Book).join(Publisher).filter(Publisher.name == requested_publisher_name)
# print(q)
print('Список магазинов, продающих книги запрашиваемого издателя:')
for s in q.all():
    print(s)

# session.commit()

session.close()