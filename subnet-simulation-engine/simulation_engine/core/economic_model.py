import random
import numpy as np

class EconomicModel:
    def __init__(self, total_supply, initial_distribution, fee_rate, transaction_volume, staking_rewards, lock_up_periods):
        self.total_supply = total_supply
        self.initial_distribution = initial_distribution
        self.fee_rate = fee_rate
        self.transaction_volume = transaction_volume
        self.staking_rewards = staking_rewards
        self.lock_up_periods = lock_up_periods
        self.current_supply = total_supply
        self.token_burned = 0

    def simulate_token_distribution(self):
        distribution = {
            'validators': self.total_supply * self.initial_distribution['validators'] / 100,
            'community': self.total_supply * self.initial_distribution['community'] / 100,
            'development': self.total_supply * self.initial_distribution['development'] / 100
        }
        return distribution

    def simulate_transaction_fees(self):
        fees_collected = self.transaction_volume * self.fee_rate
        self.token_burned += fees_collected * 0.5  # Assume 50% of fees are burned
        self.current_supply -= self.token_burned
        return fees_collected, self.token_burned

    def simulate_staking_rewards(self):
        rewards = {
            'short_term': self.staking_rewards['short_term'] * self.lock_up_periods['short_term'] / 100,
            'medium_term': self.staking_rewards['medium_term'] * self.lock_up_periods['medium_term'] / 100,
            'long_term': self.staking_rewards['long_term'] * self.lock_up_periods['long_term'] / 100
        }
        total_rewards = sum(rewards.values())
        self.current_supply += total_rewards
        return rewards, total_rewards

    def simulate_dynamic_token_supply(self, inflation_rate, deflation_rate):
        inflation_tokens = self.current_supply * inflation_rate
        deflation_tokens = self.current_supply * deflation_rate
        self.current_supply += inflation_tokens - deflation_tokens
        return inflation_tokens, deflation_tokens

    def simulate_multi_token_interactions(self, secondary_token_supply, conversion_rate):
        primary_to_secondary = self.transaction_volume * conversion_rate
        secondary_token_supply -= primary_to_secondary
        return primary_to_secondary, secondary_token_supply

    def simulate_economic_scenarios(self):
        scenarios = {
            'high_volume': self.transaction_volume * 1.5,
            'low_volume': self.transaction_volume * 0.5,
            'validator_exit': self.total_supply * 0.1  # Assume 10% of tokens are unstaked and exit
        }
        return scenarios

    def run_simulation(self, inflation_rate, deflation_rate, conversion_rate, secondary_token_supply, periods=12):
        results = []
        for period in range(periods):
            # Simulate each period
            self.transaction_volume *= random.uniform(0.95, 1.05)  # Introducing variability in transaction volume
            fees_collected, token_burned = self.simulate_transaction_fees()
            rewards, total_rewards = self.simulate_staking_rewards()
            inflation_tokens, deflation_tokens = self.simulate_dynamic_token_supply(inflation_rate, deflation_rate)
            primary_to_secondary, secondary_token_supply = self.simulate_multi_token_interactions(secondary_token_supply, conversion_rate)
            scenarios = self.simulate_economic_scenarios()

            # Store results
            results.append({
                'period': period + 1,
                'transaction_volume': self.transaction_volume,
                'current_supply': self.current_supply,
                'fees_collected': fees_collected,
                'token_burned': token_burned,
                'staking_rewards': rewards,
                'total_rewards': total_rewards,
                'inflation_tokens': inflation_tokens,
                'deflation_tokens': deflation_tokens,
                'primary_to_secondary': primary_to_secondary,
                'secondary_token_supply': secondary_token_supply,
                'economic_scenarios': scenarios
            })

        return results

# Example of running the enhanced economic model
economic_model = EconomicModel(
    total_supply=100000000,
    initial_distribution={'validators': 20, 'community': 50, 'development': 30},
    fee_rate=0.01,
    transaction_volume=1000000,
    staking_rewards={'short_term': 0.05, 'medium_term': 0.10, 'long_term': 0.20},
    lock_up_periods={'short_term': 10, 'medium_term': 20, 'long_term': 30}
)

simulation_results = economic_model.run_simulation(
    inflation_rate=0.02,
    deflation_rate=0.01,
    conversion_rate=0.1,
    secondary_token_supply=500000,
    periods=12  # Simulating for 12 periods (e.g., months or years)
)

# Example: Printing simulation results for the first period
print(simulation_results[0])
