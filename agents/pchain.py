class PChain:
    def __init__(self):
        self.validators = {}
        self.subnets = {}
        self.network_activity = 0

    def add_validator(self, validator):
        self.validators[validator.id] = validator

    def remove_validator(self, validator_id):
        if validator_id in self.validators:
            del self.validators[validator_id]

    def add_subnet(self, subnet):
        self.subnets[subnet.id] = subnet

    def update_network_activity(self, increment):
        self.network_activity += increment

    def distribute_rewards(self):
        for validator in self.validators.values():
            rewards = validator.calculate_rewards(self.network_activity)
            print(f"Distributed {rewards} rewards to {validator}")

    def update_all_transaction_volumes(self):
        for subnet in self.subnets.values():
            subnet.update_transaction_volume(self.network_activity)

    def __str__(self):
        return f"PChain(validators={len(self.validators)}, subnets={len(self.subnets)}, network_activity={self.network_activity})"
