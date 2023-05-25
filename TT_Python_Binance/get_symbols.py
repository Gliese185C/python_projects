from binance.client import Client

api_key = "bb93723cd644653189078056bd64ec077d99cb8f2d7096d1dc0c21cde22e0ead"
api_secret = "ea4d56740931e539f8556baf829f9253a9fc740008f0185779b639077dba4706"
client = Client(api_key=api_key, api_secret=api_secret, testnet=True)


data = client.get_exchange_info()


with open("symbols.csv",'w',encoding='utf-8') as file:
    line = ""
    for item in data['symbols']:
        line += item['symbol'] + ','
    file.write(line)
