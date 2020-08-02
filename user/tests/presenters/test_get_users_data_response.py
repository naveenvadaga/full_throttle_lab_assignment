from datetime import datetime

import pytest

from user.interactors.storages.storage import UserDetailsDTO, UserActivityPeriodsDTO
from user.presenters.presenter_implementation import PresenterImplementation


class TestGetUsersDataResponse:

    @pytest.fixture
    def setup(self):
        user_details_dtos = [
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
        user_activity_periods_dtos = [
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
        expected_response = [
            {
                'id': '1',
                'real_name': 'test_one',
                'tz': 'test_zone_one',
                'activity_periods': [
                        {
                            'start_time': 'Jan 01 2012 02:03AM',
                            'end_time': 'Jan 01 2013 01:01AM'
                        }
                ]
            },
            {
                'id': '2',
                'real_name': 'test_two',
                'tz': 'test_zone_two',
                'activity_periods': [
                    {
                        'start_time': 'Jan 01 2015 02:03AM',
                        'end_time': 'Jan 01 2017 01:01AM'
                    }
                ]
            }
        ]

        return user_details_dtos, \
           user_activity_periods_dtos, \
           expected_response

    def test_get_users_data_response(
            self, setup):
        user_details_dtos, user_activity_periods_dtos, \
            expected_response = setup

        presenter = PresenterImplementation()

        response = presenter.get_users_data_response(
            user_details_dtos, user_activity_periods_dtos)
        assert response == expected_response

