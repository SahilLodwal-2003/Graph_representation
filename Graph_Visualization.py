import networkx as nx
import matplotlib.pyplot as plt
import random

V = 10  # Number of vertices
edge_counts = list(range(10, 46, 5))  # Target edge counts: 10, 15, ..., 45

# Create a 2x4 grid for the 8 subplots
fig, axes = plt.subplots(2, 4, figsize=(15, 8))
axes = axes.flatten()

for i, E in enumerate(edge_counts):
    # Initialize graph
    G = nx.Graph()
    G.add_nodes_from(range(V))
    
    # Connect all vertices with a random spanning tree (9 edges)
    for node in range(1, V):
        target = random.choice(range(node))
        G.add_edge(node, target)
    
    # Add random remaining edges to reach target E
    edges_to_add = E - (V - 1)
    missing_edges = list(nx.non_edges(G))
    new_edges = random.sample(missing_edges, edges_to_add)
    G.add_edges_from(new_edges)
    
    # Generate random (X, Y) coordinates
    pos = nx.random_layout(G)
    
    # Draw on the corresponding subplot
    ax = axes[i]
    nx.draw(
        G, pos, ax=ax, 
        with_labels=True, 
        node_color='lightgreen', 
        node_size=500, 
        edge_color='gray',
        font_weight='bold'
    )
    ax.set_title(f"Edges: {E}")

plt.suptitle("Graph Generation with 10 Vertices and Variable Edge Counts", fontsize=16)
plt.tight_layout()
plt.savefig("Graph Visualization.png")
