# Luke Murdock, This file uses the libraries matplotlib and pandas for the updated battle simulator, such as for Stat Visuals, Data Analysis, and Character Comparison

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from projects.battle_simulator.file_handler import read_file, intput, find

def visual(): # Shows a visual bar graph of a desired character's stats in a new window
    characs = read_file()
    charac_name, ind = find("Which character do you want to see a stat visual of?:\n", characs)
    if ind == -1:
        print(f"\n{charac_name} Can't Be Found")
        return
    stats = ('Health', 'Strength', 'Defense', 'Speed')
    stat_counts = {'Stat': np.array([characs[ind]["Health"], characs[ind]["Strength"], characs[ind]["Defense"], characs[ind]["Speed"]])}
    width = 0.6
    fig, ax = plt.subplots()
    bottom = np.zeros(4)
    for stat, stat_count in stat_counts.items():
        p = ax.bar(stats, stat_count, width, label=stat, bottom=bottom)
        bottom += stat_count
        ax.bar_label(p, label_type='center')
    ax.set_title("Character's Stats")
    ax.legend()
    plt.show()

def analysis(): # Displays a data analysis, including the mean, median, and mode, for a desired character's stats
    characs = read_file()
    charac_name, ind = find("Which character do you want to see a data analysis of?:\n", characs)
    if ind == -1:
        print(f"\n{charac_name} Can't Be Found")
        return
    data = {'stats': [characs[ind]["Health"], characs[ind]["Strength"], characs[ind]["Defense"], characs[ind]["Speed"]]}
    df = pd.DataFrame(data)
    mean = df['stats'].mean()
    print(f'\nMean of Stats: {mean}')
    median = df['stats'].median()
    print(f'Median of Stats: {median}')
    mode = df['stats'].mode()
    print(f'Mode of Stats: {'None' if '1   ' in str(mode) else str(mode)[5:7]}')

def characs_visual_analysis(): # Shows a bargraph of all of either the characters' average stat amounts, the characters' minimums, or the characters' maximums in a new window
    characs = read_file()
    which = intput("Mean(1) Median(2) Mode(3) Min(4) Max(5)\n", 1,5)
    names = []
    datas = []
    for charac in characs:
        df = pd.DataFrame({'stats': [charac["Health"], charac["Strength"], charac["Defense"], charac["Speed"]]})
        if which == 1:
            title = 'Mean'
            data = df['stats'].mean()
        elif which == 2:
            title = 'Median'
            data = df['stats'].median()
        elif which == 3:
            title = 'Mode'
            mode = str(df['stats'].mode())
            data = 0 if '1   ' in mode else int(mode[5:7]) if int(mode[5:7]) > 9 else int(mode[5])
            print("For Modes if they are 0 then that character doesn't have a mode")
        elif which == 4:
            title = 'Min'
            data = df['stats'].min()
        elif which == 5:
            title = 'Max'
            data = df['stats'].max()
        names.append(charac["Name"][:6])
        datas.append(data)
    data_counts = {'Data': np.array(datas)}
    fig, ax = plt.subplots()
    for data, data_count in data_counts.items():
        width = 0.7
        bottom = np.zeros(len(names))
        p = ax.bar(names, data_count, width, label=data, bottom=bottom)
        bottom += data_count
        ax.bar_label(p, label_type='center')
    ax.set_title(f"Characters' {title}")
    ax.legend()
    plt.show()