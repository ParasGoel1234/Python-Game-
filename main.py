import numpy as np
import pandas as pd
from matplotlib import pyplot as mp

print("hi whatsapp welcome to pycharm\n")
prices = [[23,22,11], [11,44,76], [33,55,42],[32,21,89]]
# simple_dataframe = pd.DataFrame(prices)
# print("My data frame: \n", simple_dataframe)
# header_dataframe = pd.DataFrame(prices, columns =['jan', 'feb', 'march'])
# print("the new data frame \n", header_dataframe)
#
# print("the head is:\n", simple_dataframe.head)
# Record = pd.read_csv("data.csv")
# print(Record["SYMBOL"],[12])
mp.plot(prices)
mp.show(prices)