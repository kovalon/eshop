from sqlalchemy import select

from eshop.views import dao
from eshop.views.common import validate_uuid, BAD_REQUEST, NOT_FOUND
from eshop.views.dao import to_array, user, order, product, to_dict


async def select_orders(request):
    async with request.app['db'].acquire() as conn:
        query = select([dao.order])
        result = await conn.fetch(query)
        data = await to_array(result)
    return data, 200


async def select_order_by_id(request):
    if not await validate_uuid(request.match_info['id']):
        return BAD_REQUEST
    async with request.app['db'].acquire() as conn:
        query = select([dao.order]).where(order.c.uuid == request.match_info['id'])
        result = await conn.fetch(query)
        if len(result) == 0:
            return NOT_FOUND
        data = await to_dict(result[0])
    return data, 200


async def insert_order(request):
    async with request.app['db'].acquire() as conn:
        try:
            data = await request.json()
            query = dao.order.insert().values(data)
            query = query.execution_options(autocommit=True)
            await conn.execute(query)
        except:
            return BAD_REQUEST
    return {'message': 'Order created'}, 201


async def update_order(request):
    if not await validate_uuid(request.match_info['id']):
        return BAD_REQUEST
    async with request.app['db'].acquire() as conn:
        query = select([dao.order]).where(order.c.uuid == request.match_info['id'])
        result = await conn.fetch(query)
        if len(result) == 0:
            return NOT_FOUND
        try:
            data = await request.json()
            query = dao.order.update().where(order.c.uuid == request.match_info['id']).values(data)
            query = query.execution_options(autocommit=True)
            await conn.execute(query)
        except:
            return BAD_REQUEST
    return {'message': 'Order successfully updated'}, 200


async def delete_order(request):
    if not await validate_uuid(request.match_info['id']):
        return BAD_REQUEST
    async with request.app['db'].acquire() as conn:
        query = dao.order.delete().where(order.c.uuid == request.match_info['id'])
        query = query.execution_options(autocommit=True)
        await conn.execute(query)
    return {'message': 'Order successfully deleted'}, 200


async def add_product(request):
    if not await validate_uuid(request.match_info['id']):
        return BAD_REQUEST
    if not await validate_uuid(request.match_info['product_id']):
        return BAD_REQUEST

    async with request.app['db'].acquire() as conn:
        query = select([dao.order]).where(order.c.uuid == request.match_info['id'])
        result = await conn.fetch(query)
        if len(result) == 0:
            return NOT_FOUND
        query = select([dao.product]).where(product.c.uuid == request.match_info['product_id'])
        result = await conn.fetch(query)
        if len(result) == 0:
            return NOT_FOUND
        left_in_stock = result[0]['left_in_stock']
        if left_in_stock == 0:
            return {'error': 'No food left in stock'}, 400
        query = dao.order2product.insert().values({'order_id': request.match_info['id'],
                                                   'product_id': request.match_info['product_id']})
        query = query.execution_options(autocommit=True)
        await conn.execute(query)
        query = dao.product.update().where(product.c.uuid == request.match_info['product_id'])\
            .values({'left_in_stock': left_in_stock})
        query = query.execution_options(autocommit=True)
        await conn.execute(query)
    return {'message': 'Product successfully added to order'}, 200
