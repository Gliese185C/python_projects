import random
from binance.client import Client

class Order:
    def __init__(self,api_key, secret_key):
        try:
            self.api_key = api_key
            self.api_secret = secret_key
            self.client = Client(api_key = self.api_key, api_secret=self.api_secret, testnet=True)
            self.orders = []
        except Exception as e:
            print("Ошибка при подключении к Binance API:", e)

    def create_orders(self,data):
        symbol = data["symbol"]
        type = data["type"]
        timeInForce = data["timeInForce"]
        volume = data["volume"]
        number = data["number"]
        amount_dif = data["amountDif"]
        side = data["side"]
        price_min = data["priceMin"]
        price_max = data["priceMax"]

        try:
            for _ in range(number):
                order_volume = round(volume / number + random.uniform(-amount_dif, amount_dif),2)

                order_price = round(random.uniform(price_min, price_max),2)


                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=type,
                    timeInForce=timeInForce,
                    quantity=order_volume,
                    price=order_price
                )
                print("Ордер успешно создан:", order)
                self.orders.append(order)
        except Exception as e:
            print("Ошибка при создании ордера:", e)

    def view_orders(self):
        for order in self.orders:
            print(order)


    def get_open_orders(self):

        self.orders = self.client.futures_get_open_orders()
        self.view_orders()

    def get_all_orders(self):

        self.orders = self.client.futures_get_all_orders()
        self.view_orders()


data = {
   "symbol": "LTCUSDT",
   "type": "LIMIT",
    "timeInForce": "GTC",
   "volume": 300.0,  # Объем в долларах
   "number": 5,  # На сколько ордеров нужно разбить этот объем
   "amountDif": 50.0,  # Разброс в долларах, в пределах которого случайным образом выбирается объем в верхнюю и нижнюю сторону
   "side": "SELL",  # Сторона торговли (SELL или BUY)
   "priceMin": 85,  # Нижний диапазон цены, в пределах которого нужно случайным образом выбрать цену
   "priceMax": 93  # Верхний диапазон цены, в пределах которого нужно случайным образом выбрать цену
}


api_key = "bb93723cd644653189078056bd64ec077d99cb8f2d7096d1dc0c21cde22e0ead"
api_secret = "ea4d56740931e539f8556baf829f9253a9fc740008f0185779b639077dba4706"
tmp = Order(api_key,api_secret)

tmp.create_orders(data)
tmp.get_open_orders()
