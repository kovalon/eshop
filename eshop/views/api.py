import aiohttp
from . import user
from .product import *
from . import order
from . import dao


# policy - слой бизнес-логики
# здесь же в виде swagger'а представлен view слой:
# по ссылке http://localhost:8080/api/v1/doc предоставляется
# интерфейс для взаимодействия с приложением

async def get_users(request):
    """
        ---
        description: This end-point allow to delete order.
        tags:
        - User
        produces:
        - application/json
        responses:
            "200":
                description: Got list of users
            "500":
                description: Internal Server Error
    """
    result, status = await user.select_users(request)
    return aiohttp.web.json_response(result, status=status)


async def get_user(request):
    """
        ---
        description: This end-point allow to delete order.
        tags:
        - User
        produces:
        - application/json
        parameters:
          - name: id
            in: path
            required: true
            type: string
            description: user id (in uuid format)
        responses:
            "200":
                description: Got user data
            "400":
                description: Bad Request
            "404":
                description: Not Found
            "500":
                description: Internal Server Error
    """
    result, status = await user.select_user_by_id(request)
    return aiohttp.web.json_response(result, status=status)


async def create_user(request):
    """
        ---
        description: This end-point allow to create user.
        tags:
        - User
        produces:
        - application/json
        requestBody:
            content:
                application/json:
                    schema:
                        title: createuser
                        type: object
                        properties:
                            firstname:
                                type: string
                                description: user's name
                            surname:
                                type: string
                                description: user's surname
                            middlename:
                                type: string
                                description: user's middlename
                            sex:
                                type: string
                                description: user's sex, 'M' or 'F'
                            age:
                                type: integer
                                format: int64
                                description: user's age

                        required:
                            - name
                            - surname
                            - middlename
                            - sex
                            - age
        responses:
            "201":
                description: User created
            "400":
                description: Bad Request
            "500":
                description: Internal Server Error
    """
    result, status = await user.insert_user(request)
    return aiohttp.web.json_response(result, status=status)


async def update_user(request):
    """
        ---
        description: This end-point allow to update user.
        tags:
        - User
        produces:
        - application/json
        parameters:
          - name: id
            in: path
            required: true
            type: string
            description: user id (in uuid format)
        requestBody:
            content:
                application/json:
                    schema:
                        title: updateuser
                        type: object
                        properties:
                            firstname:
                                type: string
                                description: user's name
                            surname:
                                type: string
                                description: user's surname
                            middlename:
                                type: string
                                description: user's middlename
                            sex:
                                type: string
                                description: user's sex, 'M' or 'F'
                            age:
                                type: integer
                                format: int64
                                description: user's age

                        required:
                            - name
                            - surname
                            - middlename
                            - sex
                            - age
        responses:
            "200":
                description: User updated
            "400":
                description: Bad Request
            "404":
                description: Not Found
            "500":
                description: Internal Server Error
    """
    result, status = await user.update_user(request)
    return aiohttp.web.json_response(result, status=status)


async def delete_user(request):
    """
        ---
        description: This end-point allow to delete user.
        tags:
        - User
        produces:
        - application/json
        parameters:
          - name: id
            in: path
            required: true
            type: string
            description: user id (in uuid format)
        responses:
            "200":
                description: User deleted
            "400":
                description: Bad Request
            "404":
                description: Not Found
            "500":
                description: Internal Server Error
    """
    result, status = await user.delete_user(request)
    return aiohttp.web.json_response(result, status=status)


async def add_order_to_user(request):
    """
        ---
        description: This end-point allow to add order to product.
        tags:
        - User
        produces:
        - application/json
        parameters:
          - name: id
            in: path
            required: true
            type: string
            format: uuid
            description: user id (in uuid format)
          - name: order_id
            in: path
            required: true
            type: string
            format: uuid
            description: order id (in uuid format)
        responses:
            "200":
                description: Order successfully added to user
            "400":
                description: Bad Request
            "404":
                description: Not Found
            "500":
                description: Internal Server Error
    """
    result, status = await user.add_order(request)
    return aiohttp.web.json_response(result, status=status)


async def follow_user(request):
    """
        ---
        description: This end-point allow to add order to product.
        tags:
        - User
        produces:
        - application/json
        parameters:
          - name: id
            in: path
            required: true
            type: string
            format: uuid
            description: user id who follows (in uuid format)
          - name: user_id
            in: path
            required: true
            type: string
            format: uuid
            description: following user id (in uuid format)
        responses:
            "200":
                description: Order successfully added to user
            "400":
                description: Bad Request
            "404":
                description: Not Found
            "500":
                description: Internal Server Error
    """
    result, status = await user.follow_user(request)
    return aiohttp.web.json_response(result, status=status)


async def get_orders(request):
    """
        ---
        description: This end-point allow to get list of orders.
        tags:
        - Order
        produces:
        - application/json
        responses:
            "200":
                description: Got list of orders
            "404":
                description: Not Found
            "500":
                description: Internal Server Error
    """
    result, status = await order.select_orders(request)
    return aiohttp.web.json_response(result, status=status)


async def get_order(request):
    """
        ---
        description: This end-point allow to get order.
        tags:
        - Order
        produces:
        - application/json
        parameters:
          - name: id
            in: path
            required: true
            type: string
            format: uuid
            description: order id (in uuid format)
        responses:
            "200":
                description: Got order data
            "400":
                description: Bad Request
            "404":
                description: Not Found
            "500":
                description: Internal Server Error
    """
    result, status = await order.select_order_by_id(request)
    return aiohttp.web.json_response(result, status=status)


async def create_order(request):
    """
        ---
        description: This end-point allow to create order.
        tags:
        - Order
        produces:
        - application/json
        requestBody:
            content:
                application/json:
                    schema:
                        title: createorder
                        type: object
                        properties:
                            number:
                                type: integer
                                description: order's number
                        required:
                            - number
        responses:
            "201":
                description: Order created
            "400":
                description: Bad Request
            "500":
                description: Internal Server Error
    """
    result, status = await order.insert_order(request)
    return aiohttp.web.json_response(result, status=status)


async def update_order(request):
    """
        ---
        description: This end-point allow to update order.
        tags:
        - Order
        produces:
        - application/json
        parameters:
          - name: id
            in: path
            required: true
            type: string
            description: order id (in uuid format)
        requestBody:
            content:
                application/json:
                    schema:
                        title: updateorder
                        type: object
                        properties:
                            number:
                                type: integer
                                description: order's number
                        required:
                            - number
        responses:
            "200":
                description: Order updated
            "400":
                description: Bad Request
            "404":
                description: Not Found
            "500":
                description: Internal Server Error
    """
    result, status = await order.update_order(request)
    return aiohttp.web.json_response(result, status=status)


async def delete_order(request):
    """
        ---
        description: This end-point allow to delete order.
        tags:
        - Order
        produces:
        - application/json
        parameters:
          - name: id
            in: path
            required: true
            type: string
            description: order id (in uuid format)
        responses:
            "200":
                description: Order deleted
            "400":
                description: Bad Request
            "404":
                description: Not Found
            "500":
                description: Internal Server Error
    """
    result, status = await order.delete_order(request)
    return aiohttp.web.json_response(result, status=status)


async def get_products(request):
    """
        ---
        description: This end-point allow to list of products.
        tags:
        - Product
        produces:
        - application/json
        responses:
            "200":
                description: Got list of users
            "400":
                description: Bad Request
            "404":
                description: Not Found
            "500":
                description: Internal Server Error
    """
    obj = {'message': 'List of products'}
    return aiohttp.web.json_response(obj)


async def get_product(request):
    """
        ---
        description: This end-point allow to get product data.
        tags:
        - Product
        produces:
        - application/json
        parameters:
          - name: id
            in: path
            required: true
            type: string
            format: uuid
            description: product id (in uuid format)
        responses:
            "200":
                description: Got product data
            "400":
                description: Bad Request
            "404":
                description: Not Found
            "500":
                description: Internal Server Error
    """
    obj = {'message': 'product data'}
    return aiohttp.web.json_response(obj)


async def create_product(request):
    """
        ---
        description: This end-point allow to create product.
        tags:
        - Product
        produces:
        - application/json
        requestBody:
            content:
                application/json:
                    schema:
                        title: createproduct
                        type: object
                        properties:
                            name:
                                type: string
                                description: order's name
                            description:
                                type: string
                                description: description of product
                            price:
                                type: string
                                description: price for product in different currency
                            left_in_stock:
                                type: integer
                                format: int64
                                description: the quantity of product left in stock
                        required:
                            - name
                            - description
                            - price
                            - left_in_stock
        responses:
            "201":
                description: Product created
            "400":
                description: Bad Request
            "500":
                description: Internal Server Error
    """
    obj = {'message': 'Product successfully created'}
    return aiohttp.web.json_response(obj)


async def update_product(request):
    """
        ---
        description: This end-point allow to update order.
        tags:
        - Product
        produces:
        - application/json
        parameters:
          - name: id
            in: path
            required: true
            type: string
            description: product id (in uuid format)
        requestBody:
            content:
                application/json:
                    schema:
                        title: updateuser
                        type: object
                        properties:
                            name:
                                type: string
                                description: order's name
                            description:
                                type: string
                                description: description of product
                            price:
                                type: string
                                description: price for product in different currency
                            left_in_stock:
                                type: integer
                                format: int64
                                description: the quantity of product left in stock

                        required:
                            - name
                            - description
                            - price
                            - left_in_stock
        responses:
            "200":
                description: Product updated
            "400":
                description: Bad Request
            "404":
                description: Not Found
            "500":
                description: Internal Server Error
    """
    obj = {'message': 'Product successfully updated'}
    return aiohttp.web.json_response(obj)


async def delete_product(request):
    """
        ---
        description: This end-point allow to delete order.
        tags:
        - Product
        produces:
        - application/json
        parameters:
          - name: id
            in: path
            required: true
            type: string
            description: product id (in uuid format)
        responses:
            "200":
                description: Product deleted
            "400":
                description: Bad Request
            "404":
                description: Not Found
            "500":
                description: Internal Server Error
    """
    obj = {'message': 'Product successfully deleted'}
    return aiohttp.web.json_response(obj)


async def add_product_to_order(request):
    """
        ---
        description: This end-point allow to add product to order.
        tags:
        - Order
        produces:
        - application/json
        parameters:
          - name: id
            in: path
            required: true
            type: string
            format: uuid
            description: order id (in uuid format)
          - name: product_id
            in: path
            required: true
            type: string
            format: uuid
            description: product id (in uuid format)
        responses:
            "200":
                description: Product successfully added to order
            "400":
                description: Bad request
            "404":
                description: Not Found
            "500":
                description: Internal Server Error
    """
    result, status = await order.add_product(request)
    return aiohttp.web.json_response(result, status=status)
