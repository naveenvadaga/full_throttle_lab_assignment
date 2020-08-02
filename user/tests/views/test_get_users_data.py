from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestGetUsersData(APITestCase):

    def setUp(self) -> None:
        from user.scripts.populate_database import populate_database
        populate_database()

    def test_get_users_data(self):
        from user.scripts.populate_database import get_json_data
        expected_user_data = get_json_data()['members']

        url = reverse('get_users_data')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_user_data)
