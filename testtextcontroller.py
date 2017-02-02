import unittest
import textcontroller


#Unit Test
class MyTest(unittest.TestCase):
    
    def test_service(self):
        self.assertEqual(textcontroller.return_text("test"), "test")
        self.assertEqual(textcontroller.return_text("testing a message"), "testing a message")
        self.assertEqual(textcontroller.return_text("anything else"), "anything else")

unittest.main()

