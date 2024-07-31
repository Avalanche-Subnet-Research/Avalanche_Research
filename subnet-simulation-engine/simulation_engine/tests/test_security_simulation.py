import unittest
from simulation_engine.core.security_model import SecurityModel

class TestSecuritySimulation(unittest.TestCase):
    def test_simulate_security(self):
        model = SecurityModel({'double_signing': 50, 'downtime': 10})
        result = model.simulate_security()
        self.assertEqual(result['double_signing'], 50)
        self.assertEqual(result['downtime'], 10)

if __name__ == '__main__':
    unittest.main()
