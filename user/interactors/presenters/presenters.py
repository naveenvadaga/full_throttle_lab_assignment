import abc
from typing import List

from datetime import datetime

from user.interactors.storages.storage import UserActivityPeriodsDTO, UserDetailsDTO


class Presenter:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_users_data_response(
            self, user_details_dtos: List[UserDetailsDTO],
            user_activity_period_dtos: List[UserActivityPeriodsDTO]):
        pass
