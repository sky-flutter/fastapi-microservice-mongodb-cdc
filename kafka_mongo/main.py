from product_change_stream import ProductChangeStream
from order_change_stream import OrderChangeStream



if __name__ == "__main__":
    orders_stream = OrderChangeStream()
    products_stream = ProductChangeStream()