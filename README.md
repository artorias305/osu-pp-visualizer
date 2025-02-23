# osu! PP Visualizer

A Python application that visualizes the Performance Points (PP) of the top 50 osu! players using various chart types.

## Features

- Bar chart visualization
- Line chart visualization
- Pie chart visualization
- Scatter plot visualization
- Real-time data from osu! API

## Prerequisites

- Python 3.7+
- osu! API credentials

## Installation

1. Clone the repository:
```bash
git clone https://github.com/artorias305/osu-pp-visualizer

cd osu-pp-visualizer
```
2. Install Dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your osu! API credentials:
```plaintext
OSU_CLIENT_ID=your_client_id
OSU_CLIENT_SECRET=your_client_secret
```

## Usage
Run the script:
```bash
python main.py
```