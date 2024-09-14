import random

class ValidatorConfig:
    def __init__(self, criteria, min_stake, staking_token, reward_mechanisms, performance_metrics, penalty_mechanisms):
        self.criteria = criteria
        self.min_stake = min_stake
        self.staking_token = staking_token
        self.reward_mechanisms = reward_mechanisms
        self.performance_metrics = performance_metrics
        self.penalty_mechanisms = penalty_mechanisms
        self.validators = 100  # Example initial number of validators
        self.churn_rate = 0.05  # 5% of validators churn per period
        self.delegation_rate = 0.1  # 10% of token holders delegate to validators

    # Selecting validators based on criteria like technical specs, location, and reputation
    def select_validators(self):
        selected_validators = []
        for i in range(self.validators):
            validator = {
                'id': i,
                'technical_specs': random.choice(self.criteria['technical_specs']),
                'geographical_distribution': random.choice(self.criteria['geographical_distribution']),
                'reputation': random.choice(self.criteria['reputation']),
                'stake': random.uniform(self.min_stake, self.min_stake * 2),
                'uptime': random.uniform(0.9, 1.0),  # Uptime between 90% and 100%
                'delegated_stake': 0  # Initially, no tokens are delegated
            }
            selected_validators.append(validator)
        return selected_validators

    # Validators with at least min_stake will be staked, plus delegation
    def simulate_staking(self, validators):
        staked_validators = []
        for validator in validators:
            if validator['stake'] >= self.min_stake:
                # Simulate delegation of tokens to this validator
                validator['delegated_stake'] = validator['stake'] * self.delegation_rate
                validator['total_stake'] = validator['stake'] + validator['delegated_stake']
                staked_validators.append(validator)
        return staked_validators

    # Calculate rewards based on performance metrics like uptime and participation
    def calculate_rewards(self, validators):
        for validator in validators:
            performance = validator['uptime'] * random.choice(self.performance_metrics)
            # Rewards depend on performance and total stake (including delegation)
            validator['rewards'] = performance * self.reward_mechanisms['block_rewards'] * validator['total_stake']
        return validators

    # Monitor performance issues and apply penalties for poor performance
    def monitor_performance(self, validators):
        performance_issues = []
        for validator in validators:
            if validator['uptime'] < 0.95:  # Less than 95% uptime triggers a penalty
                validator['penalty'] = self.penalty_mechanisms['slashing'] * validator['total_stake']
                validator['total_stake'] -= validator['penalty']  # Slash stake
                performance_issues.append(validator['id'])
        return performance_issues

    # Implement validator churn (entry and exit of validators)
    def churn_validators(self, validators):
        churned_validators = random.sample(validators, int(self.validators * self.churn_rate))
        for validator in churned_validators:
            validators.remove(validator)  # Validators exit
        # Add new validators (e.g., new entries)
        for i in range(len(churned_validators)):
            new_validator = {
                'id': len(validators) + i,
                'technical_specs': random.choice(self.criteria['technical_specs']),
                'geographical_distribution': random.choice(self.criteria['geographical_distribution']),
                'reputation': random.choice(self.criteria['reputation']),
                'stake': random.uniform(self.min_stake, self.min_stake * 2),
                'uptime': random.uniform(0.9, 1.0),  # Uptime between 90% and 100%
                'delegated_stake': 0
            }
            validators.append(new_validator)
        return validators

    # Simulate network load, which can affect performance and rewards
    def simulate_network_load(self, validators, load_factor):
        for validator in validators:
            # Adjust uptime based on network load; heavier loads reduce uptime
            validator['uptime'] *= random.uniform(1.0 - load_factor, 1.0)
        return validators

    # Simulate the complete validator configuration with additional state and policy functions
    def simulate_validator_config(self, periods=12):
        results = []
        selected_validators = self.select_validators()

        for period in range(periods):
            # Simulate each period's processes
            staked_validators = self.simulate_staking(selected_validators)
            staked_validators = self.simulate_network_load(staked_validators, load_factor=random.uniform(0.05, 0.2))  # Network load fluctuates
            rewarded_validators = self.calculate_rewards(staked_validators)
            performance_issues = self.monitor_performance(rewarded_validators)
            selected_validators = self.churn_validators(selected_validators)  # Churn validators
            
            # Collect period results
            results.append({
                'period': period + 1,
                'selected_validators': selected_validators,
                'staked_validators': staked_validators,
                'rewarded_validators': rewarded_validators,
                'performance_issues': performance_issues
            })

        return results
