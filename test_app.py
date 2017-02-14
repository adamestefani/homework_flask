import unittest
import textcontroller
import index


#Unit Test
class AppTestCases(unittest.TestCase):
    
    #Content for testing
    sample_text = ['hello world', 'this is 1 message', '123 and 456']
    sample_user = ['Tester', 'Joe', 'Tom']
    sample_parent_id = [0, 1, 2]
    sample_city = ['Toronto', 'Vancouver', 'San Francisco']
    
    #Ensure that REST is returning properly
    def test_service(self):
        tester = textcontroller.app.test_client(self)
        
        for sample_index in range(len(self.sample_text)):

            text = self.sample_text[sample_index]
            user = self.sample_user[sample_index]
            parent_id = self.sample_parent_id[sample_index]
            city = self.sample_city[sample_index]

            response = tester.get('/text/'+text+'/user/'+user+'/parentid/'+str(parent_id)+'/city/'+city)
            self.assertTrue(text in response.data)


    #Ensure that form is loaded
    def test_form(self):
        tester = index.app.test_client(self)
        response = tester.get('/comment')
        self.assertEqual(response.status_code, 200)


    #Ensure that form is returning the same text
    def test_form_return(self):
        tester = index.app.test_client(self)
        
        for sample_index in range(len(self.sample_text)):

            text = self.sample_text[sample_index]
            user = self.sample_user[sample_index]
            parent_id = self.sample_parent_id[sample_index]
            city = self.sample_city[sample_index]

            response = tester.post(
                '/allcomment',
                data=dict(textInput=text, userName=user, parentId=parent_id, city=city),
                follow_redirects=True
            )
            self.assertIn(text, response.data)


    #Ensure 

if __name__ == '__main__':
    unittest.main()

