from django.test import TestCase, Client
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

class ViewUserTestCase(APITestCase):
    
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = UserCreate.as_view()
        self.url = reverse('view_users')
        self.user = User.objects.create(uid = "TestDupa", username = "TestDupa", email = "TestDupa")

    def test_user_create(self):

        response = self.client.get(self.url)
        response.render()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        sample_post={
            "uid": str(self.user.uid),
            "email": str(self.user.email),
            "username": str(self.user.username)
        }
        sample_post['league'] = None
        sample_post['friends'] = []
        self.assertEqual(sample_post, json.loads(response.content)[0])


class UpdateUserTestCase(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = UserCreate.as_view()
        self.url = reverse('add-user')
        self.user = User.objects.create(uid = "TestUser", username = "TestUser", email = "TestUser")

    def test_user_update(self):
    # First, create a new user
        sample_post={
            "uid": str(self.user.uid),
            "email": str(self.user.email),
            "username": str(self.user.username)
        }
        request = self.factory.post(self.url, sample_post)
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Next, update the user with new data
        update_data = {'email': 'updated@example.com', 'username': 'UpdatedUser'}
        response = self.client.put(f'/user/{self.user.uid}/update/', update_data)
        self.assertEqual(response.status_code, 200)

        # Finally, retrieve the updated user and verify that the data was correctly updated
        response = self.client.get(f'/user/{self.user.uid}/update/')
        self.assertEqual(response.status_code, 200)

