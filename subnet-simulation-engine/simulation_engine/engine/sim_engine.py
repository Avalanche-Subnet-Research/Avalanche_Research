import matplotlib.pyplot as plt

class SimulationEngine:
    def __init__(self, evaluate_metircs, time_steps=365):
        self.evaluate_metrics = evaluate_metircs
        self.time_steps = time_steps

    def run(self):
        # Run the simulation over the specified number of time steps
        metrics = self.evaluate_metrics.run_simulation(self.time_steps)
        self.plot_results(metrics)

    def plot_results(self, metrics):
        # Example: Plot TPS over time
        plt.figure(figsize=(10, 6))
        plt.plot(metrics['tps'], label='Transaction Throughput (TPS)')
        plt.title('Transaction Throughput Over Time')
        plt.xlabel('Time (days)')
        plt.ylabel('TPS')
        plt.legend()
        plt.show()

        # Additional plots for other metrics
        plt.figure(figsize=(10, 6))
        plt.plot(metrics['finality_time'], label='Block Finality Time')
        plt.title('Block Finality Time Over Time')
        plt.xlabel('Time (days)')
        plt.ylabel('Finality Time (ms)')
        plt.legend()
        plt.show()

        plt.figure(figsize=(10, 6))
        plt.plot(metrics['validator_uptime'], label='Validator Uptime')
        plt.title('Validator Uptime Over Time')
        plt.xlabel('Time (days)')
        plt.ylabel('Uptime (%)')
        plt.legend()
        plt.show()

        plt.figure(figsize=(10, 6))
        plt.plot(metrics['validator_rewards'], label='Validator Rewards')
        plt.title('Validator Rewards Over Time')
        plt.xlabel('Time (days)')
        plt.ylabel('Rewards')
        plt.legend()
        plt.show()

        plt.figure(figsize=(10, 6))
        plt.plot(metrics['slashing_events'], label='Slashing Events')
        plt.title('Slashing Events Over Time')
        plt.xlabel('Time (days)')
        plt.ylabel('Number of Events')
        plt.legend()
        plt.show()

        plt.figure(figsize=(10, 6))
        plt.plot(metrics['inflation_rate'], label='Inflation Rate')
        plt.title('Inflation Rate Over Time')
        plt.xlabel('Time (days)')
        plt.ylabel('Inflation Rate (%)')
        plt.legend()
        plt.show()

        plt.figure(figsize=(10, 6))
        plt.plot(metrics['token_stability'], label='Token Stability')
        plt.title('Token Stability Over Time')
        plt.xlabel('Time (days)')
        plt.ylabel('Stability Index')
        plt.legend()
        plt.show()

        plt.figure(figsize=(10, 6))
        plt.plot(metrics['network_latency'], label='Network Latency')
        plt.title('Network Latency Over Time')
        plt.xlabel('Time (days)')
        plt.ylabel('Latency (ms)')
        plt.legend()
        plt.show()

        plt.figure(figsize=(10, 6))
        plt.plot(metrics['fault_tolerance'], label='Fault Tolerance')
        plt.title('Fault Tolerance Over Time')
        plt.xlabel('Time (days)')
        plt.ylabel('Fault Tolerance Index')
        plt.legend()
        plt.show()

        plt.figure(figsize=(10, 6))
        plt.plot(metrics['resource_utilization'], label='Resource Utilization')
        plt.title('Resource Utilization Over Time')
        plt.xlabel('Time (days)')
        plt.ylabel('Utilization (%)')
        plt.legend()
        plt.show()
