from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_file = current_dir / 'poem.txt'

with open(target_file, 'rt', encoding='utf-8') as f:
    for line in f:
        print(line)