import unittest
from simulation_engine.core.economic_model import EconomicModel

class TestEconomicSimulation(unittest.TestCase):
    def test_simulate_economics(self):
        model = EconomicModel(1000000, {'validators': 20, 'community': 50, 'development': 30}, 0.01)
        result = model.simulate_economics()
        self.assertEqual(result['distribution']['validators'], 200000)
        self.assertEqual(result['fee_impact'], 10000)

if __name__ == '__main__':
    unittest.main()
