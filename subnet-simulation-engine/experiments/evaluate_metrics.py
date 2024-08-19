class EvaluateMetrics:
    def __init__(self, economic_model, security_model, validator_config, network_architecture_model):
        self.economic_model = economic_model
        self.security_model = security_model
        self.validator_config = validator_config
        self.network_architecture_model = network_architecture_model

    def run_simulation(self, time_steps):
        metrics_over_time = {
            'tps': [],
            'finality_time': [],
            'validator_uptime': [],
            'validator_rewards': [],
            'slashing_events': [],
            'inflation_rate': [],
            'token_stability': [],
            'network_latency': [],
            'fault_tolerance': [],
            'resource_utilization': []
        }

        for step in range(time_steps):
            # Step 1: Network Architecture Simulation
            network_architecture = self.network_architecture_model.simulate_network_architecture()

            # Step 2: Validator Configuration
            validators = self.validator_config.simulate_validator_config()
            
            # Step 3: Security Simulation
            security = self.security_model.simulate_security()

            # Step 4: Economic Simulation
            economic_metrics = self.economic_model.simulate_economics()

            # Step 5: Collect Metrics
            metrics_over_time['tps'].append(network_architecture['transaction_throughput'])
            metrics_over_time['finality_time'].append(network_architecture['block_size_info']['propagation_delay'])
            #metrics_over_time['validator_uptime'].append(sum(validator['uptime'] for validator in validators['selected_validators']) / len(validators['selected_validators']))
            metrics_over_time['validator_rewards'].append(sum(validator['rewards'] for validator in validators['rewarded_validators']))
            metrics_over_time['slashing_events'].append(len(security['slashed_validators']))
            #åmetrics_over_time['inflation_rate'].append(economic_metrics['inflation_rate'])
            #ßmetrics_over_time['token_stability'].append(economic_metrics['token_stability'])
            metrics_over_time['network_latency'].append(network_architecture['latency'])
            metrics_over_time['fault_tolerance'].append(network_architecture['fault_tolerance'])
            #metrics_over_time['resource_utilization'].append(economic_metrics['resource_utilization'])

        return metrics_over_time
