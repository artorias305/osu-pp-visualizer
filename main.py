import matplotlib.pyplot as plt
from ossapi import Ossapi
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()

api = Ossapi(
    client_id=int(os.getenv('OSU_CLIENT_ID')), 
    client_secret=os.getenv('OSU_CLIENT_SECRET')
)

top50 = api.ranking("osu", "performance")

n = 0

def create_bar_chart(names, pps):
    plt.figure(figsize=(8, 5))
    plt.bar(names, pps, color='skyblue')
    plt.xlabel('Player Name')
    plt.ylabel('PP')
    plt.title('Player X PP')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('bar_chart.png')
    plt.show()

def create_line_chart(names, pps):
    plt.figure(figsize=(8, 5))
    plt.plot(names, pps, marker='o', linestyle='-', color='green')
    plt.xlabel('Player Name')
    plt.ylabel('PP')
    plt.title('Player X PP')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('line_chart.png')
    plt.show()

def create_pie_chart(names, pps):
    plt.figure(figsize=(8, 5))
    plt.pie(pps, labels=names, autopct="%1.1f%%", colors=['skyblue', 'lightcoral', 'lightgreen', 'gold', 'plum'])
    plt.title('PP Pie Chart')
    plt.savefig('pie_chart.png')
    plt.show()

def create_scatter_plot(names, pps):
    plt.figure(figsize=(8, 5))
    x = np.arange(len(names))
    plt.scatter(x, pps, color='red', edgecolors='black', s=100)
    plt.xticks(x, names, rotation=45)
    plt.xlabel('Player Name')
    plt.ylabel('PP')
    plt.title('PP Scatter Plot')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig('scatter_plot.png')
    plt.show()

names = []
pps = []



while n < 50:
    name = top50.ranking[n].user.username
    pp = top50.ranking[n].pp

    names.append(name)
    pps.append(pp)

    n = n + 1

create_bar_chart(names, pps)
create_line_chart(names, pps)
create_pie_chart(names, pps)
create_scatter_plot(names, pps)