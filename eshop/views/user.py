from sqlalchemy import select
from .common import *
from eshop.views import dao
from eshop.views.dao import to_array, user, order, to_dict


async def select_users(request):
    async with request.app['db'].acquire() as conn:
        query = select([dao.user])
        result = await conn.fetch(query)
        data = await to_array(result)
    return data, 200


async def select_user_by_id(request):
    if not await validate_uuid(request.match_info['id']):
        return BAD_REQUEST
    async with request.app['db'].acquire() as conn:
        query = select([dao.user]).where(user.c.uuid == request.match_info['id'])
        result = await conn.fetch(query)
        if len(result) == 0:
            return NOT_FOUND
        data = await to_dict(result[0])
    return data, 200


async def insert_user(request):
    async with request.app['db'].acquire() as conn:
        try:
            data = await request.json()
            query = dao.user.insert().values(data)
            query = query.execution_options(autocommit=True)
            await conn.execute(query)
        except:
            return BAD_REQUEST
    return {'message': 'User created'}, 201


async def update_user(request):
    if not await validate_uuid(request.match_info['id']):
        return BAD_REQUEST
    async with request.app['db'].acquire() as conn:
        query = select([dao.user]).where(user.c.uuid == request.match_info['id'])
        result = await conn.fetch(query)
        if len(result) == 0:
            return NOT_FOUND
        try:
            data = await request.json()
            query = dao.user.update().where(user.c.uuid == request.match_info['id']).values(data)
            query = query.execution_options(autocommit=True)
            await conn.execute(query)
        except:
            return BAD_REQUEST
    return {'message': 'User successfully updated'}, 200


async def delete_user(request):
    if not await validate_uuid(request.match_info['id']):
        return BAD_REQUEST
    async with request.app['db'].acquire() as conn:
        query = dao.user.delete().where(user.c.uuid == request.match_info['id'])
        query = query.execution_options(autocommit=True)
        await conn.execute(query)
    return {'message': 'User successfully deleted'}, 200


async def add_order(request):
    if not await validate_uuid(request.match_info['id']):
        return BAD_REQUEST
    if not await validate_uuid(request.match_info['order_id']):
        return BAD_REQUEST
    async with request.app['db'].acquire() as conn:
        query = select([dao.user]).where(user.c.uuid == request.match_info['id'])
        result = await conn.fetch(query)
        if len(result) == 0:
            return NOT_FOUND
        query = select([dao.order]).where(order.c.uuid == request.match_info['order_id'])
        result = await conn.fetch(query)
        if len(result) == 0:
            return NOT_FOUND
        query = dao.user2order.insert().values({'user_id': request.match_info['id'],
                                                'order_id': request.match_info['order_id']})
        query = query.execution_options(autocommit=True)
        await conn.execute(query)
    return {'message': 'Order successfully added to user'}, 200


async def follow_user(request):
    if not await validate_uuid(request.match_info['id']):
        return BAD_REQUEST
    if not await validate_uuid(request.match_info['user_id']):
        return BAD_REQUEST
    async with request.app['db'].acquire() as conn:
        query = select([dao.user]).where(user.c.uuid == request.match_info['id'])
        result = await conn.fetch(query)
        if len(result) == 0:
            return NOT_FOUND
        query = select([dao.user]).where(user.c.uuid == request.match_info['user_id'])
        result = await conn.fetch(query)
        if len(result) == 0:
            return NOT_FOUND
        query = dao.user2user.insert().values({'follower_id': request.match_info['id'],
                                               'following_id': request.match_info['user_id']})
        query = query.execution_options(autocommit=True)
        await conn.execute(query)
    return {'message': 'Successful following'}, 200
