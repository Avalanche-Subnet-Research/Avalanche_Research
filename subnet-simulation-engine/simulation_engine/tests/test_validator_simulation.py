import unittest
from simulation_engine.core.validator_config import ValidatorConfig

class TestValidatorSimulation(unittest.TestCase):
    def test_generate_validator_set(self):
        criteria = [{'cpu': '8 vCPU', 'ram': '16 GB', 'storage': '1 TB'}]
        config = ValidatorConfig(criteria, 1000, 'AVAX')
        validators = config.generate_validator_set()
        self.assertEqual(len(validators), 1)
        self.assertEqual(validators[0]['stake'], 1000)

if __name__ == '__main__':
    unittest.main()
