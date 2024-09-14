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
        self.burn_rate = 0.5

        # New State Variables
        self.transaction_volume_cap = transaction_volume * 2  # Cap the transaction volume at 200% of the base value
        self.dynamic_burn_rate = self.burn_rate  # Burn rate that can fluctuate
        self.supply_elasticity_factor = 0.01  # Supply elasticity factor to introduce dynamic supply
        self.conversion_rate_fluctuation = 0.02
        self.initial_token_value = 1.0  # Introduce fluctuation in conversion rate

    # Existing Methods (Preserved)

    def simulate_token_distribution(self):
        distribution = {
            'validators': self.total_supply * self.initial_distribution['validators'] / 100,
            'community': self.total_supply * self.initial_distribution['community'] / 100,
            'development': self.total_supply * self.initial_distribution['development'] / 100
        }
        return distribution

    def simulate_transaction_fees(self):
        fees_collected = self.transaction_volume * self.fee_rate
        self.token_burned += fees_collected * self.dynamic_burn_rate  # Assume fluctuating burn rate
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
        # Introduce supply elasticity that affects both inflation and deflation
        self.current_supply += (inflation_tokens - deflation_tokens) * (1 + self.supply_elasticity_factor)
        return inflation_tokens, deflation_tokens

    def simulate_multi_token_interactions(self, secondary_token_supply, conversion_rate):
        # Fluctuating conversion rate
        fluctuating_conversion_rate = conversion_rate * random.uniform(1 - self.conversion_rate_fluctuation, 1 + self.conversion_rate_fluctuation)
        primary_to_secondary = self.transaction_volume * fluctuating_conversion_rate
        secondary_token_supply -= primary_to_secondary
        return primary_to_secondary, secondary_token_supply

    def simulate_economic_scenarios(self):
        scenarios = {
            'high_volume': min(self.transaction_volume * 1.5, self.transaction_volume_cap),  # Cap the volume
            'low_volume': self.transaction_volume * 0.5,
            'validator_exit': self.total_supply * 0.1  # Assume 10% of tokens are unstaked and exit
        }
        return scenarios

    # New Policy: Adjust Burn Rate Based on Transaction Volume
    def update_burn_rate(self):
        # The burn rate increases with higher transaction volume
        if self.transaction_volume > self.total_supply * 0.05:  # If more than 5% of supply is transacted
            self.dynamic_burn_rate = min(self.burn_rate * 1.2, 1.0)  # Burn rate can go up to 100%
        else:
            self.dynamic_burn_rate = self.burn_rate  # Reset to base burn rate

    # New Policy: Adjust Staking Rewards Dynamically
    def adjust_staking_rewards(self):
        # Increase rewards if inflation is high, reduce if deflation is high
        inflation_rate = 0.02  # Example inflation rate
        if inflation_rate > 0.03:
            # Increase staking rewards if inflation is high
            for tier in self.staking_rewards:
                self.staking_rewards[tier] *= 1.1  # Increase by 10%
        else:
            # Reduce rewards slightly if inflation is low
            for tier in self.staking_rewards:
                self.staking_rewards[tier] *= 0.95  # Reduce by 5%

    # New State Update: Transaction Volume Caps
    def cap_transaction_volume(self):
        if self.transaction_volume > self.transaction_volume_cap:
            self.transaction_volume = self.transaction_volume_cap  # Cap transaction volume at the set limit

    def estimate_token_value(self):
        # Token value is inversely proportional to supply (basic assumption)
        # More supply generally decreases the value, and less supply increases it
        return self.initial_token_value * (self.total_supply / self.current_supply)

    

    def run_simulation(self, inflation_rate, deflation_rate, conversion_rate, secondary_token_supply, periods=12):
        results = []
        for period in range(periods):
            # Simulate each period
            self.transaction_volume *= random.uniform(0.95, 1.05)  # Introducing variability in transaction volume
            self.cap_transaction_volume()  # Apply transaction volume cap

            self.update_burn_rate()  # Adjust burn rate dynamically based on transaction volume
            self.adjust_staking_rewards()  # Adjust staking rewards based on conditions

            fees_collected, token_burned = self.simulate_transaction_fees()
            rewards, total_rewards = self.simulate_staking_rewards()
            inflation_tokens, deflation_tokens = self.simulate_dynamic_token_supply(inflation_rate, deflation_rate)
            primary_to_secondary, secondary_token_supply = self.simulate_multi_token_interactions(secondary_token_supply, conversion_rate)
            scenarios = self.simulate_economic_scenarios()

            token_value = self.estimate_token_value()

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
                'economic_scenarios': scenarios,
                'token_value': token_value
            })

        return results

