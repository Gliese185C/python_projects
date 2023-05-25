import random
import unittest
from order import Order

class TestOrder(unittest.TestCase):

    def setUp(self):
        self.order_instance = Order()


    def test_create_orders_success_type_sell(self):
        self.order_instance.orders = []
        # Подготовка тестовых данных
        data = {
            "symbol": "LTCUSDT",
            "type": "LIMIT",
            "timeInForce": "GTC",
            "volume": 300.0,  # Объем в долларах
            "number": 5,  # На сколько ордеров нужно разбить этот объем
            "amountDif": 50.0,
            # Разброс в долларах, в пределах которого случайным образом выбирается объем в верхнюю и нижнюю сторону
            "side": "SELL",  # Сторона торговли (SELL или BUY)
            "priceMin": 85,  # Нижний диапазон цены, в пределах которого нужно случайным образом выбрать цену
            "priceMax": 93  # Верхний диапазон цены, в пределах которого нужно случайным образом выбрать цену
        }



        # Вызов тестируемой функции
        self.order_instance.create_orders(data)

        # Проверка, что все ордеры были успешно созданы и добавлены в orders
        self.assertEqual(len(self.order_instance.orders), data['number'])

    def test_create_orders_success_type_buy(self):
        self.order_instance.orders = []

        # Подготовка тестовых данных
        data = {
            "symbol": "LTCUSDT",
            "type": "LIMIT",
            "timeInForce": "GTC",
            "volume": 300.0,
            "number": 5,
            "amountDif": 50.0,
            "side": "BUY",
            "priceMin": 85,
            "priceMax": 93
        }



        # Вызов тестируемой функции
        self.order_instance.create_orders(data)

        # Проверка, что все ордеры были успешно созданы и добавлены в orders
        self.assertEqual(len(self.order_instance.orders), data['number'])



    def test_create_orders_random_values(self):
        self.order_instance.orders = []
        data = {
            "symbol": "LTCUSDT",
            "type": "LIMIT",
            "timeInForce": "GTC",
            "volume": random.randint(100,1000),
            "number": random.randint(1,20),
            "amountDif": random.randint(1,500),
            "side": "SELL",
            "priceMin": random.randint(-10000,10000),
            "priceMax": random.randint(10000,20000)
        }

        # Вызов тестируемой функции
        self.order_instance.create_orders(data)

        #Проверка, что создался хотя бы один ордер либо вообще не создался
        self.assertGreaterEqual(len(self.order_instance.orders),0)

    def test_null_values(self):
        self.order_instance.orders = []
        data = {
            "symbol": "LTCUSDT",
            "type": "LIMIT",
            "timeInForce": "GTC",
            "volume": None,
            "number": None,
            "amountDif": None,
            "side": "SELL",
            "priceMin": None,
            "priceMax": None
        }

        self.order_instance.create_orders(data)

        self.assertEqual(len(self.order_instance.orders), 0)

    def test_random_symbol(self):
        self.order_instance.orders = []
        with open('symbols.csv', 'r', encoding='utf-8') as file:
            symbols = file.read().split(',')

        # Подготовка тестовых данных
        data = {
            "symbol": random.choice(symbols),
            "type": "LIMIT",
            "timeInForce": "GTC",
            "volume": 300.0,
            "number": 5,
            "amountDif": 50.0,
            "side": "SELL",
            "priceMin": 85,
            "priceMax": 93
        }

        self.order_instance.create_orders(data)

        self.assertEqual(len(self.order_instance.orders), 0)

    def test_negative_values(self):
        self.order_instance.orders = []
        data = {
            "symbol": 'LTCUSDT',
            "type": "LIMIT",
            "timeInForce": "GTC",
            "volume": -300,
            "number": -5,
            "amountDif": -50.0,
            "side": "SELL",
            "priceMin": -93,
            "priceMax": -85
        }

        self.order_instance.create_orders(data)

        self.assertEqual(len(self.order_instance.orders), 0)

if __name__ == '__main__':
    unittest.main()
