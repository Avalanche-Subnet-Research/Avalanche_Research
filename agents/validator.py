class Validator:
    def __init__(self, id, stake, cost_per_validator):
        self.id = id
        self.stake = stake
        self.cost_per_validator = cost_per_validator

    def calculate_rewards(self, network_activity):
        rewards = network_activity * 0.01  # Simplified logic for reward calculation
        return rewards

    def update_cost(self, new_cost):
        self.cost_per_validator = new_cost

    def __str__(self):
        return f"Validator(id={self.id}, stake={self.stake}, cost_per_validator={self.cost_per_validator})"
