# Import libraries
import json
import telegram_send
import datetime as DT
import requests
import time
import pymysql

import min_max_price


class Currency:
    BTC = 1
    z = 0
    crypto_day = ""
    new_date = "12"

    # percent 1
    used_crypto = []
    per_1 = 0
    used_crypto.append("")
    used_crypto[0] = "1skldnf"

    # percent 2
    used_crypto_2 = []
    per_1_2 = 0
    used_crypto_2.append("")
    used_crypto_2[0] = "1skldnf"

    # percent 3
    used_crypto_3 = []
    per_1_3 = 0
    used_crypto_3.append("")
    used_crypto_3[0] = "1skldnf"

    # percent 4
    used_crypto_4 = []
    per_1_4 = 0
    used_crypto_4.append("")
    used_crypto_4[0] = "1skldnf"

    # percent 5
    used_crypto_5 = []
    per_1_5 = 0
    used_crypto_5.append("")
    used_crypto_5[0] = "1skldnf"

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

                if new_date != date:
                    used_crypto = []
                    per_1 = 0
                    used_crypto.append("")
                    used_crypto[0] = "1skldnf"

                if new_date != date:
                    new_date = ""

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
                    print("Spreadsheet already exist")
                # Enter data in database
                ArtistTableSql = """INSERT INTO """ + data[
                    'symbol'] + """ (`DATE`, `TIME`, `PRICE`) VALUES ('""" + date + """', '""" + time + """', """ + \
                                 data['price'] + """ )"""
                cursor.execute(ArtistTableSql)

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

                crypto_name = data['symbol']


                # Crypto 1 check existing on the list
                per = 0
                while per != per_1:
                    if used_crypto[per] == data['symbol']:
                        break
                    per = per + 1

                # Crypto 2 check existing on the list
                per_0_2 = 0
                while per_0_2 != per_1_2:
                    if used_crypto_2[per_0_2] == data['symbol']:
                        break
                    per_0_2 = per_0_2 + 1

                # Crypto 3 check existing
                per_0_3 = 0
                while per_0_3 != per_1_3:
                    if used_crypto_3[per_0_3] == data['symbol']:
                        break
                    per_0_3 = per_0_3 + 1


                # Crypto 4 check existing
                per_0_4 = 0
                while per_0_4 != per_1_4:
                    if used_crypto_4[per_0_4] == data['symbol']:
                        break
                    per_0_4 = per_0_4 + 1

                # Crypto 5 check existing
                per_0_5 = 0
                while per_0_5 != per_1_5:
                    if used_crypto_5[per_0_5] == data['symbol']:
                        break
                    per_0_5 = per_0_5 + 1

                if diff_percent > 3 and used_crypto_5[per_0_5] != data['symbol']:
                    print("The ", data['symbol'], " up more the 3%")
                    telegram_send.send(messages=["The " + crypto_name + " change more the 3%"])
                    used_crypto_5.append("")
                    used_crypto_5[per_1_5] = data['symbol']

                    per_1_5 = per_1_5 + 1
                    new_date = date
                elif diff_percent > 7 and used_crypto_4[per_0_4] != data['symbol']:
                    print("The ", data['symbol'], " up more the 7%")
                    telegram_send.send(messages=["The " + crypto_name + " change more the 7%"])
                    used_crypto_4.append("")
                    used_crypto_4[per_1_4] = data['symbol']

                    per_1_4 = per_1_4 + 1
                    new_date = date
                elif diff_percent > 13 and used_crypto_3[per_0_3] != data['symbol']:
                    print("The ", data['symbol'], " up more the 13%")
                    telegram_send.send(messages=["The " + crypto_name + " change more the 13%"])
                    used_crypto_3.append("")
                    used_crypto_3[per_1_3] = data['symbol']

                    per_1_3 = per_1_3 + 1
                    new_date = date
                elif diff_percent > 20 and used_crypto_2[per_0_2] != data['symbol']:
                    print("The ", data['symbol'], " up more the 20%")
                    telegram_send.send(messages=["The " + crypto_name + " change more the 20%"])
                    used_crypto_2.append("")
                    used_crypto_2[per_1_2] = data['symbol']

                    per_1_2 = per_1_2 + 1
                    new_date = date
                # This part will execute 1 time every day if cryptocurrency price change more than on 1 percent and
                # message for chosen crypto wasn't already send in this day
                elif diff_percent > 30 and used_crypto[per] != data['symbol']:
                    print("The ", data['symbol'], " up more the 30%")
                    telegram_send.send(messages=["The " + crypto_name + " change more the 30%"])
                    used_crypto.append("")
                    used_crypto[per_1] = data['symbol']

                    per_1 = per_1 + 1
                    new_date = date
                print("used_crypto[per] = ", used_crypto[per])
                print("per = ", per)
                print("data['symbol'] = ", data['symbol'])

                print("used_crypto[per_1] = ", used_crypto[per_1])
                print("per_1 = ", per_1)

        except:
            print("Error. Something wrong. Probably problem with internet connection")
