import abc
from datetime import datetime
from typing import List

from dataclasses import dataclass


@dataclass
class UserDetailsDTO:
    user_id: str
    real_name: str
    time_zone: str


@dataclass
class UserActivityPeriodsDTO:
    user_id: str
    start_time: datetime
    end_time: datetime


class Storage:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_users_details(self) -> List[
            UserDetailsDTO]:
        pass

    @abc.abstractmethod
    def get_users_activity_periods(self) -> List[
            UserActivityPeriodsDTO]:
        pass
