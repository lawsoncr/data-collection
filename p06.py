# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 14:15:57 2021

@author: claws
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def bar_plot(df, subcategory):
    df = pd.read_csv('food_cleaned.csv')
    plt.bar(x = df['Month Sold'],
    height = df['Units Sold'])
    ax = plt.gca();
    return ax
def bars_plot(df, starts_with):
    ax = plt.gca();
    return ax
def main_bar():
    subcategory = input('Enter SubCategory: ')
    df = pd.read_csv('food_cleaned.csv')
    bar_plot(df, subcategory)
    plt.show()
def main_bars():
    starts_with = input('Enter starts-with phrase: ')
    df = pd.read_csv('food_cleaned.csv')
    bars_plot(df, starts_with)
    plt.show()
if __name__ == '__main__':
    main_bar()