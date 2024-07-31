class Subnet:
    def __init__(self, id, transaction_volume):
        self.id = id
        self.transaction_volume = transaction_volume
        self.developers = 0

    def add_developer(self, count):
        self.developers += count

    def update_transaction_volume(self, network_activity):
        self.transaction_volume = network_activity * 10  # Simplified logic for transaction volume

    def __str__(self):
        return f"Subnet(id={self.id}, transaction_volume={self.transaction_volume}, developers={self.developers})"
