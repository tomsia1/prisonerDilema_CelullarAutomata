from dataclasses import dataclass

from graph.graphInterface import GraphInterface
from visualization.visualizerInterface import VisualizerInterface

from pathlib import Path


@dataclass
class Configuration:
    graph: GraphInterface
    visualizer: VisualizerInterface
    visualizer_interval: int
    num_epochs: int
    num_round_per_play: int
    rewards: list
    save_path: Path
