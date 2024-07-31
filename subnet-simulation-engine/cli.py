import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from simulation_engine.config.config_manager import ConfigManager
from simulation_engine.core.validator_config import ValidatorConfig
from simulation_engine.core.economic_model import EconomicModel
from simulation_engine.core.security_model import SecurityModel
from simulation_engine.utils.visualization import plot_results

def main():
    config_type = sys.argv[1]
    config_file = sys.argv[2]

    config = ConfigManager.load_config(config_file)
    print("Using configuration for", config_type, "simulation:", config)  # Debugging print

    if config_type == 'validator':
        validator_config = ValidatorConfig(config['criteria'], config['min_stake'], config['staking_token'])
        validators = validator_config.generate_validator_set()
        plot_results(validators)
    elif config_type == 'economic':
        economic_model = EconomicModel(config['total_supply'], config['initial_distribution'], config['fee_rate'])
        economics = economic_model.simulate_economics()
        # Extract data for plotting
        distribution = list(economics['distribution'].values())
        fee_impact = [economics['fee_impact']]
        plot_results([distribution, fee_impact])
    elif config_type == 'security':
        security_model = SecurityModel(config['slashing_conditions'])
        security = security_model.simulate_security()
        plot_results([security])
    else:
        print("Invalid configuration type. Choose 'validator', 'economic', or 'security'.")

if __name__ == "__main__":
    main()
