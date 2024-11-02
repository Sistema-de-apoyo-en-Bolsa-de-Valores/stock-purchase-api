# app\infrastructure\interactive_broker\ibkr_client.py

# Comentar las importaciones reales de ibapi (en simulación no se usan)
# from ibapi.client import EClient
# from ibapi.wrapper import EWrapper
# from ibapi.contract import Contract
# from ibapi.order import Order
import threading
import time


# Crear una clase simulada en lugar de EWrapper y EClient
class EClientMock:
    def connect(self, host, port, client_id):
        print(f"Simulating connection to IBKR at {host}:{port} with client ID {client_id}.")

    def run(self):
        print("Simulated API run loop started.")


class EWrapperMock:
    pass


class IBapiMock(EWrapperMock, EClientMock):
    def __init__(self):
        self.next_order_id = 1  # ID simulado para la orden

    def nextValidId(self, order_id: int):
        self.next_order_id = order_id

    def placeOrder(self, order_id, contract, order):
        print(f"Simulating order placement: order_id={order_id}, symbol={contract.symbol}, action={order.action}, quantity={order.total_quantity}, price={order.lmt_price if order.order_type == 'LMT' else 'Market'}")
        print("Simulated order status: Filled")


# Clases de contrato y orden simuladas
class ContractMock:
    def __init__(self):
        self.symbol = ""
        self.sec_type = ""
        self.exchange = ""
        self.currency = ""


class OrderMock:
    def __init__(self):
        self.action = ""
        self.total_quantity = 0
        self.order_type = ""
        self.lmt_price = 0.0


class IBapiClient:
    def __init__(self):
        # Using the mock API class
        self.app = IBapiMock()
        
        # Simulated connection call
        self.app.connect('127.0.0.1', 4002, 0)
        
        # Start the simulated API loop in a separate thread
        api_thread = threading.Thread(target=self.app.run, daemon=True)
        api_thread.start()

        # Remove the loop waiting for next_order_id
        self.app.next_order_id = 1  # Set a default next order ID

    def place_order(self, symbol: str, sec_type: str, exchange: str, quantity: int, order_type: str, price: float):
        # Usar clases simuladas en lugar de Contract y Order
        contract = ContractMock()
        contract.symbol = symbol
        contract.sec_type = sec_type
        contract.exchange = exchange
        contract.currency = "USD"

        order = OrderMock()
        order.action = "BUY"
        order.total_quantity = quantity
        order.order_type = order_type
        if order_type == "LMT":
            order.lmt_price = price

        # Llamada simulada para colocar la orden
        self.app.placeOrder(self.app.next_order_id, contract, order)
        
        # Retorna el ID de orden simulado
        return self.app.next_order_id