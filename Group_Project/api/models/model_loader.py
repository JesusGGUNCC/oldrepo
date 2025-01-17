from . import orders, order_details, recipes, sandwiches, resources, account, customerInfo, dishes, menu, rating

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    customerInfo.Base.metadata.create_all(engine)
    account.Base.metadata.create_all(engine)
    dishes.Base.metadata.create_all(engine)
    menu.Base.metadata.create_all(engine)
    rating.Base.metadata.create_all(engine)