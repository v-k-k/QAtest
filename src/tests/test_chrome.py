from .test_template import TestTemplate
from settings import ChromeDriver
import unittest


class ChromeTest(TestTemplate):
    """
        Testing Chrome with 2 scenarios
    """
    PATH = ChromeDriver


if __name__ == "__main__":
    unittest.main()
