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

jb_combined = pd.merge(jb_ratings, jb_dollars, how = 'inner', on = 'title')
# %%
# Check df dimensions
jb_combined.shape
# %%
jb_combined = jb_combined.assign(inf_adj_profit_mil = lambda x: x['inf_adj_profit'] / 1000000)
jb_combined = jb_combined.assign(worldwide_mil = lambda x: x['worldwide'] / 1000000)
jb_combined = jb_combined.assign(inf_adj_worldwide_mil = lambda x: x['inf_adj_worldwide'] / 1000000)
jb_combined = jb_combined.assign(inf_adj_budget_mil = lambda x: x['inf_adj_budget'] / 1000000)

# %%
# Graph total inflation adjusted dollars
plot = (ggplot(jb_combined, aes(x = 'main_actor', y = 'inf_adj_profit_mil')) +
    geom_col(fill = 'dodgerblue') +
    coord_flip() +
    labs(x = "Actor",
         y = "Profit (M)",
         title = "Inflation Adjusted Movie Profit By Actor\nSean Connery Leads At $5,000M") +
    theme_bw() 
)

# %%
# Save the first graph
plot.save("C:/code/individual_p1_ashworth/documents/graph1_inflation_adj_profit_by_actor.png", width = 15, height = 6)

# %%
# Graph simple count of movies by actor
plot2 = (ggplot(jb_combined, aes(x = 'main_actor')) +
    geom_bar(fill = 'dodgerblue') +
    coord_flip() +
    #facet_wrap('~ main_actor', scales = 'free_y', nrow = 1) +
    labs(x = "Actor",
         y = "Movie Count",
         title = "Movie Count By Actor\nSean Connery & Roger Moore Lead With Seven") +
    #scale_size(breaks =  [1000000000, 2000000000, 3000000000, 4000000000, 5000000000],
    #               labels = ["1,000M", "2,000M", "3,000M", "4,000M", "5,000 M"]) +
    theme_bw() #+
    #theme(legend_key = element_rect(fill = 0, alpha = 0))
)

# %%
# Save the first graph
plot2.save("C:/code/individual_p1_ashworth/documents/graph2_count_by_actor.png", width = 15, height = 6)

# %%
# Create df with average movie profit by actor
def w_avg(df, values, weights):
    d = df[values]
    w = df[weights]
    return d.sum() / w.count()

wam = jb_combined.groupby(['main_actor'],as_index = False)['inf_adj_profit_mil'].sum()
wam2 = jb_combined.groupby(['main_actor'],as_index = False).apply(w_avg, 'inf_adj_profit_mil', 'title')
wam2.columns = ['main_actor', 'avg_movie_profit']

wam3 = wam.merge(wam2, how = 'inner')


# %%
# Graph Average inflation adj profit by actor
plot3 = (ggplot(wam3, aes(x = 'main_actor', y = 'avg_movie_profit')) +
    geom_col(fill = 'dodgerblue') +
    coord_flip() +
    #facet_wrap('~ main_actor', scales = 'free_y', nrow = 1) +
    labs(x = "Actor",
         y = "Average Profit Per Movie (M)",
         title = "Average Movie Profit By Actor\nSean Connery Leads At $721M") +
    #scale_size(breaks =  [1000000000, 2000000000, 3000000000, 4000000000, 5000000000],
    #               labels = ["1,000M", "2,000M", "3,000M", "4,000M", "5,000 M"]) +
    theme_bw() #+
    #theme(legend_key = element_rect(fill = 0, alpha = 0))
)

# %%
# Save the first graph
plot3.save("C:/code/individual_p1_ashworth/documents/graph3_avg_profit_by_actor.png", width = 15, height = 6)
# %%
# %%
# Graph worldwide box office without adjusted dollars
plot4 = (ggplot(jb_combined, aes(x = 'main_actor', y = 'worldwide_mil')) +
    geom_col(fill = 'dodgerblue') +
    coord_flip() +
    labs(x = "Actor",
         y = "Box Office (M)",
         title = "Worldwide Box Office Take By Actor\nDaniel Craig Leads With Over $3,000M") +
    theme_bw() 
)

# %%
# Save the first graph
plot4.save("C:/code/individual_p1_ashworth/documents/graph4_boxoffice_by_actor.png", width = 15, height = 6)

# %%
# Graph yearly box office totals
plot5 = (ggplot(jb_combined, aes(x = 'year', y = 'inf_adj_worldwide_mil')) +
    geom_line(color = 'dodgerblue') +
    geom_line(aes(y = 'inf_adj_budget_mil'), color = 'red') +
    #coord_flip() +
    labs(x = "Year",
         y = "Box Office (M)",
         title = "Worldwide Box Office\nBond Series Has A Rough Stretch 1980 to 1990\nInflation Adjusted Budget (red line) Shows Larger Budgets Did Not Guarantee Larger Profits") +
    theme_bw() 
)

# %%
# Save the first graph
plot5.save("C:/code/individual_p1_ashworth/documents/graph5_worldwide_by_year.png", width = 15, height = 6)

# %%
# Graph average imdb

wam4 = jb_combined.groupby(['main_actor'],as_index = False)['imdb_rating'].sum()
wam5 = jb_combined.groupby(['main_actor'],as_index = False).apply(w_avg, 'imdb_rating', 'title')
wam5.columns = ['main_actor', 'avg_imdb_rating']

wam6 = wam4.merge(wam5, how = 'inner')

plot6 = (ggplot(jb_combined, aes(x = 'main_actor', y = 'imdb_rating')) +
    geom_boxplot() +
    coord_flip() +
    labs(x = "Actor",
         y = "Average IMDB Rating",
         title = "IMDB Ratings\nSean Connery & Daniel Craig Lead With Over 7.00 Ratings") +
    theme_bw() 
)

# %%
# Save the first graph
plot6.save("C:/code/individual_p1_ashworth/documents/graph6_imdb_ratings_by_actor.png", width = 15, height = 6)
