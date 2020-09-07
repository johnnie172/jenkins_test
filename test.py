import unitest
from helloworld import print_hello_world


class TestUtilities(unittest.TestCase):
	
	def test_helloworld(self):
		self.assertEqual(print_hello_world(), "Hello World")