import unittest

loader = unittest.TestLoader()
tests = loader.discover('tests')
test_runner = unittest.TextTestRunner()
test_runner.run(tests)
