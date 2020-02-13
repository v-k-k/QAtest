from .test_template import TestTemplate
from settings import FireFoxDriver
import unittest


class MozillaTest(TestTemplate):
    """
        Testing FireFox with 2 scenarios
    """
    PATH = FireFoxDriver


if __name__ == "__main__":
    unittest.main()
