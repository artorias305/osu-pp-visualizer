import matplotlib.pyplot as plt
from ossapi import Ossapi
import numpy as np
from dotenv import load_dotenv
import os
import random

load_dotenv()

api = Ossapi(
    client_id=int(os.getenv('OSU_CLIENT_ID')), 
    client_secret=os.getenv('OSU_CLIENT_SECRET')
)

top50 = api.ranking("osu", "performance")

def generate_colors(n):
    return ["#" + ''.join(random.choices('0123456789ABCDEF', k=6)) for _ in range(n)]

def create_bar_chart(names, pps, save=True):
    plt.figure(figsize=(8, 5))
    plt.bar(names, pps, color='skyblue')
    plt.xlabel('Player Name')
    plt.ylabel('PP')
    plt.title('Player X PP')
    plt.xticks(rotation=90, ha='right')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.ylim(0, max(pps) * 1.1)
    plt.tight_layout()
    if save:
        plt.savefig('bar_chart.png')
    else:
        plt.show()

def create_line_chart(names, pps, save=True):
    plt.figure(figsize=(8, 5))
    plt.plot(names, pps, marker='o', linestyle='-', color='green')
    plt.xlabel('Player Name')
    plt.ylabel('PP')
    plt.title('Player X PP')
    plt.xticks(rotation=90)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.ylim(0, max(pps) * 1.1)
    plt.tight_layout()
    if save:
        plt.savefig('line_chart.png')
    else:
        plt.show()

def create_pie_chart(names, pps, save=True):
    plt.figure(figsize=(8, 5))
    plt.pie(pps, labels=names, autopct="%1.1f%%", colors=generate_colors(len(names)))
    plt.title('PP Pie Chart')
    if save:
        plt.savefig('pie_chart.png')
    else:
        plt.show()

def create_scatter_plot(names, pps, save=True):
    plt.figure(figsize=(8, 5))
    x = np.arange(len(names))
    plt.scatter(x, pps, color=generate_colors(len(names)), edgecolors='black', s=100)
    plt.xticks(x, names, rotation=90, ha='right')
    plt.xlabel('Player Name')
    plt.ylabel('PP')
    plt.title('PP Scatter Plot')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.ylim(0, max(pps) * 1.1)
    plt.grid(True, linestyle='--', alpha=0.7)
    if save:
        plt.savefig('scatter_plot.png')
    else:
        plt.show()

names = []
pps = []

while True:
    try:
        n_players = int(input("Enter the number of players to plot (max 50): "))
        if 1 <= n_players <= 50:
            break
        else:
            print("Please enter a number between 1 and 50")
    except ValueError:
        print("Please enter a valid number")

for n in range(n_players):
    name = top50.ranking[n].user.username
    pp = top50.ranking[n].pp
    names.append(name)
    pps.append(pp)

save_option = input("Do you want to save the charts? (yes/no): ").strip().lower() == 'yes'

create_bar_chart(names, pps, save=save_option)
create_line_chart(names, pps, save=save_option)
create_pie_chart(names, pps, save=save_option)
create_scatter_plot(names, pps, save=save_option)
