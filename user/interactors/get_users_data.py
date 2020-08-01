from user.interactors.presenters.presenters import Presenter
from user.interactors.storages.storage import Storage


class GetUsersData:

    def __init__(
            self, storage: Storage,
            presenter: Presenter):
        self.storage = storage
        self.presenter = presenter

    def get_users_data(self):
        user_details_dtos = self.storage.\
            get_users_details()

        user_activity_period_dtos = self.storage.\
            get_users_activity_periods()

        return self.presenter.get_users_data_response(
            user_details_dtos, user_activity_period_dtos)


