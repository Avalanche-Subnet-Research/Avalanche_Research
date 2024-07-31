from agents.pchain import PChain
from agents.subnet import Subnet
from agents.validator import Validator

class Model:
    def __init__(self):
        self.pchain = PChain()

    def add_validator(self, id, stake, cost_per_validator):
        validator = Validator(id, stake, cost_per_validator)
        self.pchain.add_validator(validator)

    def remove_validator(self, id):
        self.pchain.remove_validator(id)

    def add_subnet(self, id, transaction_volume):
        subnet = Subnet(id, transaction_volume)
        self.pchain.add_subnet(subnet)

    def update_network_activity(self, increment):
        self.pchain.update_network_activity(increment)

    def distribute_rewards(self):
        self.pchain.distribute_rewards()

    def update_transaction_volumes(self):
        self.pchain.update_all_transaction_volumes()

    def add_developers_to_subnet(self, subnet_id, count):
        if subnet_id in self.pchain.subnets:
            self.pchain.subnets[subnet_id].add_developer(count)

    def update_validator_cost(self, validator_id, new_cost):
        if validator_id in self.pchain.validators:
            self.pchain.validators[validator_id].update_cost(new_cost)

    def __str__(self):
        return str(self.pchain)

