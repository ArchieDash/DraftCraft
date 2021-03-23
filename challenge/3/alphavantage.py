import pyfiglet
import os
import requests
import pandas as pd


def upload(func, ticker, data):
   
    file_name = {
        "O": "overview",
        "T": "time_series",
        "E": "earnings",
        "I": "income"
    }

    with open(f"data/{ticker}/{file_name.get(func)}.csv", "w") as fin:
        fin.write(data)


def main():

    print(pyfiglet.figlet_format("AlphaVantage API", font="smslant"))
    apikey = "TLKJ1KPHYFL689BM"
    url = "https://www.alphavantage.co/query"
    params = {"function": "LISTING_STATUS", "apikey": apikey}
    update = input("Update the listing? Y/N\n").upper()
    if update == "Y":
        with open ("list.csv", "w") as fin:
            fin.write(requests.get(url, params=params).text)
    elif update == "N":
        pass
    df = pd.read_csv("list.csv", index_col="symbol")
    if not os.path.exists("data"):
        os.mkdir("data")

    while True:
        symbol = input("Tiker: ").upper()
        if symbol not in df.index:
            print("No info about given ticker.")
            continue
        if not os.path.exists(os.path.join("data", symbol)):
            os.mkdir(os.path.join("data", symbol))
        query = input("[O]verview\n[T]ime series\n[E]arnings\n\
[I]income\n").upper()

        if query == "Q":
            break

        functions = {
            "O": "OVERVIEW",
            "T": "TIME_SERIES_DAILY",
            "E": "EARNINGS",
            "I": "INCOME_STATEMENT"
        }

        params = {
            "function": functions.get(query),
            "symbol": symbol,
            "datatype": "csv",
            "apikey": apikey
        }

        response = requests.get(url, params=params)
        if query not in functions.keys():
            print("No such option. Please, check your query.")
            continue
        data = response.text
        upload(query, symbol, data)
        print("upload complete")


if __name__ == "__main__":
    main()