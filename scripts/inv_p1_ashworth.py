# %%
import pandas as pd
import numpy as np

# %%
# Bring in two data files for ratings and dollars
jb_ratings = pd.read_csv("C:/code/individual_p1_ashworth/data/james_bond_series.csv", compression = "infer")
jb_dollars = pd.read_csv("C:/code/individual_p1_ashworth/data/james_bond_dollars.csv", compression = "infer")

# %%
# Combine two files to combine in charts
jb_combined = pd.concat([jb_ratings, jb_dollars], join = "inner", keys = "Title", axis = 1)

# %%
