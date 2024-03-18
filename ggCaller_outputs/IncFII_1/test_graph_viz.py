
#in bash script: pip install networkx matplotlib

import subprocess

# Install networkx
subprocess.check_call(["pip", "install", "networkx"])

# Install matplotlib
subprocess.check_call(["pip", "install", "matplotlib"])


import networkx as nx

# Read the GML file
G = nx.read_gml('final_graph.gml')
import matplotlib.pyplot as plt

# Draw the graph
nx.draw(G, with_labels=True, node_size=500, node_color='skyblue', font_size=10)

# Display the plot
plt.show()