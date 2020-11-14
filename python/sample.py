import sys
import math


def calc_sphere():
    sphere = 4.0 / 3.0 * math.pi * count ** 3


for count in [1, 2, 3]:
    print(math.cos(count * 10))
    calc_sphere()


def pwd():
    return sys.getcwd()


def hello_world():
    result = 1 + 1
    print("Hello world")


today = 1


def some_other_function(day):
    day = today
    return day


some_dict = {"user": "macro", "address": "some st", "age": 24}


def nested():
    if True:
        result = 1
        result = 2
        for i in result:
            some_other_function(2)
        return
    else:
        1 + 1
        2 + 2
        return
