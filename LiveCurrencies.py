

import json
import requests
from core.numbers__ import fixed_set_precision_float
from core.aesthetics import *
from core.system import (
    clearscreen
)
from time import sleep



def USD_to_LEI():
    """ -> float .{2}"""
    current_usd_rate_url = "https://api.exchangeratesapi.io/latest?base=USD"
    response = requests.get(current_usd_rate_url)
    usd_to_lei = response.json()["rates"]["RON"]
    return fixed_set_precision_float(usd_to_lei, 2)


def EURO_to_LEI():
    """ -> float .{2}"""
    current_usd_rate_url = "https://api.exchangeratesapi.io/latest?base=EUR"
    response = requests.get(current_usd_rate_url)
    euro_to_lei= response.json()["rates"]["RON"]
    return fixed_set_precision_float(euro_to_lei, 2)


def PrintStats():
    usd_to_lei = USD_to_LEI()
    euro_to_lei = EURO_to_LEI()
    print(f"{green_bold('1')} USD == {usd_to_lei} LEI")
    print(f"{green_bold('1')} EURO == {euro_to_lei} LEI")


def LiveCurrencies():
    while 1:
        clearscreen()
        PrintStats()
        sleep(1)
         



if __name__ == '__main__':
    LiveCurrencies()

    # asta s-ar putea sa fie solutia pentru ca toate sunt cu bani acum
    # https://fcsapi.com/document/forex-api

