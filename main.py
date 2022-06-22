# Import libraries
import json

import datetime as DT
import requests
import time
import pymysql
import socket


class Currency:
    BTC = 1
    while BTC != 0:
        try:
            # Defining Binance API URL
            key = "https://api.binance.com/api/v3/ticker/price?symbol="
            print("Connect to Binance")
            # Making list for multiple crypto's
            currencies = ["BTCUSDT", "DOGEUSDT", "LTCUSDT", "ADAUSDT", "ACHBUSD"]
            j = 0

            # running loop to print all crypto prices
            for i in currencies:
                # completing API for request
                url = key + currencies[j]
                data = requests.get(url)
                data = data.json()
                j = j + 1
                print(f"{data['symbol']} price is {data['price']}")

                # Define time and data
                now = DT.datetime.now(DT.timezone.utc).astimezone()
                time_format = "%H:%M:%S"
                data_format = "%Y-%m-%d"
                time = f"{now:{time_format}}"
                date = f"{now:{data_format}}"

                # Connection to database
                connection = pymysql.connect(host="192.168.0.31", port=3306, user="pavel", passwd="1234",
                                             database="Cryptocurency")
                cursor = connection.cursor()

                create_table = """CREATE TABLE """ + data['symbol'] + """(
                                    DATE text,
                                    TIME text,
                                    PRICE float
                                    );"""
                try:
                    cursor.execute(create_table)
                except:
                    pass
                # Enter data in database
                ArtistTableSql = """INSERT INTO """ + data[
                    'symbol'] + """ (`DATE`, `TIME`, `PRICE`) VALUES ('""" + date + """', '""" + time + """', """ + \
                                 data['price'] + """ )"""

                cursor.execute(ArtistTableSql)
                print(date)
                # Analyze price for chosen currency
                # Get price for current day
                number_of_elements = cursor.execute(
                    """SELECT PRICE FROM """ + data['symbol'] + """ WHERE DATE = '""" + date + """'""")
                print("Number of elements in database response is ", number_of_elements)
                results = cursor.fetchall()
                connection.close()

                # Change data type tuple -> list, and str -> float. Was created new list
                a = 0
                lst = []
                while a < number_of_elements:
                    lst.append("")
                    lst[a] = results[a]
                    lst[a] = str(lst[a])
                    lst[a] = lst[a].replace("(", "")
                    lst[a] = lst[a].replace(",)", "")
                    lst[a] = float(lst[a])
                    a = a + 1

                # Check cryptocurrency changes
                a = 0
                minimum_price = lst[0]
                maximum_price = lst[0]
                while a < number_of_elements:

                    if lst[a] > maximum_price:
                        maximum_price = lst[a]

                    if lst[a] < minimum_price:
                        minimum_price = lst[a]
                    a = a + 1

                price_diff = maximum_price - minimum_price
                diff_percent = 100 * price_diff
                #print(diff_percent)
                diff_percent = diff_percent / minimum_price

                #print("Percent difference - ", diff_percent, "%")
                #print("Price difference - ", price_diff)
                #print("Maximus price was define - ", maximum_price)
                #print("Minimum price was define - ", minimum_price)
                if diff_percent > 1:
                    print("The", data['symbol'], "up more the 1%")

            #BTC = BTC - 1
        except:
            print("Error. Something wrong. Probably problem with internet connection")
