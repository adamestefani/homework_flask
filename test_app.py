import unittest
import textcontroller
import index


#Unit Test
class AppTestCases(unittest.TestCase):
    
    #Content for testing
    test_sample = ['hello world', 'this is 1 message', '123 and 456']
    
    #Ensure that REST is returning properly
    def test_service(self):
        tester = textcontroller.app.test_client(self)
        
        for sample in self.test_sample:
            response = tester.get('/text/'+sample)
            self.assertTrue(sample in response.data)


    #Ensure that form is loaded
    def test_form(self):
        tester = index.app.test_client(self)
        response = tester.get('/comment')
        self.assertEqual(response.status_code, 200)


    #Ensure that form is returning the same text
    def test_form_return(self):
        tester = index.app.test_client(self)
        
        for sample in self.test_sample:
            response = tester.post(
                '/allcomment',
                data=dict(textInput=sample),
                follow_redirects=True
            )
            self.assertIn(sample, response.data)


if __name__ == '__main__':
    unittest.main()

