import os
import shutil


class SimulationEngine:
    def __init__(self, graph, visualizer, rewards):
        self.graph = graph
        self.visualizer = visualizer

        self.rewards = rewards

    def play(self, u, v, num_rounds, hist_len):
        u_history = []
        v_history = []

        for _ in range(num_rounds):
            u_action = u.strategy.play(u_history, v_history)
            v_action = v.strategy.play(v_history, u_history)

            u.score += self.rewards[u_action.value][v_action.value]
            v.score += self.rewards[v_action.value][u_action.value]

            u_history.append(u_action)
            u_history = u_history[-hist_len:]

            v_history.append(v_action)
            v_history = v_history[-hist_len:]

    def run(self, num_rounds, epochs, visualizer_interval, save_path):

        shutil.rmtree(save_path, ignore_errors=True)

        print("START RUN")

        os.makedirs(save_path, exist_ok=True)

        self.visualizer.draw(save_path / "_start.png", False)

        for i in range(epochs):
            print("EPOCH: {}".format(i))

            for u in self.graph:
                u.zero_score()

            for u in self.graph:
                for v in u.neighbours:
                    if u.idx <= v.idx:
                        self.play(u, v, num_rounds, 2)

            to_update = set()
            for u in self.graph:
                if u.check_update():
                    to_update.add(u)

            for u in to_update:
                u.update()

            if i % visualizer_interval == 0:
                name = "epoch_{}.png".format(i)
                self.visualizer.draw(save_path / name, False)
