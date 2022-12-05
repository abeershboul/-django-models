from django.test import TestCase

from django.urls import reverse



# Create your tests here.
class thingsTests(TestCase):
    def test_Snack_page_status_code(self):
        url = reverse('snacks')
        print("url=",url)
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code,200)
    def test_home_page_templete(self):
        url = reverse('snacks')
        response = self.client.get(url)
        print(response)
        self.assertTemplateUsed(response,'snack_list.html') 

          
