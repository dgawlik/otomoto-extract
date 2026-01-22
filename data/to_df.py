

import duckdb
import pandas as pd


frames = []


from pathlib import Path

path = Path('.')
files = [f for f in path.iterdir() if f.is_file() and f.suffix == '.json']

for f in files:
    frames.append(pd.read_json(f.name))


df_stacked = pd.concat(frames, axis=0)

rel = duckdb.query("SELECT * FROM df_stacked")
rel.show(max_width=200, max_rows=1000)
