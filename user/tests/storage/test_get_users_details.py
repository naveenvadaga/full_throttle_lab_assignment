import pytest

from user.interactors.storages.storage import UserDetailsDTO
from user.models import User
from user.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
class TestGetUsersDetails:

    @pytest.fixture
    def setup(self):
        User.objects.create(
            id="1",
            real_name="test_one",
            time_zone="test_zone_one"
        )
        User.objects.create(
            id="2",
            real_name="test_two",
            time_zone="test_zone_two"
        )
        return [
            UserDetailsDTO(
                user_id="1",
                real_name="test_one",
                time_zone="test_zone_one"
            ),
            UserDetailsDTO(
                user_id="2",
                real_name="test_two",
                time_zone="test_zone_two"
            )
        ]

    def test_get_users_details(
            self, setup):
        expected_user_details_dtos = setup
        storage = StorageImplementation()

        response_dtos = storage.get_users_details()

        assert response_dtos == \
               expected_user_details_dtos
