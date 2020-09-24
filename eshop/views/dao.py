from sqlalchemy import Table, Text, VARCHAR, MetaData, Column, Integer
from sqlalchemy.dialects.postgresql import UUID

meta = MetaData()
user = Table(
    'users', meta,
    Column('uuid', UUID, primary_key=True),  # поменять на id
    Column('firstname', VARCHAR(50)),
    Column('surname', VARCHAR(50)),
    Column('middlename', VARCHAR(50)),
    Column('sex', VARCHAR(1)),
    Column('age', Integer)
)

user2order = Table(
    'users2orders', meta,
    Column('uuid', UUID, primary_key=True),
    Column('user_id', UUID),
    Column('order_id', UUID)
)

user2user = Table(
    'users2users', meta,
    Column('uuid', UUID, primary_key=True),
    Column('follower_id', UUID),
    Column('following_id', UUID)
)

order2product = Table(
    'orders2products', meta,
    Column('uuid', UUID, primary_key=True),
    Column('order_id', UUID),
    Column('product_id', UUID)
)

order = Table(
    'orders', meta,
    Column('uuid', UUID, primary_key=True),
    Column('number', Integer)
)


# метод преобразования объекта ORM в cловарь
async def to_dict(data):
    result = {key: value for key, value in data.items() if not str(value).startswith('__')}
    result['uuid'] = str(result['uuid'])
    return result


# метод преобразования списка объектов ORM в список словарей
async def to_array(data):
    result = []
    for i in range(len(data)):
        result.append(await to_dict(data[i]))
    return result
