import pandas as pd
from pathlib import Path
import networkx as nx

from configurations.configuration import Configuration
from strategy.alwaysCooperate import AlwaysCooperate
from strategy.alwaysDefect import AlwaysDefect
from strategy.pavlov import Pavlov
from strategy.titForTat import TitForTat
from graph.networkx_graph.networkxGraph import NetworkxGraph
from visualization.networkxVisualizer import NetworkxVisualizer
from rewards import PRISONER_REWARDS

df = pd.read_csv("resources/lasftm_asia/lastfm_asia_edges.csv")

cut_vertices = 8000

edge_list = [(row['node_1'], row['node_2']) for _, row in df.iterrows()
             if row['node_1'] < cut_vertices and row['node_2'] < cut_vertices]

G = nx.Graph()
for u, v in edge_list:
    G.add_edge(u, v)

sub_graph = sorted(nx.connected_components(G), key=len)[-1]

num_vertices = len(sub_graph)

print("NUM VERTICES: ", num_vertices)

mapper = {}
idx = 0
for u in sub_graph:
    if u not in mapper:
        mapper[u] = idx
        idx += 1

edge_list = [(mapper[u], mapper[v]) for u, v in edge_list if u in mapper and v in mapper]

quarter = int(num_vertices / 4)
strategies = [AlwaysCooperate()] * quarter + [AlwaysDefect()] * quarter +\
                [Pavlov()] * quarter + [TitForTat()] * (num_vertices - 3*quarter)

graph_config = {
    'strategies': strategies,
    'edge_list': edge_list,
    'neighbour_radius': 1
}

graph = NetworkxGraph().build(graph_config)
visualizer = NetworkxVisualizer(graph)

config_lasftm_asia_2 = Configuration(
    graph=graph,
    visualizer=visualizer,
    visualizer_interval=1,
    num_round_per_play=10,
    num_epochs=30,
    rewards=PRISONER_REWARDS,
    save_path=Path("results/res_lasftm_asia_2")
)