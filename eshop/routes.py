from .views import api


def setup_routes(app):
    # user routes
    app.router.add_route('GET', '/users', api.get_users)
    app.router.add_route('GET', '/users/{id}', api.get_user)
    app.router.add_route('POST', '/users', api.create_user)
    app.router.add_route('PUT', '/users/{id}', api.update_user)
    app.router.add_route('DELETE', '/users/{id}', api.delete_user)
    app.router.add_route('PUT', '/users/{id}/orders/{order_id}', api.add_order_to_user)
    app.router.add_route('PUT', '/users/{id}/follow/{user_id}', api.follow_user)

    # order routes
    app.router.add_route('GET', '/orders', api.get_orders)
    app.router.add_route('GET', '/orders/{id}', api.get_order)
    app.router.add_route('POST', '/orders', api.create_order)
    app.router.add_route('PUT', '/orders/{id}', api.update_order)
    app.router.add_route('DELETE', '/orders/{id}', api.delete_order)
    app.router.add_route('PUT', '/orders/{id}/products/{product_id}', api.add_product_to_order)

    # product routes
    app.router.add_route('GET', '/products', api.get_products)
    app.router.add_route('GET', '/products/{id}', api.get_product)
    app.router.add_route('POST', '/products', api.create_product)
    app.router.add_route('PUT', '/products/{id}', api.update_product)
    app.router.add_route('DELETE', '/products/{id}', api.delete_product)
