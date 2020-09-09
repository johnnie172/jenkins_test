import unitest
from helloworld import print_hello_world


class TestUtilities(unittest.TestCase):
	
	def test_helloworld(self):
		self.assertEqual(print_hello_world(), "Hello World")


def suite():

    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestUtilities))


    return test_suite

mySuit=suite()

if __name__ == '__main__':
    runner=unittest.TextTestRunner()
    runner.run(mySuit)
