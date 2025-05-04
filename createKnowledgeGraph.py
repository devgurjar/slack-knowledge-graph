import json
import networkx as nx
import matplotlib.pyplot as plt

with open('knowledge_graph.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

G = nx.DiGraph()

for entry in data:
    company = entry.get('company')
    component = entry.get('component')
    if company and component:
        G.add_edge(company, component)

plt.figure(figsize=(12, 8))
nx.draw_networkx(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
plt.title("Knowledge Graph: Company ➝ Component")
plt.axis('off')
plt.show()
