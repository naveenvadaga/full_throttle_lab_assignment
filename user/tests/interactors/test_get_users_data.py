from unittest.mock import create_autospec, Mock

from user.interactors.get_users_data import GetUsersData
from user.interactors.presenters.presenters import Presenter
from user.interactors.storages.storage import Storage


class TestGetUsersData:

    def test_get_users_data(self):
        storage_mock = create_autospec(Storage)
        presenter_mock = create_autospec(Presenter)
        users_details = Mock()
        users_activity_periods = Mock()
        expected_response = Mock()

        storage_mock.get_users_details.return_value = \
            users_details
        storage_mock.get_users_activity_periods.return_value = \
            users_activity_periods
        presenter_mock.get_users_data_response.return_value = \
            expected_response

        interactor = GetUsersData(
            storage_mock, presenter_mock)
        response = interactor.get_users_data()

        assert expected_response == response
        storage_mock.get_users_details.assert_called_once()
        storage_mock.get_users_activity_periods.assert_called_once()
        presenter_mock.get_users_data_response.assert_called_once_with(
            users_details, users_activity_periods)
