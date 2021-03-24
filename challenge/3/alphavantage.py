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


def update_listing(url, apikey):
    params = {"function": "LISTING_STATUS", "apikey": apikey}
    with open ("list.csv", "w") as fout:
            fout.write(requests.get(url, params=params).text)


def market_info(url, apikey):
    while True:
        query = input("[E]arnings calendar\n[I]PO calendar\n[B]ack\n").upper()
        functions = {"E": "EARNINGS_CALENDAR", "I": "IPO_CALENDAR"}
        if query == "B":
            break
        elif query not in functions.keys():
            print("No such function")
            continue
        params = {"function": functions[query], "apikey": apikey}
        with open (f"{functions[query]}.csv", "w") as fout:
            fout.write(requests.get(url, params=params).text)

        
def ticker_info(url, apikey, df):
    while True:
        symbol = input("Ticker(X for step back): ").upper()
        if symbol not in df.index:
            print("No info about given ticker.")
            continue
        elif symbol == "X":
            break
        if not os.path.exists(os.path.join("data", symbol)):
            os.mkdir(os.path.join("data", symbol))
        while True:    
            query = input("[O]verview\n[T]ime series\n[E]arnings\n\
[I]income\n[B]ack\n").upper()

            if query == "B":
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
            print("UPLOAD COMLETE")


def main():

    print(pyfiglet.figlet_format("AlphaVantage API", font="smslant"))
    apikey = "TLKJ1KPHYFL689BM"
    url = "https://www.alphavantage.co/query"
    query = input("Update the listing? Y/N\n").upper()
    if query == "Y":
        update_listing(url, apikey)
    elif query == "N":
        pass
    df = pd.read_csv("list.csv", index_col="symbol")
    if not os.path.exists("data"):
        os.mkdir("data")

    while True:
        query = input("[M]arket info\n[T]icker info\nE[X]it\n").upper()
        if query == "M":
            market_info(url, apikey)
        elif query == "T":
            ticker_info(url, apikey, df)
        elif query == "X":
            break


if __name__ == "__main__":
    main()