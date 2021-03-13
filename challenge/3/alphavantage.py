import pyfiglet
import requests

def upload(func, ticker, data):
   
    extensions = {
        "O": "-overview",
        "T": "-ts",
        "E": "-earnings",
        "I": "-income"
    }

    with open(f"alphavantage_data/{ticker}{extensions.get(func)}.csv", "w") as fin:
        fin.write(data)


print(pyfiglet.figlet_format("AlphaVantage API", font="smslant"))
apikey = "TLKJ1KPHYFL689BM"
url = "https://www.alphavantage.co/query"
symbol = input("Tiker: ").upper()
query = input("[O]verview\n[T]ime series\n[E]arnings\n\
[I]income\n").upper()

fuctions = {
    "O": "OVERVIEW",
    "T": "TIME_SERIES_DAILY",
    "E": "EARNINGS",
    "I": "INCOME_STATEMENT"
}

params = {
    "function": fuctions.get(query),
    "symbol": symbol,
    "datatype": "csv",
    "apikey": apikey
}

response = requests.get(url, params=params)
data = response.text
upload(query, symbol, data)
print("upload complete")
