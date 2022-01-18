from engine.simulationEngine import SimulationEngine


def main(config):

    engine = SimulationEngine(config.graph, config.visualizer, config.rewards)
    engine.run(config.num_round_per_play, config.num_epochs, config.visualizer_interval, config.save_path)


if __name__ == '__main__':

    # from configurations.configuration_set.config1 import config1 as config
    from configurations.configuration_set.config1_small import config1_small as config
    # from configurations.configuration_set.config2 import config2 as config
    # from configurations.configuration_set.config3 import config3 as config
    # from configurations.configuration_set.config4 import config4 as config
    # from configurations.configuration_set.config5 import config5 as config
    # from configurations.configuration_set.config6 import config6 as config
    # from configurations.configuration_set.config_lasftm_asia_1 import config_lasftm_asia_1 as config
    # from configurations.configuration_set.config_lasftm_asia_1_small import config_lasftm_asia_1_small as config
    # from configurations.configuration_set.config_lasftm_asia_2 import config_lasftm_asia_2 as config
    # from configurations.configuration_set.config_lasftm_asia_2_small import config_lasftm_asia_2_small as config

    main(config)


