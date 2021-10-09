# %%
import pandas as pd
import numpy as np
from plotnine import *

# %%
# Bring in two data files for ratings and dollars
jb_ratings = pd.read_csv("C:/code/individual_p1_ashworth/data/james_bond_series.csv", compression = "infer")
jb_dollars = pd.read_csv("C:/code/individual_p1_ashworth/data/james_bond_dollars.csv", compression = "infer")

# %%
# Combine two files to combine in charts
#jb_combined = pd.concat([jb_ratings, jb_dollars], join = "inner", keys = "title", axis = 1)

jb_combined = pd.merge(jb_ratings, jb_dollars, how = 'inner', on = 'title')
# %%
jb_combined.shape
# %%
jb_combined = jb_combined.assign(inf_adj_profit_mil = lambda x: x['inf_adj_profit'] / 1000000)

# %%
# Graph total inflation adjusted dollars
plot = (ggplot(jb_combined, aes(x = 'main_actor', y = 'inf_adj_profit_mil')) +
    geom_col(fill = 'dodgerblue') +
    coord_flip() +
    labs(x = "Actor",
         y = "Profit (M)") +
    theme_bw() 
)

# %%
# Save the first graph
plot.save("C:/code/individual_p1_ashworth/documents/graph1_inflation_adj_profit_by_actor.png", width = 15, height = 6)

# %%
plot2 = (ggplot(jb_combined, aes(x = 'main_actor')) +
    geom_bar(fill = 'dodgerblue') +
    coord_flip() +
    #facet_wrap('~ main_actor', scales = 'free_y', nrow = 1) +
    labs(x = "Actor",
         y = "Movie Count") +
    #scale_size(breaks =  [1000000000, 2000000000, 3000000000, 4000000000, 5000000000],
    #               labels = ["1,000M", "2,000M", "3,000M", "4,000M", "5,000 M"]) +
    theme_bw() #+
    #theme(legend_key = element_rect(fill = 0, alpha = 0))
)

# %%
# Save the first graph
plot2.save("C:/code/individual_p1_ashworth/documents/graph2_count_by_actor.png", width = 15, height = 6)