import unittest
import sys
import os

# Add the src directory to sys.path
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
print(f"Module path: {module_path}")

if module_path not in sys.path:
    sys.path.append(module_path)

try:
    from utils import add, subtract
except ModuleNotFoundError:
    raise ImportError("The 'utils' module could not be found. Ensure 'utils.py' exists in the 'src' directory.")

class TestUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

if __name__ == '__main__':
    unittest.main()
