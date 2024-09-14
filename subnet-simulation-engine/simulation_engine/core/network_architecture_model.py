import random

class NetworkArchitectureModel:
    def __init__(self, transaction_throughput_params, block_size_params, consensus_params, latency_params, topology_params, fault_tolerance_params, fee_rate=0.01):
        # Initial Parameters
        self.transaction_throughput_params = transaction_throughput_params
        self.block_size_params = block_size_params
        self.consensus_params = consensus_params
        self.latency_params = latency_params
        self.topology_params = topology_params
        self.fault_tolerance_params = fault_tolerance_params
        self.fee_rate = fee_rate

        # State Variables
        self.pending_transactions = 0
        self.current_throughput = transaction_throughput_params['base_throughput']
        self.current_latency = latency_params['base_latency']
        self.current_block_size = block_size_params['base_block_size']
        self.current_bandwidth = block_size_params['network_bandwidth']
        self.current_propagation_delay = self.current_block_size / self.current_bandwidth * 1000
        self.current_fault_tolerance = fault_tolerance_params['base_fault_tolerance']
        self.fees_collected = 0
        self.base_transaction_volume = transaction_throughput_params['base_throughput']
        self.congestion_fee_rate = self.fee_rate  # Initial fee rate, dynamic with congestion

    # State Update: Dynamic Bandwidth Management
    def update_bandwidth(self, transaction_volume):
        # Simulate bandwidth throttling under heavy transaction load
        congestion_factor = transaction_volume / self.base_transaction_volume
        if congestion_factor > 1.5:
            # If transaction volume is 150% of base, throttle bandwidth
            self.current_bandwidth *= random.uniform(0.8, 0.95)  # Reduce bandwidth
        else:
            # If load is light, expand bandwidth to simulate dynamic resource allocation
            self.current_bandwidth *= random.uniform(1.0, 1.05)

    # State Update: Dynamic Block Size Adjustment
    def adjust_block_size(self, block_utilization):
        # Automatically adjust block size based on utilization
        if block_utilization > 0.9:  # If utilization exceeds 90%
            self.current_block_size *= 1.1  # Increase block size by 10%
        elif block_utilization < 0.5:  # If utilization falls below 50%
            self.current_block_size *= 0.95  # Decrease block size by 5%
        self.current_block_size = max(self.block_size_params['base_block_size'] * 0.5, self.current_block_size)  # Ensure it doesn't go too low

    # Policy: Congestion Pricing Mechanism
    def update_fee_rate(self, transaction_volume):
        # Increase fee rate when network load is high
        congestion_factor = transaction_volume / self.base_transaction_volume
        if congestion_factor > 1.5:
            self.congestion_fee_rate = self.fee_rate * 1.5  # Increase fee rate by 50% during congestion
        else:
            self.congestion_fee_rate = self.fee_rate  # Reset to normal fee rate when not congested

    # Validator Behavior Simulation
    def simulate_validator_behavior(self):
        # Randomly simulate validators going offline or coming back online
        fault_tolerance_change = random.uniform(-0.05, 0.05)  # Simulate slight changes in fault tolerance
        self.current_fault_tolerance = max(0.5, min(1.0, self.current_fault_tolerance + fault_tolerance_change))

    # Simulate transaction throughput based on network conditions
    def simulate_throughput(self, transaction_volume):
        # Consensus efficiency impacts throughput
        consensus_efficiency = self.consensus_params['efficiency']
        
        # Adjust throughput based on network latency
        latency_factor = 1 - (self.current_latency / 100)  # Higher latency reduces throughput
        throughput = self.current_throughput * consensus_efficiency * latency_factor
        
        # Add random variability
        throughput = throughput * random.uniform(0.95, 1.05)
        
        return min(throughput, transaction_volume)  # Throughput can't exceed transaction volume

    # Existing functions: Transaction throughput, latency, block size, and fault tolerance updates
    def update_transaction_throughput(self):
        consensus_factor = self.consensus_params.get('efficiency', 1)
        latency_factor = 1 - (self.current_latency / 100)
        throughput = self.current_throughput * consensus_factor * latency_factor
        self.current_throughput = throughput * random.uniform(0.95, 1.05)

    def update_latency(self, transaction_volume):
        load_factor = transaction_volume / self.base_transaction_volume
        geographical_factor = self.latency_params['geographical_factor']
        self.current_latency = self.latency_params['base_latency'] * load_factor * geographical_factor * random.uniform(0.98, 1.02)

    def update_block_size_and_propagation_delay(self):
        self.current_block_size *= random.uniform(0.98, 1.02)
        self.current_propagation_delay = self.current_block_size / self.current_bandwidth * 1000

    def update_fault_tolerance(self):
        redundancy_factor = self.fault_tolerance_params['redundancy_factor']
        self.current_fault_tolerance = self.current_fault_tolerance * redundancy_factor * random.uniform(0.98, 1.02)

    # Simulate network performance for a specific transaction volume
    def simulate_network_performance(self, transaction_volume):
        # Update latency based on load and update bandwidth dynamically
        self.update_latency(transaction_volume)
        self.update_bandwidth(transaction_volume)
        self.update_block_size_and_propagation_delay()
        self.simulate_validator_behavior()

        # Simulate the number of transactions processed (throughput)
        processed_transactions = self.simulate_throughput(transaction_volume)

        # Calculate fees collected using the congestion-based fee rate
        fees_collected = self.calculate_fees(processed_transactions)

        # Calculate pending transactions (i.e., network congestion)
        pending_transactions = transaction_volume - processed_transactions
        self.pending_transactions += pending_transactions

        # Simulate block utilization (processed transactions / block size)
        block_utilization = min(1, processed_transactions / self.current_block_size)

        # Adjust block size based on utilization
        self.adjust_block_size(block_utilization)

        return {
            'transaction_volume': transaction_volume,
            'processed_transactions': processed_transactions,
            'pending_transactions': self.pending_transactions,
            'fees_collected': fees_collected,
            'latency': self.current_latency,
            'throughput': processed_transactions,
            'block_utilization': block_utilization,
            'fault_tolerance': self.current_fault_tolerance
        }

    def calculate_fees(self, processed_transactions):
        fees = processed_transactions * self.congestion_fee_rate
        self.fees_collected += fees
        return fees

    # Run the stress test for low, medium, and high transaction volumes
    def run_stress_test(self, periods=12):
        results = []
        for period in range(periods):
            # Low volume: 50% of base
            low_volume = self.base_transaction_volume * 0.5
            low_volume_performance = self.simulate_network_performance(low_volume)

            # Medium volume: 100% of base (baseline)
            medium_volume = self.base_transaction_volume
            medium_volume_performance = self.simulate_network_performance(medium_volume)

            # High volume: 200% of base
            high_volume = self.base_transaction_volume * 2
            high_volume_performance = self.simulate_network_performance(high_volume)

            # Store results for each period
            results.append({
                'period': period + 1,
                'low_volume': low_volume_performance,
                'medium_volume': medium_volume_performance,
                'high_volume': high_volume_performance
            })

        return results
