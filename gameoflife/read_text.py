from pathlib import Path

TEXT_PATH = Path('gameoflife') / 'data' / 'about.txt'

def read_about():
    with open(TEXT_PATH, 'r') as f:
        return f.read()