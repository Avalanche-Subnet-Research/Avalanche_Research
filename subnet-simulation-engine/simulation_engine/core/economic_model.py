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

    def simulate_economics(self):
        distribution = self.simulate_token_distribution()
        fees_collected, token_burned = self.simulate_transaction_fees()
        rewards, total_rewards = self.simulate_staking_rewards()
        inflation_tokens, deflation_tokens = self.simulate_dynamic_token_supply(0.02, 0.01)
        primary_to_secondary, secondary_token_supply = self.simulate_multi_token_interactions(500000, 0.1)
        scenarios = self.simulate_economic_scenarios()

        return {
            'distribution': distribution,
            'fees_collected': fees_collected,
            'token_burned': token_burned,
            'staking_rewards': rewards,
            'total_rewards': total_rewards,
            'inflation_tokens': inflation_tokens,
            'deflation_tokens': deflation_tokens,
            'primary_to_secondary': primary_to_secondary,
            'secondary_token_supply': secondary_token_supply,
            'economic_scenarios': scenarios,
            'current_supply': self.current_supply
        }
