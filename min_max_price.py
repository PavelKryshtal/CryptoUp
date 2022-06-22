import pymysql
# Import libraries
import json

import datetime as DT
import requests
import time
import pymysql
import socket

class Price:
    def maxprice(self):

        a = 0
        lst = []
        while a < number_of_elements:
            lst.append("")
            lst[a] = results[a]
            lst[a] = str(lst[a])
            lst[a] = lst[a].replace("(", "")
            lst[a] = lst[a].replace(",)", "")
            lst[a] = float(lst[a])
            # print("The lst[", a, "] = ", lst[a])
            # print("The data type is ", type(lst[a]))
            a = a + 1

        # print(lst)

        # Check cryptocurrency changes
        a = 0
        minimum_price = lst[0]
        maximum_price = lst[0]
        while a < number_of_elements:

            if lst[a] > maximum_price:
                # print (a)
                maximum_price = lst[a]
            # print(maximum_price)
            # print("The ", a, "number is -", lst[a], lst[a+1])
            if lst[a] < minimum_price:
                minimum_price = lst[a]
            a = a + 1
        # print(lst)

        print("Maximus price was define - ", maximum_price)
        print("Minimum price was define - ", minimum_price)
