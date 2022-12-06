from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from .views import *
from .models import *
# Create your tests here.

class CreateUserTestCase(APITestCase):
    
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = UserCreate.as_view()
        self.url = reverse('add-user')
        self.user = User.objects.create(uid = "TestDupa", username = "TestDupa", email = "TestDupa")
    def test_user_create(self):

        sample_post={
            "uid": "TestUID",
            "email": "TestEmail",
            "username": "TestUsername"
        }
        request = self.factory.post(self.url, sample_post)

        request.user = self.user

        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    