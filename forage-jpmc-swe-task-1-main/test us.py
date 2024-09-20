import json
import random
import urllib.request

# API endpoint for retrieving stock data
STOCK_API_URL = "http://localhost:8080/query?id={}"

# Number of requests to send
REQUEST_COUNT = 500


def extractStockData(stock_info):
    """ Extract key values from the stock info to generate a data entry """
    stock_symbol = stock_info['stock']
    highest_bid = float(stock_info['top_bid']['price'])
    lowest_ask = float(stock_info['top_ask']['price'])
    calculated_price = (highest_bid + lowest_ask) / 2
    return stock_symbol, highest_bid, lowest_ask, calculated_price


def computePriceRatio(price_one, price_two):
    """ Compute the ratio of price_one to price_two, handling division by zero """
    if price_two == 0:
        return None  # Prevent division by zero errors
    return price_one / price_two


# Main execution flow
if __name__ == "__main__":
    # Send requests and process stock data
    for _ in iter(range(REQUEST_COUNT)):
        stock_data = json.loads(urllib.request.urlopen(STOCK_API_URL.format(random.random())).read())

        """ Store stock prices and print relevant information """
        stock_prices = {}
        for stock_entry in stock_data:
            symbol, bid, ask, current_price = extractStockData(stock_entry)
            stock_prices[symbol] = current_price  # Store the current price in a dictionary
            print("Data for %s: (Bid: %s, Ask: %s, Calculated Price: %s)" % (symbol, bid, ask, current_price))

        """ Calculate and display the price ratio between two specific stocks """
        if "ABC" in stock_prices and "DEF" in stock_prices:
            price_ratio = computePriceRatio(stock_prices["ABC"], stock_prices["DEF"])
            print("Price Ratio between ABC and DEF: %s" % price_ratio)
