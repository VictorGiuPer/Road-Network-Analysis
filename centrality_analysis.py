"""
This code block:

Converts two dictionaries of centrality measures (betweenness and closeness) 
into Pandas Series for data manipulation and analysis.

Merges these Series into a single DataFrame, setting the city identifiers 
as an index column and naming the columns 'Betweenness' and 'Closeness'.

Reshapes the DataFrame to ensure cities are represented as a column rather than as an index.

Generates two histograms to visualize the distribution of betweenness 
and closeness centrality values among the cities in the road network.

The histograms provide insights into how centrality is distributed across 
the network's nodes, which can help identify key cities for transport, communication, 
or other network-related concerns. The visualization allows for easy comparison 
of the two centrality measures, revealing patterns and outliers in the data.
"""

import pandas as pd

from closeness_betweenness_analysis import betweenness, closeness
import matplotlib.pyplot as plt


betweenness_series = pd.Series(betweenness, name="Betweenness")
closeness_series = pd.Series(closeness, name="Closeness")

# Combine series into a DataFrame
centrality_df = pd.DataFrame(
    {"Betweenness": betweenness_series, "Closeness": closeness_series}
)

# Reset index to make sure cities are represented as a column
centrality_df.reset_index(inplace=True)
centrality_df.rename(columns={"index": "City"}, inplace=True)

plt.figure(figsize=(14, 6))

# Betweenness histogram
plt.subplot(1, 2, 1)
plt.hist(betweenness_series, bins=10, color="blue", alpha=0.7)
plt.title("Betweenness Centrality Distribution")
plt.xlabel("Betweenness Centrality")
plt.ylabel("Frequency")

# Closeness histogram
plt.subplot(1, 2, 2)
plt.hist(closeness_series, bins=10, color="green", alpha=0.7)
plt.title("Closeness Centrality Distribution")
plt.xlabel("Closeness Centrality")
plt.ylabel("Frequency")

# Show the plots
plt.tight_layout()
plt.show()
