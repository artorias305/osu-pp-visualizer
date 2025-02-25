import matplotlib.pyplot as plt
import seaborn as sns
from ossapi import Ossapi
import numpy as np
from dotenv import load_dotenv
import os
import random
import questionary
import pandas as pd

load_dotenv()

sns.set_style("whitegrid")
sns.set_palette("husl")

api = Ossapi(
    client_id=int(os.getenv('OSU_CLIENT_ID')), 
    client_secret=os.getenv('OSU_CLIENT_SECRET')
)

top50 = api.ranking("osu", "performance")

def generate_colors(n):
    return ["#" + ''.join(random.choices('0123456789ABCDEF', k=6)) for _ in range(n)]

def create_bar_chart(names, pps, save=True, start_at_zero=True):
    plt.figure(figsize=(10, 6))
    data = pd.DataFrame({'Player Name': names, 'PP': pps})
    sns.barplot(data=data, x='Player Name', y='PP')
    plt.xlabel('Player Name')
    plt.ylabel('PP')
    plt.title('Player PP Distribution')
    plt.xticks(rotation=90)
    if start_at_zero:
        plt.ylim(0, max(pps) * 1.1)
    plt.tight_layout()
    if save:
        plt.savefig('bar_chart.png')
    else:
        plt.show()

def create_line_chart(names, pps, save=True, start_at_zero=True):
    plt.figure(figsize=(10, 6))
    data = pd.DataFrame({'Player Name': names, 'PP': pps})
    sns.lineplot(data=data, x='Player Name', y='PP', marker='o')
    plt.xlabel('Player Name')
    plt.ylabel('PP')
    plt.title('Player PP Trend')
    plt.xticks(rotation=90)
    if start_at_zero:
        plt.ylim(0, max(pps) * 1.1)
    plt.tight_layout()
    if save:
        plt.savefig('line_chart.png')
    else:
        plt.show()

def create_pie_chart(names, pps, save=True):
    plt.figure(figsize=(15, 8))
    
    base_colors = (
        sns.color_palette("Set3", 12) +
        sns.color_palette("Dark2", 8) +
        sns.color_palette("Paired", 12) 
    )
    
    colors = base_colors[:len(names)]
    
    patterns = ['/', '\\', 'x', 'o', 'O', '.', '*', '-', '+', '|']
    patterns = patterns * (len(names) // len(patterns) + 1)
    patterns = patterns[:len(names)]
    
    total = sum(pps)
    percentages = [pp/total * 100 for pp in pps]

    legend_labels = [f'{name} ({pp:.1f}%)' for name, pp in zip(names, percentages)]
    
    patches, _ = plt.pie(
        pps, 
        colors=colors,
        labels=[''] * len(names),
        startangle=90
    )
    
    for patch, pattern in zip(patches, patterns):
        patch.set_hatch(pattern)
    
    plt.legend(
        patches,
        legend_labels,
        title="Players",
        loc="center left",
        bbox_to_anchor=(1, 0.5),
        fontsize=8
    )
    
    plt.title('PP Distribution')
    plt.axis('equal')
    
    if save:
        plt.savefig('pie_chart.png', bbox_inches='tight', dpi=300, pad_inches=0.5)
    else:
        plt.show()
    plt.close()

def create_scatter_plot(names, pps, save=True, start_at_zero=True):
    plt.figure(figsize=(10, 6))
    data = pd.DataFrame({'Player Name': names, 'PP': pps})
    sns.scatterplot(data=data, x='Player Name', y='PP', s=100)
    plt.xlabel('Player Name')
    plt.ylabel('PP')
    plt.title('PP Distribution (Scatter)')
    plt.xticks(rotation=90)
    if start_at_zero:
        plt.ylim(0, max(pps) * 1.1)
    plt.tight_layout()
    if save:
        plt.savefig('scatter_plot.png')
    else:
        plt.show()

names = []
pps = []

n_players = questionary.text(
    "Enter the number of players to plot (max 50):",
    validate=lambda text: text.isdigit() and 1 <= int(text) <= 50
).ask()
n_players = int(n_players)

for n in range(n_players):
    name = top50.ranking[n].user.username
    pp = top50.ranking[n].pp
    names.append(name)
    pps.append(pp)

save_option = questionary.select(
    "Do you wnat to save or just display the charts?",
    choices=["Save", "Display"]
).ask() == "Save"

create_bar_chart(names, pps, save=save_option)
create_line_chart(names, pps, save=save_option)
create_pie_chart(names, pps, save=save_option)
create_scatter_plot(names, pps, save=save_option)
