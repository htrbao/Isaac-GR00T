import pandas as pd
import numpy as np

# Read a parquet file
df = pd.read_parquet("demo_data/robot_sim.PickNPlace/data/chunk-000/episode_000000.parquet")
print(df.keys())
print(list(df.loc[0]))  # Print the first row of the DataFrame

print([x.shape for x in df.loc[0] if isinstance(x, np.ndarray)])  # Print shapes of Series in the first row