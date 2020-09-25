from sqlalchemy import select

from eshop.views import dao
from eshop.views.common import validate_uuid, BAD_REQUEST, NOT_FOUND


async def select_products(request):
    async with request.app['db'].acquire() as conn:
        query = select([dao.product])
        result = await conn.fetch(query)
        data = await dao.to_array(result)
    return data, 200


async def select_product_by_id(request):
    if not await validate_uuid(request.match_info['id']):
        return BAD_REQUEST
    async with request.app['db'].acquire() as conn:
        query = select([dao.product]).where(dao.product.c.uuid == request.match_info['id'])
        result = await conn.fetch(query)
        if len(result) == 0:
            return NOT_FOUND
        data = await dao.to_dict(result[0])
    return data, 200


async def insert_product(request):
    async with request.app['db'].acquire() as conn:
        try:
            data = await request.json()
            query = dao.product.insert().values(data)
            query = query.execution_options(autocommit=True)
            await conn.execute(query)
        except:
            return BAD_REQUEST
    return {'message': 'Product created'}, 201


async def update_product(request):
    if not await validate_uuid(request.match_info['id']):
        return BAD_REQUEST
    async with request.app['db'].acquire() as conn:
        query = select([dao.product]).where(dao.product.c.uuid == request.match_info['id'])
        result = await conn.fetch(query)
        if len(result) == 0:
            return NOT_FOUND
        try:
            data = await request.json()
            query = dao.product.update().where(dao.product.c.uuid == request.match_info['id']).values(data)
            query = query.execution_options(autocommit=True)
            await conn.execute(query)
        except:
            return BAD_REQUEST
    return {'message': 'Product successfully updated'}, 200


async def delete_product(request):
    if not await validate_uuid(request.match_info['id']):
        return BAD_REQUEST
    async with request.app['db'].acquire() as conn:
        query = dao.product.delete().where(dao.product.c.uuid == request.match_info['id'])
        query = query.execution_options(autocommit=True)
        await conn.execute(query)
    return {'message': 'Product successfully deleted'}, 200
