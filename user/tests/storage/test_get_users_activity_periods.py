from datetime import datetime

import pytest

from user.interactors.storages.storage import UserDetailsDTO, UserActivityPeriodsDTO
from user.models import User, UserActivityPeriod
from user.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
class TestGetUsersActivityPeriods:

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
        UserActivityPeriod.objects.create(
            user_id="1",
            start_time=datetime(2012, 1, 1, 2, 3, 3),
            end_time=datetime(2013, 1, 1, 1, 1, 1)
        )
        UserActivityPeriod.objects.create(
            user_id="2",
            start_time=datetime(2015, 1, 1, 2, 3, 3),
            end_time=datetime(2017, 1, 1, 1, 1, 1)
        )

        return [
            UserActivityPeriodsDTO(
                user_id="1",
                start_time=datetime(2012, 1, 1, 2, 3, 3),
                end_time=datetime(2013, 1, 1, 1, 1, 1)
            ),
            UserActivityPeriodsDTO(
                user_id="2",
                start_time=datetime(2015, 1, 1, 2, 3, 3),
                end_time=datetime(2017, 1, 1, 1, 1, 1)
            )
        ]

    def test_get_users_activity_details(
            self, setup):
        expected_users_activity_periods_dtos = setup
        storage = StorageImplementation()

        response_dtos = storage.get_users_activity_periods()

        assert response_dtos == \
               expected_users_activity_periods_dtos
